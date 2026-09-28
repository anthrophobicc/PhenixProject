---
id: SURV-REC-045
titre: Récupérer sur un onduleur et une batterie de secours
axe: 3
categorie: Récupération
temps: Court
contexte: 1
risque: Exposé
materiel: Récupération
priorite: normale
origine: officielle
tags: [onduleur, batterie plomb, agm, batterie externe, booster, eclairage de securite, baes, tension, recharge]
sources: ["Battery University, batteries au plomb et au lithium", "Norme NF C 71-800, blocs autonomes d'éclairage de sécurité", "INRS, charge des batteries au plomb : risques"]
---

::Derrière presque chaque ordinateur de bureau et chaque caisse de magasin se cache un onduleur avec une ou plusieurs batteries au plomb de 12 V. Et au-dessus de chaque porte de sortie d'un bâtiment public, un petit boîtier vert contient des accus et des LED : l'éclairage de secours. Des centaines de petites batteries attendent qu'on les recharge.::

## COMPRENDRE

- **Les onduleurs de bureau** contiennent des batteries au plomb étanches (souvent 12 V, 7 à 9 Ah), faciles à recharger avec un chargeur de voiture ou un régulateur solaire.
- **L'onduleur lui-même** est un petit convertisseur fait pour tenir quelques minutes : il chauffe s'il travaille longtemps. Voir [[TEC-ENE-025]].
- **Les batteries externes** de téléphone contiennent des cellules lithium et un circuit qui sort du 5 V : on s'en sert telles quelles.
- **Les boosters de démarrage** au lithium sortent du 12 V : lampes, pompe, radio.

Avant tout : les règles de la récupération. Voir [[SURV-REC-001]].

## AGIR

**Tester une batterie au plomb de 12 V** au multimètre, au repos :

| Tension | État |
|---|---|
| 12,6 V et plus | pleine |
| 12,2 V | à moitié |
| 11,8 V | vide |
| moins de 10,5 V | probablement morte |

Une batterie à plat depuis longtemps se **sulfate** ; une charge lente sur plusieurs jours la ramène parfois.

**Les assembler**

- **En parallèle** (plus avec plus, moins avec moins), des batteries **de même type et même âge** : plus d'autonomie, toujours 12 V.
- **Un fusible** sur chaque batterie, près de la borne. Voir [[TEC-ENE-016]].

**L'éclairage de secours** des bâtiments : accus et LED, à récupérer pour de petites lampes rechargeables.

## ADAPTER

- **Le plomb** : acide, lourd, et de l'hydrogène en charge. Charger dehors ou dans un lieu aéré, sans flamme.
- **Le lithium** gonflé, percé ou chaud : on ne l'utilise plus. Voir [[SURV-REC-033]].
- **Les batteries mortes** se rapportent en déchetterie : le plomb et le lithium empoisonnent les sols.

Les batteries en général : [[TEC-ENE-004]].
