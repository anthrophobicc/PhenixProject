---
id: TEC-ELN-007
titre: La sauvegarde des données
axe: 2
categorie: Électronique et Numérique
temps: Court
contexte: 1
risque: Discret
materiel: Rien
priorite: normale
origine: officielle
tags: [sauvegarde, donnees, regle 3-2-1, disque dur, ssd, cle usb, cloud, papier, restauration, archives]
sources: ["ANSSI, recommandations de sauvegarde pour les particuliers et les TPE", "US-CERT (CISA), Data Backup Options", "Backblaze, études de fiabilité des disques durs"]
---

::Une donnée qui n'existe qu'à un seul endroit attend de disparaître. Un téléphone volé, un disque qui lâche, un incendie, un rançongiciel, et dix ans de photos et de papiers s'en vont. Les professionnels de l'informatique résument la protection en trois chiffres : 3-2-1.::

## La règle du 3-2-1

- **Trois copies** de ce qui compte ;
- **sur deux supports différents**, pour ne pas dépendre d'une seule technologie ;
- **dont une ailleurs** que chez soi, pour survivre à un vol ou un incendie.

## Ce qui se sauvegarde en priorité

Les papiers (pièces d'identité, titres de propriété, contrats, diplômes, dossiers médicaux, scannés ou photographiés), les photos de famille, les contacts, les codes de récupération des comptes importants, les documents de travail et les bibliothèques de connaissances hors ligne.

## Les supports et leur durée

| Support | Usage | Faiblesse |
|---|---|---|
| Disque dur externe | Grosses sauvegardes | Mécanique fragile : une chute peut le détruire. Les études de fiabilité montrent quelques pour cent de pannes par an |
| SSD, clé USB, carte SD | Transport, petites copies | Débranchés pendant des années, surtout au chaud, ils peuvent perdre des données |
| Stockage en ligne | La copie « ailleurs » | Dépend d'internet et d'une entreprise ; les données sensibles gagnent à être chiffrées |
| Papier | L'essentiel vital | Le seul support lisible sans électricité ni appareil |
| Disque optique d'archivage | Longue durée | Lecteurs de plus en plus rares |

## Le papier, dernier recours

Les services de sécurité civile recommandent de garder sur papier, dans une enveloppe étanche et en double chez un proche : les numéros de téléphone essentiels, les traitements et allergies de chacun, les copies des pièces d'identité, les codes de récupération des comptes principaux et les points de rendez-vous de la famille. Voir [[SURV-CRI-022]].

## Ce qui fait une vraie sauvegarde

- **L'automatisation** : les sauvegardes faites « quand on y pense » ne se font pas.
- **La restauration testée** : une sauvegarde qu'on ne sait pas relire ne vaut rien.
- **La séparation** : une sauvegarde toujours branchée à l'ordinateur est chiffrée en même temps que lui par un rançongiciel.

Les mots de passe : [[TEC-ELN-008]]. L'USB et les clés : [[TEC-ELN-023]].
