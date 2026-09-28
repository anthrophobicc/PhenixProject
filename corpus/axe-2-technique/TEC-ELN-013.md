---
id: TEC-ELN-013
titre: Les composants électroniques de base
axe: 2
categorie: Électronique et Numérique
temps: Court
contexte: 1
risque: Discret
materiel: Technique
priorite: normale
origine: officielle
tags: [composants, resistance, condensateur, diode, led, transistor, regulateur, loi d'ohm, circuit]
sources: ["Horowitz P., Hill W., The Art of Electronics, 3e édition, Cambridge University Press, 2015", "Platt C., Make: Electronics, 3e édition, 2021"]
---

::Le premier transistor, en 1947, tenait dans une main. La puce d'un téléphone récent en contient une vingtaine de milliards. Mais une carte électronique de radio, de chargeur ou de lampe se lit avec une poignée de composants seulement, et une seule loi.::

## La loi d'Ohm

**Tension = résistance × intensité** (U = R × I). Tout le reste en découle.

**Exemple** : une LED qui demande 2 V et 20 mA, sur une alimentation de 5 V. Il reste 3 V à « perdre » : 3 / 0,02 = **150 ohms**. Sans cette résistance, la LED grille. Voir [[TEC-ELN-004]].

## Les composants

- **La résistance** : freine le courant. Un petit cylindre à bandes de couleur, sans sens de branchement.
- **Le condensateur** : stocke un peu d'électricité et la rend, lisse les tensions. Les gros **chimiques** (cylindres) ont un sens : la bande marquée « - » va au moins. Branchés à l'envers, ils gonflent ou éclatent. **Les gros condensateurs restent chargés** longtemps après débranchement. Voir [[SURV-REC-031]].
- **La diode** : laisse passer le courant dans un seul sens (la bague marque la sortie). Quatre diodes en pont transforment l'alternatif en continu.
- **La LED** : une diode qui éclaire.
- **Le transistor** : un interrupteur commandé ; un petit courant en commande un gros. La base de toute l'électronique.
- **Le régulateur de tension** : sort une tension fixe (5 V, 3,3 V) à partir d'une tension plus haute. Trois pattes, très utile pour alimenter un appareil USB.
- **Le relais** : un interrupteur mécanique commandé par un électroaimant. On l'entend claquer.
- **Le fusible** : un fil qui fond pour protéger le reste.
- **Le transformateur** : change la tension de l'alternatif (230 V en 12 V par exemple).

## Tester

Un multimètre mesure tension, résistance et continuité, et teste les diodes. Voir [[TEC-ENE-008]].

## Pour aller plus loin

Récupérer des composants : [[TEC-ELN-014]]. Souder : [[TEC-ELN-005]]. Lire un circuit : [[TEC-ENE-002]].
