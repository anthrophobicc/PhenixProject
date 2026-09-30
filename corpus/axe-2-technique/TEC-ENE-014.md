---
id: TEC-ENE-014
titre: La recharge d'un téléphone sans réseau électrique
axe: 2
categorie: Énergie et Électricité
temps: Court
contexte: 1
risque: Discret
materiel: Rien
priorite: normale
origine: officielle
tags: [telephone, recharge, autonomie, mode avion, batterie externe, usb, voiture, solaire, dynamo, coupure]
sources: ["USB Implementers Forum, spécifications USB 2.0 et USB Power Delivery (tensions et courants)", "Fiches techniques de batteries externes et de panneaux solaires USB", "Retours d'expérience des coupures longues (tempêtes, séismes)"]
---

::Un téléphone chargé tient plusieurs jours s'il est économisé, et quelques heures s'il cherche sans fin un réseau tombé. Lors des grandes coupures, la recharge des téléphones devient l'un des premiers besoins, avant même la nourriture : c'est par eux que passent les nouvelles et les appels à l'aide.::

## Ce qui vide une batterie

- **La recherche d'un réseau** : quand les antennes sont coupées, le téléphone augmente sa puissance d'émission pour trouver un signal, et vide sa batterie deux à trois fois plus vite. Le mode avion supprime cette consommation.
- **L'écran**, la localisation et les applications en arrière-plan.
- **Le froid** : une batterie au lithium perd une partie de sa capacité disponible quand elle est froide, et la retrouve en se réchauffant.
- **Éteint**, un téléphone ne consomme presque rien.

## Les sources de recharge

- **La batterie externe** : une batterie de 10 000 mAh recharge un téléphone environ deux fois, une de 20 000 mAh environ quatre fois, pertes déduites.
- **La voiture** : un chargeur sur la prise 12 V charge aussi vite qu'une prise murale. Moteur coupé, plusieurs recharges d'affilée peuvent empêcher la voiture de redémarrer ; moteur tournant, le danger est le monoxyde de carbone dans un lieu fermé. Voir [[TEC-MEC-014]].
- **Le panneau solaire USB** : 20 à 30 W en plein soleil rechargent un téléphone en quelques heures, beaucoup moins par temps couvert. Voir [[TEC-SOLR-001]].
- **La dynamo à manivelle** des radios et lampes de secours : quelques minutes de manivelle pour quelques minutes d'appel, pas une recharge complète.
- **Les appareils à batterie** : ordinateurs portables, onduleurs, vélos électriques et outils sans fil, avec l'adaptateur de leur marque, peuvent servir de batterie externe.
- **Les piles** : un boîtier de quatre piles alcalines AA avec sortie USB donne environ une demi-recharge.

## Ce qui ne marche pas

- **La pile au citron ou à la pomme de terre** fournit quelques milliampères, quand un téléphone en demande environ mille. Voir [[SURV-ENE-002]].
- **Un câble USB branché directement sur une batterie de 12 V** : le téléphone attend 5 V ; il faut un convertisseur. Voir [[TEC-ELN-023]].

## La charge d'une batterie au lithium

Les 80 premiers pour cent se chargent vite ; les derniers ralentissent pour protéger la batterie. En situation de crise, une charge partielle et fréquente est donc plus efficace qu'une charge complète.

Le faire soi-même, pas à pas : [[SURV-ENE-003]].
