---
id: TEC-ENE-025
titre: Onduleurs et convertisseurs
axe: 2
categorie: Énergie et Électricité
temps: Court
contexte: 1
risque: Exposé
materiel: Technique
priorite: normale
origine: officielle
tags: [onduleur, convertisseur, 12 v, 230 v, sinus pur, pic de demarrage, fusible, retour de tension, usb]
sources: ["Victron Energy, Wiring Unlimited (câbles, fusibles et convertisseurs)", "NF C 15-100, installations électriques à basse tension", "Enedis, danger du retour de tension sur le réseau"]
---

::Un convertisseur de 1 000 W branché sur une batterie de 12 V tire près de 90 ampères : de quoi faire fondre un câble trop fin et mettre le feu au coffre. La plupart des incendies d'installations de fortune viennent de là, pas de la batterie elle-même.::

## À quoi ça sert

Les batteries et les panneaux solaires donnent du **courant continu** (12, 24, 48 V). La maison fonctionne en **230 V alternatif**. Le **convertisseur** (souvent appelé onduleur) fait le passage. Voir [[TEC-ENE-016]].

## Choisir

- **Sinus pur** : un courant aussi propre que celui du réseau. Indispensable pour les moteurs (frigo, pompe), les appareils médicaux, certains chargeurs.
- **Quasi-sinus** : moins cher, il fait chauffer ou grogner les moteurs et abîme certains appareils. Pour des lampes et des outils simples seulement.
- **La puissance** : la somme de ce qu'on branchera en même temps, plus **le pic de démarrage** des moteurs (un frigo demande trois à sept fois sa puissance pendant une seconde).

## Brancher sans danger

- **Des câbles gros et courts** entre la batterie et le convertisseur : la section dépend de l'intensité, pas de la tension.
- **Un fusible** au plus près de la batterie, sur le fil positif.
- **Serrer fort** les cosses : un mauvais contact chauffe.
- **Aérer** : le convertisseur chauffe.
- **L'éteindre** quand il ne sert pas : à vide, il consomme quand même.

## Mieux que le convertisseur

Chaque conversion perd de l'énergie. Tout ce qui peut fonctionner **directement en 12 V** (lampes, chargeurs USB, ventilateurs, frigos de camping-car) gaspille moins. Un chargeur USB branché sur 12 V vaut mieux qu'un chargeur 230 V branché sur un convertisseur.

## Deux pièges

- **L'onduleur d'ordinateur** tient quelques minutes, le temps d'éteindre proprement. Pas des heures.
- **Ne jamais brancher un groupe ou un convertisseur sur une prise de la maison** avec un câble mâle-mâle pour « alimenter le tableau ». Le courant repart sur le réseau et peut électrocuter les techniciens qui réparent la ligne, ou vous. On passe par un inverseur de source posé par un électricien. Voir [[TEC-ENE-013]].
