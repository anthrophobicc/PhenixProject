---
id: TEC-ENE-003
titre: Câbler et protéger une installation
axe: 2
categorie: Énergie et Électricité
temps: Long
contexte: 1
risque: Discret
materiel: Technique
priorite: normale
origine: officielle
tags: [electricite, cable, protection, donnees]
sources: ["IEC 60364 — Installations électriques basse tension", "NF C 15-100 — Installations électriques basse tension, France", "INRS — prévention du risque électrique"]
---

::Un câble ne protège rien. C'est ce qu'on met devant lui qui décide si une surcharge coupe le courant ou met le feu.::

## Pourquoi la section compte

Un conducteur possède une résistance, faible mais réelle. Le courant qui le traverse y dissipe de la chaleur, et cette chaleur croît **avec le carré du courant**. Doubler le courant quadruple l'échauffement, comme le rappelle [[TEC-ENE-002]].

Un câble trop fin pour ce qu'il transporte chauffe donc en permanence. L'isolant vieillit, durcit, se fissure, puis fond. C'est un processus lent : l'installation fonctionne des mois avant de céder, ce qui rend le défaut invisible jusqu'au bout.

Trois facteurs déterminent la section nécessaire : le courant à transporter, la longueur du câble, et les conditions de pose. Un câble enfermé dans une gaine ou groupé avec d'autres évacue moins bien sa chaleur et doit être surdimensionné.

**La longueur intervient par un autre effet : la chute de tension.** Sur un long câble, une partie de la tension est perdue en route. En courant continu basse tension, ce phénomène devient rapidement critique : un appareil placé au bout d'un long câble sous-dimensionné ne reçoit plus assez de tension pour fonctionner, alors que tout semble correct.

## Le rôle des protections

**Le fusible et le disjoncteur protègent le câble, pas l'appareil.** C'est le point que presque tout le monde inverse.

Leur fonction est de couper avant que le câble n'atteigne une température dangereuse. On les dimensionne donc en fonction de la section du câble qu'ils protègent, jamais en fonction de la consommation de ce qui est branché au bout.

Il en découle une règle absolue : **on ne remplace jamais une protection par une plus forte.** Un fusible qui fond répète une information — quelque chose consomme trop, ou il y a un défaut. Le remplacer par un calibre supérieur ne résout rien : cela supprime seulement l'avertissement, et transfère la limite au câble, qui n'a aucun moyen de prévenir.

Deux types de protection existent, et ils ne font pas le même travail.

**La protection contre les surintensités** — fusible, disjoncteur — coupe quand le courant dépasse un seuil, que ce soit par surcharge progressive ou par court-circuit.

**La protection différentielle** compare ce qui part et ce qui revient. Si une fraction du courant s'échappe ailleurs — par une personne, par une carcasse mouillée — l'écart est détecté et le circuit est coupé en quelques millisecondes. **C'est le dispositif qui protège les personnes**, et il ne remplace pas le premier ni l'inverse.

## La terre

Sa fonction est mal comprise. Elle ne sert pas à évacuer l'électricité en général : elle sert à **donner au courant de défaut un chemin de retour de très faible résistance**, autre que le corps humain.

Si la carcasse métallique d'un appareil devient accidentellement sous tension, une terre correcte permet à un courant important de circuler, ce qui déclenche immédiatement la protection. Sans terre, la carcasse reste sous tension en attendant que quelqu'un la touche.

Une terre inefficace — piquet trop court, sol sec, connexion corrodée — donne une fausse sécurité. Elle se contrôle, elle ne se suppose pas.

## Les connexions

C'est là que la plupart des défauts naissent.

**Un mauvais contact est une résistance élevée traversée par tout le courant.** Une borne desserrée, une cosse oxydée, un fil mal serré concentrent une puissance importante sur quelques millimètres. Une connexion tiède est un avertissement ; une connexion chaude est une urgence.

Trois règles limitent le problème. **Serrer franchement**, et resserrer après quelques semaines, car le cuivre flue sous pression. **Ne jamais mélanger cuivre et aluminium** en contact direct : le couple galvanique corrode la jonction et augmente la résistance, mécanisme décrit dans [[TEC-COR-001]]. **Ne jamais étamer un fil destiné à être serré** dans une borne à vis : la soudure flue et le contact se desserre seul.

## L'ordre d'intervention

1. **Couper** au disjoncteur général, pas seulement à l'interrupteur local.
2. **Vérifier l'absence de tension** sur place, avec un appareil, et non par déduction. Un circuit peut être alimenté par deux sources.
3. **Condamner** ce qui a été coupé, pour que personne ne le rétablisse.
4. **Travailler**, en respectant les sections et les protections existantes.
5. **Vérifier avant de remettre sous tension** : absence de brins qui dépassent, serrage, isolation, continuité de la terre.

Le contrôle se fait au multimètre : voir [[TEC-ENE-008]].

## En installation autonome

Les mêmes règles s'appliquent, avec deux différences aggravantes.

**Les courants sont plus élevés.** À puissance égale, une installation basse tension fait circuler des courants bien supérieurs à ceux d'un réseau domestique. Les sections nécessaires sont donc nettement plus fortes, et c'est l'erreur la plus fréquente.

**Les batteries délivrent un courant de court-circuit énorme.** Une batterie court-circuitée fait rougir une clé en quelques secondes. **Toute batterie doit être protégée par un fusible placé au plus près de sa borne**, avant tout le reste du câblage. C'est la protection la plus importante d'une installation autonome, et la plus souvent omise — voir [[TEC-ENE-004]] et [[TEC-SOLR-001]].
