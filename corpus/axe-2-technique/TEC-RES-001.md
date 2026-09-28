---
id: TEC-RES-001
titre: Les réseaux, de la source à la prise
axe: 2
categorie: Énergie et Électricité
temps: Long
contexte: 1
risque: Discret
materiel: Rien
priorite: normale
origine: officielle
tags: [reseau, electricite, eau, telecom, gaz, egout, infrastructure]
sources: ["RTE, Bilans électriques et documentation sur l'équilibre offre-demande", "Enedis, Architecture de la distribution publique HTA et BT", "ARCEP, Rapports sur la résilience des réseaux de communication", "Agences de l'eau, Schémas d'alimentation et de distribution"]
---

::Tout ce qui sort d'un robinet, d'une prise ou d'une antenne a voyagé le long d'une chaîne que personne ne regarde. Elle a une forme, des goulots, et des endroits précis où elle casse.::

Cette fiche décrit les mécanismes. Ce qu'on fait quand ça s'arrête est dans [[URG-EFF-001]] et [[URG-EFF-002]].

## L'électricité

### Le fait qui gouverne tout : elle ne se stocke pas

À chaque instant, la production doit égaler la consommation. Il n'y a pas de réservoir dans le système. Cet équilibre se lit dans **la fréquence** du courant alternatif : cinquante hertz en Europe.

**Si la consommation dépasse la production, les alternateurs ralentissent et la fréquence descend.** À 49,8 Hz les mécanismes de secours s'enclenchent ; vers 49 Hz on coupe automatiquement des portions de réseau pour sauver le reste. C'est un indicateur public, mesurable, et c'est **le véritable tableau de bord du réseau** — bien plus parlant que n'importe quelle annonce.

### La chaîne

**Production** — centrale, barrage, parc éolien ou solaire.

**Transport** — lignes à très haute tension, de 225 000 à 400 000 volts. On monte la tension parce que les pertes dépendent du carré du courant : à puissance égale, plus de tension, c'est moins de courant, donc beaucoup moins de pertes. Voir [[MEM-ACC-005]].

**Postes sources** — on redescend en HTA, autour de 20 000 volts.

**Postes de distribution** — ces petits locaux en béton ou ces armoires au coin des rues, tous les quelques centaines de mètres. Ils redescendent à 400 volts entre phases, 230 entre phase et neutre. **C'est le dernier maillon partagé : un poste dessert un quartier.**

**Le branchement** — du poste à votre compteur, puis au tableau.

### Ce qu'il faut en retenir

**Le délestage n'est pas aléatoire.** On coupe des départs entiers depuis les postes sources, par rotation. Un hôpital ou un central téléphonique se trouve souvent sur un départ qu'on ne coupe pas — et les habitations branchées sur le même départ sont épargnées par accident. C'est une géographie qui se connaît.

**Le réseau se remonte par le haut.** Au retour, on réalimente le transport, puis les postes, puis les quartiers. C'est pourquoi le courant revient par zones et pas partout en même temps.

**Une centrale a besoin de courant pour démarrer.** Le redémarrage complet d'un réseau effondré — le démarrage en autonomie — est une manœuvre longue et délicate, qui se compte en heures ou en jours, pas en minutes.

## L'eau

### La pression vient de la hauteur, pas d'une pompe

C'est le point que presque personne ne sait, et il a des conséquences directes.

Un château d'eau ou un réservoir de colline est rempli par pompage, puis **il distribue par gravité**. Chaque dix mètres de dénivelé donne environ un bar de pression.

D'où trois conséquences :

- **Après une coupure d'électricité, il reste de l'eau** — le contenu du réservoir, soit quelques heures à un jour de consommation. **C'est exactement la fenêtre dont parle [[URG-EFF-001]] quand il dit de remplir tout de suite.**
- **Les étages hauts perdent la pression en premier**, parce qu'ils sont les plus proches du niveau du réservoir.
- **Le réseau garde une pression résiduelle** dans les canalisations basses même après. Un robinet au point le plus bas d'un immeuble coule encore quand ceux du haut sont secs.

### La chaîne

Captage — nappe, source ou rivière —, traitement, pompage vers le réservoir, distribution gravitaire, branchements. Les **postes de relevage** intermédiaires, dans les zones plates, sont les points faibles : ils sont électriques.

L'assainissement fonctionne à l'inverse et par gravité aussi : tout descend vers la station, avec des postes de relevage pour remonter quand le terrain ne suit pas. **Une coupure longue fait déborder les relevages avant de faire quoi que ce soit d'autre** — voir [[TEC-CON-006]].

## Les télécommunications

**Le cœur du réseau tient quelques heures.** Les centraux et les nœuds ont des batteries, puis des groupes électrogènes avec une réserve de carburant, dimensionnée en heures ou en jours selon l'importance du site.

**Les antennes mobiles tiennent beaucoup moins.** Une antenne ordinaire a une batterie de secours de l'ordre de la demi-heure à quelques heures. C'est la raison pour laquelle le téléphone mobile tombe bien avant le reste lors d'une coupure étendue.

**Le réseau fixe cuivre historique était alimenté depuis le central**, donc un téléphone filaire simple fonctionnait sans électricité chez vous. Ce n'est plus vrai avec la fibre et les box, qui dépendent de votre propre prise.

**Ce qui résiste le mieux est ce qui ne dépend de personne** : la radio en réception, puis la radio en émission. Voir [[SIG-COM-002]] et [[TEC-RAD-001]].

## Le gaz

Le réseau est sous pression et **ne dépend pas de l'électricité pour distribuer** — c'est le seul dans ce cas. Il continue souvent de fonctionner quand tout le reste s'arrête.

Deux choses à savoir. **Le gaz naturel est inodore** : l'odeur caractéristique est un composé soufré ajouté exprès pour qu'une fuite se sente. Et la pression descend par paliers, de la conduite de transport aux détenteurs de quartier puis au branchement.

## Ce que cette architecture apprend

**Tout converge vers des points peu nombreux.** Un poste de distribution pour un quartier, un réservoir pour une commune, une antenne pour un secteur. La redondance existe en amont, presque jamais en aval. **Le dernier kilomètre est le maillon fragile de tous les réseaux à la fois.**

**Les dépendances sont croisées.** L'eau dépend de l'électricité pour pomper. Les télécoms dépendent de l'électricité pour tenir. L'électricité dépend des télécoms pour se piloter et du carburant pour ses secours. Aucun de ces réseaux n'est autonome, et c'est ce qui rend les pannes longues plus larges qu'on ne l'imagine — le mécanisme est celui de [[MEM-EFF-001]] et de [[MEM-ANT-002]].

**Et la conséquence pratique :** connaître la chaîne permet de savoir combien de temps il reste à chaque étage, et donc quoi faire en premier. C'est tout l'objet de [[URG-EFF-001]].
