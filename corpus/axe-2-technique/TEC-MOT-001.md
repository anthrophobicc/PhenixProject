---
id: TEC-MOT-001
titre: Les moteurs de bateau — typologie complète
axe: 2
categorie: Mécanique et Transport
temps: Long
contexte: 1
risque: Discret
materiel: Technique
priorite: normale
origine: officielle
tags: [moteur, bateau, mecanique, transport]
sources: []
---

::Un moteur marin ne se distingue pas d'un moteur terrestre par sa mécanique, mais par ce qu'il subit.::

Trois contraintes définissent toute motorisation marine, et elles expliquent chaque choix technique qui suit.

**La charge est permanente.** Un moteur de voiture passe l'essentiel de sa vie en charge partielle. Un moteur de bateau pousse une masse d'eau en continu, sans temps mort, sans descente. Il travaille près de son régime de couple maximal pendant des heures. C'est pourquoi un moteur de voiture transplanté sur un bateau casse : il n'a jamais été dimensionné pour ça. Le fonctionnement commun aux deux est décrit dans [[TEC-MOTH-001]].

**Le refroidissement se fait par l'eau où l'on navigue.** C'est gratuit, illimité, et corrosif. Toute la conception marine tourne autour de ce compromis.

**Une panne n'est pas un arrêt sur le bas-côté.** La redondance et la réparabilité ne sont pas du luxe.

## Le classement par implantation

**Hors-bord.** Bloc complet — moteur, transmission, hélice — accroché au tableau arrière. Il bascule pour relever l'hélice, il se démonte entièrement, il se remplace en quelques minutes. C'est la motorisation la plus réparable et la plus interchangeable qui existe sur l'eau. Sa faiblesse est la position du poids, haut et en arrière.

**In-bord.** Moteur à l'intérieur de la coque, arbre traversant la coque via un presse-étoupe, hélice sous la carène. Poids bas et centré, donc bien meilleure tenue de mer. En contrepartie : un passage de coque à étancher en permanence, un arbre à aligner au dixième de millimètre, un accès contraint, et une ligne d'arbre qui impose l'inclinaison de l'hélice.

**Semi-hors-bord, dit embase Z.** Moteur dedans, transmission dehors sur une embase orientable. Compromis entre les deux : rendement d'hélice d'un hors-bord, poids interne d'un in-bord. Complexité mécanique nettement supérieure, et un soufflet en caoutchouc traversant la coque dont la rupture coule le bateau.

**Propulsion par jet.** Une pompe aspire l'eau et l'éjecte. Aucun appendice sous la coque, donc navigation en eau très peu profonde et absence de risque de blessure par hélice. Rendement médiocre à basse vitesse, sensibilité aux corps flottants aspirés.

**Pod électrique.** Moteur électrique immergé dans une nacelle orientable à 360 degrés. Manœuvrabilité totale sans propulseur d'étrave. Sur les grandes unités, un groupe diesel produit l'électricité et les pods propulsent : cela découple production et propulsion, et permet de couper des générateurs quand la demande baisse.

## Le classement par cycle

**Deux temps.** Une explosion par tour. Puissance élevée pour un poids faible, très peu de pièces mobiles, réparabilité exceptionnelle. Il consomme davantage, il fume, et il rejette une part d'huile imbrûlée. Les réglementations d'émissions l'ont fait reculer partout, mais dans un contexte de réparation autonome, sa simplicité redevient décisive. Sur les modèles à injection directe, une grande partie du défaut de consommation disparaît.

**Quatre temps.** Sobre, propre, silencieux, coupleux à bas régime. Circuit d'huile séparé donc vidanges, plus de pièces, davantage de choses à comprendre avant d'intervenir.

**Diesel.** Couple énorme à bas régime, exactement ce que demande une hélice. Pas de circuit d'allumage à corroder — un avantage considérable en atmosphère saline. Durée de vie très supérieure. En contrepartie : masse importante, injection haute pression intolérante à l'eau, démarrage difficile par grand froid.

**Électrique.** Couple maximal dès l'arrêt, silence total, aucune vibration, aucun échappement. La limite est l'énergie embarquée, et son calcul est dans [[TEC-ENE-001]]. En usage lent et court — pêche, canaux, annexes — c'est déjà supérieur à tout le reste.

**Vapeur.** Marginal aujourd'hui, mais mentionné pour une raison précise : c'est le seul type qui accepte **n'importe quel combustible solide**. Bois, charbon, déchets. Dans une logique de rupture d'approvisionnement en carburant raffiné, c'est la seule motorisation qui reste alimentable indéfiniment.

## Le refroidissement, là où tout se joue

**Circuit ouvert.** L'eau de navigation traverse directement le moteur. Simple, léger, peu de pièces. Elle dépose du sel, elle corrode, elle entartre. Un moteur à circuit ouvert en mer se rince à l'eau douce après chaque sortie, sinon il se détruit lentement de l'intérieur.

**Circuit fermé.** Un circuit interne de liquide de refroidissement cède sa chaleur à l'eau de mer dans un échangeur. L'eau salée ne touche jamais le moteur. Plus lourd, plus cher, incomparablement plus durable.

Dans les deux cas, **la turbine de pompe à eau en caoutchouc est la pièce d'usure critique**. Elle est détruite en quelques secondes si le moteur tourne hors de l'eau, parce qu'elle est lubrifiée et refroidie par l'eau qu'elle pompe. C'est la première pièce de rechange à posséder, avant toutes les autres.

## L'hélice

Deux nombres la définissent : le **diamètre**, qui détermine la surface d'eau brassée, et le **pas**, la distance théorique parcourue en un tour. Grand pas et petit diamètre pour la vitesse, petit pas et grand diamètre pour la poussée.

Une hélice surdimensionnée empêche le moteur d'atteindre son régime maximal et le fait travailler en surcharge permanente : c'est la cause la plus fréquente de destruction lente d'un moteur marin. Une hélice sous-dimensionnée laisse le moteur s'emballer sans produire de poussée.

La **{{cavitation|Formation de bulles de vapeur par chute de pression sur les pales, qui érode le métal et fait perdre la poussée.}}** — formation de bulles de vapeur par chute de pression sur le dos des pales — érode physiquement le métal et fait perdre la poussée. Elle signale toujours un problème de géométrie, de profondeur d'immersion ou de régime.

## Identifier une motorisation marine

1. **Regardez où il est.** Dehors, dedans, ou mi-chemin : vous savez déjà comment y accéder et ce qu'il faut démonter.
2. **Cherchez la bougie.** Présente : essence. Absente : diesel.
3. **Cherchez la jauge d'huile.** Présente : quatre temps. Absente et carburant mélangé : deux temps.
4. **Suivez le circuit d'eau depuis la prise sous la coque.** Directement au bloc : circuit ouvert. Par un échangeur : circuit fermé.
5. **Trouvez le témoin d'eau à l'échappement.** Pas de filet d'eau au démarrage : coupez immédiatement, la turbine est en train de mourir.
6. **Relevez la plaque.** Puissance, régime maximal, année, numéro de série.

## Critères de choix

**Vous devez choisir une motorisation à construire ou à récupérer.** Diesel in-bord si vous cherchez la durée et le couple. Hors-bord deux temps si vous cherchez la réparabilité et l'interchangeabilité. Électrique si vos trajets sont courts et votre production électrique existe.

**Vous n'avez plus de carburant raffiné.** Le diesel accepte des huiles végétales filtrées avec des adaptations. La vapeur accepte tout ce qui brûle. L'essence n'accepte à peu près rien d'autre qu'elle-même.

**Vous devez manœuvrer vous-même.** Les gestes, le balisage et les règles de barre sont dans [[TEC-NAV-001]].

**Vous cannibalisez.** Un hors-bord se transporte entier, se monte sur n'importe quelle coque munie d'un tableau arrière, et s'échange comme une pièce. C'est la motorisation la plus proche d'un standard universel sur l'eau.
