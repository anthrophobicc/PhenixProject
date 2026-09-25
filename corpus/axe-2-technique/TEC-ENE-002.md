---
id: TEC-ENE-002
titre: Lire un circuit électrique
axe: 2
categorie: Énergie et Électricité
temps: Court
contexte: 1
risque: Discret
materiel: Technique
priorite: normale
origine: officielle
tags: [electricite, circuit, mesure, donnees]
sources: ["IEC 60050 — Vocabulaire électrotechnique international", "IEC 60364 — Installations électriques basse tension", "INRS — Effets du courant électrique sur le corps humain"]
---

::Trois grandeurs, une relation entre elles, deux façons de brancher. Tout le reste de l'électricité en découle.::

## Les trois grandeurs

**La tension**, en volts, est une différence de potentiel entre deux points. Elle n'existe jamais en un seul point : parler de la tension d'un fil n'a de sens que par rapport à un autre. C'est ce qui pousse.

**Le courant**, en ampères, est le débit de charges qui traverse une section. C'est ce qui circule, et c'est ce qui chauffe, travaille et blesse.

**La résistance**, en ohms, est ce qui s'oppose au passage. Elle transforme une partie de l'énergie en chaleur.

Elles sont liées par une seule relation : **la tension est le produit du courant par la résistance.** Connaissant deux valeurs, on obtient la troisième — et cela suffit à résoudre la quasi-totalité des problèmes rencontrés.

La **puissance**, en watts, est le produit de la tension par le courant. Multipliée par une durée en heures, elle donne une énergie en wattheures, seule unité qui permette de comparer un besoin à une réserve, comme l'explique [[TEC-ENE-001]].

## Série et parallèle

**En série**, les éléments se suivent sur un chemin unique. Le même courant traverse tout le monde, et les tensions s'additionnent. Une rupture en un point coupe tout — c'est le principe de la guirlande d'ampoules anciennes, où une lampe grillée éteignait l'ensemble.

Les résistances s'additionnent, et les tensions se répartissent proportionnellement à chacune. C'est ce qui permet d'abaisser une tension, et c'est aussi ce qui explique pourquoi une seule cellule faible dans une batterie limite l'ensemble : le courant qui la traverse est le courant de toute la chaîne.

**En parallèle**, les éléments sont branchés entre les deux mêmes points. Ils reçoivent tous la même tension, et les courants s'additionnent. Une branche qui casse laisse les autres fonctionner : c'est ainsi que sont câblées toutes les installations domestiques.

Une conséquence à retenir : **plus on ajoute de branches en parallèle, plus le courant total augmente**, alors que la résistance de l'ensemble diminue. C'est la cause la plus fréquente de surcharge : brancher davantage sur une même ligne ne partage pas le courant, il l'ajoute.

## Ce qui chauffe et pourquoi

L'échauffement d'un conducteur croît **avec le carré du courant**. Doubler le courant quadruple la chaleur produite pour une même résistance.

C'est pourquoi la section des câbles compte autant. Un câble trop fin pour le courant qu'il transporte chauffe, son isolant vieillit, se fissure, puis fond. La plupart des incendies d'origine électrique viennent de là ou d'un mauvais contact.

**Un mauvais contact est une résistance locale élevée traversée par tout le courant.** Une borne desserrée, une cosse oxydée, un domino mal vissé concentrent une puissance importante sur quelques millimètres. Une connexion tiède est un avertissement ; une connexion chaude est une urgence.

## Continu et alternatif

Le **courant continu** circule toujours dans le même sens. Il a une polarité, et l'inverser détruit l'électronique instantanément. C'est celui des batteries et des panneaux solaires.

Le **courant alternatif** change de sens périodiquement. Il n'a pas de polarité au sens précédent, et surtout il se transforme facilement en une tension différente au moyen d'un transformateur — ce qui est la raison pour laquelle les réseaux de distribution l'utilisent.

Une même valeur en volts ne représente pas la même chose dans les deux cas : la valeur affichée pour l'alternatif est une valeur efficace, et la tension de crête réellement atteinte est nettement supérieure.

## Ce qui blesse

Ce n'est pas la tension, c'est **le courant qui traverse le corps**, et le trajet qu'il emprunte.

La résistance du corps humain varie énormément selon l'état de la peau : une peau sèche résiste considérablement plus qu'une peau mouillée. C'est pourquoi une tension inoffensive dans une situation devient dangereuse dans une autre — mains humides, pieds nus, sol conducteur.

Le trajet décide de la gravité. Un courant qui passe d'une main à l'autre traverse la cage thoracique et le cœur. Un courant qui passe d'une main au pied du même côté suit un trajet moins critique. **D'où l'habitude, chez ceux qui travaillent sous tension, de garder une main dans le dos.**

Les effets vont de la contraction musculaire qui empêche de lâcher la prise, à la fibrillation, à la brûlure profonde sur tout le trajet interne — dont l'étendue réelle n'a aucun rapport avec ce qui se voit à la peau, comme le rappelle [[URG-BRUL-001]].

## Mesurer plutôt que deviner

Un multimètre répond à trois questions, et elles couvrent presque toutes les pannes.

**Y a-t-il une tension**, et de quel type. Mesure en parallèle, aux bornes.

**Le circuit est-il continu**, c'est-à-dire le courant peut-il passer. Mesure hors tension, sur un élément isolé du reste : c'est ainsi qu'on trouve un fil coupé ou un fusible fondu.

**Quelle résistance**, pour identifier un composant ou détecter une fuite. Toujours hors tension, et sur un élément déconnecté — sinon on mesure tout le circuit à la fois et le résultat n'a aucun sens.
