---
id: TEC-ELN-020
titre: Les capteurs
axe: 2
categorie: Électronique et Numérique
temps: Court
contexte: 1
risque: Discret
materiel: Technique
priorite: normale
origine: officielle
tags: [capteurs, flotteur, thermostat, temperature, humidite, niveau d'eau, mouvement, detecteur de monoxyde, regulation]
sources: ["Vitruve, De l'architecture, livre IX (l'horloge à eau à flotteur de Ctésibios)", "Fraden J., Handbook of Modern Sensors, 5e édition, Springer, 2016", "Norme NF EN 50291, détecteurs de monoxyde de carbone à usage domestique"]
---

::Le flotteur de votre chasse d'eau est un capteur : il mesure le niveau et ferme le robinet tout seul. Le même principe réglait déjà les horloges à eau de l'ingénieur grec Ctésibios, il y a plus de deux mille ans. Mesurer, comparer, agir : c'est l'idée de tous les automatismes, du thermostat au pilote automatique.::

## Le principe

1. **Un capteur** transforme une grandeur (chaleur, humidité, niveau, mouvement) en un signal : un mouvement, une tension, un contact.
2. **On compare** à ce qu'on veut.
3. **On agit** : on ouvre, on ferme, on chauffe, on alerte.

## Les capteurs sans électronique

- **Le flotteur** : niveau d'une citerne, d'un abreuvoir, d'une chasse d'eau.
- **Le bilame** des thermostats : deux métaux collés qui se courbent avec la chaleur et ouvrent un contact.
- **La girouette et le manche à air** : direction du vent.
- **Le pluviomètre** : une bouteille graduée.

## Les capteurs électroniques courants

- **Température** : sonde étanche, pour l'eau, le sol, la serre, le congélateur.
- **Humidité de l'air**, **humidité du sol** : préférer les capteurs dits capacitifs, qui ne rouillent pas dans la terre.
- **Niveau d'eau** : interrupteur à flotteur, ou capteur à ultrasons au-dessus de la citerne.
- **Mouvement** : détecteur infrarouge, pour une lampe ou une alarme. Voir [[SURV-DEF-008]].
- **Lumière**, **courant** consommé, **position** (GPS), **inclinaison**.

On les branche sur un microcontrôleur, qui lit et décide. Voir [[TEC-ELN-019]].

## Ce qu'on ne bricole pas

Les **détecteurs de fumée** et de **monoxyde de carbone** qui protègent des vies : on achète des appareils certifiés et on teste leurs piles. Les petits capteurs de gaz des kits électroniques ne sont pas fiables pour ça. Voir [[TEC-CON-010]].

## Bien mesurer

- **Placer le capteur** au bon endroit : une sonde de température au soleil mesure le soleil, pas l'air.
- **Vérifier** de temps en temps avec un thermomètre, un niveau à l'œil, une mesure à la main.

Les composants : [[TEC-ELN-013]]. Mesurer avec un multimètre : [[TEC-ENE-008]].
