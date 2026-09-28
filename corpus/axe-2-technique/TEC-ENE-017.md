---
id: TEC-ENE-017
titre: La dynamo et l'alternateur
axe: 2
categorie: Énergie et Électricité
temps: Moyen
contexte: 1
risque: Discret
materiel: Technique
priorite: normale
origine: officielle
tags: [dynamo, alternateur, generatrice, aimant, bobine, faraday, moteur recupere, eolienne, diode]
sources: ["Faraday M., Experimental Researches in Electricity, 1831-1832", "Piggott H., A Wind Turbine Recipe Book, 2014", "Hughes E., Electrical and Electronic Technology, Pearson"]
---

::Un aimant qui tourne près d'une bobine de fil, et le courant apparaît. Faraday l'a montré en 1831 ; presque toute l'électricité du monde, nucléaire compris, sort encore de ce principe. Et presque tout moteur électrique récupéré, qu'on fait tourner à la main, devient une génératrice.::

## Le principe

Quand un aimant bouge près d'un fil enroulé, il y fait circuler du courant. **Plus il tourne vite, plus la tension monte.** Une centrale, une éolienne, un alternateur de voiture et une dynamo de vélo font la même chose, à des échelles différentes.

- **La dynamo** donne du courant continu.
- **L'alternateur** donne du courant alternatif, souvent redressé ensuite : celui d'une voiture charge la batterie en 12 à 14 V.

## Les génératrices qu'on trouve partout

- **La dynamo de moyeu** d'un vélo : 6 V, 3 W, faite pour tourner lentement. Avec un petit régulateur USB, elle recharge un téléphone en roulant.
- **Les moteurs à aimants permanents** : moteurs de tapis de course, de trottinette, de visseuse, de lave-linge récents à entraînement direct. Tournés, ils produisent du courant. Ce sont eux qu'on utilise pour les petites éoliennes et les turbines bricolées.
- **L'alternateur de voiture** : robuste, mais il doit tourner vite (plus de mille tours par minute) et a besoin de courant pour s'exciter. Bien sur un moteur, mauvais sur une éolienne lente.

## Brancher sans casser

1. **Une diode** entre la génératrice et la batterie : sans elle, quand on arrête de tourner, la batterie fait tourner la génératrice comme un moteur et se vide.
2. **Un régulateur de charge** : sans lui, une rafale ou un coup de pédale surcharge la batterie.
3. **Mesurer** la tension à vide et en charge avec un multimètre. Voir [[TEC-ENE-008]].

## Bon à savoir

Un ministre aurait demandé à Faraday à quoi servait sa découverte ; il aurait répondu qu'un jour, on pourrait la taxer. L'anecdote est sans doute inventée, mais elle s'est vérifiée.

Le vélo générateur : [[TEC-ENE-018]]. Les batteries : [[TEC-ENE-004]].
