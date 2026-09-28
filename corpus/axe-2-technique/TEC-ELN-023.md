---
id: TEC-ELN-023
titre: L'USB
axe: 2
categorie: Électronique et Numérique
temps: Court
contexte: 1
risque: Discret
materiel: Technique
priorite: normale
origine: officielle
tags: [usb, usb-c, cable, prise, 5 volts, power delivery, charge, cle usb, otg, fat32, exfat, badusb, batterie externe]
sources: ["USB Implementers Forum (USB-IF), spécifications USB 2.0, USB 3.2, USB4 et USB Power Delivery", "USB-IF, Battery Charging Specification, révision 1.2, 2010", "Directive (UE) 2022/2380 du 23 novembre 2022 relative au chargeur universel", "Wikipédia, article « Universal Serial Bus »"]
---

::Avant 1996, chaque appareil avait sa prise : clavier, souris, imprimante, modem. L'USB les a tous remplacées, et depuis fin 2024, dans l'Union européenne, tout téléphone neuf se charge en USB-C. Savoir ce qui passe dans ce câble, c'est pouvoir recharger, réparer et lire des données avec presque n'importe quoi.::

## Ce qui passe dans le câble

- **En USB 2.0, quatre fils** : rouge, le +5 V ; noir, la masse ; vert et blanc, les données (D+ et D−). Les câbles bon marché ne respectent pas toujours les couleurs : on vérifie au multimètre.
- **L'USB 3 ajoute deux paires** pour le haut débit. Un port bleu à l'intérieur est presque toujours de l'USB 3.
- **L'USB-C** a 24 broches, se branche dans les deux sens, et possède des broches qui servent à négocier la puissance.

## Les versions

| Nom | Année | Débit maximal |
|---|---|---|
| USB 1.1 | 1998 | 12 Mbit/s |
| USB 2.0 | 2000 | 480 Mbit/s |
| USB 3.0, devenu 3.2 Gen 1 | 2008 | 5 Gbit/s |
| USB 3.1, devenu 3.2 Gen 2 | 2013 | 10 Gbit/s |
| USB 3.2 Gen 2x2 | 2017 | 20 Gbit/s |
| USB4 | 2019 | 40 Gbit/s |
| USB4 version 2 | 2022 | 80 Gbit/s |

En pratique, une clé USB 2.0 copie autour de 30 Mo par seconde, bien moins que son maximum théorique.

## Les prises

- **Type A** : le rectangle plat des ordinateurs et des chargeurs.
- **Type B** : le carré des imprimantes.
- **Mini-B** : vieux appareils photo, GPS.
- **Micro-B** : téléphones Android d'avant 2017 environ, liseuses, lampes. La version large, en USB 3, équipe les disques durs externes.
- **Type C** : ovale et réversible, sur les téléphones et les ordinateurs récents.
- **Lightning**, la prise des anciens iPhone, n'est pas de l'USB : Apple est passé à l'USB-C en 2023.

## La puissance

- **Un port USB 2.0 donne 5 V et 0,5 A**, soit 2,5 W ; un port USB 3, 0,9 A. Un chargeur dédié monte à 1,5 A.
- **L'USB-C donne 5 V et 3 A** (15 W) sans négociation.
- **Avec Power Delivery**, le chargeur et l'appareil négocient une tension plus haute : jusqu'à 20 V et 5 A (100 W), et 48 V (240 W) depuis 2021. Le chargeur ne monte que si l'appareil le demande : on peut brancher un téléphone sur le chargeur d'un ordinateur.
- **Au-delà de 3 A**, il faut un câble 5 A qui contient une puce d'identification. Un câble ordinaire plafonne à 60 W.

## Les sources d'alimentation

- **La tension d'un port USB classique** doit rester entre 4,75 et 5,25 V.
- **Une batterie externe de 10 000 mAh** stocke environ 37 Wh : à peu près deux recharges de téléphone, une fois les pertes déduites. Voir [[TEC-ENE-004]].
- **Les prises USB de voiture** abaissent le 12 V du véhicule à 5 V. Voir [[TEC-MEC-014]].
- **Les panneaux solaires USB** pliants délivrent directement du 5 V. Voir [[TEC-SOLR-001]].
- **Comment un téléphone sait qu'il peut tirer plus de 0,5 A** : selon la norme de charge, un chargeur dédié relie entre eux les fils de données D+ et D−. Les iPhone attendent d'autres tensions sur ces fils, propres à Apple.

## Les données

- **Un téléphone lit une clé USB** : une clé USB-C, ou un petit adaptateur OTG pour les prises micro-USB. Photos, PDF, et fiches Phenix au format .md, que l'application importe hors ligne.
- **Le format de la clé** : FAT32 est lu partout mais refuse les fichiers de plus de 4 Go ; exFAT accepte les gros fichiers et se lit sur presque tous les appareils récents ; NTFS pour Windows ; ext4 pour Linux. Pour échanger avec n'importe qui : exFAT. Pour un vieil autoradio : FAT32.
- **L'éjection avant retrait** sert à écrire les dernières données gardées en mémoire tampon ; une clé arrachée en pleine écriture peut perdre des fichiers.
- **Une clé n'est pas une archive** : sans courant pendant des années, surtout au chaud, la mémoire flash perd ses données. Voir [[TEC-ELN-007]].

## Les risques

- **Les clés piégées** : une clé peut se faire passer pour un clavier et taper des commandes en une seconde (attaque dite BadUSB). D'autres, les « USB killers », envoient une décharge qui grille le port. Une clé trouvée est l'appât classique.
- **Les prises USB publiques** des gares et des aéroports peuvent être trafiquées pour lire un téléphone. Un chargeur branché sur une prise électrique, ou un câble sans fils de données, supprime ce risque.
- **Le câble « charge seule »** n'a pas de fils de données : un téléphone branché à un ordinateur charge mais n'apparaît pas.
- **Un téléphone qui charge mal** a très souvent des peluches de poche tassées au fond de sa prise, qui empêchent le connecteur d'entrer à fond. Voir [[TEC-ELN-018]].

Comment marche un téléphone : [[TEC-ELN-017]].
