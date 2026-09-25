---
id: TEC-MEC-006
titre: Le drone
axe: 2
categorie: Mécanique et Transport
temps: Court
contexte: 1
risque: Discret
materiel: Technique
priorite: normale
origine: officielle
tags: [drone, multiroteur, moteur, brushless, batterie, lipo, GPS, caméra, militaire]
sources: ["Documentation technique sur l'architecture des multiroteurs civils", "Études sur les drones militaires — catégories, systèmes et emploi", "Manuels de pilotage et d'entretien des drones civils"]
---

::Un drone est un robot volant avec des yeux. Quatre hélices, une batterie, un ordinateur qui tient l'équilibre mille fois par seconde, et une caméra qui voit ce que le pilote ne peut pas voir. Comprendre ce qu'il y a dedans, c'est comprendre ce qu'il peut et ce qu'il ne peut pas.::

## COMPRENDRE

### Architecture d'un multiroteur

**Le châssis.** Carbone ou aluminium, en X ou en H. Les bras portent les moteurs ; le centre porte l'électronique et la batterie.

**Les moteurs brushless.** Sans balai, sans frottement mécanique, haute vitesse. Chaque moteur contient des bobines de cuivre (stator) et des aimants permanents en néodyme (rotor). C'est le même moteur qu'on retrouve dans les disques durs, les ventilateurs d'ordinateur et les véhicules électriques — en plus puissant.

**Les ESC (variateurs).** Un par moteur. Ils convertissent le courant continu de la batterie en signal triphasé qui fait tourner le moteur à la vitesse commandée. Sans eux, le moteur ne tourne pas.

**La batterie LiPo.** Lithium polymère — énergie dense, légère, dangereuse si percée ou surchargée (emballement thermique, feu chimique). Tension : 3,7 volts par cellule, assemblées en série (3S = 11,1 V, 4S = 14,8 V, 6S = 22,2 V). Voir [[TEC-ENE-004]].

**Le contrôleur de vol.** Le cerveau. Il contient un accéléromètre, un gyroscope, un magnétomètre (boussole), un baromètre, et souvent un GPS. Il lit les capteurs mille fois par seconde et ajuste la vitesse de chaque moteur pour maintenir la stabilité. Sans lui, un multiroteur est incontrôlable par un humain — le temps de réaction est trop court.

**Le récepteur radio.** Reçoit les ordres du pilote. Portée : quelques centaines de mètres à plusieurs kilomètres selon la puissance et les antennes.

**La caméra.** De la simple caméra HD au capteur thermique ou multispectral. Stabilisée sur une nacelle motorisée (gimbal) qui compense les vibrations.

### Physique du vol

Quatre hélices, dont deux tournent dans un sens et deux dans l'autre — cela annule le couple de rotation. Pour monter : toutes accélèrent. Pour avancer : les hélices arrière accélèrent, les avant ralentissent — le drone s'incline et la poussée le tire en avant. Pour tourner : on accélère les paires qui tournent dans le même sens. Tout cela est calculé par le contrôleur, pas par le pilote.

### Les types de drones

**Multiroteur (civil).** Quatre à huit hélices. Maniable, décollage vertical, vol stationnaire. Autonomie courte : vingt à quarante minutes. C'est le drone de loisir, de photo, d'inspection.

**Aile fixe.** Comme un avion miniature. Longue endurance (une heure et plus), grande vitesse, couverture de surface. Ne peut pas faire de vol stationnaire. Nécessite un lancement (à la main, par catapulte) et un atterrissage (ventre, filet, parachute).

**VTOL.** Hybride — décollage vertical comme un multiroteur, puis transition en vol d'avion. Combine les avantages mais la mécanique est complexe.

**Drones militaires.** Les petits (quelques kilos) sont des multiroteurs de reconnaissance avec caméra thermique. Les moyens (Switchblade, Lancet) sont des munitions rôdeuses — ils volent, repèrent, et frappent une cible. Les grands (Reaper, Bayraktar TB2) sont des avions sans pilote de plusieurs tonnes, motorisés, armés, opérés depuis une station sol à des milliers de kilomètres. Voir [[SURV-REC-014]] et [[SURV-REC-015]].

### Autonomie et automatismes

Un drone civil moderne suit des waypoints GPS, revient au point de décollage si le signal est perdu (return-to-home), évite les obstacles par capteurs. Il n'est pas « autonome » au sens d'une intelligence — il suit un programme. La batterie est le facteur limitant : plus de charge utile = moins d'autonomie, et l'autonomie ne dépasse jamais la capacité de la batterie à fournir du courant.

## AGIR

### Principes de pilotage

Le pilotage se fait à deux sticks. Le stick gauche contrôle l'altitude (monter/descendre) et la rotation (tourner sur place). Le stick droit contrôle l'inclinaison : avant/arrière et gauche/droite. Le contrôleur de vol fait le reste — le pilote indique une intention, l'ordinateur la traduit en commandes moteur.

En mode FPV (First Person View), le pilote porte un masque qui affiche l'image de la caméra embarquée. Il vole comme s'il était à bord. La latence du signal (quelques dizaines de millisecondes) et la portée radio sont les limites.

### Entretien

**Hélices.** Vérifier avant chaque vol. Une hélice ébréchée vibre et fatigue les moteurs. Remplacer par des hélices du même diamètre et pas (angle).

**Moteurs.** Ecouter : un moteur qui gratte a un roulement usé ou un corps étranger. Vérifier que chaque moteur tourne librement et à la même vitesse.

**Batterie.** Ne jamais stocker chargée à fond ou vide — stocker à demi-charge. Ne jamais charger sans surveillance. Une LiPo gonflée est dangereuse : ne plus l'utiliser.

**Calibration.** L'IMU et le compas se dérivent. Recalibrer régulièrement (la procédure est dans le contrôleur de vol).

## ADAPTER

**Le signal GPS est brouillé ou absent.** Le drone perd la stabilisation de position et dérive au vent. Certains contrôleurs passent en mode altitude seule (baromètre) ou en mode manuel. Sans GPS, pas de return-to-home — le perdre de vue, c'est le perdre.

**Vous voulez utiliser un drone trouvé.** Il faut la radiocommande appairée ou pouvoir en appairer une compatible. Sans radiocommande, le drone est inutilisable. En revanche, ses composants se récupèrent : voir [[SURV-REC-014]].

**Le vent est fort.** Un multiroteur se bat contre le vent en s'inclinant — il perd de l'altitude et de l'autonomie. Au-delà de quarante à cinquante kilomètres par heure, la plupart des drones civils sont cloués au sol.

## Ce qu'il faut retenir

**Le contrôleur de vol est le coeur** : sans lui, un multiroteur est une toupie incontrôlable. C'est un ordinateur à capteurs multiples qui fait le travail qu'aucun réflexe humain ne pourrait faire.

**La batterie est le facteur limitant.** Tout se ramène à elle : autonomie, charge utile, portée. Et une LiPo mal traitée prend feu.

**Un drone militaire et un drone civil partagent les mêmes principes** — moteurs, batteries, contrôleur, GPS. Ce qui change, c'est la charge utile, la portée et le prix.
