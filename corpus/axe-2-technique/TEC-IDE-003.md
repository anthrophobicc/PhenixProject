---
id: TEC-IDE-003
titre: La fiche Phenix
axe: 2
categorie: Information et Données
temps: Court
contexte: 1
risque: Discret
materiel: Rien
priorite: normale
origine: officielle
tags: [phenix, fiche, documentation, format, contribuer, écrire, méthode]
sources: ["Documentation interne du projet Phenix — format de fiche et règles de rédaction"]
---

::Phenix n'est pas un livre fermé. C'est un corpus ouvert, et chaque fiche est un fichier texte lisible par n'importe quoi. Si vous savez lire une fiche, vous savez en écrire une — et le corpus grandit.::

## COMPRENDRE

### Ce qu'est une fiche

Une fiche Phenix est un fichier texte structuré qui traite **un seul sujet** — une action, un mécanisme, un événement. Pas un cours, pas un chapitre de livre. Un sujet, une fiche, autosuffisante.

Chaque fiche a trois parties : un en-tête (les métadonnées), une accroche (une phrase qui résume l'essentiel en une image), et le corps (le contenu structuré).

### Les trois axes

**Axe 1 — Mémoire.** Ce qui s'est passé. Le titre est un événement ou un fait historique. La fiche raconte un épisode et tire un enseignement.

**Axe 2 — Technique.** Comment les choses fonctionnent. Le titre est un **nom** (mécanisme). La fiche explique un phénomène, un matériau, un processus. Pas de procédure d'urgence — c'est du savoir, pas de l'action.

**Axe 3 — Survie.** Ce qu'il faut faire. Le titre est un **verbe** (action). La fiche donne des gestes, des protocoles, des procédures. La structure COMPRENDRE / AGIR / ADAPTER s'applique.

### L'en-tête

L'en-tête est en YAML entre deux lignes de trois tirets. Chaque champ est obligatoire sauf mention contraire.

- **id** : identifiant unique (ex: TEC-MAT-004). Préfixe par catégorie (TEC, SURV, URG, SIG, MEM), suffixe par sous-domaine et numéro.
- **titre** : le nom de la fiche. Nom pour l'Axe 2, verbe pour l'Axe 3.
- **axe** : 1, 2 ou 3.
- **categorie** : une des catégories existantes. En créer une nouvelle est exceptionnel.
- **temps** : Flash (urgence immédiate), Court, Long.
- **contexte** : 1 (seul), 2 (binôme), 2+ (groupe).
- **risque** : Discret, Exposé.
- **materiel** : Rien, Récupération, Technique.
- **priorite** : flash, haute, normale.
- **origine** : officielle (sources vérifiables), terrain (retour d'expérience).
- **tags** : mots-clés entre crochets.
- **sources** : liste de références entre crochets et guillemets.

### L'accroche

Une phrase entre doubles deux-points : celle qu'on retient quand on a oublié le reste. Assertive, visuelle, pas une définition de dictionnaire.

### Le corps

**Axe 3 :** trois sections obligatoires.
- **COMPRENDRE** : pourquoi ce sujet compte, la mécanique sous-jacente.
- **AGIR** : les gestes, numérotés, concrets, dans l'ordre.
- **ADAPTER** : les variantes — quand les conditions changent, quand le matériel manque, quand ça ne se passe pas comme prévu.
- **Ce qu'il faut retenir** : trois phrases maximum qui résument l'essentiel.

**Axes 1 et 2 :** chapitres libres nommés selon le contenu. COMPRENDRE et AGIR sont fréquents mais pas obligatoires — c'est le sujet qui décide de la structure.

### Les règles d'écriture

- **Vouvoiement.** Toujours.
- **Ton assertif.** Pas de « il est possible que » ni de « certains pensent que ». On affirme ou on ne dit pas.
- **Pas de remplissage.** Chaque phrase apporte une information. Si une phrase ne dit rien de nouveau, elle n'a pas sa place.
- **Cross-links.** Quand un sujet est traité dans une autre fiche, on y renvoie entre doubles crochets : un renvoi vers la fiche TEC-SAN-001 s'écrit en entourant son identifiant de doubles crochets. Le logiciel crée le lien automatiquement.
- **Sources obligatoires.** Toute affirmation vérifiable doit être traçable.
- **Pas de backticks ni de dollar-accolade dans le corps.** C'est une contrainte technique du format d'injection.

## AGIR

### Écrire votre première fiche

**1.** Choisir un sujet que vous connaissez ou que vous pouvez documenter. Un sujet, pas un thème.

**2.** Décider de l'axe. Si le sujet est « comment faire X » : Axe 3. Si c'est « comment X fonctionne » : Axe 2. Si c'est « ce qui s'est passé quand X » : Axe 1.

**3.** Copier l'en-tête d'une fiche existante du même axe. Modifier les champs.

**4.** Écrire l'accroche — la phrase qui reste.

**5.** Rédiger le corps en suivant la structure de l'axe. Commencer par COMPRENDRE (pourquoi ce sujet compte), puis AGIR (quoi faire), puis ADAPTER (les variantes).

**6.** Ajouter les sources. Au moins deux sources vérifiables.

**7.** Relire en se demandant : « Si je n'avais que cette fiche et rien d'autre, pourrais-je agir ? » Si non, il manque quelque chose.

## ADAPTER

**Vous ne trouvez pas de source.** Si le savoir vient de votre expérience directe, indiquer « origine: terrain » et décrire le contexte. Un retour d'expérience vaut une source quand il est honnête sur ses limites.

**Le sujet est trop gros pour une fiche.** Le découper. La couture est une fiche, le vêtement en est une autre, le fil une troisième. Chacune se tient seule et renvoie aux autres.

**Vous voulez proposer une fiche au projet.** Écrire le fichier au format décrit ci-dessus et le soumettre. Le corpus est ouvert aux contributions qui respectent le format et le ton.

## Ce qu'il faut retenir

**Une fiche = un sujet, autosuffisant.** C'est la règle qui empêche le corpus de devenir un livre illisible.

**L'axe décide de la structure, le sujet décide du contenu.** Axe 2 explique, Axe 3 fait agir, Axe 1 raconte pour transmettre.

**Écrire une fiche, c'est contribuer au corpus.** Phenix est conçu pour grandir — chaque fiche ajoutée renforce le réseau des renvois et comble un trou.
