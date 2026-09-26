---
id: SURV-REC-007
titre: Réparer un câble, une prise, un contact
axe: 3
categorie: Récupération
temps: Court
contexte: 1
risque: Discret
materiel: Technique
priorite: normale
origine: officielle
tags: [electricite, reparation, cable, recuperation]
sources: []
---

::La grande majorité des pannes électriques ne sont pas des composants morts. Ce sont des fils coupés et des contacts sales.::

## COMPRENDRE

Un circuit ne fonctionne que s'il est **fermé** : le courant part, traverse la charge, et revient. Une interruption n'importe où produit exactement le même symptôme — rien ne marche — que le défaut soit à l'aller ou au retour.

Les points de rupture sont toujours les mêmes, et cette liste couvre presque tout : **là où le câble bouge**, c'est-à-dire à la sortie d'une prise ou d'un appareil ; **là où deux métaux se touchent**, c'est-à-dire aux connexions ; **là où l'humidité stagne**.

Un contact dégradé n'est pas une coupure franche : c'est une résistance qui apparaît. Elle chauffe, s'oxyde davantage, chauffe plus. **Un contact tiède est un contact en train de mourir** — mécanisme détaillé dans [[TEC-ENE-003]].

## AGIR

**Trouver le défaut avant de réparer.**

1. **Coupez et vérifiez l'absence de tension.** Toujours, et avec un appareil, jamais par déduction.
2. **Regardez et pliez.** Un câble se casse près des embouts : pliez doucement sur toute la longueur, une gaine dure, craquelée, molle ou déformée localement signale l'endroit.
3. **Testez la continuité** d'un bout à l'autre, conducteur par conducteur, câble débranché des deux côtés — voir [[TEC-ENE-008]]. Faites bouger le câble pendant la mesure : un défaut intermittent se révèle ainsi.
4. **Vérifiez les deux conducteurs.** Le retour casse aussi souvent que l'aller.

**Réparer une coupure.**

5. **Coupez franchement de part et d'autre** de la zone douteuse. Ne réparez pas au ras du défaut : le câble est fatigué sur plusieurs centimètres.
6. **Dénudez sans entailler le cuivre.** Une entaille crée un point faible qui cassera au premier mouvement. Faites tourner la lame autour de l'isolant plutôt que de trancher dedans.
7. **Décalez les jonctions.** Ne raccordez jamais les deux conducteurs au même endroit : un décalage de quelques centimètres évite qu'ils ne se touchent si l'isolation cède.
8. **Assemblez mécaniquement avant tout.** Torsadez serré dans le sens du toron, ou mieux, entourez un fil autour de l'autre en spires jointives. **La jonction doit tenir toute seule à la traction avant d'être isolée.**
9. **Soudez si vous pouvez.** Une soudure descend la résistance de contact à presque rien. Sinon, un domino ou un connecteur serti fait l'affaire.
10. **Isolez chaque conducteur séparément**, puis l'ensemble. Plusieurs tours croisés, en débordant largement de chaque côté.
11. **Ajoutez une décharge de traction.** Une boucle, un nœud ou un collier qui reprend l'effort avant la jonction : sans cela, votre réparation cassera au même endroit.

**Nettoyer un contact.**

12. **Grattez l'oxydation** au papier abrasif fin, à la lame ou à la gomme. Un contact terne conduit mal.
13. **Resserrez.** Le cuivre flue sous pression et une borne se desserre seule avec le temps.
14. **Protégez** d'une trace de graisse une fois le contact propre et serré, si l'ambiance est humide — voir [[TEC-COR-001]].

## ADAPTER

**Le câble est intermittent.** C'est presque toujours un brin cassé sous l'isolant, à un point de flexion. Il faut couper généreusement de part et d'autre : réparer trop court laisse la partie fatiguée en place.

**Vous n'avez pas de ruban isolant.** Une gaine thermorétractable est meilleure ; à défaut, du ruban adhésif épais, du caoutchouc de chambre à air découpé en bande et étiré en spires serrées, ou une immersion dans une matière plastique fondue.

**Vous n'avez aucun outil.** Grattez avec ce que vous avez : une clé de maison, le bord d'une pièce, une pierre, du sable sur un chiffon. Une cosse de batterie desserrée s'enfonce sur une borne conique : poussez-la à fond, tapez-la avec une pierre, puis tournez-la pour la bloquer. En dernier recours, une bande d'aluminium (papier de chewing-gum, canette découpée) glissée entre la cosse et la borne rattrape le jeu, le temps de repartir. **Ne reliez jamais les deux bornes avec un objet en métal** : une batterie de voiture débite des centaines d'ampères et le métal devient brûlant.

**Vous n'avez rien pour souder.** Une jonction mécanique bien faite fonctionne des années. Ce qui compte est le serrage, la surface de contact et la protection contre l'humidité, pas la soudure elle-même.

**Les fils ne sont pas du même métal.** Cuivre et aluminium en contact direct se corrodent — voir [[TEC-COR-001]]. Utilisez un connecteur prévu, ou intercalez une pièce adaptée.

**C'est un câble d'un appareil que vous voulez alimenter autrement.** Vérifiez tension, polarité et puissance avant tout branchement. Une inversion de polarité en courant continu détruit instantanément — voir [[TEC-ENE-001]] et [[TEC-ENE-002]].

**C'est sur un véhicule.** Les câbles y sont abondants, souples et de sections variées : c'est le meilleur gisement de matière première — voir [[SURV-REC-003]].
