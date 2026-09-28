---
id: TEC-COR-001
titre: La corrosion des métaux
axe: 2
categorie: Chimie et Matériaux
temps: Long
contexte: 1
risque: Discret
materiel: Récupération
priorite: normale
origine: officielle
tags: [metaux, corrosion, materiaux, entretien]
sources: ["NACE International, Corrosion Basics", "ASM International, Handbook of Corrosion", "Centre technique des industries mécaniques, corrosion galvanique"]
---

::Un métal ne rouille pas parce qu'il est vieux. Il rouille parce qu'il retourne à l'état où on l'a trouvé.::

Presque tous les métaux existent dans la nature sous forme d'oxydes — c'est-à-dire déjà combinés à l'oxygène. Les extraire demande une énorme quantité d'énergie. La corrosion est simplement le chemin inverse : **le métal rend l'énergie qu'on lui a donnée et redevient du minerai.** C'est spontané, et rien ne l'arrête définitivement. On ne fait que le ralentir.

## Ce qu'il faut pour que ça corrode

Trois ingrédients, et il faut les trois : un métal, de l'oxygène, et de l'eau. Retirez-en un et la corrosion s'arrête.

C'est pourquoi un objet en fer conservé au sec ne rouille pas, et pourquoi un objet immergé dans une eau privée d'oxygène se conserve remarquablement bien — des épaves entières ont traversé les siècles ainsi.

Deux facteurs accélèrent tout massivement.

**Le sel.** Il rend l'eau conductrice et multiplie la vitesse de corrosion. C'est toute la difficulté du milieu marin, et cela explique les choix de conception décrits dans [[TEC-MOT-001]].

**L'humidité alternée.** Un objet mouillé en permanence corrode moins vite qu'un objet qui sèche et se remouille sans cesse. L'alternance renouvelle l'oxygène à chaque cycle.

## Pourquoi certains métaux résistent

Ils corrodent aussi, mais leur couche d'oxyde les protège au lieu de les trahir.

**L'aluminium** forme instantanément une couche d'oxyde extrêmement mince, dense et adhérente, qui bloque l'accès à l'oxygène. Cette couche se reforme seule si on la raye. L'aluminium est en réalité un métal très réactif : il ne survit que grâce à son propre oxyde.

**L'acier inoxydable** doit sa résistance au chrome qu'il contient, qui forme le même type de couche protectrice. Il n'est pas inoxydable en toute circonstance : privé d'oxygène — sous un joint, dans un interstice, sous un dépôt — il ne peut plus reformer sa couche et se corrode alors localement, en profondeur.

**Le fer**, lui, forme une rouille poreuse, volumineuse et non adhérente. Elle se détache et expose du métal neuf. C'est la différence entière : une couche d'oxyde qui protège contre une couche d'oxyde qui écaille.

## Le piège du contact entre deux métaux

C'est la cause de panne la plus fréquente et la moins comprise en récupération.

Deux métaux différents en contact, en présence d'humidité, forment une pile. L'un des deux devient l'{{anode|Électrode qui se dégrade dans un couple électrochimique, protégeant l'autre métal.}} et se dégrade rapidement, l'autre est protégé. **Ce n'est pas un phénomène marginal : la corrosion peut être plusieurs dizaines de fois plus rapide qu'en isolé.**

L'ordre est constant. Le zinc et l'aluminium se sacrifient face à l'acier. L'acier se sacrifie face au laiton, au cuivre et à l'inox. Plus les deux métaux sont éloignés dans cet ordre, plus l'attaque est violente.

D'où deux conséquences pratiques opposées et également utiles. **À éviter :** une vis en inox dans une tôle d'aluminium détruit l'aluminium autour d'elle. **À exploiter :** c'est exactement le principe de la galvanisation, où une couche de zinc protège l'acier en se dégradant à sa place, et celui des anodes sacrificielles montées sur les coques et les chauffe-eau.

## Évaluer et protéger une pièce

**Évaluer une pièce récupérée, dans cet ordre.**

1. **Grattez.** Une rouille superficielle laisse du métal sain dessous. Si le grattage traverse, la pièce est perdue mécaniquement, quelle que soit son apparence.
2. **Regardez les zones cachées** : sous les têtes de vis, dans les interstices, aux points de contact entre deux pièces, aux endroits où l'eau stagne. La corrosion commence toujours là, jamais sur la surface exposée qui sèche.
3. **Tapez légèrement.** Un son clair indique du métal sain, un son mat une structure attaquée en profondeur.
4. **Cherchez le contact entre métaux différents** et la présence d'un dépôt poudreux blanc — signe d'aluminium en train d'être sacrifié.

**Protéger, dans l'ordre d'efficacité.**

1. **Sécher et ventiler.** Le geste le plus efficace et le moins coûteux. Un local sec conserve indéfiniment.
2. **Nettoyer avant de protéger.** Une protection appliquée sur de la rouille l'enferme avec son humidité et accélère les choses au lieu de les ralentir.
3. **Barrière physique** : graisse, huile, cire, peinture. Toute couche continue qui exclut l'eau et l'air.
4. **Isoler les métaux différents** par une rondelle, un joint, une peinture ou un ruban, dès qu'ils sont en contact et exposés.

## Selon le milieu

**Vous stockez du métal longtemps.** Nettoyez, huilez généreusement, emballez avec un absorbeur d'humidité, et stockez au-dessus du sol et à température stable. La condensation nocturne sur une pièce froide fait plus de dégâts que la pluie.

**Vous récupérez en milieu salin.** Rincez à l'eau douce immédiatement et abondamment — c'est la règle qui gouverne aussi l'entretien des motorisations décrites dans [[TEC-MOT-001]]. Le sel qui reste continue de travailler des mois après. C'est la règle absolue de tout ce qui a touché la mer.

**Vous n'avez rien pour protéger.** N'importe quel corps gras disponible vaut mieux que rien : huile de cuisine, graisse animale, suif. Ils s'oxydent avec le temps et doivent être renouvelés, mais ils excluent l'eau, ce qui est l'essentiel.

**Vous évaluez une pièce trouvée sur place.** Le tri complet, au-delà de la seule corrosion, est dans [[SURV-REC-002]].

**Vous choisissez un matériau pour durer.** L'inox pour ce qui est exposé et ventilé, le galvanisé pour ce qui est exposé et bon marché, l'aluminium pour ce qui doit être léger et ne touchera pas d'autre métal, le fer pour ce qui restera au sec ou sera entretenu régulièrement.
