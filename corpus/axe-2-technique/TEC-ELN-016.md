---
id: TEC-ELN-016
titre: Comment marche un ordinateur
axe: 2
categorie: Électronique et Numérique
temps: Court
contexte: 1
risque: Discret
materiel: Rien
priorite: normale
origine: officielle
tags: [ordinateur, processeur, memoire, stockage, binaire, systeme d'exploitation, linux, ssd, apollo]
sources: ["Petzold C., Code: The Hidden Language of Computer Hardware and Software, 2e édition, 2022", "NASA, Apollo Guidance Computer, caractéristiques techniques"]
---

::L'ordinateur qui a posé Apollo 11 sur la Lune avait environ 4 kilo-octets de mémoire vive. Un téléphone d'aujourd'hui en a des millions de fois plus. Pourtant, tous les deux font la même chose : suivre une liste d'instructions très simples, très vite, avec des interrupteurs qui ne connaissent que deux positions.::

## Tout est 0 et 1

Un ordinateur est fait de milliards de **transistors**, des interrupteurs qui laissent passer le courant (1) ou non (0). Un **bit** vaut 0 ou 1 ; huit bits font un **octet**, de quoi écrire une lettre. Une photo pèse quelques millions d'octets (Mo), un film quelques milliards (Go). Voir [[TEC-ELN-013]].

## Les organes

- **Le processeur** : il exécute les instructions, des milliards par seconde.
- **La mémoire vive** : le plan de travail, rapide, **vidé à l'extinction**.
- **Le stockage** (disque dur ou SSD) : l'armoire, qui garde tout quand c'est éteint.
- **La carte mère** relie tout ; **l'alimentation** fournit le courant.
- **Le système d'exploitation** (Windows, macOS, Linux) fait le lien entre l'appareil, les programmes et vous.

## Les pannes courantes

- **Il est devenu lent** : trop de programmes au démarrage, disque plein, ou vieux disque dur. **Remplacer le disque dur par un SSD** rend une seconde jeunesse à la plupart des vieux ordinateurs.
- **Il chauffe et souffle fort** : poussière dans le ventilateur. Débrancher, ouvrir, souffler.
- **Il ne démarre plus** : chargeur, batterie, barrettes de mémoire mal enfoncées. Voir [[TEC-ELN-006]].

## Un vieil ordinateur a encore de la valeur

- **Linux**, gratuit, avec une version légère, rend utilisable un ordinateur trop lent sous Windows.
- Il peut servir de **bibliothèque hors ligne** pour tout un groupe. Voir [[TEC-ELN-011]] et [[TEC-ELN-012]].
- **La consommation** : un portable consomme 15 à 60 W, une petite carte comme le Raspberry Pi moins de 10 W. Sur un panneau solaire, ça change tout.

## Protéger ce qu'il contient

Sauvegarder : [[TEC-ELN-007]]. Les mots de passe : [[TEC-ELN-008]].
