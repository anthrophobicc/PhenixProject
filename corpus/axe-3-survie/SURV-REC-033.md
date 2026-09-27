---
id: SURV-REC-033
titre: Faire une batterie avec des cellules récupérées
axe: 3
categorie: Récupération
temps: Long
contexte: 1
risque: Exposé
materiel: Technique
priorite: normale
origine: officielle
tags: [batterie, 18650, lithium, cellules, bms, recuperation, portable, powerbank, securite]
sources: ["Battery University, BU-302 et BU-808 (assemblage en série et parallèle, vieillissement)", "Fiches techniques des cellules lithium-ion 18650 (Samsung, LG, Panasonic)", "INERIS, emballement thermique des batteries lithium-ion"]
---

::Un vieil ordinateur portable contient six à neuf cellules lithium qui marchent souvent encore. Assemblées avec soin, elles font une batterie de secours. Assemblées n'importe comment, elles font un incendie.::

## COMPRENDRE

**La cellule 18650** : un cylindre de 18 mm sur 65 mm, **3,6 à 3,7 V** nominal, **4,2 V** chargée, à ne pas descendre sous **2,5 à 3 V**. Capacité : 1 500 à 3 500 mAh selon le modèle et l'usure.

On les trouve dans les batteries d'ordinateurs portables, de trottinettes, d'outils sans fil, de lampes puissantes et de batteries externes.

**En parallèle**, on additionne les capacités (même tension). **En série**, on additionne les tensions : 3 cellules en série font environ 11 à 12,6 V, **4 en série** font environ 13 à 16,8 V.

## AGIR

**Trier les cellules**

1. **Écartez sans discuter** toute cellule cabossée, percée, gonflée, rouillée, qui a fui, ou dont l'enveloppe plastique est déchirée.
2. **Mesurez la tension** au multimètre : moins de 2 V, elle a trop souffert ; on la jette (au recyclage).
3. **Chargez-les une par une** avec un chargeur de cellules lithium, puis laissez-les reposer quelques jours : **une cellule qui perd sa tension toute seule** est défaillante. **Une cellule qui chauffe en charge** aussi.
4. **Mesurez la capacité** si le chargeur le permet, et **regroupez les cellules de capacités proches**.

**Assembler**

- **Une carte de protection (BMS)** adaptée au nombre de cellules en série est **obligatoire** : elle coupe en cas de surcharge, de décharge profonde et de court-circuit.
- **Un fusible** sur la sortie positive.
- **Des cellules de même état** dans un même pack.
- **Les liaisons** se font par soudure par points (idéal) ou avec des supports de piles du commerce. **Souder directement sur une cellule** la chauffe et l'abîme : si on n'a pas le choix, on le fait très vite, avec un gros fer très chaud et beaucoup de flux, pour chauffer le moins longtemps possible.
- **Isolez tout** : papier isolant, gaine thermorétractable. Un court-circuit libère une énergie énorme.

## ADAPTER

**Le plus simple et le plus sûr** : des **boîtiers de batterie externe** vendus vides, avec leur électronique de charge et leur protection, dans lesquels on insère des cellules triées. Aucune soudure.

**Pour du 12 V**, quatre cellules en série de lithium fer phosphate (LiFePO4, 3,2 V chacune) donnent une tension très proche d'une batterie de voiture et sont bien plus sûres ; les cellules d'ordinateur portable (lithium-ion) font environ 11 à 16 V en 4 séries, et demandent un régulateur.

**Stockez et chargez** sur une surface non inflammable, jamais la nuit sans surveillance, jamais au soleil. Une cellule qui gonfle sort de la maison. Voir [[SURV-REC-032]].

Récupérer les cellules d'un ordinateur : [[SURV-REC-021]]. Les batteries en général : [[TEC-ENE-004]].
