---
id: TEC-ENE-001
titre: L’énergie électrique dans les objets
axe: 2
categorie: Énergie et Électricité
temps: Long
contexte: 1
risque: Discret
materiel: Technique
priorite: normale
origine: officielle
tags: [electricite, recuperation, materiel]
sources: []
---

::Une installation électrique se lit avec quatre valeurs et un seul calcul. Tout le reste en découle.::

## Lire une installation

Tout commence par une plaque signalétique. Quatre valeurs, et rien d'autre n'est nécessaire pour décider.

- **La tension**, en volts. C'est la valeur qui détruit. Alimenter un appareil sous une tension inadaptée le tue immédiatement, parfois violemment.
- **Le courant**, en ampères. Ce que l'appareil appelle.
- **La puissance**, en watts. Souvent inscrite ; en courant continu, c'est le produit de la tension par le courant.
- **Le type de courant.** Une ligne droite pour le continu, une ligne ondulée pour l'alternatif. Ce ne sont pas des variantes de la même chose.

Les relations entre tension, courant et résistance, ainsi que les branchements en série et en parallèle, sont détaillés dans [[TEC-ENE-002]].

Un seul calcul sert tous les jours. Une puissance en watts multipliée par une durée en heures donne une énergie en wattheures. C'est la seule unité qui permette de comparer un besoin à une réserve. Une capacité en ampères-heures ne dit rien seule : multipliez-la par la tension nominale. C'est pour cela que deux batteries annoncées à la même capacité peuvent contenir des énergies très différentes.

Une fois ce calcul acquis, le dimensionnement devient trivial : additionnez vos wattheures par jour, comparez à ce que vous stockez, vous savez combien de jours vous tenez. C'est ce même calcul qui décide si une propulsion électrique est envisageable, voir [[TEC-MOT-001]].

## Règles de manipulation

1. **Coupez et vérifiez l'absence de tension avant toute intervention.** Un appareil débranché n'est pas un appareil sûr.
2. **Lisez la plaque avant de brancher quoi que ce soit.** Toujours.
3. **Respectez la polarité en courant continu.** Il a un sens. Une inversion détruit l'électronique instantanément et sans avertissement.
4. **Écartez toute cellule lithium déformée.** Gonflée, percée, écrasée : elle ne se répare pas, elle ne se teste pas. Elle peut partir en {{emballement thermique|Réaction en chaîne qui s'auto-entretient dans une cellule lithium endommagée, sans besoin d'oxygène extérieur.}}.
5. **Ne touchez jamais les gros condensateurs d'une alimentation à découpage, d'un micro-ondes ou d'un flash.** Ils conservent une charge capable de tuer plusieurs minutes après le débranchement, parfois beaucoup plus.

## Où trouver quoi

**Vous cherchez du stockage.** Les cellules lithium cylindriques standard équipent une grande partie des blocs d'outillage portatif et d'ordinateurs. Un bloc mort l'est rarement en entier : c'est presque toujours une ou deux cellules qui font chuter l'ensemble, les autres restant bonnes.

**Vous n'avez pas d'électronique de gestion.** Alors préférez le plomb. Les batteries d'onduleurs et d'alarmes gardent une charge résiduelle longtemps et se rechargent avec des moyens rudimentaires. C'est leur avantage décisif sur le lithium, qui exige une gestion précise sous peine d'incendie.

**Vous cherchez de la production.** Les panneaux solaires de signalisation routière, d'éclairage de jardin et de mobilier urbain sont partout, peu surveillés, et produisent immédiatement. Le dimensionnement complet d'une installation est dans [[TEC-SOLR-001]].

**Vous récupérez sur place.** Le tri de ce qui est encore utilisable est dans [[SURV-REC-002]], et la méthode de fouille dans [[SURV-REC-001]].

**Vous voulez aller plus loin.** Le raccordement, la protection contre les surintensités, la mise à la terre et l'intervention sous tension relèvent de fiches distinctes. Ce sont les sujets où l'erreur est mortelle et non coûteuse : ils se traitent seuls, jamais en fin de fiche.
