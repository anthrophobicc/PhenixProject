---
id: TEC-ENE-004
titre: Les batteries
axe: 2
categorie: Énergie et Électricité
temps: Long
contexte: 1
risque: Discret
materiel: Technique
priorite: normale
origine: officielle
tags: [batterie, energie, stockage, donnees]
sources: ["IEC 62133 — Safety requirements for secondary cells", "Battery University — technical documentation", "Linden's Handbook of Batteries"]
---

::Une batterie ne contient pas de l'électricité. Elle contient une réaction chimique qu'on force à l'envers pour la recharger, et cette réaction s'use.::

## Les grandeurs qui comptent

**La tension nominale** dépend de la chimie et du nombre de cellules en série. Une cellule au plomb délivre environ deux volts, une cellule lithium-ion environ trois volts et demi à trois volts sept selon la variante.

**La capacité**, en ampères-heures, indique combien de courant la batterie peut fournir pendant combien de temps. **Elle ne dit rien seule** : il faut la multiplier par la tension pour obtenir des wattheures, seule unité comparable. Deux batteries de même capacité affichée peuvent stocker des énergies très différentes — c'est le calcul central de [[TEC-ENE-001]].

**Le courant maximal** que la batterie accepte de fournir ou de recevoir. Le dépasser la chauffe et l'abîme.

**La {{profondeur de décharge|Fraction de la capacité d'une batterie réellement utilisée avant recharge ; plus elle est faible, plus la batterie dure.}}** est la fraction réellement utilisable. C'est le paramètre le plus souvent ignoré et celui qui décide de la durée de vie.

## Les chimies, et leurs caractères

**Le plomb-acide.** Lourd, encombrant, peu cher, très tolérant. Il accepte une charge rudimentaire et supporte une électronique de gestion approximative. En contrepartie, il n'aime pas être déchargé profondément : descendre régulièrement sous la moitié de sa capacité réduit fortement son espérance de vie. Laissé déchargé, il se sulfate et devient irrécupérable en quelques semaines. **C'est le meilleur choix quand on n'a pas d'électronique fiable**, et le pire quand le poids compte.

**Le lithium-ion.** Bien plus dense en énergie pour le même poids, sans effet de mémoire, faible autodécharge. Mais il exige une gestion précise : une surcharge, une décharge trop profonde ou une charge par grand froid l'endommagent, parfois dangereusement. C'est le rôle du circuit de protection intégré aux blocs.

**Le lithium-fer-phosphate**, une variante, stocke un peu moins mais tolère bien plus de cycles, se dégrade moins vite et présente un comportement thermique nettement plus sûr.

**Le nickel-métal-hydrure**, celui des accumulateurs de format courant, est robuste, sans danger particulier, mais s'autodécharge notablement — sauf les versions dites à faible autodécharge.

## Ce qui use une batterie

Trois facteurs, et ils se cumulent.

**Le nombre de cycles.** Chaque charge complète use un peu. Mais une décharge partielle use bien moins qu'une décharge profonde : **maintenir une batterie entre vingt et quatre-vingts pour cent multiplie considérablement sa durée de vie**, quelle que soit la chimie.

**La température.** La chaleur accélère toutes les réactions de dégradation. Une batterie stockée au chaud vieillit vite même sans être utilisée. Le froid, lui, réduit temporairement la capacité disponible sans abîmer — sauf en charge, où charger une cellule lithium en dessous de zéro provoque des dépôts internes irréversibles.

**Le repos à un état de charge extrême.** Stockée pleine ou vide pendant des mois, une batterie se dégrade davantage qu'à mi-charge. Pour un stockage long, la règle est de laisser environ la moitié.

## Reconnaître une cellule dangereuse

**Gonflée, percée, écrasée ou déformée : elle s'écarte.** Elle ne se répare pas et ne se teste pas. Une cellule lithium endommagée peut entrer en {{emballement thermique|Réaction en chaîne qui s'auto-entretient dans une cellule lithium endommagée, sans besoin d'oxygène extérieur.}}, réaction qui s'auto-entretient et qu'on n'éteint pas facilement.

Une odeur douceâtre, une chaleur anormale en charge, une tension qui s'effondre sous charge légère sont autant de motifs de mise à l'écart.

Un feu de batterie lithium n'a pas besoin d'oxygène extérieur pour se poursuivre : on refroidit massivement à l'eau et l'on éloigne le reste plutôt que de chercher à l'étouffer — voir [[URG-INC-001]].

## En récupération

Les cellules cylindriques standard équipent une grande partie des blocs d'outillage portatif et d'ordinateurs. **Un bloc mort l'est rarement en entier** : c'est presque toujours une ou deux cellules qui font chuter l'ensemble, parce qu'elles sont en série et que la plus faible limite tout le monde, comme l'explique [[TEC-ENE-002]].

Séparer les cellules, mesurer chacune à vide puis sous charge, et écarter celles qui s'effondrent permet de reconstituer un ensemble utilisable. Cela demande de mesurer, jamais de deviner.

Les batteries au plomb d'onduleurs, d'alarmes et d'éclairages de secours sont partout, gardent une charge résiduelle longtemps et se rechargent avec des moyens simples. Le tri d'un matériel trouvé relève de [[SURV-REC-002]].

## Charger correctement

Une charge se fait en deux temps : à courant constant tant que la tension monte, puis à tension constante pendant que le courant diminue. Couper trop tôt laisse la batterie partiellement chargée ; maintenir la tension trop longtemps la dégrade.

Un régulateur est indispensable dès qu'une source variable est en jeu, comme un panneau solaire — voir [[TEC-SOLR-001]]. Sans lui, la batterie est détruite par surcharge le jour, ou déchargée dans le panneau la nuit.

Enfin, une batterie au plomb en charge dégage de l'hydrogène, inflammable et explosif en espace confiné. **On ventile, et on n'approche aucune flamme ni étincelle.**
