---
id: TEC-ELN-006
titre: Un appareil qui ne s'allume plus
axe: 2
categorie: Électronique et Numérique
temps: Court
contexte: 1
risque: Discret
materiel: Technique
priorite: normale
origine: officielle
tags: [panne, depannage, appareil, alimentation, fusible, condensateur, telephone mouille, reparation]
sources: ["iFixit, guides de réparation et méthode de diagnostic", "Repair Café (fondation), fiches de diagnostic des petits appareils", "INRS, risques électriques liés aux condensateurs des appareils secteur"]
---

::La moitié des appareils « morts » apportés dans les ateliers de réparation ont une panne bête : une prise, un câble, un fusible, une pile qui a coulé. On commence toujours par le plus simple, et on finit rarement par le plus compliqué.::

## Dans l'ordre

1. **L'alimentation** : la prise marche-t-elle (testez-la avec une lampe) ? Le câble est-il abîmé, le chargeur chaud et silencieux ou froid et mort ? Essayez un autre chargeur, un autre câble.
2. **Les piles ou la batterie** : vides, mal posées, oxydées ? **Une coulure blanche** sur les contacts se nettoie au vinaigre ou au jus de citron, puis on frotte à la gomme. Voir [[TEC-ENE-012]].
3. **La réinitialisation** : batterie retirée si possible, bouton marche appuyé 30 secondes, puis on remet tout. Beaucoup d'appareils bloqués repartent.
4. **Le fusible** : dans la fiche, dans l'appareil, sur la carte. Un fusible grillé se voit (fil coupé, verre noirci) ou se teste au multimètre. Remplacez-le **par le même calibre**. S'il regrille aussitôt, il y a un court-circuit derrière. Voir [[TEC-ENE-011]].
5. **Les yeux et le nez** : ouvrez (appareil débranché), regardez. **Un condensateur gonflé** (dessus bombé, fendu, ou qui a fui) est la panne la plus courante des alimentations et des écrans. Une odeur de brûlé, un composant noirci, une piste coupée.
6. **Les connecteurs** : une nappe mal enfoncée, une prise de charge desserrée ou encrassée (une aiguille en bois pour retirer la poussière tassée).

## L'appareil a pris l'eau

- **Éteignez-le tout de suite**, ne le rallumez pas pour « voir s'il marche ».
- **Retirez la batterie** si possible, la carte SIM, les cartes.
- **Séchez à l'air**, dans un endroit sec et tiède, ouvert si possible, **48 heures au moins**.
- **Le riz ne sert à rien** : il n'absorbe pas mieux que l'air, et ses poussières entrent dans les prises.
- **L'eau de mer ou sucrée** corrode vite : un nettoyage des cartes à l'alcool isopropylique, au pinceau, sauve souvent l'appareil.

## Le danger

**Les appareils branchés sur le secteur** (alimentations, micro-ondes, vieux téléviseurs, écrans) contiennent des **condensateurs qui gardent une charge mortelle** longtemps après avoir été débranchés. Le micro-ondes en particulier : on ne l'ouvre pas sans savoir décharger son condensateur haute tension. Les petits appareils à piles, les téléphones et les ordinateurs portables sont sans danger électrique.

## Les astuces des réparateurs

- **Photographiez chaque étape** du démontage : c'est le mode d'emploi du remontage.
- **Rangez les vis** dans l'ordre, dans une boîte à œufs ou sur un papier où l'on dessine leur emplacement.
- **Un appareil sans panne visible** se répare souvent en remplaçant la pièce la plus sollicitée : batterie, prise de charge, alimentation.
- **Récupérez** ce qui peut servir sur l'appareil irréparable : voir [[SURV-REC-021]].

Souder un composant : [[TEC-ELN-005]].
