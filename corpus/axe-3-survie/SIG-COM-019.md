---
id: SIG-COM-019
titre: Construire un récepteur radio
axe: 3
categorie: Signaux et Communications
temps: Long
contexte: 1
risque: Discret
materiel: Récupération
priorite: normale
origine: officielle
tags: [radio, electricite, communication, recuperation]
sources: ["ARRL — The Radio Amateur's Handbook, récepteurs à détection", "Terman F. E., Radio Engineers' Handbook", "US Army Signal Corps — field expedient receivers, documentation historique"]
---

::Un récepteur qui ne demande aucune source d'énergie est possible. Il tire toute sa puissance de l'onde elle-même.::

## COMPRENDRE

Ce que c'est et comment ça marche : [[TEC-RAD-001]].

**Ce qu'une onde transporte**

Un émetteur fait osciller un courant dans une antenne, ce qui rayonne une onde. Cette onde fait osciller un courant, infiniment plus faible, dans toute autre antenne qu'elle rencontre.

Le problème n'est donc jamais de capter : **toutes les stations arrivent en même temps sur votre fil**. Le problème est d'en isoler une et d'en extraire le son.

Une onde seule ne porte rien. On lui fait porter un signal en faisant varier son amplitude au rythme du son : c'est la **modulation d'amplitude**, celle des ondes moyennes et des grandes ondes. C'est la seule que l'on puisse démoduler sans électronique active, et c'est ce qui rend ce montage possible.

Un récepteur à détection comporte quatre parties, pas une de plus : une **antenne** qui capte, un **circuit accordé** qui sélectionne, un **détecteur** qui extrait le son, un **écouteur** qui le restitue.

## AGIR

**Le circuit accordé**

Une bobine associée à un condensateur résonne à une fréquence précise, comme un diapason sur une note. À cette fréquence la réponse est maximale, ailleurs elle s'effondre. C'est ce qui sépare les stations.

Plus la bobine ou le condensateur sont grands, plus la fréquence reçue est basse.

**La bobine** s'obtient en enroulant du fil de cuivre isolé, jointif et régulier, sur un cylindre isolant : tube de carton, bouteille, manche de bois. De l'ordre de cent tours sur un diamètre de cinq à sept centimètres couvre les ondes moyennes. Le fil émaillé se récupère dans tout transformateur, moteur, relais ou haut-parleur.

**L'accord** se règle de deux façons. Un condensateur variable pris sur un vieux poste est l'idéal. À défaut, on gratte l'émail sur une bande le long de la bobine et l'on fait glisser un contact le long des spires : on change le nombre de tours actifs, donc la fréquence. C'est plus grossier et cela fonctionne.

**Un condensateur se fabrique** : deux surfaces conductrices séparées par un isolant. Deux feuilles d'aluminium enroulées avec du papier entre elles ; ou deux tubes recouverts d'aluminium et emboîtés coulissants, ce qui donne une valeur variable.

**Le détecteur, la pièce décisive**

Un signal modulé en amplitude oscille symétriquement autour de zéro : sa moyenne est nulle, et un écouteur n'en tirerait rien. Il faut ne garder qu'une moitié de l'oscillation, ce qui fait apparaître l'enveloppe, c'est-à-dire le son. Il faut donc un composant qui laisse passer le courant dans un seul sens.

**Une diode au germanium** est le meilleur choix : elle conduit dès une très faible tension, ce qui compte quand le signal est minuscule. Elle se récupère sur d'anciens appareils. Une diode au silicium fonctionne mais exige un signal plus fort, donc une meilleure antenne.

**Sans diode, un contact ponctuel suffit.** C'est le principe historique du poste à galène : une pointe métallique posée sur un cristal semi-conducteur conduit mieux dans un sens que dans l'autre. Les montages de campagne utilisaient une lame d'acier bleui, oxydée, et une mine de crayon taillée en pointe appuyée dessus par un ressort souple. On déplace la pointe jusqu'à trouver le point sensible, et il faut le rechercher après chaque choc.

Le contact doit rester **léger et exploratoire**. Trop appuyé, il conduit dans les deux sens et le son disparaît.

**L'écouteur**

C'est le point qui fait échouer la plupart des tentatives. La puissance disponible est infime : un haut-parleur ordinaire, de basse impédance, ne produira rien.

Il faut un **écouteur à haute impédance**, écouteur piézoélectrique, ou écouteur magnétique ancien. Ils se récupèrent sur d'anciens téléphones, appareils auditifs, appareils de mesure. À défaut, un écouteur ordinaire branché à travers un petit transformateur d'adaptation, bobine de relais, transformateur de récupération, améliore beaucoup les choses.

**L'antenne et la terre**

C'est ici que la réception se gagne ou se perd, bien plus que dans le reste du montage.

**L'antenne** doit être longue et haute : un fil isolé de dix à trente mètres, tendu le plus haut possible, à l'écart des murs et des masses métalliques. La longueur compte, la hauteur davantage.

**La terre est indispensable et systématiquement négligée.** Le circuit doit se refermer. Un piquet métallique enfoncé dans un sol humide, une canalisation d'eau métallique, un radiateur relié à la terre. Sans terre correcte, un récepteur à détection ne fonctionne pratiquement pas.

Une règle sans exception : **on n'installe jamais une antenne au-dessus, en travers ou près d'une ligne électrique**, et on ne la laisse pas en place par temps d'orage. Un long fil élevé capte aussi les décharges atmosphériques.

**Le montage et le réglage**

L'antenne arrive à une extrémité de la bobine, l'autre extrémité va à la terre. Le condensateur d'accord se place aux bornes de la bobine. Le détecteur prélève le signal sur la bobine et l'envoie à l'écouteur, dont l'autre borne rejoint la terre. Un petit condensateur en parallèle sur l'écouteur lisse le résultat et améliore nettement le son.

Le réglage se fait dans cet ordre : établir une bonne terre, tendre la plus longue antenne possible, chercher le point sensible du détecteur, puis seulement balayer l'accord lentement.

**Ce que ce récepteur peut et ne peut pas**

Il reçoit les émissions en modulation d'amplitude, ondes moyennes et grandes ondes. Elles portent très loin, particulièrement la nuit, et couvrent d'immenses territoires depuis peu d'émetteurs. C'est le type de diffusion retenu pour l'information de sécurité, et c'est ce qui rend ce montage utile plutôt que pittoresque, voir [[URG-EFF-001]].

Il ne reçoit pas la modulation de fréquence ni les émissions numériques : leur démodulation demande une électronique active, donc une alimentation.

Il ne transmet rien. Recevoir est passif, silencieux et discret ; émettre demande de l'énergie, une antenne accordée, et occupe des fréquences dont d'autres ont besoin. Dans une situation dégradée, le rôle premier d'un poste est d'écouter, voir [[SIG-COM-001]].

## ADAPTER

**Améliorer un poste existant**

Si vous avez un récepteur à piles, trois gestes valent mieux qu'un montage complet. Rallonger l'antenne, en reliant un long fil à l'antenne télescopique ou en l'enroulant autour. Relier le poste à une bonne terre. Et l'éloigner des structures métalliques et des appareils électroniques, qui produisent un bruit électrique important.

Un poste consomme très peu et s'alimente depuis n'importe quelle source continue à la bonne tension : le calcul est dans [[TEC-ENE-001]], les branchements dans [[TEC-ENE-002]].
