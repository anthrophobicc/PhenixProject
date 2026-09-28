---
id: TEC-ENE-008
titre: Le multimètre
axe: 2
categorie: Énergie et Électricité
temps: Court
contexte: 1
risque: Discret
materiel: Rien
priorite: normale
origine: officielle
tags: [multimetre, tension, courant, resistance, continuite, diagnostic, recherche de panne, categorie de mesure, calibre]
sources: ["IEC 61010, Safety requirements for electrical equipment for measurement, control and laboratory use", "Fluke Corporation, documentation technique sur les catégories de mesure", "INRS, mesurage en électricité"]
---

::Le multimètre mesure la tension, le courant et la résistance d'un circuit électrique. Il ne répare rien : il remplace les hypothèses par des faits, ce qui est presque toujours l'étape qui manque pour trouver une panne.::

## Les trois mesures

- **La tension**, en volts : l'appareil se branche en parallèle entre deux points, circuit sous tension. C'est la mesure la plus courante et la plus sûre. Elle dit s'il y a du courant disponible, et combien.
- **La résistance et la continuité** : l'appareil envoie lui-même un petit courant et mesure ce qui revient. Elle se fait hors tension, sur un élément isolé du reste du circuit, sinon on mesure tout le montage à la fois. Elle dit si le courant peut passer par un fil, un fusible, un interrupteur.
- **Le courant**, en ampères : l'appareil se branche en série, dans le circuit ouvert. C'est la mesure la plus délicate et celle qui détruit le plus de multimètres, car un ampèremètre branché en parallèle crée un court-circuit.

## Ce que révèlent les mesures

- **Une tension qui s'effondre dès qu'on branche une charge** : source faible ou mauvais contact en série (batterie fatiguée, connexion oxydée, câble trop fin).
- **Une continuité absente** là où elle devrait être : fil coupé, fusible fondu, interrupteur défaillant. C'est la panne la plus fréquente.
- **Une continuité présente** là où elle ne devrait pas : court-circuit, isolant percé, humidité.
- **Une résistance qui augmente en chauffant** : une connexion en train de mourir.

## La recherche de panne

La méthode des électriciens vaut pour n'importe quel circuit inconnu : vérifier d'abord la source, puis suivre la tension de proche en proche vers l'appareil. Le point où elle disparaît est l'endroit du défaut. Le fil de retour compte autant que l'aller. Dans la grande majorité des cas, la panne est une interruption ou un mauvais contact : fils, connexions, fusibles, interrupteurs.

## Les pièges de l'appareil

- **Le sélecteur et les bornes** : la borne des forts courants est séparée ; une pointe oubliée dedans pendant une mesure de tension provoque un court-circuit.
- **Le calibre** : sur les appareils non automatiques, on part du plus élevé.
- **Le faux zéro** : une pile usée, un fusible interne fondu ou un cordon coupé affichent zéro, une lecture rassurante et fausse. Les électriciens vérifient leur appareil sur une source connue avant de conclure qu'un circuit est coupé.
- **La catégorie de mesure** (CAT II, III, IV) indique les surtensions qu'il encaisse sans danger. Un appareil bon marché utilisé sur une installation trop puissante peut éclater.

## Ce qu'il ne dit pas

Il ne dit pas si une batterie a encore de la capacité (elle peut afficher une tension correcte à vide et s'effondrer en charge, voir [[TEC-ENE-004]]), ni si un câble chauffera (voir [[TEC-ENE-003]]). Ce n'est pas un vérificateur d'absence de tension, l'instrument de sécurité des électriciens.
