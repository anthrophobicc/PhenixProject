# Phenix 001 v0, avec ce que tu as

Deux montages, un seul ESP32-C3 (tu le reflashes entre les deux) :

1. **La borne** : ESP32-C3 + carte SD. Elle ouvre un WiFi « Phenix » et n'importe quel téléphone lit toute l'appli, sans internet. Le plus simple, à faire en premier.
2. **L'écran** : ESP32-C3 + l'écran de ton Nokia 6300. Les 189 fiches sont dans la mémoire de l'ESP32, deux boutons pour naviguer.

Pour tout réunir dans un seul boîtier (écran + carte SD + 5 boutons), il faudra un ESP32-S3 : l'ESP32-C3 n'a pas assez de broches. Le code reste le même.

## Sur l'ordinateur, une fois

1. Installer Arduino IDE 2 (arduino.cc).
2. Fichier > Préférences > URL de cartes supplémentaires : `https://espressif.github.io/arduino-esp32/package_esp32_index.json`
3. Gestionnaire de cartes : installer **esp32** (Espressif). Carte : **ESP32C3 Dev Module**. Outils > **USB CDC On Boot : Enabled**.
4. Si le téléversement ne démarre pas : débrancher, garder **BOOT** appuyé, rebrancher, relâcher, téléverser.

## 1. La borne (ESP32-C3 + carte SD)

### La carte SD sans lecteur : l'adaptateur SD

Prends l'adaptateur SD (celui dans lequel on glisse une micro SD) et soude des fils sur ses contacts dorés. En partant du **coin coupé**, les contacts sont dans cet ordre : 9, 1, 2, 3, 4, 5, 6, 7, 8.

| Contact SD | Rôle | ESP32-C3 |
|---|---|---|
| 1 | CS | GPIO7 |
| 2 | MOSI | GPIO6 |
| 3 | GND | GND |
| 4 | 3,3 V | 3V3 |
| 5 | SCK | GPIO4 |
| 6 | GND | GND |
| 7 | MISO | GPIO5 |
| 8, 9 | rien | |

Si tu as un module lecteur micro SD pour Arduino : mêmes broches (CS, MOSI, SCK, MISO). S'il porte un régulateur, alimente-le par le 5V de l'ESP32 ; sinon par le 3V3.

### Préparer la carte

1. Sur le PC : `node outils/carte-sd.js`. Il crée `sortie-sd/` (1,5 Mo).
2. Carte SD formatée en **FAT32** (32 Go au plus). Copier **le contenu** de `sortie-sd/` à la racine de la carte.

### Flasher et tester

1. Ouvrir `materiel/phenix-001-v0/borne/borne.ino`, téléverser.
2. Moniteur série (115200) : « Carte SD : … Mo » puis « WiFi Phenix ouvert ».
3. Téléphone : WiFi **Phenix**. La page s'ouvre toute seule (sinon : `http://192.168.4.1`). « Ouvrir la bibliothèque » : toute l'appli, hors ligne.

## 2. L'écran du Nokia 6300

Écran 2 pouces, 240 × 320, contrôleur MC2PA8201, bus 8 bits, logique en **3,3 V maximum**. Connecteur JST 24R-JANK-GSAN-TF, 24 broches au pas de **0,4 mm** (c'est la partie dure).

### Souder le connecteur

- Le plus propre : dessouder le connecteur femelle de la carte du Nokia (air chaud ou beaucoup de flux et deux fers), puis souder des fils sur ses pattes. Ou commander le connecteur (référence ci-dessus).
- Les fils : du **fil émaillé** de 0,1 à 0,2 mm, récupéré sur un moteur de drone ou une bobine de haut-parleur. Étame les bouts à 380 °C, le vernis fond. Loupe, flux, pointe fine.
- **Repérer la broche 1** au multimètre (continuité) : les broches 4, 7, 16 et 21 sont toutes reliées entre elles (masses). Si ce n'est pas le cas, tu lis le connecteur à l'envers.

### Branchements

| Broche écran | Signal | ESP32-C3 |
|---|---|---|
| 6 | D0 | GPIO0 |
| 18 | D1 | GPIO1 |
| 8 | D2 | GPIO2 |
| 17 | D3 | GPIO3 |
| 9 | D4 | GPIO4 |
| 15 | D5 | GPIO5 |
| 10 | D6 | GPIO6 |
| 14 | D7 | GPIO7 |
| 5 | WR | GPIO10 |
| 19 | RS | GPIO20 |
| 12 | RESET | GPIO21 |
| 11 | CS | GND |
| 20 | RD | 3V3 |
| 3 | VDDI | 3V3 |
| 22 | VDD | 3V3 |
| 4, 7, 16, 21 | GND | GND |
| 13 | TE | rien |

Boutons : un bouton entre **GPIO8** et GND (BAS). Le bouton **BOOT** de la carte sert de OK.

### Le rétroéclairage (sinon l'écran reste noir)

Quatre LED blanches en série : il faut environ 13 V et 20 mA.

- Relier la broche **1** à la broche **23**.
- Broche **2** au GND.
- Broche **24** : le + d'un **chargeur d'ordinateur portable (19 V)** à travers une **résistance de 330 Ω**. Le − du chargeur au GND.
- **Jamais** le 19 V sur une autre broche : il grille l'écran et l'ESP32.
- En portable plus tard : un module MT3608 (boost) réglé à 14 V au multimètre **avant** de brancher, avec 68 Ω.

### Flasher et tester

1. Gestionnaire de bibliothèques : installer **Adafruit GFX Library** et **U8g2_for_Adafruit_GFX**.
2. Outils > Partition Scheme : **Huge APP (3MB No OTA/1MB SPIFFS)**.
3. Ouvrir `materiel/phenix-001-v0/ecran/ecran.ino`, téléverser (la bibliothèque, 1 Mo de texte, est dans `fiches.h`).
4. Au démarrage : **trois bandes rouge, verte, bleue**. Si tu les vois, l'écran est bon. Puis la liste des fiches, urgences en tête.
   - Image en miroir ou à l'envers : changer `ORIENTATION` en haut du fichier (0x00, 0x40 ou 0x80).
   - Rien du tout : vérifier le rétroéclairage, puis RESET, WR, RS, et l'ordre D0 à D7.
   - Si la carte ne démarre plus avec l'écran branché : résistance de 10 kΩ entre GPIO2 et 3V3.
5. Mettre à jour les fiches : `node outils/export-esp32.js` (ou `en` pour l'anglais), puis re-téléverser.

## Alimentation sur batterie

Le plus simple : **une batterie externe (powerbank) démontée**. Elle contient la cellule, le chargeur et une sortie 5 V : branche l'ESP32 sur son port USB. Ta cellule Li-ion de 1000 mAh seule demande un chargeur (module TP4056) avant d'aller sur la broche 5V.

Sources : brochage et contrôleur de l'écran relevés par Andy Brown (andybrown.me.uk, « Generic Nokia LCD hacking board » et « Nokia N82 », même connecteur) ; séquence d'initialisation de sa bibliothèque stm32plus (MC2PA8201).
