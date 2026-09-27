---
id: TEC-ENE-016
titre: Le 12 volts à la maison
axe: 2
categorie: Énergie et Électricité
temps: Long
contexte: 1
risque: Discret
materiel: Technique
priorite: normale
origine: officielle
tags: [12 volts, batterie, solaire, fusible, section de cable, convertisseur, eclairage led, autonomie]
sources: ["Norme NF C 15-100, installations en très basse tension", "Victron Energy, Wiring Unlimited (dimensionnement des câbles et fusibles en courant continu)", "Guides d'installation électrique des camping-cars et des bateaux"]
---

::Le 12 volts, c'est l'électricité des voitures, des bateaux et des camping-cars. Sans danger pour le corps, simple, compatible avec les batteries et les panneaux solaires. Mais il a un piège : il met le feu aux fils trop fins.::

## Pourquoi le 12 volts

- **Il ne tue pas** au toucher : on peut câbler sans électricien.
- **Il se stocke directement** dans une batterie, sans conversion.
- **Tout ce qui sert en crise existe en 12 V** : lampes LED, chargeurs USB, radios, ventilateurs, pompes à eau, réfrigérateurs de camping.

## Les éléments

1. **Une batterie** : plomb (AGM, gel) ou lithium fer phosphate (LiFePO4), plus légère et qui supporte d'être vidée presque entièrement. Voir [[TEC-ENE-004]].
2. **De quoi la charger** : panneau solaire avec régulateur, chargeur sur secteur, alternateur de voiture, groupe. Voir [[TEC-SOLR-001]].
3. **Un fusible au plus près de la batterie**, sur le fil positif.
4. **Des câbles de bonne section.**
5. **Un petit tableau** de fusibles pour chaque circuit : éclairage, prises USB, pompe.

## Le piège : les fils

À tension basse, pour la même puissance, **le courant est vingt fois plus fort** qu'en 230 V. Un fil trop fin chauffe et perd de la tension.

| Courant | Longueur (aller et retour compris) | Section conseillée |
|---|---|---|
| 5 A (éclairage) | jusqu'à 10 m | 1,5 à 2,5 mm² |
| 10 A (pompe, frigo) | jusqu'à 10 m | 4 mm² |
| 20 A | jusqu'à 10 m | 6 à 10 mm² |
| Convertisseur 1 000 W | moins de 2 m | 25 mm² et plus |

**Dans le doute, plus gros.** Un fil de lampe de salon sur une batterie de voiture peut prendre feu en quelques secondes en cas de court-circuit.

## Le fusible qui sauve

**Une batterie en court-circuit** peut débiter des centaines d'ampères : les fils rougissent et l'isolant brûle. **Le fusible doit être à moins de 20 cm de la borne positive**, calibré pour protéger le fil. C'est la règle la plus importante de toute installation 12 V.

## Le convertisseur (onduleur)

Il fabrique du 230 V à partir du 12 V, pour les appareils qui n'existent pas en 12 V. Mais il **consomme même à vide**, perd 10 à 15 % de l'énergie, et un appareil de 1 000 W tire près de 100 A sur la batterie. **Tout ce qui peut rester en 12 V ou en USB y reste.**

## Ce qu'on alimente avec quoi

Une batterie de 100 Ah en 12 V stocke environ **1 200 Wh**, dont 600 utilisables en plomb, presque tout en lithium. Cela fait par exemple : cinq lampes LED de 5 W pendant 10 heures, quatre recharges de téléphone, une radio toute la journée, et il en reste. Voir [[TEC-ENE-014]].
