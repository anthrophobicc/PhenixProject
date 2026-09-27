---
id: SURV-ENE-002
titre: Fabriquer une pile
axe: 3
categorie: Feu, Eau et Ressources
temps: Court
contexte: 1
risque: Discret
materiel: Récupération
priorite: normale
origine: officielle
tags: [pile, citron, volta, aluminium, sel, vinaigre, electricite, led, sans reseau]
sources: ["Volta A., On the Electricity excited by the mere Contact of conducting Substances of different kinds, Philosophical Transactions of the Royal Society, 1800", "Linden D., Reddy T., Handbook of Batteries, McGraw-Hill (couples électrochimiques et potentiels standard)", "Royal Society of Chemistry, Education : aluminium-air cell et piles à fruits (fiches expérimentales)"]
---

::Deux métaux différents et un peu de vinaigre font de l'électricité. Pas assez pour charger un téléphone, mais assez pour allumer une lumière dans le noir, et ça, avec rien, c'est déjà beaucoup.::

## COMPRENDRE

Une pile, c'est **deux métaux différents** qui ne se touchent pas, et **un électrolyte** entre eux : un liquide ou une pâte qui conduit les charges, eau salée, vinaigre, jus de citron. Le métal le plus « pressé » de se dissoudre (le zinc, l'aluminium, le magnésium) cède des électrons, qui passent par le fil pour rejoindre l'autre côté. Voir [[TEC-ENE-012]].

**La tension dépend du couple de métaux**, pas de la taille :

| Couple | Tension par cellule, environ |
|---|---|
| Zinc et cuivre | 0,8 à 1 V |
| Aluminium et charbon de bois (pile aluminium-air) | 0,7 à 1,2 V |
| Magnésium et cuivre | 1,5 à 2 V |
| Fer et cuivre | 0,3 à 0,5 V |

**Le courant dépend de la surface** des métaux et de la qualité de l'électrolyte. Plus c'est grand, plus ça débite.

**Pour plus de tension**, on met plusieurs cellules en série : le cuivre de l'une relié au zinc de la suivante. C'est exactement ce qu'a fait Volta en 1800 avec sa « pile » de disques empilés, qui a donné son nom à toutes les autres.

**La réalité, à connaître avant de commencer :** un citron donne environ 0,9 volt et **moins d'un milliampère**. Un téléphone demande 5 volts et environ un ampère pour se recharger. Il faudrait des milliers de citrons. Une pile de fortune sert à **une LED, une calculatrice, une horloge, un petit signal**, pas à recharger un appareil.

## AGIR

### La pile de pièces (la plus pratique)

Il vous faut : des pièces de cuivre ou cuivrées (les pièces de 1, 2 et 5 centimes d'euro sont de l'acier recouvert de cuivre, ça marche), des rondelles **galvanisées** (grises, en zinc, au rayon visserie), du carton, du sel ou du vinaigre.

1. Découpez des ronds de carton ou de papier absorbant un peu plus petits que les pièces.
2. Trempez-les dans de l'eau très salée ou du vinaigre, et égouttez-les : **humides, pas dégoulinants**, sinon le liquide relie les cellules entre elles et tout s'arrête.
3. Empilez : pièce, carton, rondelle, pièce, carton, rondelle… Chaque trio donne environ 0,5 à 0,8 V.
4. Six à huit étages suffisent pour une LED rouge ; dix à douze pour une blanche.
5. Le fil du bas touche la première pièce (le plus), celui du haut la dernière rondelle (le moins). La LED se branche **dans le bon sens** : patte longue vers le cuivre. Voir [[TEC-ELN-004]].
6. Serrez la pile avec un élastique ou dans un morceau de tuyau.

### La pile aluminium-air (celle qui débite le plus)

1. Une feuille de **papier aluminium** à plat.
2. Par-dessus, un papier absorbant trempé dans de l'eau **saturée de sel**.
3. Par-dessus, une couche de **charbon de bois écrasé en poudre**, humidifiée de la même eau salée (le charbon actif d'un filtre est le meilleur).
4. Appuyez un fil de cuivre, une mine de crayon ou une plaque de métal sur le charbon, sans toucher l'aluminium : c'est le plus. L'aluminium est le moins.

Une seule cellule de la taille d'une main peut donner environ un volt et quelques dizaines de milliampères. Deux ou trois en série allument une LED plusieurs heures, jusqu'à ce que l'aluminium soit rongé.

### La pile à fruits ou à légumes

Un clou galvanisé et une pièce ou un fil de cuivre plantés dans un citron, une pomme de terre ou un pot de choucroute, à deux ou trois centimètres l'un de l'autre. Trois ou quatre en série font briller faiblement une LED rouge. Bouillir la pomme de terre avant améliore nettement le résultat.

## ADAPTER

**Vous n'avez pas de multimètre.** Testez chaque cellule sur la langue, comme les électriciens d'autrefois testaient une pile 9 V : un léger picotement dit qu'il y a de la tension. Seulement sur ces petites piles de fortune, jamais sur autre chose. Mieux : voir [[TEC-ENE-008]].

**La LED ne s'allume pas.** Retournez-la. Puis vérifiez qu'aucun liquide ne coule d'une cellule à l'autre. Puis ajoutez des cellules.

**Vous voulez vraiment de l'énergie.** Les piles de fortune ne sont pas la solution. Récupérez des cellules de batterie sur un ordinateur portable ([[SURV-REC-021]]), une trottinette ou un outil sans fil, et rechargez-les au soleil ou avec une dynamo : voir [[SURV-ENE-001]].

**Vous voulez écouter la radio.** Un poste à galène n'a besoin d'aucune pile : l'énergie vient de l'onde elle-même. Voir [[TEC-RAD-001]].

**Les piles de fortune s'épuisent** quand le zinc ou l'aluminium est rongé : remplacez la rondelle ou la feuille, et retrempez les cartons. Elles se reconstruisent à l'infini, tant qu'il y a du métal.
