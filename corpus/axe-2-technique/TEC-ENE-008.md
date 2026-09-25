---
id: TEC-ENE-008
titre: Mesurer avec un multimètre
axe: 2
categorie: Énergie et Électricité
temps: Court
contexte: 1
risque: Discret
materiel: Technique
priorite: normale
origine: officielle
tags: [mesure, electricite, diagnostic, donnees]
sources: ["IEC 61010 — Safety requirements for electrical measuring equipment", "Fluke Corporation — technical documentation on measurement categories", "INRS — mesurage en électricité"]
---

::Un multimètre ne répare rien. Il remplace les hypothèses par des faits, ce qui est presque toujours l'étape manquante.::

## Les trois mesures qui suffisent

**La tension.** On mesure entre deux points, l'appareil branché **en parallèle**, circuit sous tension. C'est la mesure la plus courante et la plus sûre. Elle répond à : y a-t-il quelque chose ici, et combien.

**La continuité et la résistance.** L'appareil envoie lui-même un petit courant et mesure ce qui revient. Elle se fait **impérativement hors tension**, et sur un élément isolé du reste du circuit — sinon on mesure tout le montage en même temps et le résultat n'a aucun sens. Elle répond à : le courant peut-il passer par là.

**Le courant.** L'appareil se branche **en série**, donc il faut ouvrir le circuit et l'insérer dedans. C'est la mesure la plus délicate et celle qui détruit le plus de multimètres : brancher en parallèle alors qu'on est en position ampèremètre crée un court-circuit franc. Elle répond à : combien consomme réellement cet appareil.

## Ce que chaque mesure révèle

**Une tension présente mais qui s'effondre dès qu'on branche une charge** signale une source faible ou une résistance en série quelque part — batterie fatiguée, mauvais contact, câble sous-dimensionné.

**Une continuité absente là où elle devrait être** : fil coupé, fusible fondu, interrupteur défaillant, connexion oxydée. C'est le test qui trouve la panne la plus fréquente.

**Une continuité présente là où elle ne devrait pas être** : court-circuit, isolant percé, humidité, brin qui touche la carcasse.

**Une résistance qui augmente en chauffant** signale une connexion en train de mourir.

## La méthode de recherche de panne

Elle vaut plus que la connaissance des appareils : elle s'applique à n'importe quel circuit inconnu.

1. **Vérifiez qu'il y a une source.** Mesurez la tension à la source elle-même, avant tout le reste. Une grande partie des pannes s'arrête là.
2. **Suivez le chemin.** Mesurez la tension de proche en proche, en avançant vers la charge. **Le point où elle disparaît est le point du défaut.** C'est la méthode la plus rapide et elle ne demande aucune connaissance du montage.
3. **Vérifiez le retour.** Un circuit ne fonctionne que s'il est fermé : un défaut sur le conducteur de retour donne exactement les mêmes symptômes qu'un défaut sur l'aller.
4. **Isolez avant de conclure.** Débranchez l'élément suspect et mesurez-le seul.

Un principe résume tout : **une panne est presque toujours une interruption ou un contact, jamais un composant mystérieux.** Fils, connexions, fusibles et interrupteurs représentent la grande majorité des défauts.

## Utiliser l'appareil sans le détruire

**Vérifiez la position du sélecteur avant chaque mesure**, et l'emplacement des pointes de touche. La borne des courants forts est séparée : y laisser une pointe pour mesurer une tension provoque un court-circuit.

**Commencez sur le calibre le plus élevé** si l'appareil n'est pas automatique, puis descendez.

**Vérifiez l'appareil sur une source connue** avant de conclure qu'un circuit est hors tension. Une pile usée dans le multimètre, un fusible interne fondu ou un cordon coupé donnent une lecture de zéro parfaitement rassurante et parfaitement fausse. **Tester le testeur est la seule habitude qui protège vraiment.**

**Respectez la catégorie de mesure** indiquée sur l'appareil et les cordons. Elle indique le niveau de surtension qu'il peut encaisser sans danger. Un appareil bon marché utilisé sur une installation qu'il n'est pas prévu pour peut se rompre violemment.

## Ce qu'un multimètre ne dit pas

Il ne dit pas si une batterie a de la capacité : une batterie morte affiche souvent une tension correcte à vide et s'effondre en charge. Il faut mesurer sous charge — voir [[TEC-ENE-004]].

Il ne dit pas si un câble est correctement dimensionné : il ne détecte pas un échauffement futur, seulement une chute de tension actuelle. Voir [[TEC-ENE-003]].

Il ne remplace pas un vérificateur d'absence de tension pour la sécurité. C'est un instrument de diagnostic, pas un dispositif de protection.
