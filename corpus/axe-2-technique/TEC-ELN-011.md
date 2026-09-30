---
id: TEC-ELN-011
titre: Un réseau local sans internet
axe: 2
categorie: Électronique et Numérique
temps: Long
contexte: 2+
risque: Discret
materiel: Technique
priorite: normale
origine: officielle
tags: [wifi, reseau local, routeur, kiwix, meshtastic, briar, antenne, raspberry pi, hors ligne]
sources: ["Kiwix, documentation de kiwix-serve", "Internet-in-a-Box, documentation", "Meshtastic, documentation", "Briar Project, fonctionnement hors ligne"]
---

::Un routeur WiFi marche très bien sans internet. Il crée un réseau local : tout le monde dans un rayon d'une centaine de mètres peut lire la même encyclopédie, s'envoyer des messages et partager des fichiers. Pour un quartier, un camp ou une école, c'est l'internet qui reste.::

## Ce qu'il faut

- **Un routeur WiFi** ordinaire, ou un téléphone en point d'accès (sans données, il partage quand même le réseau local).
- **Un serveur** : un vieil ordinateur portable ou une petite carte comme un Raspberry Pi.
- **Du courant** : un routeur consomme 5 à 10 W, souvent en 12 V (voir l'étiquette). Une batterie et un petit panneau solaire suffisent.

## Ce qu'on peut y mettre

- **Wikipédia, des livres, des cours** avec Kiwix : le serveur les rend lisibles dans le navigateur de chaque téléphone connecté. Des projets comme Internet-in-a-Box ou RACHEL en font des bibliothèques clés en main pour les écoles sans connexion.
- **Des cartes**, des vidéos de formation, des fiches Phenix.
- **Un partage de fichiers** et une messagerie locale.

## Les réseaux maillés

- **Briar** : une messagerie qui passe par le Bluetooth et le WiFi de téléphone à téléphone, sans serveur ni internet.
- **Meshtastic** : de petits modules radio LoRa, à quelques dizaines d'euros, qui relaient des messages texte de proche en proche sur plusieurs kilomètres, sans licence.

## Aller plus loin

- Un routeur **en hauteur**, au centre de la zone, couvre bien mieux.
- **Une antenne directionnelle** (même bricolée dans une boîte de conserve) relie deux bâtiments à plusieurs kilomètres, en vue directe.
- **Plusieurs routeurs en relais** couvrent un village.

## Précautions

- Un **mot de passe** sur le réseau, et pas d'informations sensibles sur le serveur partagé. Voir [[TEC-ELN-008]].
- Les radios longue portée restent soumises à la réglementation : puissance et fréquences autorisées.

Télécharger les contenus avant : [[TEC-ELN-012]]. Les talkies-walkies : [[SIG-COM-010]].
