---
id: TEC-MEC-007
titre: L'impression 3D
axe: 2
categorie: Mécanique et Transport
temps: Long
contexte: 1
risque: Discret
materiel: Technique
priorite: normale
origine: officielle
tags: [impression3d, FDM, PLA, ABS, fabrication, couche, modèle, buse]
sources: ["Documentation technique sur l'impression FDM et SLA", "RepRap Project, imprimantes auto-réplicables", "Guides de paramétrage et de maintenance des imprimantes grand public"]
---

::Une imprimante 3D construit un objet en empilant des couches de matière fondue, une par une, du bas vers le haut. C'est lent, limité et révolutionnaire — parce que la seule machine qui fabrique n'importe quelle forme sans moule, sans outil de coupe et sans savoir-faire manuel.::

## COMPRENDRE

### Le principe : la fabrication additive

Au lieu de tailler dans un bloc (soustraire) ou de couler dans un moule (former), on ajoute de la matière couche par couche. Chaque couche est une tranche horizontale de l'objet. Empilées, elles donnent la forme complète. Pas de déchet, pas de moule, mais un objet dont la résistance dépend de l'adhérence entre les couches.

### Les deux procédés courants

**FDM (dépôt de fil fondu).** Un fil plastique (le filament) passe dans une buse chauffée qui le fond et le dépose sur un plateau, ligne par ligne, couche par couche. C'est le procédé le plus répandu, le moins cher, le plus réparable. Les imprimantes grand public (Creality, Prusa, Bambu) sont toutes FDM.

**SLA (stéréolithographie).** Une résine liquide dans un bac est durcie point par point par un laser UV ou un écran. Plus précis que le FDM, meilleur état de surface, mais les pièces sont plus fragiles, la résine est toxique avant durcissement, et le post-traitement est obligatoire (lavage, cure UV). Plus adapté aux petites pièces de détail.

### Les matériaux FDM

**PLA.** Le plus facile. Biodégradable (issu de l'amidon de maïs), imprime à basse température (190 à 210 degrés), peu de retrait, bonne précision. Faiblesse : ramollit vers 60 degrés, fragile aux chocs, ne tient pas à l'extérieur longtemps.

**ABS.** Plus résistant mécaniquement et thermiquement. Imprime plus chaud (230 à 250 degrés), dégage des fumées toxiques (ventiler), se rétracte en refroidissant (nécessite un plateau chauffant et un caisson fermé).

**PETG.** Bon compromis entre PLA et ABS. Résistant, flexible, imprime sans fumées excessives, bonne tenue thermique. Le matériau par défaut pour les pièces fonctionnelles.

**Nylon.** Très solide, flexible, résistant à l'usure. Absorbe l'humidité (il faut le sécher avant usage) et nécessite des températures élevées. Pour les pièces mécaniques sollicitées — engrenages, charnières, attaches.

### Le flux de travail

**1. Le modèle 3D.** Un fichier numérique (STL, 3MF) qui décrit la forme. On le dessine (logiciel de CAO : FreeCAD, Fusion 360, TinkerCAD), on le télécharge (Thingiverse, Printables), ou on scanne un objet existant (photogrammétrie, scanner 3D).

**2. Le trancheur (slicer).** Un logiciel (Cura, PrusaSlicer, OrcaSlicer) découpe le modèle en couches et génère le G-code — les instructions de déplacement de la buse et du plateau, ligne par ligne.

**3. L'impression.** Le G-code est envoyé à l'imprimante (carte SD, USB, réseau). L'impression d'une pièce simple prend de quelques minutes à plusieurs heures. Une pièce grande et détaillée peut prendre une journée.

## AGIR

### Paramètres essentiels

**Hauteur de couche.** Plus fin (0,1 mm) = plus lisse mais plus lent. Plus épais (0,3 mm) = plus rapide mais plus rugueux. 0,2 mm est le compromis standard.

**Remplissage.** L'intérieur de la pièce n'est pas plein — il est rempli d'une structure en grille ou en nid d'abeille. 15 a 20 pour cent suffisent pour la plupart des usages. 100 pour cent donne une pièce pleine et lourde — rarement nécessaire.

**Support.** Les surplombs au-delà de 45 degrés ne tiennent pas en l'air sans support. Le slicer génère des structures de soutien temporaires qu'on casse après impression. L'orientation de la pièce sur le plateau peut éliminer ou réduire le besoin de support.

**Température.** Buse trop froide : le filament colle mal. Trop chaude : filament trop fluide, bavures. Chaque matériau a sa plage.

**Adhérence au plateau.** La première couche doit coller. Plateau chauffant, laque, bâton de colle ou ruban de peintre selon le matériau.

### Maintenance

**Calibrer le plateau.** La distance entre la buse et le plateau doit être constante partout — une feuille de papier doit glisser avec une légère résistance. Un plateau mal calibré donne une première couche ratée et tout le reste avec.

**Nettoyer la buse.** Le filament résiduel carbonise et bouche. Un fil d'acupuncture ou une aiguille de nettoyage dégage le trou. Chauffer la buse d'abord.

**Tendre les courroies.** Les axes X et Y sont entraînés par des courroies crantées. Une courroie détendue donne des décalages de couche — des couches qui glissent visiblement sur le côté.

**Sécher le filament.** Le PETG et le nylon absorbent l'humidité de l'air. Un filament humide crépite à l'impression et donne des surfaces bulleuses. Un passage au four (50 degrés, quelques heures) ou un boîtier étanche avec dessiccant règle le problème.

## ADAPTER

**Vous imprimez une pièce mécanique.** Orientez-la pour que les couches soient perpendiculaires à la force principale. Les couches sont le point faible : une pièce se casse entre les couches, pas à travers.

**L'imprimante est dans un lieu sans électricité stable.** Une coupure en cours d'impression ruine la pièce. Certaines imprimantes reprennent après coupure (power recovery), mais le résultat est souvent fragile à la jonction. Un onduleur résout le problème.

**Vous voulez dupliquer un objet cassé.** Mesurer les dimensions, modéliser en CAO, imprimer. C'est l'usage le plus concret de l'impression 3D : recréer une pièce de rechange qui n'existe plus nulle part.

## Ce qu'il faut retenir

**L'impression 3D est lente et limitée en résistance** — mais c'est la seule machine qui fabrique n'importe quelle forme à partir d'un fichier, sans moule et sans outil.

**La résistance entre les couches est le point faible.** L'orientation de la pièce, le matériau et le remplissage décident de la solidité.

**Une imprimante FDM se calibre, se nettoie et se répare** — c'est une machine mécanique simple, pas une boîte noire. Les pièces d'usure (buse, courroie, plateau) se remplacent pour quelques euros.
