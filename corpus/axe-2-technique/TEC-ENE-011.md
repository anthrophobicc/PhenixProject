---
id: TEC-ENE-011
titre: Le disjoncteur
axe: 2
categorie: Énergie et Électricité
temps: Court
contexte: 1
risque: Discret
materiel: Technique
priorite: normale
origine: officielle
tags: [disjoncteur, differentiel, fusible, tableau electrique, court-circuit, surcharge, securite]
sources: ["Norme NF C 15-100, installations électriques à basse tension", "Norme NF EN 60898-1, disjoncteurs pour installations domestiques", "Norme NF EN 61008 et 61009, interrupteurs et disjoncteurs différentiels", "Promotelec, guides de l'installation électrique"]
---

::Un disjoncteur ne protège pas vos appareils. Il protège vos fils contre le feu, et le différentiel protège votre corps. Quand il saute, il vous dit quelque chose : il faut comprendre quoi avant de le remonter.::

## Ce qu'il surveille

Un fil électrique chauffe quand le courant le traverse. Trop de courant, et il chauffe au point de faire fondre sa gaine et de mettre le feu dans le mur. **Le disjoncteur coupe avant.** Il surveille deux dangers différents, avec deux mécanismes :

- **La surcharge** : trop d'appareils sur le même circuit. Le courant est un peu trop fort, longtemps. Une **lame bimétallique** (deux métaux collés qui ne se dilatent pas pareil) chauffe, se courbe et déclenche la coupure au bout de quelques secondes à quelques minutes.
- **Le court-circuit** : deux fils qui se touchent. Le courant devient énorme d'un coup. Une **bobine** crée un champ magnétique qui ouvre le contact en quelques millisecondes.

## Lire un disjoncteur

**Le calibre**, en ampères, est inscrit dessus : c'est le courant qu'il laisse passer en permanence. En France, la norme lie le calibre à la section du fil qu'il protège :

| Circuit | Fil | Calibre |
|---|---|---|
| Éclairage | 1,5 mm² | 10 A (16 A admis) |
| Prises ordinaires | 1,5 mm² ou 2,5 mm² | 16 A ou 20 A |
| Lave-linge, lave-vaisselle, four | 2,5 mm² | 20 A |
| Plaque de cuisson | 6 mm² | 32 A |

**Jamais un calibre plus fort que ce que le fil supporte.** Remplacer un disjoncteur de 16 A qui saute par un 32 A, c'est retirer la protection : le fil chauffera jusqu'à ce que quelque chose brûle.

**La lettre** devant le calibre (B, C ou D) dit à partir de quand il coupe instantanément : C pour les usages domestiques courants, B pour les longues lignes, D pour les moteurs qui démarrent fort.

## Le différentiel : celui qui sauve les vies

Le courant qui part par la phase doit revenir par le neutre. S'il en manque, c'est qu'il s'échappe ailleurs : par un appareil mouillé, par un fil abîmé, **ou par quelqu'un**. Le **différentiel** compare les deux et coupe dès que la différence atteint son seuil : **30 milliampères** pour ceux qui protègent les personnes, en quelques dizaines de millisecondes. C'est assez rapide pour qu'une électrisation ne devienne pas une électrocution.

- Il a un **bouton de test** : appuyez dessus une fois par mois, il doit couper net.
- Il existe en **type AC** et **type A** : le type A est obligatoire pour les circuits de plaque de cuisson et de lave-linge, dont l'électronique produit des fuites que le type AC ne voit pas toujours.

**Le disjoncteur de branchement**, près du compteur, coupe toute la maison. Il est souvent aussi différentiel, avec un seuil plus élevé et un léger retard, pour laisser les différentiels de 30 mA agir d'abord.

## Il a sauté : lire le message

- **Il ressaute immédiatement** quand on le remonte : un **court-circuit**. Débranchez tout sur ce circuit, remontez, puis rebranchez un appareil à la fois. Le coupable fait sauter au rebranchement.
- **Il saute au bout de quelques minutes**, quand tout tourne en même temps : une **surcharge**. Répartissez les appareils sur d'autres circuits.
- **C'est le différentiel qui saute** : une **fuite**. Cherchez l'eau : une prise extérieure, une salle de bain, un appareil qui a pris l'humidité, un chauffe-eau. Même méthode : tout débrancher, remonter, rebrancher un par un.
- **Il saute par temps d'orage** : une surtension, ou de l'eau qui s'infiltre quelque part.

## Les astuces d'électricien

- **Ne tenez jamais le levier levé** pour empêcher un disjoncteur de sauter. Les modernes coupent quand même, les anciens non, et c'est comme ça que les incendies commencent.
- **Un disjoncteur tiède ou qui sent le chaud** a presque toujours une vis de raccordement desserrée. Un mauvais contact chauffe, voir [[TEC-ENE-003]].
- **Étiquetez votre tableau** le jour où tout va bien. Le jour où il faut couper la cuisine dans le noir, vous n'aurez pas le temps de chercher.
- **Les vieux fusibles** se remplacent par un fusible du même calibre, jamais par un fil de cuivre ou du papier d'aluminium.
- **Avant le retour du courant après une longue coupure**, abaissez les circuits des appareils fragiles ou dangereux (radiateurs, four, pompes), et remontez-les un par un : le réseau revient souvent avec des à-coups.
- **Un groupe électrogène ne se branche jamais sur une prise murale** avec un câble à deux fiches mâles. Il renverrait le courant dans le réseau et peut tuer un technicien qui travaille sur la ligne, à des centaines de mètres. Il faut un inverseur de source, installé par un électricien. Voir [[URG-RES-001]].
