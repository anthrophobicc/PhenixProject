---
id: TEC-IDE-009
titre: Les appareils Phenix
axe: 2
categorie: Information et Données
temps: Long
contexte: 1
risque: Discret
materiel: Technique
priorite: normale
origine: officielle
tags: [phenix, appareil, esp32, borne, wifi, carte sd, prototype, documentation, fabrication]
sources: ["Dépôt du projet Phenix : materiel/phenix-001-v0/LISEZMOI.md, borne-sans-sd.ino, borne.ino, ecran.ino", "Espressif Systems, ESP32-C3 Series Datasheet et documentation arduino-esp32", "Andy Brown, Generic Nokia LCD hacking board (brochage des écrans de téléphones Nokia)"]
---

::Un appareil Phenix doit pouvoir se construire avec des pièces qu'on trouve partout, se réparer avec un fer à souder, et tenir la bibliothèque entière dans la poche. Tout est ouvert : les plans, le code, les erreurs.::

**Tout ce qui suit est au stade de prototype.** Rien n'est vendu. Les rendus 3D des appareils sont des concepts ; seule la borne WiFi a déjà fonctionné sur un vrai téléphone.

## Les deux appareils

**Phenix 001, le petit.** Un lecteur de poche, pas plus gros qu'une petite télécommande, qui contient toute la bibliothèque sur une carte mémoire et l'affiche sur un petit écran économe. Pièces courantes, boîtier qu'on ouvre avec un tournevis, batterie remplaçable.

**Phenix 002, le grand.** Un appareil plus grand, avec un écran couleur assez large pour lire des cartes. Deux fentes pour cartes mémoire sous une trappe en caoutchouc : il peut **lire la carte d'un Phenix 001, vérifier sa bibliothèque et réparer les fiches abîmées**. Des modules s'y branchent sur des broches : panneau solaire, dynamo, lampe. Et un Phenix cassé doit pouvoir repartir sur un écran de récupération, même celui d'un vieux terminal de paiement.

## Ce qui existe déjà : la borne Phenix

C'est le premier prototype qui marche. Une carte électronique de quelques euros ouvre un réseau WiFi nommé **Phenix**, sans mot de passe. **N'importe quel téléphone qui s'y connecte ouvre toute la bibliothèque**, sans internet, sans rien installer : la page s'affiche d'elle-même, comme le portail WiFi d'un hôtel.

**Les pièces**

| Pièce | Rôle | Prix indicatif |
|---|---|---|
| ESP32-C3 « Super Mini » | Le cerveau et le WiFi | 3 à 5 € |
| Câble USB-C | Alimentation et programmation | déjà chez vous |
| Batterie externe (powerbank) | Autonomie | déjà chez vous |
| Module carte micro SD (facultatif) | Pour une bibliothèque plus grosse | 1 à 2 € |

**Deux versions**

- **Sans carte SD** : l'application complète, compressée (moins d'un mégaoctet), est écrite directement dans la mémoire de la carte. Rien à souder. C'est la version qui a fonctionné.
- **Avec carte SD** : la bibliothèque est sur une carte micro SD en FAT32, préparée sur l'ordinateur. Branchements : CS sur GPIO7, MOSI sur GPIO6, SCK sur GPIO4, MISO sur GPIO5, plus 3,3 V et masse.

**La fabriquer**

1. Installer **Arduino IDE 2**, ajouter les cartes ESP32 d'Espressif, choisir la carte **ESP32C3 Dev Module**.
2. Dans le menu Outils : **Partition Scheme : Huge APP**, et **USB CDC On Boot : Enabled**.
3. Ouvrir le programme de la borne, dans le dossier **materiel/phenix-001-v0** du dépôt, et téléverser.
4. Si le téléversement ne démarre pas : débrancher, **garder le bouton BOOT appuyé**, rebrancher, relâcher, recommencer.
5. Sur le téléphone : réglages WiFi, réseau **Phenix**. Si la page ne s'ouvre pas seule, taper **192.168.4.1** dans le navigateur.

## Ce qui a été essayé, et ce qu'on en a appris

**L'écran d'un vieux téléphone Nokia** : l'idée était de réutiliser l'écran couleur d'un téléphone mort. Deux obstacles l'ont arrêtée : un connecteur de 24 broches espacées de 0,4 mm, presque impossible à souder sans matériel fin, et un rétroéclairage qui demande environ 13 volts. **Leçon** : pour un appareil que tout le monde doit pouvoir refaire, un module d'écran vendu pour les microcontrôleurs, déjà monté sur sa petite carte, vaut mieux qu'une pièce de récupération exotique. Voir [[TEC-ELN-001]].

**La suite prévue** : un écran couleur de 2,8 pouces avec lecteur de carte SD intégré, ou un écran à **encre électronique** de 2,9 pouces, qui garde sa page sans courant et se lit en plein soleil, voir [[TEC-ELN-003]].

## Les principes qui guident la conception

- **Des pièces qu'on trouve partout**, en ligne comme dans les magasins d'électronique, et qu'on peut remplacer une par une.
- **Tout est documenté** : schémas, code, liste des pièces, dans le dépôt public. Un appareil dont personne ne connaît l'intérieur ne se répare pas.
- **La bibliothèque reste lisible sans l'appareil** : ce sont les mêmes fichiers texte que partout ailleurs. Une carte SD sortie d'un Phenix cassé se lit sur n'importe quel ordinateur.
- **L'énergie d'abord** : un appareil qui doit tenir loin des prises choisit ses composants pour leur consommation avant leur puissance.

Le projet dans son ensemble est présenté dans [[TEC-IDE-008]].
