---
id: TEC-NUI-001
titre: La vision nocturne
axe: 2
categorie: Énergie et Électricité
temps: Long
contexte: 1
risque: Discret
materiel: Technique
priorite: normale
origine: officielle
tags: [vision nocturne, intensification de lumiere, thermographie, proche infrarouge, capteur, filtre infrarouge, adaptation a l'obscurite, jumelles, pupille]
sources: ["Hecht S., Haig C., Chase A., The influence of light adaptation on subsequent dark adaptation of the eye", "Night Vision and Electronic Sensors Directorate, technical reports on image intensification", "Documentation technique des capteurs CMOS et filtres infrarouges"]
---

::Trois choses différentes s'appellent « vision nocturne ». Une seule se fabrique avec de la récupération, et ce n'est pas celle qu'on imagine.::

## Les trois familles, et ce qu'elles font

**L'intensification de lumière** amplifie le peu de lumière disponible. Un photon frappe une photocathode, arrache un électron, qui est multiplié dans un tube sous très haute tension, puis reconverti en lumière sur un écran. C'est la technologie des jumelles vertes.

Elle **ne se fabrique pas artisanalement** : le tube exige un vide poussé, des matériaux photosensibles spécifiques et une alimentation de plusieurs milliers de volts.

**La thermographie** détecte le rayonnement infrarouge lointain émis par la chaleur des corps. Elle voit dans l'obscurité totale et à travers la fumée. Le capteur est un composant spécialisé qui ne s'improvise pas davantage.

**L'imagerie proche infrarouge** utilise une lumière juste au-delà du visible, invisible à l'œil mais parfaitement captée par les capteurs photographiques ordinaires. **C'est la seule des trois qui puisse se bricoler** avec du matériel courant : elle demande un capteur qui la voit, et une source qui l'éclaire.

## Pourquoi un appareil photo voit l'infrarouge

Les capteurs des appareils photo et des téléphones sont naturellement sensibles bien au-delà du rouge visible. Cette sensibilité fausserait les couleurs, donc les constructeurs placent devant le capteur un **filtre bloquant l'infrarouge**.

Retirer ce filtre rend l'appareil sensible au proche infrarouge. C'est une opération de démontage délicate mais réelle, pratiquée couramment sur des webcams et de vieux appareils. Une fois le filtre ôté, on place à sa place un filtre inverse, qui bloque le visible et laisse passer l'infrarouge, et l'on obtient une caméra qui ne voit que l'infrarouge.

**Une expérience simple le montre** : une télécommande pointée vers l'objectif d'un téléphone apparaît à l'écran comme une diode violet pâle, alors que l'œil nu ne voit rien. La plupart des caméras frontales, moins bien filtrées, réagissent mieux que les caméras arrière.

## L'éclairage

Une caméra infrarouge sans source infrarouge ne voit rien la nuit : elle a besoin d'être éclairée, exactement comme une caméra ordinaire.

Les **diodes infrarouges** se récupèrent en quantité dans les télécommandes, les anciens systèmes de transmission et surtout les caméras de surveillance, qui en portent une couronne complète. Elles s'alimentent comme n'importe quelle diode, avec une résistance de limitation calculée selon [[TEC-ENE-002]].

À défaut, une lampe ordinaire recouverte d'un **filtre qui bloque le visible** émet essentiellement dans l'infrarouge : plusieurs épaisseurs de film photographique développé et entièrement noirci font office de filtre passable. Le rendement est mauvais, cela chauffe, et cela fonctionne.

**Une propriété décisive : cet éclairage est invisible à l'œil nu**, mais parfaitement visible pour quiconque possède un capteur non filtré. Un éclairage infrarouge n'est discret que face à des yeux, pas face à un appareil.

## Ce qui améliore la vision sans électronique

C'est la partie la plus rentable, et la moins connue.

**L'adaptation à l'obscurité** est un gain considérable et gratuit. L'essentiel se joue dans les vingt à trente premières minutes et continue au-delà ; une seule exposition à une lumière blanche vive l'annule en une seconde. Une lumière rouge de faible intensité la préserve en grande partie. Ce mécanisme et la technique de vision décalée sont détaillés dans [[SURV-NUIT-001]].

**L'ouverture optique** décide de la quantité de lumière recueillie. Ce qui compte dans une jumelle utilisée de nuit n'est pas le grossissement mais le **diamètre de la lentille rapporté au grossissement** : plus ce rapport est élevé, plus l'image est lumineuse. Une jumelle peu grossissante à grosses lentilles montre bien plus de choses la nuit qu'une forte grossissante compacte. Ce rapport ne sert à rien au-delà du diamètre de la pupille dilatée, qui plafonne autour de sept millimètres chez un jeune adulte et diminue avec l'âge.

**Le contraste plutôt que l'intensité.** De nuit, on distingue des formes et des mouvements, pas des détails. Se placer bas pour détacher les silhouettes sur le ciel, éviter d'avoir une source lumineuse dans le champ, et laisser le regard balayer lentement rendent bien plus que n'importe quel appareil.

## Les limites d'un système infrarouge improvisé

Un ensemble caméra infrarouge, éclairage infrarouge et petit écran donne une vision nocturne sur quelques dizaines de mètres, s'il y a de l'électricité (voir [[TEC-ENE-001]]). Il est encombrant, consomme, se voit de tout autre capteur, et l'écran détruit l'adaptation naturelle de l'œil. Il sert en poste fixe, pour surveiller un accès ou observer un animal ; pour se déplacer, l'œil adapté reste supérieur.
