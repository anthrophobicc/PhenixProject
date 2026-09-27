---
id: TEC-ELN-001
titre: Les écrans
axe: 2
categorie: Électronique et Numérique
temps: Court
contexte: 1
risque: Discret
materiel: Technique
priorite: normale
origine: officielle
sommaire: oui
parcours: Lisez d'abord cette fiche, qui explique ce qu'ont en commun tous les écrans. Le chapitre sur l'écran à cristaux liquides couvre presque tout ce que vous avez sous la main ; celui sur l'encre électronique explique pourquoi c'est l'écran des appareils qui doivent tenir des semaines sur une pile.
tags: [ecran, pixel, affichage, resolution, lcd, oled, encre electronique, electronique]
sources: ["Chen J., Cranton W., Fihn M. (dir.), Handbook of Visual Display Technology, Springer, 2e édition", "Society for Information Display, Display Technology Guide", "E Ink Holdings, documentation technique des afficheurs électrophorétiques"]
---

::Un écran ne montre pas une image. Il allume, éteint ou masque des millions de petits points assez vite pour que l'œil les prenne pour une image.::

Ce sujet se lit en trois temps : cette fiche, qui explique ce que tous les écrans ont en commun, puis deux chapitres, [[TEC-ELN-002]] sur les cristaux liquides et [[TEC-ELN-003]] sur l'encre électronique. Les LED, qui éclairent la plupart des écrans et en forment certains à elles seules, ont leur propre fiche : [[TEC-ELN-004]].

## Le pixel

Tout écran est une grille de **pixels**. Sur un écran couleur, chaque pixel est fait de trois **sous-pixels**, rouge, vert et bleu. En réglant l'intensité de chacun, on obtient toutes les couleurs : les trois à fond donnent du blanc, les trois éteints du noir.

**La définition** est le nombre de pixels : 1920 × 1080 pour la « Full HD », 3840 × 2160 pour la 4K. **La densité** est le nombre de pixels par pouce (ppp, ou ppi en anglais) : au-delà d'environ 300 ppp à la distance de lecture d'un téléphone, l'œil ne distingue plus les points.

Un même nombre de pixels donne une image fine sur un téléphone et grossière sur un grand téléviseur : c'est la densité qui compte pour la netteté, pas la définition seule.

## Trois façons de faire de la lumière

Tous les écrans se rangent dans l'une de ces familles.

| Famille | Principe | Exemples | Au soleil | Dans le noir |
|---|---|---|---|---|
| Émissifs | Chaque point produit sa propre lumière | OLED, LED géantes, anciens tubes cathodiques, plasma | Moyen | Parfait |
| Transmissifs | Une lampe derrière, des volets devant | Écran LCD d'ordinateur, de télévision, de téléphone | Moyen à mauvais | Bon |
| Réfléchissants | Pas de lampe : ils renvoient la lumière ambiante, comme le papier | Encre électronique, LCD de calculatrice et de montre | Parfait | Illisible sans éclairage |

**Ce tableau décide de la consommation.** Un écran émissif ou transmissif dépense de l'énergie à chaque seconde où il est allumé, et la lampe arrière est souvent le premier poste de consommation d'un téléphone ou d'un ordinateur. Un écran réfléchissant ne dépense presque rien : une calculatrice à cristaux liquides tourne des années sur une pile bouton, une liseuse des semaines.

## Rafraîchir l'image

Un écran d'ordinateur redessine son image 60 fois par seconde ou plus (60 Hz, 120 Hz). C'est ce qui rend le mouvement fluide. Un écran à encre électronique, lui, ne change l'image que quand on le lui demande, et met une fraction de seconde à le faire : parfait pour une page, inutilisable pour une vidéo.

## Comment un écran reçoit l'image

- **Les grands écrans** reçoivent l'image par un câble vidéo : HDMI, DisplayPort, et plus anciennement VGA (analogique, encore très répandu sur les vieux écrans et projecteurs).
- **Les petits écrans** des appareils électroniques sont pilotés directement par un petit contrôleur, par une liaison série à quelques fils (SPI, I2C) ou par un bus parallèle. C'est ce qu'on utilise pour construire un appareil soi-même, avec un microcontrôleur, voir [[TEC-IDE-009]].
- **Le contrôleur** est une puce collée derrière la dalle, qui garde l'image en mémoire et la redessine seule. Chaque modèle a ses commandes : sans sa documentation, un écran récupéré est très difficile à faire fonctionner.

## Ce qu'on apprend en démontant

- **Les écrans de vieux téléphones se réutilisent mal.** Leurs connecteurs ont des broches au pas de 0,4 mm ou moins, leur contrôleur est souvent sans documentation publique, et leur rétroéclairage demande parfois plus de 10 volts. Pour un montage, un module d'écran vendu pour les microcontrôleurs, déjà monté sur une petite carte, coûte quelques euros et fait gagner des jours.
- **Un écran de portable cassé** contient une dalle lumineuse diffusante, derrière les cristaux liquides : un excellent panneau d'éclairage plat, une fois alimenté. Voir [[TEC-ELN-002]].
- **Un écran qui reste noir** n'est pas forcément mort : souvent, c'est seulement la lampe arrière qui ne s'allume plus. Éclairez l'écran de biais avec une lampe torche, l'image apparaît.
- **Les écrans tactiles** sont une couche de plus, collée devant la dalle : on peut casser la vitre tactile d'un téléphone sans toucher l'écran, et inversement.
