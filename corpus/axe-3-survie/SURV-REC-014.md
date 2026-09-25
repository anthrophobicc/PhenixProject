---
id: SURV-REC-014
titre: Récupérer sur un drone civil
axe: 3
categorie: Récupération
temps: Court
contexte: 1
risque: Exposé
materiel: Récupération
priorite: normale
origine: officielle
tags: [drone, batterie, lipo, moteur, brushless, caméra, récupération, aimant]
sources: ["Documentation technique sur les composants des multiroteurs civils DJI, Parrot et assimilés", "Manuels de démontage et de réparation de drones grand public"]
---

::Un drone civil au sol est une batterie, quatre moteurs, une caméra et un ordinateur — le tout dans un kilo ou deux. Chaque composant a une seconde vie, et certains n'existent nulle part ailleurs aussi concentrés.::

## COMPRENDRE

### Ce qu'il y a dans un drone civil

Un multiroteur grand public (DJI, Parrot, FPV) est un assemblage de composants de haute qualité, légers et compacts. Voir [[TEC-MEC-006]] pour le fonctionnement.

## AGIR

### Inventaire par composant

**Batterie LiPo.** C'est le composant le plus précieux. Lithium polymère, haute densité d'énergie, rechargeable. Tension de 11,1 a 22,2 volts selon le modèle. Utilisable pour alimenter des appareils basse tension (lampes LED, radios, chargeurs de téléphone via un convertisseur). **Danger** : une LiPo percée, gonflée ou déformée peut s'enflammer spontanément. Ne pas percer, écraser ou court-circuiter. Voir [[TEC-ENE-004]].

**Moteurs brushless.** Quatre à huit par drone. Bobines de cuivre, aimants permanents en néodyme. Les aimants de néodyme sont les aimants les plus puissants disponibles — récupérables pour fabriquer des générateurs, des capteurs, des fermetures magnétiques, ou simplement pour accrocher du métal. Le cuivre des bobines se récupère en démontant le stator. En faisant tourner un moteur brushless (à la main, par le vent, par l'eau), il produit du courant : c'est un générateur. Voir [[TEC-ENE-001]].

**Hélices.** Carbone ou plastique renforcé. Les pales en carbone sont des lames rigides et légères — utilisables comme spatule, racloir, attelle de doigt. Les pales en plastique sont plus souples mais tranchantes au bout.

**Caméra et nacelle.** La caméra contient une lentille de verre de qualité (loupe, concentration de lumière — voir [[TEC-SAN-007]]), un capteur CMOS (inutile sans circuit), et un moteur de nacelle (petit brushless de précision, récupérable). Le câble de la caméra contient du cuivre fin.

**ESC (variateurs).** Circuits imprimés contenant des MOSFET de puissance, des condensateurs et des régulateurs de tension. Les composants individuels se dessoudent pour d'autres projets electroniques.

**Contrôleur de vol.** Circuit imprimé miniature. Contient un accéléromètre, un gyroscope et un baromètre MEMS — composants trop petits pour être récupérés individuellement, mais le circuit entier peut servir de plateforme de capteurs si on sait le reprogrammer. Le module GPS, lui, est récupérable si compatible avec d'autres systèmes.

**Châssis.** Les bras en carbone sont des tiges rigides et légères, utilisables comme attelle, structure, renfort. Le carbone ne se plie pas — il casse net, et les éclats coupent.

**Câblage et connecteurs.** Connecteurs XT60 ou XT30 soudés sur fil de cuivre de fort calibre — réutilisables tels quels pour tout circuit de puissance.

### Réparer un drone trouvé

**Hélice cassée.** Remplacer par une hélice de même diamètre et même pas. Le sens de rotation (CW ou CCW) est marqué — l'inverser fait chuter le drone.

**Moteur bloqué.** Roulement grippé ou débris coincé. Démonter la cloche (les aimants sont collés dedans), nettoyer, remonter.

**Batterie morte.** Mesurer la tension de chaque cellule. En dessous de 3,0 V par cellule, la LiPo est souvent irrécupérable — les cellules au lithium se dégradent irréversiblement quand elles se vident complètement.

**Pas de radiocommande.** Sans la radiocommande appairée, le drone est inopérable. Certains contrôleurs de vol open source (Betaflight, ArduPilot) acceptent n'importe quel récepteur compatible — mais il faut le savoir et le matériel pour rebinder.

## ADAPTER

**Vous avez plusieurs drones endommagés.** Cannibaliser : prendre les pièces fonctionnelles de chacun pour en assembler un qui vole. C'est la logique de [[SURV-REC-001]] appliquée à l'électronique.

**Vous voulez juste l'énergie.** La batterie LiPo + un petit convertisseur DC-DC (récupérable dans un chargeur USB de voiture) donne une alimentation portable pour téléphone, lampe, radio.

## Ce qu'il faut retenir

**La batterie est le trésor.** Rechargeable, dense en énergie, compatible avec beaucoup d'usages via un convertisseur.

**Les moteurs sont des générateurs.** Faites-les tourner et ils produisent du courant. Plus les aimants sont gros, plus le courant est fort.

**Les aimants en néodyme ne se trouvent pas ailleurs aussi facilement.** Quatre moteurs, huit aimants au minimum — c'est un stock d'aimants puissants dans un objet d'un kilo.
