---
id: SURV-REC-021
titre: Récupérer sur un ordinateur portable
axe: 3
categorie: Récupération
temps: Court
contexte: 1
risque: Discret
materiel: Récupération
priorite: normale
origine: officielle
tags: [recuperation, electronique, batterie, lithium, signal]
sources: ["Battery University — cellules lithium-ion : décharge profonde, stockage, sécurité", "INRS — Batteries au lithium : risques d'incendie", "iFixit — guides de démontage d'ordinateurs portables"]
---

::Un ordinateur portable mort contient une batterie, des aimants parmi les plus puissants qui existent, un miroir parfait et un écran. À condition de savoir quoi garder, et quoi ne jamais percer.::

## AGIR

1. **Essayez-le d'abord.** Un portable qui démarre, avec son chargeur, vaut bien plus entier : il lit des cartes hors ligne, des documents, une bibliothèque comme Phenix. Ne démontez que ce qui est vraiment mort.
2. **Débranchez la batterie avant tout.** Elle se trouve sous le clavier ou sous la coque du dessous. Déclipsez son connecteur **avant** de toucher quoi que ce soit d'autre.
3. **Regardez-la.** Gonflée, percée, chaude, ou qui sent le solvant : ne l'ouvrez pas, ne la pliez pas. Posez-la dehors, loin de tout ce qui brûle, sur de la terre ou du sable.
4. **Gardez, dans l'ordre :**
   - **la batterie** saine : des cellules lithium pour une lampe ou une batterie de secours (voir ADAPTER) ;
   - **le chargeur** : une alimentation propre de 19 à 20 volts ;
   - **le disque dur**, s'il en a un : deux aimants au néodyme et des plateaux qui font des miroirs ;
   - **les ventilateurs, haut-parleurs, la webcam, la petite pile ronde** de la carte mère ;
   - **les vis, les fils fins, la coque** en aluminium s'il y en a.
5. **Rangez les cellules isolées**, bornes recouvertes de ruban, jamais en vrac dans une poche avec des pièces ou des clés.

## ADAPTER

**Faire un miroir de signalisation.** Ouvrez le disque dur (vis Torx, souvent une cachée sous l'étiquette). Le plateau est un miroir presque parfait. Dans les portables, il est souvent en verre : ne le percez pas, visez avec la main tendue, voir [[SIG-COM-001]].

**Les aimants.** Ils se collent l'un à l'autre avec assez de force pour pincer la peau jusqu'au sang. Tenez-les loin d'un stimulateur cardiaque, des cartes bancaires et des boussoles. Collés sur une aiguille aimantée ou un tournevis, ils servent toute une vie.

**Faire une batterie de secours.** Les vieux portables ont des cellules cylindriques, les récents des poches plates. Une cellule seule se recharge avec un petit module de charge USB prévu pour le lithium, jamais branchée directement sur une alimentation. Associées à un module élévateur USB, elles rechargent un téléphone.

**La cellule est presque vide.** Mesurez sa tension au multimètre : en dessous de 2,5 volts environ, elle a été trop déchargée. Ne la rechargez pas, elle peut chauffer et prendre feu pendant la charge.

**L'écran.** Il ne marche pas seul, mais avec une petite carte contrôleur adaptée à sa référence (étiquette au dos), il devient un moniteur. Même cassé, sa dalle arrière diffuse la lumière : derrière elle, une bande de LED fait un éclairage doux et uniforme.

**Un feu de batterie.** Ne vous penchez pas au-dessus. Éloignez tout ce qui brûle, et noyez-le sous beaucoup d'eau ou recouvrez-le de sable s'il est dehors : un extincteur à poudre éteint les flammes mais la cellule repart souvent. Voir [[URG-INC-002]].

**Les données.** Le disque contient la vie de quelqu'un. Ce qui est utile à tous, cartes, livres, notices, peut se garder. Le reste ne vous regarde pas.

## COMPRENDRE

**Pourquoi le lithium est si dangereux abîmé.** Une cellule lithium est un sandwich très fin de deux électrodes séparées par une membrane de quelques millièmes de millimètre. Percée, écrasée ou trop chauffée, la membrane cède : les électrodes se touchent, la cellule chauffe, décompose son propre électrolyte et libère de quoi entretenir le feu. C'est l'emballement thermique, et il se propage d'une cellule à la voisine.

**Pourquoi 2,5 volts.** Une cellule « vide » s'arrête normalement vers 3 volts : son circuit de protection la coupe avant. Restée des mois sans ce circuit, elle peut descendre bien plus bas. Le cuivre d'une électrode commence alors à se dissoudre, puis se redépose en aiguilles pendant la recharge suivante. Ces aiguilles peuvent traverser la membrane : court-circuit interne, sans prévenir. Le seuil de 2,5 volts garde une marge.

**Pourquoi un plateau de disque dur est un si bon miroir.** Les têtes de lecture volent à quelques nanomètres de sa surface : elle doit être polie presque à l'atome près, bien au-delà d'un miroir de salle de bains.

**Pourquoi des aimants si forts dans si peu de place.** Le bras qui déplace les têtes doit sauter d'une piste à l'autre en quelques millisecondes. Les aimants au néodyme donnent cette force dans quelques grammes, et c'est pour ça qu'on les récupère.
