# Mettre Phenix en ligne

De rien à une adresse publique. Comptez une heure la première fois, sans rien
installer sur votre ordinateur — tout se fait dans le navigateur.

À la fin, vous aurez :

```
https://VOTRE-PSEUDO.github.io/phenix/
```

---

## Étape 1 — Créer le compte GitHub

1. github.com → **Sign up**
2. Choisissez un nom d'utilisateur court : il apparaîtra dans l'adresse du site.
   `phenix-projet` donne `phenix-projet.github.io`.
3. Confirmez votre adresse e-mail.

---

## Étape 2 — Créer le dépôt

1. En haut à droite, **+** → **New repository**
2. **Repository name** : `phenix`
3. **Public**
4. Ne cochez rien d'autre
5. **Create repository**

---

## Étape 3 — Déposer les fichiers

1. Sur la page du dépôt vide, cliquez **uploading an existing file**
2. Faites glisser **tout le contenu** du dossier que vous avez reçu :
   `README.md`, `app/`, `corpus/`, `site/`, `docs/`, `src-tauri/`, les licences
3. En bas, écrivez `Première version` dans la case de description
4. **Commit changes**

Si le glisser-déposer ne prend pas les dossiers, envoyez-les un par un. C'est plus
long mais ça marche toujours.

---

## Étape 4 — Activer le site

1. Onglet **Settings** du dépôt
2. Menu de gauche, **Pages**
3. **Source** : `Deploy from a branch`
4. **Branch** : `main`, et dossier `/docs`… **non** — choisissez la racine `/ (root)`
5. **Save**

Attendez deux à trois minutes, rafraîchissez la page. GitHub affiche l'adresse.

**Le site se trouve dans le sous-dossier `site/`**, donc votre adresse d'accueil est :

```
https://VOTRE-PSEUDO.github.io/phenix/site/
```

### Pour une adresse plus courte

Si vous préférez `https://VOTRE-PSEUDO.github.io/phenix/` directement, déplacez le
contenu de `site/` à la racine du dépôt. Le plus simple : recommencez l'envoi en
déposant le contenu de `site/` à la racine, et les autres dossiers à côté.

---

## Étape 5 — Vérifier

Ouvrez l'adresse sur votre téléphone. Vous devez voir :

- la page d'accueil avec le logo et les quatre actions
- **Explorer** qui liste les fiches, chacune lisible
- **Télécharger** qui propose l'application
- **Contribuer** qui affiche le formulaire

Le formulaire n'envoie encore rien : c'est normal, il manque l'étape suivante.
Testez-le quand même — il doit vous rendre un fichier `.md` au lieu d'échouer
silencieusement.

---

## Étape 6 — Brancher les contributions

Suivez [BACKEND.md](BACKEND.md). Il faut créer un projet Supabase, exécuter le script
de création des tables, régler la sécurité, et coller deux valeurs dans `site/lab.js`.

Pour modifier ce fichier depuis GitHub : ouvrez `site/lab.js`, cliquez sur l'icône
crayon en haut à droite, changez les deux lignes, **Commit changes**. Le site se met
à jour tout seul en une minute.

---

## Étape 7 — Tester en vrai

Depuis votre téléphone, remplissez le formulaire avec une fausse fiche et envoyez.

Vous devez voir apparaître une référence du type `SUB-2026-0001`. Allez dans Supabase,
**Table Editor → propositions** : la ligne est là.

**Faites ce test avant de communiquer sur le projet.** Un formulaire qui échoue le jour
du lancement coûte tous les contributeurs de ce jour-là.

---

## Étape 8 — Publier

Vous avez maintenant une adresse à mettre en biographie Instagram.

Vérifiez avant de la partager :

- [ ] Le site s'ouvre correctement sur téléphone
- [ ] Le logo s'affiche
- [ ] Une fiche au moins se lit du début à la fin
- [ ] Le téléchargement de l'application fonctionne
- [ ] L'application téléchargée s'ouvre et garde une fiche créée
- [ ] Le formulaire enregistre bien dans Supabase
- [ ] Les liens du pied de page marchent

---

## Mettre à jour plus tard

Toute modification passe par le même chemin : sur GitHub, ouvrez le fichier, crayon,
modifiez, **Commit changes**. Le site se régénère seul.

Pour ajouter une fiche au corpus : déposez un fichier `.md` dans
`corpus/axe-N-nom/`, puis reportez-la dans `app/phenix.html` — le corpus de
l'application est embarqué dans le fichier, à l'intérieur du bloc `const CORPUS`.

C'est le point le plus fastidieux du système actuel, et c'est assumé : cela garantit
qu'un seul fichier téléchargé contient tout, sans dépendance.

---

## Ce que ça coûte

| Poste | Coût |
|---|---|
| GitHub Pages | 0 € |
| Supabase, offre gratuite | 0 € |
| Adresse en `github.io` | 0 € |
| Nom de domaine personnel | environ 10 à 15 € par an, **optionnel** |

**Total pour démarrer : zéro.**

Deviendront payants seulement avec le volume : un serveur de tuiles cartographiques
si les cartes sont beaucoup utilisées, un certificat de signature pour l'application
de bureau, et un plan Supabase supérieur au-delà de plusieurs milliers de
contributions.
