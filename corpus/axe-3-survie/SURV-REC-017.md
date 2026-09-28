---
id: SURV-REC-017
titre: Récupérer sur un satellite
axe: 3
categorie: Récupération
temps: Long
contexte: 1
risque: Exposé
materiel: Récupération
priorite: normale
origine: officielle
tags: [satellite, panneau solaire, néodyme, hydrazine, espace, MLI, récupération]
sources: ["ESA, Composition et architecture des satellites en orbite basse", "NASA, Guide de sécurité pour la récupération de débris spatiaux", "Documentation sur les matériaux et systèmes embarqués des satellites de communication et d'observation"]
---

::Un satellite tombé est un objet d'exception : panneaux solaires de qualité aérospatiale, aimants de précision, métaux rares — et parfois un réservoir d'hydrazine qui tue au contact. La valeur est immense, le danger aussi.::

## COMPRENDRE

### Pourquoi un satellite est au sol

Les satellites en orbite basse (moins de mille kilomètres d'altitude) redescendent quand leur orbite se dégrade — freinage atmosphérique résiduel, fin de carburant, dysfonctionnement. La rentrée atmosphérique détruit la majorité de la structure, mais les pièces les plus denses et les plus résistantes survivent et touchent le sol. Les grands satellites (plusieurs tonnes) laissent un champ de débris de plusieurs kilomètres.

### Ce qui survit à la rentrée

Les pièces en titane, en acier inoxydable, les réservoirs sous pression, les roues de réaction, les optiques protégées et les batteries résistantes. L'aluminium fond souvent, le carbone brûle, l'électronique légère se désintègre. Ce qui arrive au sol est déformé mais pas détruit.

## AGIR

### DANGER PREMIER : l'hydrazine

Beaucoup de satellites utilisent l'hydrazine comme propergol. C'est un liquide incolore à l'odeur forte d'ammoniac, **extrêmement toxique** — mortel par inhalation, par contact cutané et par ingestion. Cancérigène avéré. Il corrode les métaux et les tissus biologiques.

**Tout réservoir de satellite est suspect.** Les réservoirs de propulsion sont des sphères ou cylindres en titane, souvent enveloppés de MLI dorée. **Ne jamais ouvrir, percer ou chauffer un réservoir de satellite.** S'il fuit (odeur d'ammoniac intense), s'éloigner immédiatement et rester au vent. Marquer la zone.

### Composants récupérables (hors zone de propulsion)

**Panneaux solaires.** Cellules photovoltaïques en arséniure de gallium — rendement supérieur aux panneaux terrestres en silicium (environ trente pour cent contre vingt). Si les panneaux ont survécu à la rentrée (ce qui est rare — ils sont légers et brûlent), ils fonctionnent sous le soleil. Plus probablement, on récupère les cellules individuelles, fragiles mais fonctionnelles si intactes. Voir [[TEC-SOLR-001]].

**Roues de réaction.** Des gyroscopes motorisés qui orientent le satellite. Chaque roue contient un moteur brushless de haute précision, des roulements à billes parfaits et des aimants en néodyme de qualité supérieure. C'est le composant mécanique le plus précieux — les roulements spatiaux sont les meilleurs qu'on puisse trouver.

**MLI (isolation multi-couche).** Les « couvertures dorées » des satellites : des dizaines de feuilles alternées d'aluminium, de mylar et de Dacron. L'aluminium réfléchit le rayonnement thermique (utilisable comme réflecteur solaire, couverture de survie, écran thermique). Le mylar est étanche, léger et résistant.

**Antennes.** Paraboles en aluminium ou en composite, guides d'ondes en cuivre ou en aluminium, connecteurs plaqués or. La parabole elle-même est une surface réfléchissante et un contenant.

**Structure.** Les cadres en aluminium aérospatial (alliage 7075) ou en titane sont des métaux de qualité supérieure — plus légers et plus résistants que tout ce qu'on trouve dans l'industrie courante.

**Câblage.** Cuivre de haute pureté, isolé en PTFE (résistant à la chaleur et aux produits chimiques). Les connecteurs sont plaqués or — le placage se récupère chimiquement si on dispose d'acide nitrique, mais la quantité est infime.

**Optiques.** Les satellites d'observation portent des miroirs et des lentilles de précision extrême. Si l'optique a survécu, c'est un outil de valeur — télescope, loupe de haute qualité, concentration lumineuse.

### Et l'ISS ?

La Station spatiale internationale pèse quatre cent vingt tonnes. Un retour non contrôlé laisserait un champ de débris considérable. Les mêmes composants s'y trouvent, en bien plus grand : panneaux solaires géants, dizaines de batteries lithium-ion, modules pressurisés en aluminium épais (habitat réutilisable), scaphandres (combinaison étanche, casque en polycarbonate, système de survie autonome), réservoirs d'eau, oxygène stocké. Les propergols (MMH et NTO, aussi toxiques que l'hydrazine) rendent les modules de propulsion tout aussi dangereux.

## ADAPTER

**Vous trouvez un débris que vous ne pouvez pas identifier.** Tout objet métallique tombé du ciel qui porte des traces de brûlure de rentrée (surface noircie, métal déformé par la chaleur) est potentiellement spatial. Photographier, marquer, ne pas toucher les parties tubulaires ou sphériques (réservoirs).

**Le débris est radioactif.** Certains vieux satellites (surtout soviétiques, séries Cosmos) utilisaient des générateurs thermoélectriques à radio-isotopes (RTG). Un boîtier dense, anormalement chaud, ou qui déclenche un compteur Geiger est un RTG — extrêmement dangereux. S'éloigner immédiatement.

**Vous voulez les panneaux solaires mais ils sont brisés.** Les cellules GaAs individuelles sont petites (quelques centimètres carrés) et fragiles. Même brisées, certaines produisent encore du courant sous le soleil. Tester avec un multimètre. Voir [[TEC-ENE-008]].

## Ce qu'il faut retenir

**L'hydrazine tue.** Tout réservoir de satellite est suspect. Ne jamais ouvrir, percer ou chauffer. Si une odeur d'ammoniac se dégage, fuir.

**Les roues de réaction contiennent les meilleurs roulements et aimants au monde.** Ce sont des composants de précision introuvables ailleurs.

**Le MLI est une couverture de survie spatiale** — légère, réfléchissante, étanche — et il y en a des mètres carrés sur chaque satellite.
