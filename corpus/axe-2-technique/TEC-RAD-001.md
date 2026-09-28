---
id: TEC-RAD-001
titre: Le poste à galène
axe: 2
categorie: Énergie et Électricité
temps: Court
contexte: 1
risque: Discret
materiel: Rien
priorite: normale
origine: officielle
tags: [poste a galene, recepteur a detection, radio, modulation d'amplitude, circuit accorde, diode, germanium, antenne, terre, foxhole radio]
sources: ["ARRL, The Radio Amateur's Handbook, récepteurs à détection", "Terman F.E., Radio Engineers' Handbook, 1943", "Wikipédia, article « Poste à galène »"]
---

::Le poste à galène est un récepteur radio qui fonctionne sans pile ni prise : toute l'énergie du son vient de l'onde captée par l'antenne. C'est le poste des débuts de la radio, dans les années 1920. Pendant la Seconde Guerre mondiale, des soldats en ont improvisé dans leurs tranchées avec une lame de rasoir et une mine de crayon.::

## Ce qu'une onde transporte

- **Un émetteur fait osciller un courant dans son antenne**, qui rayonne une onde. Cette onde fait naître un courant infiniment plus faible dans toute antenne qu'elle rencontre : toutes les stations arrivent en même temps sur le même fil.
- **En modulation d'amplitude** (grandes ondes, ondes moyennes), le son fait varier la force de l'onde. C'est la seule modulation qu'on peut démoduler sans électronique alimentée.

## Les quatre parties

- **L'antenne** : un long fil, de dix à trente mètres, tendu le plus haut possible, avec une prise de terre (un piquet dans un sol humide, une canalisation métallique). Sans terre, un tel poste ne fonctionne pratiquement pas.
- **Le circuit accordé** : une bobine de fil et un condensateur qui résonnent à une fréquence précise, comme un diapason sur une note. En faisant varier l'un ou l'autre, on choisit la station. Une centaine de tours de fil sur un tube de cinq à sept centimètres couvrent les ondes moyennes.
- **Le détecteur** : un composant qui ne laisse passer le courant que dans un sens. Il ne garde qu'une moitié de l'oscillation, ce qui fait apparaître l'enveloppe du signal, c'est-à-dire le son. À l'origine, un cristal de galène (sulfure de plomb) touché par une pointe métallique fine, le « chat moustache » ; aujourd'hui, une diode au germanium, qui conduit dès une très faible tension.
- **L'écouteur** : il doit être à haute impédance (piézoélectrique, ou magnétique ancien), car la puissance disponible est infime. Un haut-parleur ordinaire ne produit aucun son.

## Les postes de tranchée

Les « foxhole radios » de la Seconde Guerre mondiale remplaçaient le cristal par une lame de rasoir bleuie, oxydée, et une mine de crayon appuyée dessus : le contact entre l'oxyde et le graphite laisse passer le courant mieux dans un sens que dans l'autre. Le point sensible se cherchait en déplaçant la mine, et se perdait au moindre choc.

## Ce qu'il reçoit

- **Les émissions en modulation d'amplitude**, qui portent très loin, surtout la nuit. Plusieurs pays gardent des émetteurs puissants en grandes ondes ou ondes moyennes pour l'information en cas de crise. Voir [[URG-EFF-001]].
- **Pas la FM ni la radio numérique**, dont la démodulation demande une électronique alimentée.
- **Il n'émet rien** : recevoir est passif et silencieux. Voir [[SIG-COM-002]].

## Les dangers

Un long fil tendu en hauteur capte aussi les décharges atmosphériques : les antennes de ce type ne restent pas en place par temps d'orage, et ne passent jamais près d'une ligne électrique.

Les composants électroniques : [[TEC-ELN-013]].
