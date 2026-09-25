---
id: TEC-MEC-001
titre: Assembler
axe: 2
categorie: Mécanique et Transport
temps: Long
contexte: 1
risque: Discret
materiel: Technique
priorite: normale
origine: officielle
tags: [assemblage, mecanique, outils, donnees]
sources: ["Machinery's Handbook — fasteners and joining", "American Welding Society — welding fundamentals", "USDA Forest Products Laboratory — Wood Handbook, chapitre sur les assemblages"]
---

::Un assemblage se choisit sur une seule question : est-ce que je veux pouvoir le défaire ?::

## Les deux familles

**Démontable** — vis, boulon, goupille, ligature, emboîtement. On peut revenir en arrière, remplacer une pièce, ajuster. En contrepartie, l'assemblage garde du jeu et peut se desserrer.

**Définitif** — rivet, soudure, collage, clou. Plus résistant, plus rigide, plus compact. Mais démonter détruit, et réparer demande de refaire.

En récupération, la question est décisive : **un assemblage démontable rend la pièce réutilisable ailleurs**, ce qui vaut souvent plus que la résistance gagnée.

## La vis et le boulon

Une vis est un plan incliné enroulé : elle transforme un couple de rotation en une force axiale considérable, selon le principe exposé dans [[TEC-MAC-001]].

**Ce qui tient un assemblage boulonné n'est pas la vis, c'est le serrage.** La tension dans la vis presse les pièces l'une contre l'autre, et c'est le frottement entre elles qui reprend les efforts. Une vis correctement serrée ne travaille presque pas en cisaillement.

D'où la conséquence pratique : **un boulon desserré ne tient plus grand-chose**, même s'il est en place. Le desserrage vient des vibrations, de la dilatation, et du fluage des matériaux tendres. On le combat par un contre-écrou, une rondelle élastique, un frein filet, ou un simple fil de freinage — et surtout par un resserrage périodique.

Une vis pour le bois travaille autrement : elle s'ancre en déformant les fibres. Un avant-trou évite de fendre et augmente la tenue, contrairement à l'intuition.

## Le rivet

Deux pièces percées, une tige insérée, une extrémité écrasée. L'assemblage est définitif, résistant en cisaillement, insensible aux vibrations, et il ne se desserre jamais.

C'est le mode d'assemblage des structures avant la soudure, et il reste excellent en récupération : un clou coupé à longueur et maté sur une rondelle fait un rivet parfaitement fonctionnel.

## La soudure

Elle fond localement les deux pièces pour n'en faire qu'une. C'est l'assemblage le plus résistant et le plus étanche.

Trois choses à savoir avant d'y compter.

**Elle demande une source d'énergie importante**, ce qui la rend peu accessible sans réseau. Un poste à souder rudimentaire peut se faire à partir de batteries en série, avec toutes les précautions de [[TEC-ENE-004]].

**Elle modifie le métal autour du cordon.** La zone chauffée puis refroidie change de dureté et peut devenir fragile — c'est le même mécanisme que le traitement thermique décrit dans [[TEC-MEC-005]].

**Elle ne s'applique pas à tout.** Chaque métal demande un procédé adapté, et l'on ne soude pas ensemble n'importe quels métaux.

Le **{{brasage|Assemblage où seul le métal d'apport fond, sans faire fondre les pièces.}}**, où seul l'apport fond, demande beaucoup moins d'énergie et convient bien aux petites pièces et à l'étanchéité.

## La ligature

Sous-estimée, et pourtant l'un des assemblages les plus efficaces sans outillage.

Elle fonctionne par frottement et par serrage. Trois règles la rendent solide : **des tours nombreux et jointifs**, une **{{{{frette|Tours de lien passés perpendiculairement entre les pièces ligaturées, qui serrent l'ensemble.}}|Tours de lien passés perpendiculairement entre les pièces, qui serrent la ligature.}}** — des tours perpendiculaires passés entre les pièces qui viennent serrer l'ensemble — et un **matériau qui se rétracte** en séchant, comme le cuir humide, le tendon ou la fibre végétale mouillée.

Bien faite, une ligature reprend des efforts considérables et se répare sur place. La fabrication du lien est dans [[TEC-MAT-003]].

## L'assemblage bois

Le bois s'assemble mieux qu'il ne se cloue. Une entaille ajustée transmet l'effort par contact sur une grande surface, alors qu'un clou concentre tout sur un point et fend en travaillant.

Deux principes gouvernent tout : **travailler dans le sens des fibres**, parce que le bois est faible en travers ; et **laisser le bois bouger**, parce qu'il gonfle et retreint avec l'humidité. Un assemblage bloqué de toutes parts se fend au premier changement de saison — mécanisme expliqué dans [[TEC-MAT-001]].

## Choisir, en pratique

**Effort important et permanent** : boulonné serré, ou soudé.
**Effort avec vibrations** : rivet, ou boulon freiné.
**Assemblage à démonter** : vis et écrou, goupille.
**Sans outillage** : ligature, emboîtement, coin.
**Étanchéité** : soudure, brasage, ou joint comprimé par serrage.

Et une règle qui vaut partout : **un assemblage casse presque toujours à sa jonction avec le reste**, pas en son milieu. C'est la reprise d'effort aux extrémités qu'il faut soigner, jamais le centre.
