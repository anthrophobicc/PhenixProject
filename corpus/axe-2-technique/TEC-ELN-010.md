---
id: TEC-ELN-010
titre: Le GPS
axe: 2
categorie: Électronique et Numérique
temps: Court
contexte: 1
risque: Discret
materiel: Rien
priorite: normale
origine: officielle
tags: [gps, galileo, satellites, coordonnees, relativite, brouillage, carte hors ligne, telephone]
sources: ["GPS.gov, US Space Force, fonctionnement et précision du GPS", "Ashby N., Relativity in the Global Positioning System, Living Reviews in Relativity, 2003", "EUSPA, Agence de l'Union européenne pour le programme spatial, Galileo"]
---

::Le GPS de votre téléphone marche sans réseau et sans forfait. Ce qui manque en pleine forêt, ce n'est pas le GPS : c'est la carte, qu'on n'a pas téléchargée.::

## Comment ça marche

Une trentaine de satellites tournent à 20 000 km d'altitude. Chacun porte des **horloges atomiques** et envoie en continu l'heure exacte et sa position.

Le récepteur mesure **combien de temps chaque signal a mis** pour arriver. Avec quatre satellites, il calcule sa position en trois dimensions et corrige sa propre horloge.

**La précision** : environ 5 mètres pour un téléphone, à ciel ouvert. Moins bonne en ville entre les immeubles, en forêt dense, en fond de vallée.

## Einstein dans votre poche

Là-haut, les horloges avancent d'environ **38 millionièmes de seconde par jour** par rapport au sol : la relativité, pour de vrai. Sans correction, la position dériverait d'une dizaine de kilomètres chaque jour.

## Les autres systèmes

Galileo (Europe), GLONASS (Russie), BeiDou (Chine). Les téléphones récents les écoutent tous à la fois : plus rapide, plus précis.

## Bien s'en servir

- **Télécharger la carte avant** de partir. Voir [[TEC-ELN-012]].
- **Économiser la batterie** : mode avion, localisation activée. Le GPS reçoit sans émettre.
- **Noter ses coordonnées** pour les secours : latitude (Nord ou Sud) puis longitude (Est ou Ouest). Paris est vers 48,86 N et 2,35 E.
- **Le premier calcul** peut prendre quelques minutes sans réseau : à l'arrêt, à découvert, patience.

## Ses limites

- **Le brouillage et le leurrage** sont devenus courants près des zones de conflit : des avions de ligne perdent leur GPS chaque jour au-dessus de la Baltique et du Moyen-Orient.
- **Une batterie vide** et il n'y a plus rien.

Toujours une carte papier et une boussole : [[SURV-ORI-002]], [[SURV-ORI-006]].
