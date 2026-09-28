---
id: SURV-REC-019
titre: Un moteur qui ne démarre pas
axe: 3
categorie: Récupération
temps: Court
contexte: 1
risque: Discret
materiel: Technique
priorite: normale
origine: officielle
tags: [moteur, mecanique, panne, vehicule, reparation]
sources: ["Robert Bosch GmbH, Automotive Handbook", "US Army TM 9-8000, Principles of Automotive Vehicles"]
---

::Un moteur à essence ne démarre que s'il réunit quatre choses : du carburant, de l'air, une étincelle et de la compression. Quand il refuse, il en manque une. Cherchez laquelle, dans l'ordre.::

## AGIR

**Écoutez d'abord ce qui se passe quand vous lancez le moteur.** C'est le tri le plus rapide, et il ne demande aucun outil.

1. **Rien, ou un seul clic sec.** Le démarreur ne tourne pas : le problème est électrique. Voyants très faibles ou qui s'éteignent : batterie vide. Voyants normaux mais un clic : cosse desserrée ou oxydée, relais ou démarreur. **Nettoyez et resserrez les deux cosses de la batterie avant toute autre chose**, c'est la panne la plus fréquente — voir [[SURV-REC-007]].
2. **Le moteur tourne, mais de plus en plus lentement.** Batterie faible, souvent à cause du froid. Laissez-la reposer une minute entre deux essais, ou démarrez avec des câbles (voir ADAPTER).
3. **Le moteur tourne à vitesse normale mais ne part pas.** La batterie et le démarreur vont bien. Il manque du carburant, une étincelle ou de l'air : continuez.
4. **Le moteur tourne plus vite et plus facilement que d'habitude, avec un bruit régulier.** Arrêtez tout de suite. C'est le signe classique d'une courroie de distribution cassée : sur beaucoup de moteurs, chaque nouvel essai peut tordre les soupapes.

**Carburant.**

5. **Vérifiez le niveau réel, pas la jauge.** Une jauge peut mentir, surtout après une longue immobilisation.
6. **Écoutez la pompe.** Sur la plupart des moteurs à injection, une pompe électrique bourdonne une ou deux secondes quand on met le contact. Silence complet : fusible, relais ou pompe.
7. **Regardez une bougie.** Après quelques tentatives, dévissez-en une. **Humide et qui sent l'essence** : le carburant arrive, cherchez du côté de l'étincelle, ou le moteur est noyé. **Sèche** : le carburant n'arrive pas.

**Étincelle.**

8. **Testez l'allumage avec un testeur d'étincelle** branché entre le fil et la bougie, s'il y en a un sous la main : il doit clignoter franchement pendant que le moteur tourne. Pas d'éclair : bobine, fil, capteur ou alimentation de l'allumage. Sans testeur, une bougie noire, grasse ou dont les électrodes sont rongées se change avant de chercher plus loin.

**Air.**

9. **Suivez le chemin de l'air**, de l'entrée du filtre jusqu'au pot d'échappement. Un filtre gorgé d'eau, une durite d'admission débranchée ou un pot bouché par de la boue, de la neige ou un chiffon suffisent à empêcher un démarrage.

## COMPRENDRE

Un moteur thermique brûle un mélange d'air et de carburant dans un cylindre fermé, et transforme cette poussée en rotation — le fonctionnement complet est dans [[TEC-MOTH-001]]. Pour que ça démarre, les quatre conditions doivent être réunies **en même temps** : le bon mélange, comprimé, et enflammé au bon moment.

Le démarreur ne fait que lancer ce cycle. Tant qu'il tourne normalement, la batterie et le démarreur sont hors de cause, et le problème se trouve dans l'une des quatre conditions. C'est pour cela que l'ordre compte : on élimine d'abord ce qui est simple et fréquent, et on garde pour la fin ce qui demande de démonter.

**Le diesel est différent.** Il n'a pas de bougies d'allumage : c'est la chaleur de l'air fortement comprimé qui enflamme le gazole. Ses pannes de démarrage viennent donc du froid (préchauffage), d'air entré dans le circuit de carburant, ou d'un gazole figé par le gel qui bouche le filtre.

## ADAPTER

**Le moteur est noyé.** Forte odeur d'essence, bougies mouillées. Attendez dix à quinze minutes que l'excès s'évapore. Sur beaucoup de voitures à injection, relancer le moteur **accélérateur enfoncé à fond** coupe l'injection pendant le démarrage et aide à le dénoyer.

**C'est un diesel.** Attendez que le voyant de préchauffage s'éteigne avant de lancer le moteur, et recommencez deux ou trois fois par temps froid. Après une panne sèche, il faut chasser l'air du circuit : beaucoup de filtres ont une petite pompe d'amorçage manuelle à actionner jusqu'à ce qu'elle devienne dure.

**Il fait très froid.** Une batterie perd une grande partie de sa puissance par grand froid et l'huile épaissit. Ramener la batterie au chaud pour la nuit suffit souvent pour le démarrage du matin.

**C'est un petit moteur** (tondeuse, groupe électrogène, tronçonneuse). Les mêmes quatre conditions s'appliquent. Le coupable le plus courant est une **essence restée plusieurs mois** dans le réservoir : elle perd ses composants les plus volatils et encrasse le carburateur. Vidangez-la et remplacez-la par de l'essence fraîche.

**Vous avez une batterie de secours.** Branchez les câbles dans cet ordre : rouge sur le + de la batterie à plat, rouge sur le + de la batterie saine, noir sur le − de la batterie saine, et enfin noir sur une **partie métallique nue du moteur en panne**, loin de sa batterie. Démarrez le véhicule qui fonctionne, puis l'autre. Débranchez dans l'ordre inverse.

**Vous n'avez rien de tout ça, et une boîte manuelle.** Démarrez en poussant : contact mis, deuxième vitesse engagée, embrayage enfoncé. À la vitesse d'un pas de course, relâchez l'embrayage d'un coup, puis débrayez dès que le moteur prend. Cela ne marche pas avec une boîte automatique.
