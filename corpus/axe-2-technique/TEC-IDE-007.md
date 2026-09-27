---
id: TEC-IDE-007
titre: Le fond vert
axe: 2
categorie: Information et Données
temps: Court
contexte: 1
risque: Discret
materiel: Technique
priorite: normale
origine: officielle
tags: [fond vert, incrustation, chroma key, video, cinema, eclairage, montage]
sources: ["Foster J., The Green Screen Handbook: Real-World Production Techniques, Sybex", "Documentation OBS Studio et DaVinci Resolve, filtres d'incrustation", "Brinkmann R., The Art and Science of Digital Compositing, Morgan Kaufmann"]
---

::Le fond vert ne remplace pas le décor. Il remplace une couleur. Tout le travail consiste à ce que cette couleur n'existe que derrière vous.::

## Le principe

La caméra filme une personne devant un fond d'une seule couleur, uniforme. Le logiciel repère tous les pixels de cette couleur et les rend transparents. On glisse une autre image derrière. C'est l'**incrustation**, ou *chroma key*.

C'est la même idée que la météo à la télévision, les effets spéciaux au cinéma, ou le fond de n'importe quel créateur de vidéo.

## Pourquoi vert, et pourquoi parfois bleu

**Le vert** est la couleur la plus éloignée de la peau humaine, quelle que soit sa teinte. Et les capteurs des caméras ont deux fois plus de pixels verts que de rouges ou de bleus : le vert est la couleur la plus détaillée, donc la plus facile à découper proprement.

**Le bleu** sert quand le sujet porte du vert, pour les scènes de nuit, et donne moins de reflets colorés sur la peau. Mais il demande plus de lumière.

Règle absolue : **pas de vêtement, d'accessoire ou d'objet de la couleur du fond.** Il deviendrait transparent. Attention aussi aux objets brillants, lunettes, montres, bijoux : ils reflètent le fond.

## Les trois lois de l'éclairage

C'est l'éclairage qui fait 80 % du résultat. Un logiciel ne rattrape pas un fond mal éclairé.

1. **Le fond doit être uniforme.** Pas de zone plus sombre dans les coins, pas de pli, pas de reflet. Deux lampes diffuses, à 45 degrés de chaque côté du fond, au lieu d'une seule en face.
2. **Le sujet s'éclaire à part**, avec ses propres lampes, comme pour n'importe quelle vidéo.
3. **Éloignez le sujet du fond : 1,5 à 2 mètres au moins.** Trop près, le vert se reflète sur les épaules et les cheveux, c'est le *débordement*, et l'ombre du sujet tombe sur le fond.

## Les réglages de la caméra

- **Vitesse d'obturation élevée** (1/100 s ou plus) : le flou de mouvement mélange le sujet et le vert, et le détourage bave.
- **Mise au point sur le sujet.** Un fond légèrement flou se découpe même mieux.
- **Pas trop d'exposition** : un vert brûlé devient presque blanc.
- **La meilleure définition possible**, et un format peu compressé si la caméra le propose.

## Le logiciel

Les logiciels gratuits suffisent : OBS pour le direct, DaVinci Resolve, CapCut ou Shotcut pour le montage. Le réglage suit toujours le même ordre :

1. choisir la couleur à retirer avec la pipette, sur une zone moyenne du fond ;
2. monter la tolérance jusqu'à ce que tout le fond disparaisse, pas plus ;
3. adoucir un peu les bords ;
4. activer la **suppression du débordement** (*spill suppression*), qui retire le reflet vert sur les contours.

## Les astuces de ceux qui en font tous les jours

- **Un tissu se repasse**, ou se tend sur un cadre. Chaque pli fait une ombre, et chaque ombre est une autre teinte de vert. Un mur peint en vert mat vaut mieux qu'un tissu froissé.
- **Découpez large, recadrez après.** Si le sujet sort du fond, même d'un doigt, il est perdu. Faites le cadre, puis masquez tout ce qui dépasse du fond avec un masque grossier (*garbage matte*).
- **Les cheveux fins** sont l'épreuve de vérité. Une lumière placée derrière le sujet, vers le haut de sa tête, sépare les cheveux du fond et rend le détourage beaucoup plus propre.
- **Le décor d'arrivée décide de la lumière.** Si le fond final est un coucher de soleil, éclairez le sujet chaud et de côté. Un sujet éclairé comme dans un bureau posé sur une plage ne trompe personne.
- **Pas de fond vert ?** Un drap bleu, un mur uni, un ciel dégagé derrière vous. Le logiciel accepte n'importe quelle couleur, pourvu qu'elle soit uniforme et absente du sujet.
- **Les nouveaux outils d'intelligence artificielle** détourent sans fond vert. Ils se trompent sur les mains et les cheveux en mouvement : le fond vert reste plus fiable dès qu'on bouge.
