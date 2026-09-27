---
id: TEC-ELN-005
titre: Souder en électronique
axe: 2
categorie: Électronique et Numérique
temps: Court
contexte: 1
risque: Discret
materiel: Technique
priorite: normale
origine: officielle
tags: [soudure, fer a souder, etain, flux, electronique, reparation, dessoudage, cable]
sources: ["IPC-A-610, Acceptability of Electronic Assemblies (aspect des soudures)", "Adafruit Learning System, Adafruit Guide to Excellent Soldering", "INRS, fumées de soudage à l'étain et flux"]
---

::Une bonne soudure se fait en trois secondes : on chauffe les deux pièces, on apporte l'étain sur elles, pas sur le fer, et il coule tout seul. La plupart des soudures ratées l'ont été parce qu'on a fait fondre l'étain sur la panne.::

## Le matériel

- **Un fer à souder** de 25 à 60 watts, idéalement à température réglable (320 à 370 °C selon l'étain).
- **De l'étain à âme décapante** (le flux est à l'intérieur du fil) : l'étain au plomb (60/40) fond plus bas et se travaille plus facilement ; l'étain sans plomb demande un peu plus de chaleur.
- **Une éponge humide** ou de la laine de laiton pour nettoyer la panne.
- **De la tresse à dessouder** ou une pompe à dessouder.
- **De la gaine thermorétractable** pour isoler les raccords de fils.

## Le geste

1. **Nettoyez et étamez la panne** : une fine couche d'étain brillant dessus aide la chaleur à passer.
2. **Posez la panne contre les deux pièces à la fois** (la patte du composant et la pastille du circuit, ou les deux fils).
3. **Après une à deux secondes, apportez l'étain sur les pièces**, de l'autre côté de la panne : il fond au contact des pièces chaudes et coule autour.
4. **Retirez l'étain, puis le fer**, sans bouger la pièce pendant que ça refroidit.

**Une bonne soudure** est brillante, lisse, en forme de petit cône ou de volcan, qui épouse la patte. **Une mauvaise** est terne, granuleuse, en boule posée dessus : c'est une soudure froide, qui lâchera.

## Relier deux fils

1. Dénudez 1 cm, enfilez d'abord la gaine thermorétractable sur l'un des fils.
2. **Étamez chaque fil** séparément.
3. Torsadez-les ou mettez-les côte à côte, chauffez, ajoutez un peu d'étain.
4. Faites glisser la gaine sur la soudure et chauffez-la pour qu'elle se resserre.

## Dessouder

La tresse posée sur la soudure, la panne par-dessus : l'étain fondu remonte dans la tresse par capillarité. Coupez la partie pleine et recommencez.

## Les astuces

- **Aérez** : les fumées de flux irritent les poumons. Travaillez près d'une fenêtre ou avec un petit ventilateur qui les éloigne.
- **Lavez-vous les mains** après avoir manipulé de l'étain au plomb.
- **Posez toujours le fer sur son support** : il brûle la main, la table et les câbles.
- **Sans fer électrique** : une grosse tige de cuivre ou un clou épais chauffé sur un réchaud permet quelques soudures de dépannage sur de gros fils.
- **Récupérer des composants** sur une carte : chauffez chaque patte et tirez doucement, ou chauffez toute la zone à l'air chaud.

Réparer un câble sans souder : [[SURV-REC-007]]. Le multimètre pour vérifier : [[TEC-ENE-008]].
