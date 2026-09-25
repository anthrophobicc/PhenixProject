# Recevoir les contributions — Supabase

Objectif : quelqu'un remplit le formulaire sur son téléphone, vous recevez sa fiche,
vous la relisez, vous décidez. Sans serveur à maintenir, sans coût.

---

## Pourquoi Supabase

Vous avez besoin de trois choses : une base pour stocker les propositions, un endroit
pour les images, et un écran pour les relire. Supabase fournit les trois, avec une
offre gratuite qui suffit très largement au démarrage — comptez plusieurs milliers de
propositions avant de la saturer.

**Une limite à connaître dès maintenant :** un projet Supabase gratuit est mis en pause
après une période d'inactivité. Il se réveille en quelques clics, mais si votre
formulaire reste sans usage pendant des semaines, la première soumission échouera.
Le script du formulaire gère ce cas : il rend son fichier `.md` à la personne au lieu
de perdre son travail.

---

## 1. Créer le projet

1. Compte sur supabase.com, puis **New project**
2. Nom : `phenix`, mot de passe de base de données : générez-le et **notez-le**
3. Région : la plus proche de vous
4. Attendez deux minutes

---

## 2. Créer les tables

Ouvrez **SQL Editor** dans le menu de gauche, collez ceci, exécutez.

```sql
-- Numérotation lisible des propositions : SUB-2026-0001
create sequence if not exists numero_proposition start 1;

create table propositions (
  id           uuid primary key default gen_random_uuid(),
  reference    text unique not null default
               'SUB-' || to_char(now(),'YYYY') || '-' ||
               lpad(nextval('numero_proposition')::text, 4, '0'),

  -- contenu proposé
  titre        text not null check (char_length(titre) between 4 and 140),
  contenu      text not null check (char_length(contenu) between 200 and 120000),
  resume       text check (char_length(resume) <= 400),
  axe          smallint check (axe between 1 and 3),
  categorie    text check (char_length(categorie) <= 80),
  langue       text not null default 'fr' check (langue in ('fr','en')),
  urgence      boolean not null default false,
  sources      text,
  note_editeur text,

  -- auteur, tout est facultatif
  auteur       text check (char_length(auteur) <= 60),
  contact      text check (char_length(contact) <= 120),

  -- suivi éditorial
  statut       text not null default 'submitted'
               check (statut in ('submitted','under_review','changes_requested',
                                 'rejected','community','verified','official')),
  motif        text,          -- pourquoi refusée, ou quoi corriger
  fiche_id     text,          -- identifiant Phenix attribué à l'intégration
  commentaire  text,          -- notes internes, jamais publiques

  cree_le      timestamptz not null default now(),
  modifie_le   timestamptz not null default now()
);

create index on propositions (statut, cree_le desc);

-- Horodatage automatique des modifications
create or replace function touch_modifie_le() returns trigger as $$
begin new.modifie_le = now(); return new; end;
$$ language plpgsql;

create trigger t_touch before update on propositions
for each row execute function touch_modifie_le();

-- Signalements sur une fiche publiée
create table signalements (
  id          uuid primary key default gen_random_uuid(),
  fiche_id    text not null,
  motif       text not null
              check (motif in ('erreur','qualite','dangereux','illegal',
                               'spam','hors_sujet','droits')),
  detail      text,
  source      text,          -- ce qui contredit, pour une erreur factuelle
  traite      boolean not null default false,
  cree_le     timestamptz not null default now()
);

create index on signalements (traite, cree_le desc);
```

---

## 3. La sécurité

C'est l'étape à ne pas sauter. Sans elle, n'importe qui pourrait lire les adresses
de contact de vos contributeurs, ou effacer la table.

```sql
alter table propositions enable row level security;
alter table signalements enable row level security;

-- Le public peut déposer une proposition, rien d'autre.
create policy "deposer" on propositions
  for insert to anon with check (true);

-- Le public peut signaler un problème, rien d'autre.
create policy "signaler" on signalements
  for insert to anon with check (true);
```

Aucune politique de lecture pour `anon` : **personne d'autre que vous ne peut lire les
propositions.** Vous, vous y accédez par le tableau Supabase, qui passe par un canal
séparé.

Limitez aussi le volume : dans **Authentication → Rate Limits**, réglez les requêtes
anonymes à une valeur basse. Cela suffit contre un envoi automatisé massif.

---

## 4. Les images

Menu **Storage** → **New bucket**

- Nom : `propositions`
- **Public : non**
- Taille maximale par fichier : 5 Mo
- Types autorisés : `image/png`, `image/jpeg`, `image/webp`

Puis, dans le SQL Editor :

```sql
create policy "deposer image" on storage.objects
  for insert to anon
  with check (bucket_id = 'propositions');
```

Là encore, dépôt autorisé, lecture interdite au public.

---

## 5. Brancher le formulaire

Dans **Project Settings → API**, copiez :

- **Project URL**
- **anon public key**

Ouvrez `site/lab.js` et remplacez les deux premières lignes :

```js
const SUPABASE_URL  = "https://xxxxx.supabase.co";
const SUPABASE_ANON = "eyJhbGci...";
```

La clé `anon` est publique par nature, elle est faite pour être dans une page web.
Ce qui protège vos données, ce sont les politiques de l'étape 3, pas le secret de
cette clé. **Ne mettez jamais la clé `service_role` dans le site** : celle-là ignore
toutes les politiques.

---

## 6. Le flux exact d'une soumission

```
Personne remplit le formulaire sur son téléphone
        ↓
Contrôles côté page  (titre ≥ 4, fiche ≥ 200 caractères, piège à robots)
        ↓
INSERT dans « propositions »  → statut = submitted
        ↓
Référence retournée et affichée : SUB-2026-0001
        ↓
Images éventuelles déposées dans Storage sous cette référence
        ↓
Message : « Contribution reçue. Elle sera examinée. »
```

Si la base est injoignable, le script **télécharge la fiche en `.md` sur l'appareil de
la personne**. Personne ne perd son travail à cause d'une panne.

---

## 7. Relire les propositions

Vous n'avez pas besoin de construire un tableau d'administration. Le tableau Supabase
suffit et il est fait pour ça.

**Table Editor → propositions.** Vous voyez tout, vous pouvez trier par statut,
modifier une case directement.

Pour aller plus vite, créez des vues. SQL Editor :

```sql
-- À traiter en priorité
create view a_relire as
  select reference, titre, axe, langue, auteur,
         left(contenu, 300) as extrait, cree_le
  from propositions
  where statut in ('submitted','under_review')
  order by cree_le;

-- Prêtes à intégrer au corpus
create view a_integrer as
  select reference, titre, axe, categorie, langue, auteur, contenu, sources
  from propositions
  where statut in ('community','verified','official')
  order by modifie_le desc;
```

Elles apparaissent ensuite dans Table Editor comme des tables ordinaires.

---

## 8. Les statuts, et ce qu'ils engagent

| Statut | Signification | Visible publiquement |
|---|---|---|
| `submitted` | Reçue, pas encore lue | non |
| `under_review` | En cours de relecture | non |
| `changes_requested` | Il manque quelque chose, `motif` le dit | non |
| `rejected` | Refusée, `motif` le dit | non |
| `community` | Publiée, non vérifiée, signalée comme telle | oui |
| `verified` | Sources contrôlées | oui |
| `official` | Intégrée au corpus Phenix | oui |

**Une proposition ne devient jamais officielle automatiquement.** Le passage à
`official` est une action manuelle et délibérée.

Une fiche communautaire ne remplace jamais une fiche officielle : elle coexiste avec
son propre identifiant. Modifier une fiche officielle produit une nouvelle version,
elle n'écrase pas le noyau.

---

## 9. Récupérer une fiche acceptée

Dans Table Editor, ouvrez la ligne, copiez le champ `contenu`, et créez un fichier
`.md` dans `corpus/axe-N-nom/` du dépôt GitHub, avec l'en-tête complet.

Pour en récupérer plusieurs d'un coup, SQL Editor :

```sql
select reference, titre, axe, categorie, langue, auteur, contenu, sources
from propositions
where statut = 'verified'
order by modifie_le;
```

Puis **Download CSV** en haut à droite du résultat.

---

## 10. Répondre à un contributeur

Si la personne a laissé un contact et que sa fiche demande une correction, passez le
statut à `changes_requested`, écrivez précisément dans `motif` ce qui manque, et
écrivez-lui. Une demande de correction précise obtient une réponse ; un refus sec n'en
obtient aucune.

Si elle n'a pas laissé de contact, ce n'est pas grave : sa fiche reste utilisable, et
c'est vous qui la corrigez.

---

## Ce que ça coûte

Rien, tant que vous restez dans l'offre gratuite : 500 Mo de base, 1 Go de stockage,
et une bande passante largement suffisante. À raison de quelques kilooctets par
proposition, vous pouvez en recevoir des dizaines de milliers.

Ce qui coûterait, plus tard : un usage intensif du stockage d'images, ou un projet
qu'on veut garder actif en permanence sans mise en pause. On en reparlera si ça arrive.
