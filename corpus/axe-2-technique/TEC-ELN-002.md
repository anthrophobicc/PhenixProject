---
id: TEC-ELN-002
titre: L'écran à cristaux liquides (LCD)
axe: 2
categorie: Électronique et Numérique
temps: Court
contexte: 1
risque: Discret
materiel: Technique
priorite: normale
origine: officielle
parent: TEC-ELN-001
chapitre: 1
tags: [lcd, cristaux liquides, ecran, polariseur, retroeclairage, tft, ips]
sources: ["Yang D.-K., Wu S.-T., Fundamentals of Liquid Crystal Devices, Wiley, 2e édition", "Chen J., Cranton W., Fihn M. (dir.), Handbook of Visual Display Technology, Springer", "Castellano J., Liquid Gold: The Story of Liquid Crystal Displays and the Creation of an Industry, World Scientific"]
---

::Un écran LCD ne fait pas de lumière. C'est une lampe, et devant elle, des millions de volets qui s'ouvrent et se ferment. Tout ce qu'on voit, on le voit à travers.::

## Le principe en trois couches

**La lumière d'une lampe** traverse d'abord un **polariseur** : un filtre qui ne laisse passer que la lumière qui vibre dans une seule direction.

**Les cristaux liquides**, pris en sandwich entre deux plaques de verre, ont une propriété étrange : leurs molécules en bâtonnets s'alignent d'elles-mêmes, et en s'alignant en spirale, elles font **tourner** la direction de la lumière qui les traverse. Quand on applique une petite tension, les molécules se redressent et ne la font plus tourner.

**Un second polariseur**, croisé par rapport au premier, ne laisse passer que la lumière qui a tourné.

Résultat : sans tension, la lumière tourne et passe, le point est clair. Avec tension, elle ne tourne plus et bute sur le second filtre, le point est sombre. En réglant la tension, on obtient tous les gris.

**La couleur** vient de minuscules filtres rouges, verts et bleus devant chaque sous-pixel. Un écran LCD couleur laisse passer, au mieux, environ un dixième de la lumière de sa lampe : le reste est absorbé par les filtres et les polariseurs.

## Les familles

- **LCD à segments** : les chiffres d'une calculatrice, d'une montre, d'un thermostat. Pas de lampe, un miroir derrière : ils sont réfléchissants et consomment quelques millionièmes de watt.
- **Matrice passive** : les vieux écrans monochromes de téléphones et d'appareils. Simples, lents, peu contrastés.
- **Matrice active (TFT)** : un transistor derrière chaque sous-pixel garde sa tension entre deux passages. C'est l'écran de presque tous les ordinateurs, télévisions et téléphones non OLED.
- **TN, VA, IPS** : trois façons d'orienter les cristaux. Le TN est rapide et bon marché mais change de couleur dès qu'on le regarde de côté ; l'IPS garde ses couleurs sous tous les angles ; le VA donne les meilleurs noirs.

## La lampe arrière

Les écrans récents sont éclairés par des **LED**, souvent posées sur un bord : une plaque de plastique guide la lumière et la répartit sur toute la surface. Les écrans d'avant 2010 environ utilisaient des **tubes fluorescents** fins (CCFL), qui contiennent un peu de mercure et demandent une haute tension pour s'allumer.

## Ce qui l'abîme

- **La pression** : appuyer fort écrase les cristaux et fait des taches, parfois définitives.
- **Le froid** : en dessous de −20 °C environ, les cristaux deviennent visqueux, l'image traîne. Ça revient en se réchauffant.
- **La forte chaleur** : un écran de tableau de bord en plein soleil peut devenir noir. Au-delà d'une certaine température, les cristaux deviennent un liquide ordinaire et perdent leur effet. Ça revient aussi en refroidissant.
- **Les pixels morts ou bloqués** : un transistor défaillant laisse un point toujours noir ou toujours allumé.

## Les astuces de ceux qui en ont démonté

- **Écran noir, appareil allumé ?** Éclairez l'écran de biais avec une torche, tout près. Si l'image apparaît, faiblement, seule la lampe arrière est morte : l'appareil reste utilisable pour récupérer des données ou lire un réglage.
- **La lumière d'un LCD est polarisée.** Avec des lunettes de soleil polarisantes, un écran peut devenir noir quand on penche la tête de 90 degrés. Ce n'est pas une panne.
- **La dalle arrière d'un écran de portable cassé** (le guide de lumière et ses LED) fait un panneau lumineux plat et régulier, idéal pour éclairer une pièce, un plan de travail, ou pour décalquer. Ses LED se branchent souvent en série : il faut leur donner la tension prévue, voir [[TEC-ELN-004]].
- **Les feuilles de polariseur** se décollent d'un écran mort. Deux feuilles croisées montrent les tensions dans le plastique transparent sous forme d'arcs-en-ciel, et une seule sert de filtre polarisant pour la photo.
- **Un vieil écran à tubes fluorescents cassé** : ne respirez pas la poussière des tubes brisés, aérez, ramassez sans aspirateur.
- **Pour un montage**, les petits modules LCD couleur de 2 à 3 pouces pilotés en SPI (contrôleurs ILI9341, ST7789) coûtent quelques euros et sont documentés partout.
