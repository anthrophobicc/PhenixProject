# Phenix

**Une bibliothèque du savoir qui fonctionne sans internet, sans compte, et sans serveur.**

Phenix rassemble des fiches de connaissance — survie, technique, histoire — dans un format texte durable, consultable hors ligne sur n'importe quel appareil capable d'ouvrir un fichier.

Le logiciel n'est qu'un lecteur. **Si Phenix disparaît, les fiches restent lisibles.** C'est le principe qui gouverne toute l'architecture.

---

## Installation

### Utilisation immédiate, sans rien installer

1. Téléchargez `app/phenix.html`
2. Double-cliquez dessus

C'est tout. Le fichier s'ouvre dans votre navigateur et fonctionne hors ligne.

### Sur téléphone

Ouvrez https://anthrophobicc.github.io/PhenixProject/phenix.html, puis ajoutez la page à l'écran d'accueil (iPhone : Safari, Partager, *Sur l'écran d'accueil* ; Android : Chrome, menu ⋮, *Installer l'application*). Elle a sa propre icône et continue de marcher sans connexion. À la première ouverture, elle suit la langue du téléphone.

### Application de bureau

Le projet Tauri est dans `src-tauri/`. Voir [BUILD.md](BUILD.md) pour fabriquer un `.exe`, un `.dmg` ou un `.AppImage`. L'application pèse moins de 10 Mo et écrit vos données directement sur votre ordinateur.

---

## Utilisation

**Chercher.** La barre de recherche parcourt les titres, les identifiants, les étiquettes et le texte intégral des fiches.

**Filtrer par balises.** Quatre axes de lecture orientent la recherche selon votre situation réelle :

| Balise | Valeurs | Question posée |
|---|---|---|
| Temps | Flash · Court · Long | Combien de temps avez-vous ? |
| Contexte | Seul · À deux · En groupe | Combien êtes-vous ? |
| Risque | Discret · Exposé | Pouvez-vous être vu ? |
| Matériel | Aucun · Récupération · Technique | Qu'avez-vous en main ? |

**Naviguer.** Les fiches sont reliées entre elles par des hyperliens. Suivez-les : le fil d'Ariane en haut de l'écran vous ramène toujours à votre point de départ.

**Créer.** Le bouton « + Fiche » ouvre un éditeur avec mise en forme, insertion d'images, balises et aperçu avant enregistrement.

**Cartes.** Cadrez une zone, enregistrez ses tuiles, consultez-la ensuite sans connexion. Posez des repères sur un calque séparé, exportable indépendamment du fond de carte.

**Sauvegarder.** Paramètres → Exporter. Un seul fichier contient vos fiches, vos listes, vos cartes et vos repères.

---

## Structure d'une fiche

Une fiche est un fichier `.md` avec un en-tête de métadonnées.

```markdown
---
id: URG-HYPO-001
titre: Hypothermie
axe: 3
categorie: Protocoles d'urgence
temps: Flash
contexte: 2
risque: Exposé
materiel: Rien
priorite: flash
origine: officielle
tags: [urgence, froid, secourisme]
sources: ["ICAR-MEDCOM — Classification suisse de l'hypothermie"]
---

::Rien ne brûle comme le froid.::

## AGIR
...
## ADAPTER
...
## COMPRENDRE
...
```

### Les trois axes

- **Axe 1 — La Mémoire.** Ce qui s'est passé et ce que ça nous apprend.
- **Axe 2 — La Technique.** Comment une chose fonctionne, et les données techniques qui vont avec : plans, cotes, unités, tableaux de référence. On explique et on renseigne ; le geste à faire va en Axe 3.
- **Axe 3 — La Survie.** Quoi faire, maintenant, dans une situation dégradée.

Quand un sujet relève des deux, la règle est l'intention et non la matière. *Réparer un câble* va en Axe 3, *comment fonctionne un câble* va en Axe 2, et les deux fiches se citent l'une l'autre. **On n'écrit jamais deux fois la même chose : on relie.**

### Les deux structures

- **Urgence** — AGIR, puis ADAPTER, puis COMPRENDRE. Le lecteur n'a pas le temps.
- **Savoir** — COMPRENDRE, puis AGIR, puis ADAPTER. Le geste juste découle du mécanisme.

### Les deux origines

Les fiches **officielles** sont livrées avec le logiciel et relues avant intégration. Les fiches **communautaires** viennent d'un import ou d'une rédaction locale. Elles cohabitent, se distinguent partout dans l'interface, et ne se remplacent jamais.

---

## Fonctionnalités

- Consultation, recherche plein texte et filtrage par balises
- Liens bidirectionnels entre fiches, avec fil d'Ariane
- Création et modification de fiches, avec images et aperçu
- Favoris et listes de lecture
- Cartes hors ligne par zone, avec calques de repères séparés
- Fusion de cartes et de calques
- Bibliothèque d'ouvrages complets importables
- Quatre modules intégrés : **Inventaire** (cases, lieux, alertes de péremption et de stock bas, export CSV), **Notes** (reliées aux fiches par `[[ID]]`), **Calendrier** (événements, répétition annuelle) et **Convertisseur** (unités, températures, batteries et solaire). Leurs données voyagent avec la sauvegarde.
- Modules de la communauté importables et exportables
- **Phenix Lab**, quand il y a du réseau : proposer une idée ou une fiche entière, voter « utile » et commenter sous chaque fiche officielle et sous les propositions publiées. Tout le reste marche sans connexion.
- Huit thèmes, deux dispositions (colonnes, ou liste en haut et lecture centrée)
- Sur téléphone : menu déroulant des vues, panneau des cartes rangé dans un tiroir, bouton de retour au corpus pendant la lecture
- Import et export en `.md` et `.json`

---

## Limites actuelles

Elles sont réelles et assumées. Les connaître évite les mauvaises surprises.

- **L'enregistrement dépend du mode d'ouverture.** En application de bureau, tout est écrit sur le disque. Dans un navigateur, tout est enregistré localement et survit à la fermeture. Dans certains aperçus restreints, aucun enregistrement n'est possible : l'indicateur en haut à droite vous le dit, et l'export manuel devient obligatoire.
- **Les tuiles de carte proviennent d'OpenStreetMap**, dont la politique d'usage interdit le téléchargement en masse. Les zones enregistrables sont donc volontairement limitées. Une source de tuiles dédiée est nécessaire avant toute diffusion large.
- **Le corpus est encore petit.** Cent quatre-vingt-trois fiches, dont quarante-quatre traduites en anglais, là où le projet en vise des milliers. Toutes les catégories des trois axes ont au moins une fiche.
- **Le corpus est embarqué dans le fichier de l'application.** Ajouter une fiche demande de la reporter à deux endroits. C'est le prix du fichier unique sans dépendance.
- **Aucune vérification cryptographique** des fiches n'est encore implémentée. À la place, le logiciel connaît la liste des fiches qu'il embarque : toute fiche importée est communautaire, quoi que dise son en-tête. Cela empêche l'usurpation locale, pas la diffusion d'une copie modifiée du logiciel lui-même.
- **Les fonctions en ligne sont jeunes.** Les propositions, votes et commentaires passent par une base Supabase gratuite (voir `docs/BACKEND.md`) : sans compte, avec des garde-fous contre les envois en rafale, et une relecture humaine avant toute publication.

---

## Feuille de route

**v0.2** — Signature des binaires · corpus élargi · format visuel des fiches
**v0.3** — Vérification d'intégrité des fiches · format visuel et hybride abouti
**v0.4** — Source de tuiles dédiée · cartes régionales officielles
**Plus tard** — Assistance locale de recherche · échange entre terminaux

---

## Contribuer

Le plus simple : la page **Lab** du site, ou le module **Phenix Lab** de l'application. Une idée prend dix secondes ; une fiche complète peut avoir des images. Sans compte.

Les contributions se font aussi par *pull request* sur ce dépôt.

**Pour proposer une fiche :**

1. Créez un fichier `.md` dans le dossier de l'axe concerné
2. Respectez l'en-tête de métadonnées et la structure en trois blocs
3. **Indiquez vos sources.** Une fiche sans source ne sera pas intégrée au corpus officiel
4. Reliez votre fiche aux fiches existantes par des hyperliens
5. Ouvrez une *pull request*

**Le ton.** Assertif, vouvoiement, aucune phrase pour combler. Phrases courtes dans l'urgence, longues dans l'explication. Le rythme de la fiche est le rythme de la situation.

**Ce qui sera refusé :** contenu sans source sur un sujet où l'erreur blesse, procédures médicales relevant d'une formation, techniques dont l'efficacité n'est pas établie.

---

## Lire la bibliothèque sur un petit écran

`node outils/export-flipper.js` écrit toutes les fiches en texte simple dans `sortie-flipper/phenix/` (une fiche par fichier, rangées par langue et par axe) : de quoi les lire sur un Flipper Zero ou sur le premier prototype du Phenix 001. Le plan du prototype est dans `materiel/mvp-001.md`.

---

## Sécurité

Phenix ne collecte rien, n'envoie rien, ne trace rien. Tout reste sur votre appareil.

Deux points appellent votre attention :

- **Le contenu importé n'est pas de confiance.** Une fiche ou un module venu d'ailleurs peut contenir n'importe quoi. Lisez avant d'appliquer, surtout sur les sujets où l'erreur coûte cher.
- **Les fonctions de carte utilisent le réseau.** Le chargement d'une zone et la recherche de lieu contactent OpenStreetMap. Tout le reste fonctionne hors ligne.

Pour signaler une faille ou une erreur factuelle dans une fiche, ouvrez une *issue*.

---

## Sauvegarde et restauration

**Sauvegarder** — Paramètres → Exporter. Vous obtenez `sauvegarde-phenix.json` contenant vos fiches personnelles, listes, favoris, cartes, repères, ouvrages et modules.

**Restaurer** — Paramètres → Importer, puis sélectionnez le fichier.

**Exports partiels** — une fiche seule en `.md`, une carte seule, un calque de repères seul. Chacun s'importe indépendamment, ce qui permet de partager un calque sans partager sa carte.

Conservez vos sauvegardes en plusieurs exemplaires et en plusieurs endroits. Une réserve qu'on ne peut ni déplacer ni défendre n'est pas une sécurité.

---

## Le site public

Le dossier `site/` contient un site statique prêt pour GitHub Pages : présentation,
lecture des fiches sans installation, téléchargement, et **Phenix Lab**, le formulaire
de contribution pensé pour le téléphone. Il est entièrement produit par
`node outils/construire-site.js`, y compris `site/phenix.html` (l'application de `app/`,
installable sur téléphone grâce à `manifest.webmanifest` et `sw.js`) et `links.html`,
la page de liens prévue pour la bio Instagram. Après avoir ajouté ou traduit une fiche,
relancez-le en dernier.

- [MISE-EN-LIGNE.md](docs/MISE-EN-LIGNE.md) — du dépôt vide à l'adresse publique
- [BACKEND.md](docs/BACKEND.md) — recevoir et modérer les contributions
- [DISTRIBUTION.md](docs/DISTRIBUTION.md) — les options d'empaquetage
- [BUILD.md](BUILD.md) — fabriquer l'application de bureau

Coût de départ : zéro euro.

---

## Licence

Le **logiciel** est sous licence MIT.
Le **corpus de fiches** est sous licence Creative Commons Attribution-ShareAlike 4.0.

Vous pouvez copier, modifier et redistribuer les deux, y compris commercialement, à condition de citer la source et de partager les fiches dérivées sous la même licence.

---

*Le savoir est votre seule immunité.*




