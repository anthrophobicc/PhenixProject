---
id: TEC-SOLR-001
titre: Le solaire photovoltaïque, du panneau à la prise
axe: 2
categorie: Énergie et Électricité
temps: Long
contexte: 1
risque: Discret
materiel: Technique
priorite: normale
origine: officielle
tags: [electricite, solaire, energie, autonomie]
sources: ["IEA Photovoltaic Power Systems Programme, technical reports", "Sandia National Laboratories, Photovoltaic Systems Handbook", "IEC 61215, qualification des modules photovoltaïques"]
---

::Un panneau solaire ne produit pas de l'électricité quand il fait chaud. Il en produit quand il reçoit de la lumière, et il en produit moins quand il chauffe.::

## La chaîne complète

Quatre éléments, et chacun peut être le maillon qui limite tout.

**Le panneau** transforme la lumière en courant continu. Sa puissance affichée en watts-crête correspond à des conditions de laboratoire qu'on n'atteint presque jamais en conditions réelles.

**Le régulateur** est indispensable dès qu'il y a une batterie. Un panneau branché directement sur une batterie la détruit, soit par surcharge, soit par décharge nocturne dans le panneau. C'est l'erreur la plus fréquente et la plus coûteuse.

**La batterie** stocke, parce que la production a lieu quand le soleil est là et la consommation quand il n'y est plus. C'est presque toujours l'élément le plus cher et le plus fragile de l'installation.

**L'onduleur** convertit le continu en alternatif, uniquement si vous devez alimenter des appareils qui l'exigent. Chaque conversion coûte de l'énergie : un appareil qui fonctionne directement en continu doit y rester.

## Ce qui détermine la production réelle

**L'orientation et l'inclinaison.** Face à l'équateur, incliné approximativement de la valeur de votre latitude. Un écart modéré coûte peu ; une orientation franchement mauvaise coûte beaucoup.

**L'ombre, et c'est ici que se trouve le piège majeur.** Dans un panneau classique, les cellules sont en série. Une seule cellule ombrée limite le courant de toute la chaîne, comme un tuyau pincé. **Une ombre portée sur un dixième de la surface peut faire chuter la production de bien plus qu'un dixième.** Une branche, un mât, un fil électrique, une cheminée suffisent. C'est le premier point à vérifier avant tout calcul.

**La saleté.** Poussière, sable, fientes, pollen. Un nettoyage à l'eau claire restitue une part appréciable de la production perdue.

**La température, à contre-courant de l'intuition.** Le rendement d'une cellule silicium **diminue quand elle chauffe**. Un panneau ventilé par l'arrière produit davantage qu'un panneau plaqué sur une surface qui accumule la chaleur. Une journée froide et lumineuse est meilleure qu'une journée caniculaire.

**La saison.** Sous nos latitudes, l'écart entre production estivale et hivernale est considérable. Dimensionner sur la moyenne annuelle garantit de manquer d'énergie l'hiver, précisément quand les besoins d'éclairage et de chauffage augmentent. **On dimensionne sur le mois le plus défavorable.**

## Le calcul qui décide de tout

Le même que dans [[TEC-ENE-001]] : additionnez ce que vous consommez par jour en wattheures, comparez à ce que vous pouvez produire et stocker.

Deux corrections indispensables. Les pertes de la chaîne complète — câbles, régulateur, rendement de charge et de décharge, conversion — sont loin d'être négligeables et se cumulent. Et une batterie ne se vide jamais entièrement : sa capacité réellement utilisable est nettement inférieure à sa capacité affichée, sauf à la détruire prématurément.

## Dimensionner et installer

1. **Mesurez avant d'acheter.** Listez vos usages réels, leur puissance et leur durée quotidienne. Presque toutes les installations décevantes viennent d'un besoin sous-estimé.
2. **Réduisez le besoin avant d'augmenter la production.** Diviser une consommation par deux coûte toujours moins cher que doubler une production.
3. **Vérifiez les ombres sur une journée entière**, pas à un seul moment. L'ombre de midi en juin n'a rien à voir avec celle de dix heures en décembre.
4. **Installez le régulateur entre le panneau et la batterie**, jamais l'inverse, et respectez la polarité — une inversion détruit l'électronique instantanément.
5. **Protégez chaque branche par un fusible adapté**, au plus près de la batterie. Une batterie court-circuitée délivre un courant énorme et provoque un incendie en quelques secondes.
6. **Ventilez l'arrière des panneaux** et le local des batteries.

**Sécurité.** Un panneau exposé à la lumière est sous tension en permanence : il n'y a pas d'interrupteur naturel. On le couvre d'un tissu opaque avant d'intervenir. Une batterie au plomb en charge dégage de l'hydrogène, inflammable et explosif en espace confiné : ventilation obligatoire, aucune flamme ni étincelle à proximité.

## Les configurations

**Vous récupérez du matériel.** Les panneaux de signalisation routière, d'éclairage urbain et de mobilier de jardin sont partout et fonctionnent immédiatement. Vérifiez l'absence de fissure dans le verre : un panneau fissuré laisse entrer l'humidité et perd sa puissance progressivement, sans que rien ne se voie au premier essai.

**Vous n'avez pas de régulateur.** Une charge très petite au regard de la capacité de la batterie peut être tolérée un temps sous surveillance, mais c'est un pis-aller. Le régulateur est la pièce à trouver en priorité, avant même un panneau supplémentaire.

**Vous choisissez une batterie.** Le plomb pardonne l'absence d'électronique de gestion et se recharge avec des moyens rudimentaires. Le lithium stocke bien plus pour le même poids mais exige une gestion précise sous peine d'incendie. Ce compromis est détaillé dans [[TEC-ENE-001]].

**Vous voulez le maximum avec le minimum.** Alimentez directement en courant continu, à la tension de votre batterie, des appareils prévus pour. Vous supprimez l'onduleur, ses pertes et sa panne possible.
