---
id: SURV-LUM-001
titre: Fabriquer une lampe
axe: 3
categorie: Feu, Eau et Ressources
temps: Court
contexte: 1
risque: Discret
materiel: Récupération
priorite: normale
origine: officielle
tags: [lumiere, led, pile, batterie, fabrication, recuperation, nuit]
sources: ["Fiches techniques constructeurs de LED, caractéristiques directes courantes", "INRS, Risques liés aux accumulateurs lithium-ion", "Documentation Leroy Merlin et ADEME sur l'éclairage LED", "Pratiques documentées d'éclairage de secours en milieu isolé"]
---

::Une lampe, c'est trois choses : quelque chose qui brille, quelque chose qui pousse le courant, et quelque chose qui coupe. Le reste est de la carrosserie.::

## COMPRENDRE

### La LED a changé la donne

Une ampoule à filament transforme en lumière environ cinq pour cent de ce qu'elle consomme ; le reste part en chaleur. Une LED blanche fait dix à vingt fois mieux.

En pratique, cela veut dire qu'**une LED éclaire une nuit entière sur deux piles bâtons là où une ampoule les vide en une heure.** Quand l'énergie ne se recharge plus, c'est toute la différence.

Trois choses à savoir avant de brancher quoi que ce soit.

**Elle est polarisée.** Elle ne s'allume que dans un sens. La patte longue est le plus, le côté aplati du boîtier est le moins. Branchée à l'envers, elle ne fait rien — elle ne casse pas pour autant à basse tension.

**Elle veut une tension précise.** Environ 1,8 à 2,2 volts pour une rouge, 3 à 3,4 volts pour une blanche ou une bleue.

**Elle ne limite pas son courant toute seule.** C'est le point qui tue les LED des débutants : au-dessus de sa tension, une LED tire tout ce qu'on lui donne, chauffe et meurt en quelques secondes. **Il faut une résistance en série**, sauf dans un cas particulier expliqué plus bas.

### Le calcul, une seule formule

La résistance vaut la tension en trop divisée par le courant voulu.

**R = (tension de la pile − tension de la LED) ÷ courant**

Exemple concret. Trois piles bâtons font 4,5 volts, une LED blanche en consomme 3,2, il reste 1,3 volt à absorber. Pour vingt milliampères, soit 0,02 ampère : 1,3 ÷ 0,02 = **65 ohms**. On prend la valeur du dessus qu'on a sous la main, 68 ou 100 ohms. Plus la résistance est forte, moins ça éclaire, plus ça dure.

En dessous de dix milliampères une LED éclaire encore utilement pour lire ou se déplacer. **Pour une lampe qui doit tenir, visez bas.**

### Le cas sans résistance

Une pile bouton au lithium, du type de celles des montres et des cartes mères, a une résistance interne élevée : elle ne peut physiquement pas débiter assez pour détruire une LED. **Une LED blanche posée directement sur une pile bouton de trois volts fonctionne et tient plusieurs heures.** C'est la lampe la plus simple qui existe, et elle tient dans une poche de chemise.

## AGIR

**1. Trouvez la LED.** Guirlande électrique, lampe de vélo, éclairage de secours, plafonnier de voiture, feu arrière, lampe frontale morte, panneau publicitaire, rétroéclairage d'écran. Les télécommandes en contiennent aussi, mais elles émettent en infrarouge : invisibles à l'œil, inutiles ici.

**2. Trouvez l'énergie.** Piles bâtons, piles boutons, batterie de téléphone, batterie d'outil électroportatif, batterie de voiture. Le tri de ce qui est encore vivant est dans [[TEC-ENE-004]].

**3. Testez le sens.** Touchez brièvement les deux pattes sur une pile bouton. Ça s'allume ou pas. Notez le plus.

**4. Assemblez.** LED, résistance en série sur l'une des deux pattes, interrupteur ou simple lame de métal qu'on plie, et les fils. À souder si vous avez de quoi, sinon torsadé serré et serré dans du ruban adhésif — la méthode propre est dans [[SURV-REC-007]].

**5. Faites un porte-piles.** Deux vis dans une planchette, un ressort de stylo comme contact arrière, une bande de métal découpée dans une boîte de conserve. Le contact est ce qui lâche en premier : serrez-le et protégez-le de l'humidité.

**6. Ajoutez un réflecteur et un diffuseur.** Une boîte de conserve polie ou doublée d'aluminium concentre le faisceau. À l'inverse, **une bouteille en plastique remplie d'eau, posée sur la lampe, transforme un point aveuglant en lumière douce qui éclaire toute une pièce.** C'est le meilleur rapport effort-résultat de la fiche.

**7. Fermez le tout.** Un tube de PVC, une boîte de conserve, un bidon coupé. Prévoyez que ça tombe, que ça prenne l'eau, et que la pile devra se changer dans le noir.

## ADAPTER

**Vous n'avez pas de résistance.** Prenez-en une sur n'importe quelle carte électronique morte, ou remplacez-la par une deuxième LED en série, qui absorbera la tension en trop en éclairant elle aussi. Un bout de fil très fin et long fait office de résistance de fortune, mais c'est imprécis.

**Vous n'avez que des ampoules à filament.** Elles tolèrent tout, ne demandent aucune résistance et se moquent du sens. Une ampoule de voiture sur une batterie de voiture éclaire fort et vide la batterie vite. Réservez-les aux besoins courts et intenses.

**Vous avez une batterie de voiture.** C'est une réserve d'énergie énorme, et **un court-circuit y fait fondre un outil et démarre un incendie en quelques secondes.** Mettez un fusible dès la borne, isolez tout, et ne posez jamais un objet métallique en travers des deux bornes. Voir [[SURV-REC-003]] et [[TEC-ENE-003]].

**Vous récupérez des cellules d'ordinateur portable.** Les cellules cylindriques qu'on y trouve font 3,7 volts et une belle capacité, mais le lithium-ion ne pardonne pas : **une cellule percée, écrasée, gonflée ou court-circuitée peut s'emballer thermiquement, cracher des gaz toxiques et prendre feu toute seule.** Une cellule gonflée se met dehors, à l'écart, et ne se récupère pas. Ne chargez jamais sans un circuit prévu pour.

**Vous voulez préserver votre vision de nuit.** Utilisez une LED rouge, ou peignez la vôtre au marqueur rouge. L'œil adapté à l'obscurité met vingt à trente minutes à le redevenir après une lumière blanche, et quelques secondes après une rouge. Voir [[TEC-NUI-001]] et [[SURV-NUIT-001]].

**Vous devez rester discret.** Une lampe se voit de très loin la nuit, bien plus loin qu'on ne l'imagine. Baissez le courant, filtrez en rouge, éclairez vers le bas, et masquez tout sauf un trou de la taille d'une pièce.

**Vous n'avez aucune électricité.** Une mèche de coton dans un bocal d'huile végétale, posée sur une rondelle de métal percée, brûle des heures avec une flamme stable. Toute combustion consomme l'oxygène de la pièce et produit du monoxyde : ventilez. Voir [[SURV-FEU-001]] et [[URG-AIR-001]].

**Vous voulez recharger.** Un petit panneau solaire de jardin, une dynamo de vélo, un chargeur de voiture : le raccordement et les précautions sont dans [[TEC-SOLR-001]] et [[TEC-ENE-001]].
