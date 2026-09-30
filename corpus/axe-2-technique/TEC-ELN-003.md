---
id: TEC-ELN-003
titre: L'écran à encre électronique
axe: 2
categorie: Électronique et Numérique
temps: Court
contexte: 1
risque: Discret
materiel: Technique
priorite: normale
origine: officielle
parent: TEC-ELN-001
chapitre: 2
tags: [encre electronique, e-ink, liseuse, ecran, electrophorese, basse consommation]
sources: ["Comiskey B., Albert J., Yoshizawa H., Jacobson J., An electrophoretic ink for all-printed reflective electronic displays, Nature, 1998", "E Ink Holdings, fiches techniques des afficheurs Carta, Kaleido et Spectra", "Heikenfeld J. et al., Review Paper: A critical review of the present and future prospects for electronic paper, Journal of the SID, 2011"]
---

::Une liseuse dont la batterie est morte affiche encore sa dernière page. Un écran qui garde son image sans courant, c'est exactement ce qu'il faut à un appareil qui doit durer.::

## Le principe

L'écran est rempli de **microcapsules** plus fines qu'un cheveu. Chacune contient un liquide transparent et des milliers de **particules de pigment** : des blanches, chargées dans un sens, des noires, chargées dans l'autre.

Des électrodes au-dessus et au-dessous de chaque point créent un champ électrique. Selon son sens, il attire les particules blanches ou les noires vers la surface. Le point devient blanc ou noir. C'est l'**électrophorèse**, le déplacement de particules chargées dans un liquide.

L'invention vient du MIT, à la fin des années 1990 ; la société E Ink l'a industrialisée, et la première liseuse grand public l'a utilisée en 2004.

## Ce qui la rend unique

**Elle est bistable.** Une fois déplacées, les particules restent là où elles sont, sans courant. L'écran ne consomme de l'énergie **que pendant le changement d'image**. Une page affichée pendant une semaine ne coûte rien.

**Elle est réfléchissante.** Comme le papier, elle renvoie la lumière ambiante. Elle se lit parfaitement en plein soleil, sous tous les angles, et fatigue moins les yeux qu'un écran éclairé. Dans le noir, il faut une lumière frontale : une rangée de LED sur le bord qui éclaire la surface par-dessus.

## Ses limites

- **Lente** : une image se change en quelques dixièmes de seconde. Pas de vidéo, des animations saccadées.
- **Les fantômes** : l'image précédente laisse une trace légère. L'écran se « nettoie » régulièrement en clignotant tout noir puis tout blanc : ce flash est normal.
- **Le froid** : en dessous de 0 °C environ, le liquide épaissit et les changements d'image deviennent lents ou incomplets. Beaucoup d'afficheurs sont prévus pour fonctionner entre 0 et 50 °C. **L'image déjà affichée, elle, reste.**
- **La couleur** existe, en deux versions : avec des filtres colorés devant l'écran noir et blanc (couleurs pâles, rapide), ou avec des pigments de plusieurs couleurs dans chaque capsule (couleurs franches, mais un changement d'image prend plusieurs secondes).
- **Le prix** : à taille égale, plus cher qu'un LCD.

## Où on la trouve

- Les liseuses et certaines tablettes d'écriture.
- **Les étiquettes de prix électroniques** des supermarchés : chacune est un petit afficheur à encre électronique avec une pile bouton qui dure des années, mis à jour par radio.
- Les panneaux d'horaires de certains arrêts de bus alimentés par panneau solaire.
- Les montres et les badges à très longue autonomie.

## Ses atouts loin d'une prise

Un appareil de lecture qui doit fonctionner des semaines loin de toute prise a trois besoins : consommer presque rien, se lire en plein jour, et **montrer quelque chose même quand sa batterie est vide**. L'encre électronique est la seule technologie qui coche les trois. C'est pour cela qu'elle est envisagée pour les appareils de lecture hors ligne, voir [[TEC-IDE-009]].

## Les astuces

- **Une liseuse morte garde sa dernière page** : si vous y laissez une carte, une liste de fréquences ou une fiche d'urgence avant qu'elle s'éteigne, l'information reste lisible.
- **Un écran figé à moitié** après un choc de froid se récupère souvent en le réchauffant contre soi, puis en forçant un rafraîchissement complet.
- **Pour un montage**, les modules à encre électronique de 1,5 à 7,5 pouces pilotés en SPI se trouvent pour une dizaine à quelques dizaines d'euros. Ils demandent d'envoyer l'image entière, puis de laisser l'écran se rafraîchir, souvent 2 à 15 secondes selon le modèle.
- **Ne laissez pas un écran à encre électronique en plein soleil derrière une vitre** : la chaleur et les ultraviolets finissent par jaunir et abîmer les capsules.
