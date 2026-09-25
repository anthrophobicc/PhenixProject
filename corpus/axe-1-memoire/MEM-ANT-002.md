---
id: MEM-ANT-002
titre: Les réseaux, la puissance et la fragilité
axe: 1
categorie: L'anthropocène
temps: Long
contexte: 2+
risque: Discret
materiel: Rien
priorite: normale
origine: officielle
tags: [histoire, reseaux, dependance, organisation]
sources: ["Perrow C., Normal Accidents: Living with High-Risk Technologies", "Tainter J., The Collapse of Complex Societies", "Rapports d'analyse sur les grandes pannes de réseaux électriques et logistiques"]
---

::Les grandes pannes de réseau documentées suivent le même déroulement : un incident local, un report de charge, une cascade en quelques minutes.::

## Ce qu'un réseau fait gagner

Relier des points permet à chacun de se spécialiser. Une région produit ce qu'elle produit le mieux, une autre autre chose, et l'échange rend tout le monde plus riche que l'autarcie. C'est le mécanisme décrit dans [[MEM-ECH-001]], et il fonctionne réellement.

Le gain est double. Il y a le gain de spécialisation, et il y a le **gain de mutualisation** : un réseau électrique permet à une région excédentaire de couvrir une région déficitaire, ce qui réduit les capacités à installer partout. Un réseau logistique permet de tenir avec moins de stock, puisqu'on peut être réapprovisionné.

**Le stock est remplacé par le flux.** C'est ce qui rend un système efficace, et c'est aussi ce qui le rend fragile : un stock absorbe une interruption, un flux non.

## Comment une panne se propage

Un réseau ne tombe presque jamais d'un coup. Il tombe par cascade, et le schéma se répète dans des domaines très différents.

Un élément lâche. Sa charge se reporte sur les éléments voisins, qui n'avaient pas de marge, et qui lâchent à leur tour. **La défaillance se propage plus vite que la capacité à réagir.** Les analyses des grandes pannes de réseaux électriques montrent régulièrement ce déroulement : un incident local, un report de charge, une cascade en quelques minutes, et une remise en service qui prend des jours.

Deux propriétés aggravent le phénomène.

**Le couplage serré.** Quand les éléments dépendent les uns des autres sans délai ni tampon, il n'y a aucun temps pour intervenir. Plus un système est optimisé, plus il est couplé serré.

**L'interdépendance croisée.** Les réseaux dépendent les uns des autres : le transport a besoin de carburant, le carburant a besoin d'électricité pour être pompé, l'électricité a besoin de télécommunications pour être pilotée, les télécommunications ont besoin d'électricité. **Une panne dans un réseau se manifeste comme une panne dans un autre**, ce qui rend le diagnostic difficile au moment où il compte.

## Ce que l'histoire ajoute

Cette configuration n'est pas nouvelle. Le système d'échanges de la fin de l'âge du bronze reliait une dizaine de puissances par des flux de métaux, de céréales et d'artisans, chacune plus riche grâce aux autres et incapable de vivre sans elles. Quand quelques nœuds ont cédé, l'ensemble s'est défait en quelques décennies.

Ce qui a changé depuis n'est pas la nature du mécanisme mais **la vitesse et la profondeur du couplage**. Une caravane mettait des mois ; un ordre de paiement met une seconde. Le gain est immense et le délai de réaction a disparu avec lui.

C'est le même arbitrage que celui décrit dans [[MEM-EFF-001]] : chaque gain d'efficacité consomme une marge, et la marge est précisément ce qui absorbe les chocs.

## Les grandes pannes documentées

**Le nord-est américain, 2003.** Une ligne à haute tension entre en contact avec un arbre en Ohio. Un défaut logiciel empêche l'alarme de se déclencher. La charge se reporte sur les lignes voisines, qui déclenchent à leur tour. En quelques minutes, plusieurs dizaines de millions de personnes sont privées d'électricité sur deux pays. Le rétablissement complet prend plusieurs jours.

**L'Italie, la même année.** Un incident sur une ligne d'interconnexion en Suisse isole progressivement le pays du réseau européen. La quasi-totalité du territoire est privée d'électricité en moins d'une demi-heure.

**L'Inde, 2012.** Deux effondrements successifs du réseau en deux jours privent de courant un nombre de personnes estimé à plusieurs centaines de millions.

Dans les trois cas, le rapport d'analyse retient le même enchaînement : un événement initial banal, une marge insuffisante, un report de charge, et une propagation plus rapide que la capacité humaine à intervenir.

## L'interdépendance entre réseaux

Les analyses de ces événements documentent des couplages qui n'apparaissent qu'en situation de panne.

Les **stations de pompage** d'eau potable s'arrêtent sans électricité. Les **stations-service** ne peuvent plus pomper le carburant. Les **télécommunications** tiennent sur batteries pendant une durée limitée, puis s'arrêtent — ce qui empêche le pilotage des autres réseaux. Les **feux de circulation** éteints paralysent les axes, ce qui empêche l'acheminement des équipes de réparation.

Chaque réseau suppose le fonctionnement d'un autre, et le diagnostic devient difficile au moment précis où il compte le plus.

## Le précédent ancien

Le système d'échanges de la Méditerranée orientale à la fin de l'âge du bronze présentait la même structure : des puissances spécialisées, reliées par des flux de métaux, de céréales et d'artisans, chacune plus riche grâce aux autres et incapable de produire seule ce qu'elle consommait. Sa rupture est décrite dans [[MEM-EFF-001]].

Ce qui distingue les deux périodes n'est pas la nature du couplage mais sa vitesse : une caravane mettait des mois, une transaction met une seconde.
