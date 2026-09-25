---
id: TEC-MOTH-001
titre: Le moteur thermique — fonctionnement complet
axe: 2
categorie: Mécanique et Transport
temps: Long
contexte: 1
risque: Discret
materiel: Technique
priorite: normale
origine: officielle
tags: [moteur, mecanique, transport, energie]
sources: []
---

::Un moteur thermique fait une seule chose : il transforme une explosion en rotation. Tout le reste n'est que le prix à payer pour que ça dure.::

## Le principe, en une image

Un gaz qui brûle prend de l'expansion. Enfermez cette expansion dans un tube fermé d'un côté et mobile de l'autre, et vous obtenez une poussée. Reliez ce mobile à une manivelle, et la poussée devient une rotation. C'est tout. Un moteur de voiture, de tronçonneuse ou de cargo ne fait rien d'autre.

Le tube est le **cylindre**. Le mobile est le **piston**. La manivelle est le **vilebrequin**, et la tige qui les relie est la **bielle**.

## Les quatre temps

Le cycle qui équipe la quasi-totalité des moteurs de voiture se déroule en quatre courses du piston, soit deux tours de vilebrequin.

1. **Admission.** Le piston descend, une soupape s'ouvre, le mélange d'air et de carburant est aspiré.
2. **Compression.** Les soupapes se ferment, le piston remonte et comprime le mélange. Comprimer chauffe et rapproche les molécules : la combustion sera plus rapide et plus violente.
3. **Combustion.** Le mélange s'enflamme. Le gaz repousse violemment le piston vers le bas. **C'est le seul temps qui produit du travail.** Les trois autres le consomment.
4. **Échappement.** Le piston remonte, l'autre soupape s'ouvre, les gaz brûlés sont chassés.

Un moteur à un seul cylindre ne produirait donc de la force qu'un quart du temps, et vibrerait de façon insupportable.

![Le cycle à quatre temps](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1NjAgMjIyIiB3aWR0aD0iNTYwIiBoZWlnaHQ9IjIyMiI+PHJlY3Qgd2lkdGg9IjU2MCIgaGVpZ2h0PSIyMjIiIGZpbGw9Im5vbmUiLz48dGV4dCB4PSIyODAiIHk9IjI0IiBmb250LWZhbWlseT0idWktc2Fucy1zZXJpZixzeXN0ZW0tdWksLWFwcGxlLXN5c3RlbSxTZWdvZSBVSSxIZWx2ZXRpY2EsQXJpYWwsc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMyIgZmlsbD0iIzFGMUQxQSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC13ZWlnaHQ9IjYwMCI+VW4gc2V1bCB0ZW1wcyBzdXIgcXVhdHJlIHByb2R1aXQgZHUgdHJhdmFpbDwvdGV4dD48cmVjdCB4PSIzMCIgeT0iNDQiIHdpZHRoPSI4NiIgaGVpZ2h0PSIxMDQiIHJ4PSI1IiBmaWxsPSJub25lIiBzdHJva2U9IiMyODYwN0YiIHN0cm9rZS13aWR0aD0iMS41Ii8+PHJlY3QgeD0iNDYiIHk9IjcwIiB3aWR0aD0iNTQiIGhlaWdodD0iMjAiIHJ4PSIyIiBmaWxsPSIjMjg2MDdGIiBvcGFjaXR5PSIuODUiLz48bGluZSB4MT0iNzMiIHkxPSI5MCIgeDI9IjczIiB5Mj0iMTQyIiBzdHJva2U9IiMyODYwN0YiIHN0cm9rZS13aWR0aD0iMiIvPjx0ZXh0IHg9IjczIiB5PSIxNjYiIGZvbnQtZmFtaWx5PSJ1aS1zYW5zLXNlcmlmLHN5c3RlbS11aSwtYXBwbGUtc3lzdGVtLFNlZ29lIFVJLEhlbHZldGljYSxBcmlhbCxzYW5zLXNlcmlmIiBmb250LXNpemU9IjEyIiBmaWxsPSIjMjg2MDdGIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXdlaWdodD0iNjAwIj5BZG1pc3Npb248L3RleHQ+PHRleHQgeD0iNzMiIHk9IjE4MiIgZm9udC1mYW1pbHk9InVpLXNhbnMtc2VyaWYsc3lzdGVtLXVpLC1hcHBsZS1zeXN0ZW0sU2Vnb2UgVUksSGVsdmV0aWNhLEFyaWFsLHNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTAuNSIgZmlsbD0iIzhBODM3OCIgdGV4dC1hbmNob3I9Im1pZGRsZSI+bGUgcGlzdG9uIGRlc2NlbmQ8L3RleHQ+PHJlY3QgeD0iMTY1IiB5PSI0NCIgd2lkdGg9Ijg2IiBoZWlnaHQ9IjEwNCIgcng9IjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iIzhBODM3OCIgc3Ryb2tlLXdpZHRoPSIxLjUiLz48cmVjdCB4PSIxODEiIHk9IjEwOCIgd2lkdGg9IjU0IiBoZWlnaHQ9IjIwIiByeD0iMiIgZmlsbD0iIzhBODM3OCIgb3BhY2l0eT0iLjg1Ii8+PGxpbmUgeDE9IjIwOCIgeTE9IjEyOCIgeDI9IjIwOCIgeTI9IjE0MiIgc3Ryb2tlPSIjOEE4Mzc4IiBzdHJva2Utd2lkdGg9IjIiLz48dGV4dCB4PSIyMDgiIHk9IjE2NiIgZm9udC1mYW1pbHk9InVpLXNhbnMtc2VyaWYsc3lzdGVtLXVpLC1hcHBsZS1zeXN0ZW0sU2Vnb2UgVUksSGVsdmV0aWNhLEFyaWFsLHNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTIiIGZpbGw9IiM4QTgzNzgiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtd2VpZ2h0PSI2MDAiPkNvbXByZXNzaW9uPC90ZXh0Pjx0ZXh0IHg9IjIwOCIgeT0iMTgyIiBmb250LWZhbWlseT0idWktc2Fucy1zZXJpZixzeXN0ZW0tdWksLWFwcGxlLXN5c3RlbSxTZWdvZSBVSSxIZWx2ZXRpY2EsQXJpYWwsc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMC41IiBmaWxsPSIjOEE4Mzc4IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5sZSBwaXN0b24gbW9udGU8L3RleHQ+PHJlY3QgeD0iMzAwIiB5PSI0NCIgd2lkdGg9Ijg2IiBoZWlnaHQ9IjEwNCIgcng9IjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iI0EzMkUyMiIgc3Ryb2tlLXdpZHRoPSIxLjUiLz48cmVjdCB4PSIzMTYiIHk9IjczIiB3aWR0aD0iNTQiIGhlaWdodD0iMjAiIHJ4PSIyIiBmaWxsPSIjQTMyRTIyIiBvcGFjaXR5PSIuODUiLz48bGluZSB4MT0iMzQzIiB5MT0iOTMiIHgyPSIzNDMiIHkyPSIxNDIiIHN0cm9rZT0iI0EzMkUyMiIgc3Ryb2tlLXdpZHRoPSIyIi8+PHRleHQgeD0iMzQzIiB5PSIxNjYiIGZvbnQtZmFtaWx5PSJ1aS1zYW5zLXNlcmlmLHN5c3RlbS11aSwtYXBwbGUtc3lzdGVtLFNlZ29lIFVJLEhlbHZldGljYSxBcmlhbCxzYW5zLXNlcmlmIiBmb250LXNpemU9IjEyIiBmaWxsPSIjQTMyRTIyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXdlaWdodD0iNjAwIj5Db21idXN0aW9uPC90ZXh0Pjx0ZXh0IHg9IjM0MyIgeT0iMTgyIiBmb250LWZhbWlseT0idWktc2Fucy1zZXJpZixzeXN0ZW0tdWksLWFwcGxlLXN5c3RlbSxTZWdvZSBVSSxIZWx2ZXRpY2EsQXJpYWwsc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMC41IiBmaWxsPSIjOEE4Mzc4IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5kw6l0ZW50ZSBtb3RyaWNlPC90ZXh0PjxyZWN0IHg9IjQzNSIgeT0iNDQiIHdpZHRoPSI4NiIgaGVpZ2h0PSIxMDQiIHJ4PSI1IiBmaWxsPSJub25lIiBzdHJva2U9IiM4QTgzNzgiIHN0cm9rZS13aWR0aD0iMS41Ii8+PHJlY3QgeD0iNDUxIiB5PSIxMDgiIHdpZHRoPSI1NCIgaGVpZ2h0PSIyMCIgcng9IjIiIGZpbGw9IiM4QTgzNzgiIG9wYWNpdHk9Ii44NSIvPjxsaW5lIHgxPSI0NzgiIHkxPSIxMjgiIHgyPSI0NzgiIHkyPSIxNDIiIHN0cm9rZT0iIzhBODM3OCIgc3Ryb2tlLXdpZHRoPSIyIi8+PHRleHQgeD0iNDc4IiB5PSIxNjYiIGZvbnQtZmFtaWx5PSJ1aS1zYW5zLXNlcmlmLHN5c3RlbS11aSwtYXBwbGUtc3lzdGVtLFNlZ29lIFVJLEhlbHZldGljYSxBcmlhbCxzYW5zLXNlcmlmIiBmb250LXNpemU9IjEyIiBmaWxsPSIjOEE4Mzc4IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXdlaWdodD0iNjAwIj7DiWNoYXBwZW1lbnQ8L3RleHQ+PHRleHQgeD0iNDc4IiB5PSIxODIiIGZvbnQtZmFtaWx5PSJ1aS1zYW5zLXNlcmlmLHN5c3RlbS11aSwtYXBwbGUtc3lzdGVtLFNlZ29lIFVJLEhlbHZldGljYSxBcmlhbCxzYW5zLXNlcmlmIiBmb250LXNpemU9IjEwLjUiIGZpbGw9IiM4QTgzNzgiIHRleHQtYW5jaG9yPSJtaWRkbGUiPmxlIHBpc3RvbiBtb250ZTwvdGV4dD48cmVjdCB4PSIzMDAiIHk9IjQ0IiB3aWR0aD0iODYiIGhlaWdodD0iMTA0IiByeD0iNSIgZmlsbD0iI0EzMkUyMiIgb3BhY2l0eT0iLjA3Ii8+PHRleHQgeD0iMjgwIiB5PSIyMDgiIGZvbnQtZmFtaWx5PSJ1aS1zYW5zLXNlcmlmLHN5c3RlbS11aSwtYXBwbGUtc3lzdGVtLFNlZ29lIFVJLEhlbHZldGljYSxBcmlhbCxzYW5zLXNlcmlmIiBmb250LXNpemU9IjExIiBmaWxsPSIjOEE4Mzc4IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5MZXMgbW90ZXVycyDDoCBwbHVzaWV1cnMgY3lsaW5kcmVzIGTDqWNhbGVudCBsZXMgY3ljbGVzIHBvdXIgcXUndW4gcGlzdG9uIHBvdXNzZSBlbiBwZXJtYW5lbmNlPC90ZXh0Pjwvc3ZnPg==)
 C'est la seule raison d'être des moteurs à plusieurs cylindres : décaler les cycles pour qu'il y ait toujours un piston en train de pousser. Un quatre cylindres a une combustion tous les demi-tours. Un six, tous les tiers de tour. Plus il y a de cylindres, plus la rotation est lisse — et plus il y a de pièces à entretenir.

## Ce qui allume le mélange

C'est la seule différence de fond entre les deux grandes familles.

**L'essence** utilise une étincelle. Une bougie produit un arc électrique à l'instant précis choisi. Le mélange doit donc être précis et ne doit surtout pas s'enflammer tout seul sous la compression — d'où un taux de compression modéré, et d'où l'indice d'octane, qui mesure la résistance d'un carburant à l'auto-inflammation.

**Le diesel** n'a pas de bougie d'allumage. Il comprime de l'air seul, beaucoup plus fort, jusqu'à ce que cet air atteigne plusieurs centaines de degrés par le seul effet de la compression. Puis il injecte le gazole dedans, qui s'enflamme au contact. Conséquences en cascade : pas de circuit d'allumage à entretenir, un rendement supérieur parce que la compression est plus élevée, un couple bien plus important à bas régime, une construction plus lourde parce que les pressions sont énormes, et une intolérance totale à l'eau et aux impuretés dans le carburant, parce que l'injection travaille à des pressions où la moindre particule raye tout.

## Le deux temps

Il fait la même chose en deux courses au lieu de quatre : admission et compression pendant la montée, combustion et échappement pendant la descente. Une explosion à chaque tour au lieu d'un tour sur deux.

Il n'a ni soupapes, ni arbre à cames, ni circuit d'huile séparé — l'huile est mélangée au carburant et brûle avec lui. Résultat : très peu de pièces mobiles, un rapport puissance sur poids excellent, et une réparabilité exceptionnelle avec peu d'outillage. En contrepartie, il consomme davantage, il fume, et il rejette une part d'huile imbrûlée, ce qui l'a fait disparaître des voitures pour des raisons d'émissions. **Dans un contexte où l'on répare soi-même avec ce qu'on trouve, cette simplicité redevient un argument décisif.**

## Les organes annexes, et pourquoi chacun existe

**La distribution.** L'arbre à cames ouvre et ferme les soupapes au bon moment, entraîné par le vilebrequin via une courroie ou une chaîne. Si ce lien casse ou saute d'un cran, les soupapes ouvrent pendant que le piston monte : elles se rencontrent, et le moteur est détruit en une fraction de seconde. C'est la panne la plus destructrice qui existe sur un quatre temps.

**Le circuit d'huile.** Une pompe envoie l'huile en pression dans des canaux jusqu'aux coussinets du vilebrequin. L'huile ne sert pas seulement à réduire les frottements : elle forme un film qui empêche le métal de toucher le métal, elle évacue une partie de la chaleur, et elle emporte les particules d'usure vers le filtre. **Un moteur sans pression d'huile se détruit en quelques dizaines de secondes.**

**Le refroidissement.** Un tiers environ de l'énergie du carburant part en chaleur pure. Un circuit d'eau glycolée la transporte du bloc vers le radiateur, où l'air l'emporte. Le thermostat maintient la température dans une plage étroite, parce qu'un moteur froid s'use vite et consomme trop, tandis qu'un moteur surchauffé déforme sa culasse.

**L'alimentation en air.** Le moteur est une pompe à air : sa puissance est directement liée à la quantité d'air qu'il avale. Sur l'eau, cette contrainte change complètement, voir [[TEC-MOT-001]]. C'est toute la raison d'être du turbocompresseur, qui utilise l'énergie des gaz d'échappement pour comprimer l'air d'admission et faire entrer plus de mélange dans le même cylindre.

**Le volant moteur.** Un disque lourd sur le vilebrequin qui stocke l'énergie du temps moteur pour la restituer pendant les trois autres. Sans lui, le moteur s'arrêterait entre deux combustions.

**Le démarreur et l'alternateur.** Un moteur ne peut pas se lancer seul : il faut le faire tourner de l'extérieur pour amorcer le premier cycle. L'alternateur, ensuite, recharge la batterie et alimente tout le reste — c'est le point d'entrée de toute récupération électrique, traité dans [[TEC-ENE-001]].

## Identifier un moteur inconnu

Devant un moteur inconnu, l'ordre d'identification est toujours le même.

1. **Cherchez les bougies.** Présentes : essence. Absentes : diesel. C'est la première question parce qu'elle détermine tout le reste.
2. **Cherchez la jauge d'huile.** Présente : quatre temps. Absente, avec un carburant mélangé à l'huile : deux temps.
3. **Comptez les cylindres** en suivant les fils de bougie ou les injecteurs.
4. **Repérez la courroie ou la chaîne de distribution** et son état. Une courroie craquelée ou huileuse est une bombe à retardement.
5. **Vérifiez les niveaux avant de tenter quoi que ce soit.** Huile et liquide de refroidissement. Une huile laiteuse signale de l'eau dans l'huile, donc un joint de culasse percé.
6. **Relevez la plaque ou les numéros gravés sur le bloc.** C'est ce qui vous permettra de retrouver une pièce compatible sur un autre moteur.

## Comparer les motorisations

**Vous cherchez ce qui durera.** Un diesel atmosphérique ancien, à injection mécanique et sans électronique, est ce qui se rapproche le plus d'un moteur éternel : peu de capteurs, peu de choses à comprendre, et une tolérance mécanique élevée.

**Vous devez conduire le véhicule.** Les commandes, l'embrayage et la conduite sont dans [[TEC-VOI-001]] ; le vol dans [[TEC-AER-001]].

**Vous cherchez ce qui se répare avec rien.** Un deux temps. Une bougie, un carburateur, un joint, et vous avez couvert la majorité des pannes possibles.

**Vous n'avez plus de carburant raffiné.** Le diesel accepte des huiles végétales filtrées, dans certaines limites de viscosité et de température, avec des adaptations. L'essence n'accepte à peu près rien d'autre qu'elle-même. C'est un critère de choix décisif dans une logique de long terme.

**Vous cannibalisez.** Les pièces qui se réutilisent le plus facilement d'un moteur à l'autre sont l'alternateur, le démarreur, la pompe à eau et les durites. Le bloc et la culasse, eux, ne s'échangent qu'entre modèles identiques.
