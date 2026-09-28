---
id: SURV-REC-012
titre: Récupérer dans une gare
axe: 3
categorie: Récupération
temps: Long
contexte: 1
risque: Exposé
materiel: Récupération
priorite: normale
origine: officielle
tags: [gare, rail, caténaire, isolateur, cuivre, céramique, infrastructure, récupération]
sources: ["SNCF Réseau, Architecture et composants de l'infrastructure ferroviaire", "Documentation sur l'alimentation électrique des lignes ferroviaires, caténaire et sous-stations", "Retours d'expérience sur la maintenance et les composants des gares"]
---

::Une gare est un entrepôt qui s'ignore. Des kilomètres de cuivre au-dessus des voies, des tonnes d'acier dans les rails, de l'énergie stockée dans les armoires techniques, et des isolateurs en céramique que personne ne regarde — jusqu'au jour où chaque composant compte.::

## COMPRENDRE

### Pourquoi une gare est un site majeur

Une gare concentre quatre systèmes qu'on ne retrouve nulle part ailleurs en un seul lieu : une infrastructure électrique haute tension, un réseau de communication autonome, des kilomètres de métal de qualité, et des locaux techniques équipés. Tout cela dans un bâtiment ouvert, conçu pour être accessible.

La gare de triage est encore plus riche : ateliers de maintenance, outillage lourd, réserves de lubrifiants et de pièces. Une gare rurale est plus modeste en stock commercial mais riche en infrastructure.

## AGIR

### Les voies et la caténaire — le gros lot

**Les rails.** Acier de haute qualité, profilé en I. Difficile à couper sans outillage, mais les éclisses — plaques de jonction boulonnées entre deux rails — se démontent à la clé. Chaque éclisse est une plaque d'acier percée, réutilisable comme enclume, plaque de cuisson, renfort de structure.

**Tire-fonds et boulonnerie.** Des centaines par kilomètre. Acier traité, filetage solide. Récupérables avec un arrache-tire-fond ou une clé à douille. Les traverses en bois (chêne créosoté) brûlent longtemps mais la créosote est toxique à la combustion.

**Le fil de contact.** C'est le câble que le pantographe touche : cuivre pur ou alliage cuivre-argent, section d'environ cent cinquante millimètres carrés. Un kilomètre de voie, c'est un kilomètre de fil et des dizaines de kilos de cuivre. Le câble porteur au-dessus est en bronze. **Sous tension — 25 000 volts en alternatif, 1 500 en continu selon les lignes — c'est la mort immédiate.** Vérifier l'absence de tension est un préalable absolu, et le doute vaut refus.

**Les isolateurs en céramique.** Les disques ou cloches en porcelaine — souvent blanc-gris, parfois bleu ou brun — qui séparent le fil de contact des pylônes. Ils résistent à des températures extrêmes, ne conduisent pas l'électricité, ne pourrissent pas. Leur surface dure sert d'abrasif fin, de support de cuisson réfractaire, ou de matériau de construction inerte. Les chaînes d'isolateurs des postes de sectionnement sont en céramique haute densité, parfois cinq ou six éléments empilés — chacun est un objet quasi indestructible. On les trouve aussi sur les poteaux électriques le long des voies.

**Le ballast.** Gravier concassé calibré — pas du sable. Utile en drainage, en remblai, en fondation de construction. Voir [[TEC-CON-002]].

### Les locaux techniques

**Armoires électriques.** Disjoncteurs, relais, contacteurs, câblage cuivre calibré et isolé, barres de cuivre. Les batteries de secours — plomb-acide ou nickel-cadmium — alimentent la signalisation en cas de coupure : elles se reconditionnent, et leur acide est un réactif chimique. Voir [[TEC-ENE-004]].

**Postes de signalisation.** Outillage de maintenance (clés, pinces, tournevis calibrés), huiles, graisses, lampes, fusibles. Les vieux postes mécaniques contiennent des leviers, des câbles de traction, des contrepoids en fonte — du métal de qualité en grande quantité.

**Locaux de maintenance.** Compresseurs, vérins, chalumeaux, établis, étaux. Les gares de triage en ont de véritables ateliers avec tours, perceuses à colonne, postes de soudure.

### Le bâtiment voyageurs

**Sanitaires.** Tuyauterie cuivre ou PVC, robinetterie, réservoirs. L'eau peut être coupée mais les ballons et chasses d'eau contiennent des litres utilisables.

**Commerces et distributeurs.** Les distributeurs automatiques contiennent un compresseur, un circuit frigorifique, un monnayeur en métal, et de l'électronique récupérable. Les stocks alimentaires ne durent pas, mais les emballages et contenants restent.

**Vitrage.** Le verre des abris de quai est trempé — il se brise en cubes non coupants. Le verre feuilleté du bâtiment principal est plus intéressant : grandes plaques utilisables comme panneau de serre, protection, surface plane. Voir [[TEC-CON-005]].

**Toiture et gouttières.** Zinc, cuivre ou aluminium selon l'époque. Les gouttières en zinc se découpent, se plient, se soudent à basse température.

**Sécurité.** Extincteurs (poudre, CO2, eau — voir [[URG-INC-001]]), bornes incendie (eau sous pression si le réseau tient), haches dans les coffrets rouges, plans d'évacuation plastifiés.

### Communications

**Haut-parleurs.** Aimants permanents à l'intérieur — en néodyme pour les récents, en ferrite pour les anciens. Le câblage de sonorisation parcourt la gare entière et c'est du cuivre utilisable.

**Caméras de surveillance.** Petites caméras étanches avec optique de qualité, câble coaxial ou Ethernet, alimentation PoE. L'optique seule vaut la récupération : lentilles de verre poli, utilisables comme loupe ou pour concentrer la lumière. Voir [[TEC-SAN-007]].

## ADAPTER

**La gare est encore sous tension.** On n'y touche pas. L'électrification ferroviaire est mortelle et les automatismes de réenclenchement peuvent remettre le courant sans prévenir. Si le réseau est durablement mort — et seulement alors —, l'absence de tension se vérifie avec un détecteur, pas à l'oeil. Voir [[TEC-ENE-003]].

**C'est une gare de triage ou un dépôt.** Le vrai trésor : ateliers complets, pièces de rechange, wagons-citernes (fioul, produits chimiques — lire l'étiquetage avant de toucher), grues, ponts roulants.

**C'est un petit arrêt rural.** Moins de stock, mais un abri de quai, un local technique même petit, et la voie elle-même avec tout ce qu'elle porte.

**Vous ne savez pas si quelque chose est dangereux.** L'infrastructure ferroviaire contient de l'amiante (anciennes isolations), des PCB (vieux transformateurs), du plomb (peintures). La règle : ce qu'on ne sait pas identifier, on ne le manipule pas. Les étiquettes et pictogrammes existent pour une raison. Voir [[TEC-CHI-001]].

## Ce qu'il faut retenir

**La caténaire est le gros lot** — des kilomètres de cuivre pur, mais mortelle sous tension. Vérifier d'abord, récupérer ensuite.

**Les isolateurs en céramique** ne valent rien pour qui ne sait pas quoi en faire — et tout pour qui le sait : réfractaire, isolant, indestructible, gratuit.

**Les locaux techniques** contiennent l'outillage et les batteries que le bâtiment voyageurs ne montre pas. Chercher les portes marquées « interdit au public » — c'est derrière qu'on trouve l'utile.
