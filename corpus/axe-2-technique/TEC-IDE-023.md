---
id: TEC-IDE-023
titre: Le calendrier et le jour de la semaine
axe: 2
categorie: Information et Données
temps: Court
contexte: 1
risque: Discret
materiel: Rien
priorite: normale
origine: officielle
tags: [calendrier, jour de la semaine, annees bissextiles, calendrier gregorien, calcul de tete, conway, compter les jours]
sources: ["Conway J.H., Tomorrow is the day after doomsday, Eureka, 1973", "Grégoire XIII, bulle Inter gravissimas, 1582", "IMCCE, Observatoire de Paris, calendriers et éphémérides"]
---

::En France, le 9 décembre 1582 a été suivi directement du 20 décembre : il fallait rattraper dix jours de retard accumulés par l'ancien calendrier. Sans téléphone, perdre la date arrive vite, dans une cave, un camp, une longue maladie. Un mathématicien anglais a trouvé une astuce pour retrouver de tête le jour de la semaine de n'importe quelle date.::

## Les années bissextiles

Une année a 366 jours si elle est **divisible par 4**, sauf les années de siècle qui ne sont pas divisibles par 400. 2000 était bissextile, 1900 ne l'était pas, 2100 ne le sera pas.

## L'astuce des jours pivots

Chaque année, certaines dates tombent **toutes le même jour de la semaine** :

- **4 avril, 6 juin, 8 août, 10 octobre, 12 décembre** (4/4, 6/6, 8/8, 10/10, 12/12) ;
- **9 mai et 5 septembre**, **11 juillet et 7 novembre** ;
- **le dernier jour de février** ;
- **le 14 mars** (« 3/14 ») et le **4 juillet**.

**En 2026, ce jour pivot est un samedi.** Donc le 5 septembre 2026 est un samedi, et le 28 septembre, 23 jours plus tard (trois semaines et deux jours), est un lundi.

**Pour une date** : on part du jour pivot le plus proche dans le même mois, et on compte les semaines et les jours d'écart.

**D'une année à la suivante**, le jour pivot avance d'un jour, de deux après une année bissextile : 2027 sera un dimanche, 2028 (bissextile) un mardi.

## Garder la date

- **Un calendrier papier**, et une croix chaque soir.
- **Des encoches** sur un bâton, une par jour, une plus longue le dimanche, comme Robinson Crusoé sur son poteau.
- **La Lune** pour vérifier grossièrement les semaines. Voir [[TEC-TER-012]].
- **Les dates qui comptent** : traitements, règles, grossesse, rations, semis. Voir [[SURV-SOC-009]].

Calculer de tête : [[TEC-IDE-013]]. L'heure sans montre : [[SURV-ORI-005]].
