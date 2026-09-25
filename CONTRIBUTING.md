# Contribuer à Phenix

## Ce que nous cherchons

Des fiches précises, sourcées, reliées aux autres, écrites pour être utiles
sous contrainte. Une fiche courte et juste vaut mieux qu'une fiche longue
et approximative.

## Écrire une fiche

### 1. Choisir l'axe

- **Axe 1 — La Mémoire.** Ce qui s'est passé et ce que ça nous apprend.
- **Axe 2 — La Technique.** Comment une chose fonctionne. On explique.
- **Axe 3 — La Survie.** Quoi faire, maintenant, en situation dégradée.

Un sujet peut relever de deux axes. La règle est l'intention, pas la matière.
Écrivez la fiche dans l'axe qui correspond à l'intention, et reliez-la à
l'autre par un hyperlien. **On n'écrit jamais deux fois la même chose.**

### 2. Choisir la structure

Les blocs AGIR, ADAPTER et COMPRENDRE **n'existent que dans l'Axe 3**. Ce sont
des structures d'action.

**Urgence (Axe 3)** — AGIR, ADAPTER, COMPRENDRE.
**Savoir (Axe 3)** — COMPRENDRE, AGIR, ADAPTER.
**Axe 2 — La Technique** — aucun bloc. Des chapitres nommés selon le propos.
C'est de l'information et des données : comment une chose fonctionne, avec
quelles valeurs et quelles limites. Pas de consigne, pas de cadrage survie.
**Axe 1 — La Mémoire** — aucun bloc non plus. Des chapitres, par exemple
« Le problème de la copie manuscrite » ou « Ce que cela implique aujourd'hui ».
Une fiche d'histoire est un raisonnement suivi.

Écrivez `## AGIR`, `## COMPRENDRE`, `## ADAPTER` : la mise en forme est
automatique.

### 3. Remplir l'en-tête

```yaml
---
id: AXE-SUJET-001        # majuscules, unique
titre: Titre lisible
axe: 3
categorie: Feu, Eau et Ressources
temps: Court             # Flash | Court | Long
contexte: 1              # 1 | 2 | 2+
risque: Discret          # Discret | Exposé
materiel: Rien           # Rien | Récupération | Technique
priorite: normale        # normale | flash
origine: communaute
tags: [eau, base]
sources: ["Source 1", "Source 2"]
---
```

### 4. Le ton

Assertif. Vouvoiement. Aucune phrase pour combler. Une accroche en tête,
entre doubles deux-points : `::Rien ne brûle comme le froid.::`

Phrases courtes dans l'urgence. Phrases longues dans l'explication.

Dans COMPRENDRE, expliquez le **mécanisme**, pas seulement le fait. Le lecteur
doit pouvoir en déduire quoi faire dans un cas que la fiche ne décrit pas.

### 5. Relier

Les hyperliens s'écrivent `[[ID-DE-LA-FICHE]]` et se placent **dans le texte**,
là où le lecteur en a besoin, pas seulement en fin de fiche.

### 6. Sourcer

Une fiche sans source ne rejoint pas le corpus officiel. Sur les sujets où
l'erreur blesse — santé, électricité, structures — les sources primaires sont
exigées.

## Ce qui sera refusé

- Contenu non sourcé sur un sujet à risque
- Procédures médicales relevant d'une formation
- Techniques dont l'efficacité n'est pas établie, même répandues
- Contenu recopié d'une source protégée

## Proposer

1. Fork du dépôt
2. Fiche dans `/corpus/axe-N-nom/`
3. Vérifiez qu'elle s'ouvre correctement dans `app/phenix.html`
4. Pull request avec une phrase expliquant ce que la fiche apporte

## Signaler une erreur

Ouvrez une issue avec l'identifiant de la fiche, le passage concerné et la
source qui contredit. Les corrections factuelles sont prioritaires sur les
ajouts.
