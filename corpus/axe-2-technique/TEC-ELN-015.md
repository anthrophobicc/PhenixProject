---
id: TEC-ELN-015
titre: Les moteurs électriques
axe: 2
categorie: Électronique et Numérique
temps: Court
contexte: 1
risque: Discret
materiel: Technique
priorite: normale
origine: officielle
tags: [moteurs electriques, courant continu, balais, sans balais, pas a pas, servomoteur, asynchrone, condensateur de demarrage]
sources: ["Hughes A., Drury B., Electric Motors and Drives, 5e édition, Newnes, 2019", "Platt C., Make: Electronics, 3e édition, 2021"]
---

::Un moteur de pompe ou de ventilateur qui ronronne sans tourner a, une fois sur deux, un condensateur de démarrage mort : une pièce à quelques euros, deux fils à changer. Savoir quel moteur on a devant soi, c'est savoir comment le réparer, le commander ou le réutiliser.::

## Les familles

- **À courant continu, à balais** : jouets, essuie-glaces, perceuses sans fil, petits ventilateurs. On inverse les fils, il tourne dans l'autre sens ; on baisse la tension, il ralentit. Ses **balais** en carbone s'usent : étincelles et perte de puissance.
- **Sans balais** : drones, vélos électriques, ventilateurs d'ordinateur. Plus durables, ils ont besoin d'une petite carte de commande.
- **Pas à pas** : imprimantes, imprimantes 3D, scanners. Ils tournent par petits crans précis, commandés par une carte.
- **Servomoteurs** de modélisme : ils vont à une position donnée et la tiennent. Pratiques pour ouvrir une trappe, une vanne.
- **Asynchrones** (à induction), en 230 V : pompes, ventilateurs, compresseurs, vieux lave-linge. Increvables. En monophasé, ils démarrent grâce à un **condensateur**.
- **Universels** : aspirateurs, mixeurs, perceuses filaires, meuleuses. Rapides et bruyants, à balais.

## Diagnostiquer

- **Il ronronne sans tourner** : condensateur de démarrage (moteur 230 V) ou roulement bloqué. On essaie de lancer l'axe à la main, **débranché**.
- **Odeur de brûlé, fumée** : bobinage grillé. On change de moteur.
- **Beaucoup d'étincelles, perte de puissance** : balais usés.
- **Il chauffe vite** : surcharge, ventilation bouchée, roulement fatigué.

## Réutiliser

- **En génératrice** : un moteur à aimants qu'on fait tourner produit du courant. Voir [[TEC-ENE-017]].
- **Moteurs de tapis de course, de lave-linge** : touret à meuler, petit tour, broyeur.
- **Un moteur d'essuie-glace** : très lent, très fort, en 12 V. Parfait pour une porte de poulailler ou un tournebroche.

Récupérer : [[TEC-ELN-014]]. Engrenages et courroies : [[TEC-MEC-028]].
