---
id: TEC-IDE-024
titre: La localisation et les coordonnées
axe: 2
categorie: Information et Données
temps: Court
contexte: 1
risque: Discret
materiel: Rien
priorite: normale
origine: officielle
tags: [position, coordonnees, latitude, longitude, degres decimaux, degres minutes secondes, points repere, autoroute, 112, localisation avancee, aml]
sources: ["IGN, systèmes de coordonnées et carroyages des cartes", "Commission européenne, localisation avancée des appels au 112", "Réseau autoroutier français, bornes d'appel d'urgence et points repères"]
---

::Une erreur de format dans des coordonnées, et un hélicoptère cherche à plusieurs kilomètres. Sur les routes françaises, de petits panneaux numérotés au bord de la voie, les points repères, situent un véhicule à cent mètres près. Pour les secours, savoir où se trouve la victime est souvent la moitié du travail.::

## Les coordonnées géographiques

- **La latitude** mesure la position au nord ou au sud de l'équateur, **la longitude** à l'est ou à l'ouest du méridien de Greenwich. On donne toujours la latitude en premier.
- **Deux écritures coexistent**, et les confondre est une erreur classique :
  - les **degrés décimaux** : 48,8584 N et 2,2945 E ;
  - les **degrés, minutes et secondes** : 48° 51' 30" N et 2° 17' 40" E.
- **La précision** : un degré de latitude représente environ 111 km ; la troisième décimale, une centaine de mètres ; la cinquième, environ un mètre.
- **Le GPS du téléphone** calcule sa position sans réseau téléphonique, grâce aux satellites. Voir [[TEC-ELN-010]].

## La localisation automatique des appels

Dans l'Union européenne, la plupart des smartphones envoient automatiquement leur position aux centres d'urgence lors d'un appel au 112, par un système appelé localisation avancée (AML), bien plus précis que la position approximative donnée par l'antenne.

## Les repères sans coordonnées

- **Sur route et autoroute** : nom de la route, sens de circulation, dernière sortie ou dernier village, et point repère. Les bornes d'appel d'urgence des autoroutes indiquent automatiquement leur emplacement.
- **En montagne et en forêt** : nom du sentier, poteau indicateur, altitude, éléments visibles (lac, sommet, refuge).
- **En ville** : rue, numéro, étage, code d'accès, repère visible.
- **Les éléments marquants** : pylône, antenne, rivière, couleur d'un bâtiment.

## Être trouvé

Les secours recommandent de rester à l'endroit indiqué, de se rendre visible (couleur vive, lumière, miroir, feu) et de garder le téléphone allumé en économisant sa batterie. Voir [[SIG-COM-001]] et [[SIG-COM-013]].

Lire une carte : [[SURV-ORI-002]]. Perdu : [[URG-PERDU-001]].
