---
id: TEC-ELN-005
titre: La soudure à l'étain
axe: 2
categorie: Électronique et Numérique
temps: Court
contexte: 1
risque: Discret
materiel: Rien
priorite: normale
origine: officielle
tags: [soudure, brasage tendre, fer a souder, etain, plomb, flux, soudure froide, dessoudage, rohs, electronique, reparation]
sources: ["IPC-A-610, Acceptability of Electronic Assemblies (aspect des soudures)", "Adafruit Learning System, Adafruit Guide to Excellent Soldering", "INRS, fumées de soudage à l'étain et flux"]
---

::Ce qu'on appelle soudure en électronique est en réalité un brasage : un alliage fondu, l'étain, mouille deux métaux et les relie en refroidissant, sans les faire fondre eux-mêmes. C'est ainsi que sont fixés tous les composants d'un circuit. La plupart des soudures ratées le sont pour une raison simple : l'étain a été fondu sur le fer, et non sur les pièces à relier.::

## Comment ça tient

- **L'étain fondu mouille les métaux chauds et propres** : il s'étale, s'infiltre et forme en refroidissant une couche d'alliage avec le cuivre. Le lien est à la fois mécanique et électrique.
- **Le flux**, une résine contenue au cœur du fil d'étain, dissout l'oxyde qui recouvre les métaux et empêche l'étain d'accrocher. Sans flux, l'étain roule en boule.
- **La chaleur doit être dans les pièces** : l'étain fond au contact des pièces chaudes et coule autour d'elles. Fondu sur la panne puis déposé, il se fige sans avoir mouillé.

## Les alliages

- **L'étain-plomb** (60 % d'étain, 40 % de plomb) fond vers 183 à 190 °C et se travaille facilement.
- **L'étain sans plomb**, imposé dans l'électronique vendue dans l'Union européenne depuis 2006, fond vers 217 à 220 °C et demande un fer plus chaud.
- **Le fer** d'électronique fait de 25 à 60 W et travaille en général entre 320 et 370 °C.

## Reconnaître une soudure

- **Une bonne soudure** est brillante, lisse, en forme de petit cône qui épouse la patte du composant et la pastille.
- **Une soudure froide** est terne, granuleuse, en boule posée dessus : le lien électrique est mauvais ou intermittent, et elle finit par lâcher. C'est une cause classique de pannes qui vont et viennent.
- **Un pont** est une goutte d'étain qui relie deux pastilles voisines : un court-circuit.

## Le dessoudage

La tresse à dessouder, un ruban de cuivre imprégné de flux, aspire l'étain fondu par capillarité ; la pompe à dessouder l'aspire d'un coup. L'air chaud chauffe toute une zone pour retirer les composants à nombreuses pattes.

## Les risques

- **Les fumées de flux** irritent les voies respiratoires : les postes de soudure sont ventilés ou aspirés.
- **Le plomb** passe par les mains à la bouche : lavage des mains après usage.
- **Le fer** atteint plus de 300 °C : brûlures et départs de feu sur les câbles et les tables.

Vérifier une soudure : [[TEC-ENE-008]]. Réparer un câble sans souder : [[SURV-REC-007]]. Les composants : [[TEC-ELN-013]].
