---
id: TEC-ELN-004
titre: Les LED
axe: 2
categorie: Électronique et Numérique
temps: Court
contexte: 1
risque: Discret
materiel: Technique
priorite: normale
origine: officielle
tags: [led, diode, eclairage, resistance, oled, ampoule, electronique]
sources: ["Schubert E. F., Light-Emitting Diodes, Cambridge University Press, 2e édition", "Fondation Nobel, Prix Nobel de physique 2014 : diodes électroluminescentes bleues efficaces (Akasaki, Amano, Nakamura)", "US Department of Energy, LED Lighting Facts et rapports sur la durée de vie des lampes LED"]
---

::Une LED, c'est un morceau de cristal qui s'illumine quand le courant le traverse dans le bon sens. Elle a remplacé l'ampoule à filament en quinze ans, parce qu'elle fait la même lumière avec dix fois moins d'énergie.::

## Ce qui se passe dedans

Une LED (diode électroluminescente) est une **diode** : un composant qui ne laisse passer le courant que dans un sens. Au cœur, deux couches de semi-conducteur se touchent. Quand le courant passe, des électrons tombent d'un niveau d'énergie à un autre en libérant chacun un grain de lumière.

**La couleur dépend du matériau**, pas d'un filtre : le rouge et l'infrarouge sont connus depuis les années 1960, le bleu efficace n'est arrivé que dans les années 1990, ce qui a valu le prix Nobel de physique 2014 à ses inventeurs. **La LED blanche** est une LED bleue recouverte d'une poudre jaune (un phosphore) : le mélange bleu et jaune donne du blanc.

## Les chiffres utiles

**Chaque couleur demande sa tension**, appelée tension de seuil :

| Couleur | Tension de seuil typique |
|---|---|
| Infrarouge | 1,2 à 1,5 V |
| Rouge, orange, jaune | 1,8 à 2,2 V |
| Verte, bleue, blanche | 2,8 à 3,4 V |

**Une petite LED témoin** de 3 ou 5 mm supporte environ **20 milliampères**. Au-delà, elle chauffe et meurt.

**Le sens compte.** La patte la plus longue est le plus (l'anode). Le côté plat du bord de la LED est le moins (la cathode). Branchée à l'envers, elle ne s'allume pas, et au-delà de quelques volts à l'envers, elle peut griller.

## La règle d'or : toujours limiter le courant

Une LED branchée directement sur une pile trop forte grille en une fraction de seconde : dès qu'elle dépasse sa tension de seuil, elle laisse passer autant de courant qu'on lui en donne. On met donc **une résistance en série**, calculée ainsi :

**R = (tension de la source − tension de la LED) ÷ courant voulu**

Exemple : une LED blanche (3 V) sur une alimentation USB de 5 V, à 20 mA : (5 − 3) ÷ 0,02 = **100 ohms**. En cas de doute, prenez la valeur au-dessus : la LED éclairera un peu moins, et vivra plus longtemps. Voir [[TEC-ENE-002]].

## L'éclairage

- **Rendement** : une ampoule LED produit environ 100 lumens par watt ou plus, contre 10 à 15 pour une ampoule à filament. Pour la même lumière, **dix fois moins d'énergie** : c'est ce qui rend l'éclairage possible sur une petite batterie ou un panneau solaire.
- **Durée de vie** : les LED elles-mêmes durent des dizaines de milliers d'heures. Dans une ampoule, c'est presque toujours **l'électronique d'alimentation qui lâche d'abord**, à cause de la chaleur. Une ampoule LED enfermée dans un plafonnier étanche vit beaucoup moins longtemps.
- **La chaleur** est l'ennemie : une LED de puissance doit être collée sur un radiateur métallique.

## Les écrans

- **LCD** : les LED servent de lampe arrière, voir [[TEC-ELN-002]].
- **OLED** : chaque sous-pixel est une minuscule LED organique qui fait sa propre lumière. Noirs parfaits et contraste infini, mais les pixels s'usent à la longue et une image fixe laissée des mois peut rester marquée.
- **Écrans géants** des stades et des façades : une mosaïque de LED classiques, visibles en plein soleil.

## Les astuces de bricoleur

- **Tester une LED** : un multimètre en position diode l'allume faiblement. Ou une pile bouton de 3 V, pattes pincées dessus : une LED rouge, verte ou blanche s'allume sans résistance, car la pile ne peut pas fournir assez de courant pour la griller.
- **Voir l'infrarouge** : la LED d'une télécommande est invisible à l'œil, mais l'appareil photo d'un téléphone la voit clignoter en violet. C'est le test de télécommande le plus rapide qui existe.
- **Une ampoule LED qui ne s'allume plus** n'a souvent qu'une seule LED morte sur une chaîne montée en série : un point noir brûlé à sa surface la trahit. Ponter cette LED avec un fil suffit parfois à faire repartir les autres. **Attention : ces ampoules fonctionnent directement sur le 230 volts, on n'y touche que débranchées et condensateurs déchargés.**
- **Tirer la dernière goutte d'une pile usée** : un petit montage appelé « voleur de joules » (un transistor, une résistance, une bobine enroulée sur une petite ferrite) élève la tension d'une pile de 1,5 V à moitié morte pour allumer une LED blanche des heures durant.
- **Les bandes de LED en 12 V** se coupent tous les trois LED environ, aux marques prévues. Elles se branchent directement sur une batterie de voiture ou de moto, sans résistance à ajouter : elle est déjà sur la bande.

Pour allumer une LED sans réseau, voir [[SURV-ENE-001]] et [[SURV-ENE-002]].
