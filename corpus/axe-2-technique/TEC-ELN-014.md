---
id: TEC-ELN-014
titre: Récupérer des composants électroniques
axe: 2
categorie: Électronique et Numérique
temps: Court
contexte: 1
risque: Exposé
materiel: Récupération
priorite: normale
origine: officielle
tags: [recuperation, composants, dessouder, alimentation atx, moteurs pas a pas, condensateurs, detecteur de fumee, laser]
sources: ["Platt C., Make: Electronics, 3e édition, 2021", "The Restart Project, guides de réparation", "INRS, risques électriques et condensateurs"]
---

::Une imprimante jetée contient des moteurs de précision, des rails, des courroies, des engrenages et une alimentation. Une vieille alimentation de PC devient une alimentation d'atelier 12 V et 5 V avec un bout de fil. Les poubelles électroniques sont les magasins de pièces de ceux qui savent démonter.::

## Où trouver quoi

- **Alimentation de PC** : 12 V et 5 V costauds. Pour la démarrer hors du PC, on relie le fil vert du gros connecteur à un fil noir.
- **Imprimantes, scanners, lecteurs de disques** : moteurs pas à pas, rails, courroies, ressorts, engrenages.
- **Chargeurs et blocs secteur** : de petites alimentations prêtes à l'emploi, étiquette lue.
- **Ordinateurs portables** : cellules lithium, ventilateurs, écran. Voir [[SURV-REC-033]].
- **Haut-parleurs** : aimants puissants.
- **Jouets, perceuses, brosses à dents** : petits moteurs, piles rechargeables, engrenages.
- **Ampoules LED** : LED et petites alimentations.
- **Téléphones** : vibreurs, micros, petits écrans.

## Dessouder

- **La pompe à dessouder** : on chauffe la soudure, on aspire.
- **La tresse** : posée sur la soudure et chauffée, elle boit l'étain.
- **La coupe** : pour un composant à pattes, couper au ras de la carte est souvent plus rapide.
- **Le décapeur thermique** chauffe toute une zone : les composants tombent. Aérer, loin du plastique.

Tester chaque pièce au multimètre avant de la réutiliser. Voir [[TEC-ENE-008]].

## Les dangers

- **Les gros condensateurs** (alimentations, micro-ondes, flashs d'appareil photo, téléviseurs) restent chargés : les décharger avec une résistance tenue par des pinces isolées, jamais les doigts. Voir [[SURV-REC-031]].
- **Les vieux téléviseurs à tube** gardent une très haute tension dans le tube : on ne les ouvre pas.
- **Les lasers** des lecteurs de disques abîment les yeux : jamais regarder dedans.
- **Les détecteurs de fumée ioniques** contiennent une petite source radioactive : on ne les démonte pas, on les rapporte.
- **Les cellules lithium** percées prennent feu. Voir [[SURV-REC-033]].
- **L'étain au plomb** des vieilles cartes : se laver les mains.

Les composants : [[TEC-ELN-013]].
