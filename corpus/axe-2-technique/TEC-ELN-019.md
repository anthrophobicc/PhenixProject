---
id: TEC-ELN-019
titre: Les microcontrôleurs
axe: 2
categorie: Électronique et Numérique
temps: Court
contexte: 1
risque: Discret
materiel: Technique
priorite: normale
origine: officielle
tags: [microcontroleur, arduino, esp32, programmation, arrosage automatique, capteurs, relais, lora, basse consommation]
sources: ["Banzi M., Shiloh M., Getting Started with Arduino, 4e édition, Make Community, 2022", "Espressif Systems, documentation de l'ESP32", "Meshtastic, documentation"]
---

::En 2005, dans une école de design d'Ivrea, en Italie, des enseignants créent une petite carte électronique bon marché pour que leurs étudiants, qui n'étaient pas ingénieurs, puissent faire clignoter une lampe ou tourner un moteur : l'Arduino. Aujourd'hui, pour le prix d'un café, une carte avec WiFi mesure, décide et commande, en consommant presque rien.::

## Ce que c'est

Un **microcontrôleur** est un tout petit ordinateur sur une seule puce, qui fait **une seule chose, en boucle, pour toujours** :

1. **Lire** des capteurs (température, humidité, niveau d'eau, lumière). Voir [[TEC-ELN-020]].
2. **Décider** selon un petit programme.
3. **Agir** : allumer une lampe, ouvrir une vanne, lancer une pompe, envoyer un message.

Il consomme **quelques milliwatts** à un watt : une petite batterie et un panneau solaire suffisent.

## Les cartes courantes

- **Arduino** : la plus simple pour apprendre, des milliers d'exemples.
- **ESP32** : quelques euros, avec **WiFi et Bluetooth**.
- **Les cartes LoRa** : elles envoient de petits messages à plusieurs kilomètres. Voir [[TEC-ELN-011]].

## Ce qu'on en fait

- **L'arrosage automatique** : un capteur d'humidité du sol commande une électrovanne ou une pompe. Voir [[TEC-AGR-008]].
- **La serre** : alarme de gel ou de surchauffe, ouverture d'un aérateur. Voir [[TEC-AGR-011]].
- **La citerne** : niveau d'eau affiché ou envoyé au téléphone.
- **La batterie** : surveillance de la tension, coupure avant qu'elle ne se vide trop. Voir [[TEC-ENE-016]].
- **Le poulailler** : une porte qui s'ouvre au lever du jour et se ferme à la nuit.
- **Une station météo** simple.

## Apprendre

- **Le logiciel** pour programmer est gratuit ; les exemples fournis montrent presque tout.
- **Commencer en basse tension** (5 V, 12 V). Pour commander du 230 V, uniquement des modules relais sous boîtier, avec protection. Voir [[TEC-ENE-003]].
- **Télécharger** la documentation et les exemples pendant qu'on a internet. Voir [[TEC-ELN-012]].

Les composants : [[TEC-ELN-013]]. Souder : [[TEC-ELN-005]].
