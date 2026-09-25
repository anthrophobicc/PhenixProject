---
id: TEC-IDE-001
titre: L'identification
axe: 2
categorie: Information et Données
temps: Long
contexte: 1
risque: Discret
materiel: Rien
priorite: normale
origine: officielle
tags: [identite, donnees, biometrie, recoupement, empreinte, reseau, tracage]
sources: ["de Montjoye Y.-A. et al., Unique in the Crowd, Scientific Reports, 2013", "Sweeney L., Simple Demographics Often Identify People Uniquely, Carnegie Mellon, 2000", "Narayanan A., Shmatikov V., Robust De-anonymization of Large Sparse Datasets, IEEE S&P, 2008", "Eckersley P., How Unique Is Your Web Browser?, EFF Panopticlick, 2010"]
---

::Une trace ne désigne personne. Deux traces qui se recoupent désignent quelqu'un. C'est tout le sujet, et l'écart entre les deux est beaucoup plus court qu'on ne l'imagine.::

Cette fiche explique le mécanisme. Ce qu'on en fait est dans [[SIG-COM-007]].

## Les cinq familles d'identifiants

**Ce qu'on vous a attribué.** Numéro national, état civil, immatriculation, numéro de compte, adresse de courrier. Stable, unique, universellement reconnu — et c'est ce qui en fait la clé de jointure entre toutes les bases qui vous concernent.

**Ce que vous êtes.** Empreintes, visage, iris, voix, démarche, ADN. Non révocable : une donnée biométrique compromise l'est définitivement, contrairement à un mot de passe.

**Ce que vous portez.** Téléphone, carte de transport, badge, clé de voiture, montre. Chacun émet et chacun se relie à un compte.

**Ce que vous faites.** Horaires, trajets, achats, fréquentations, façon d'écrire. C'est la famille la plus sous-estimée et la plus révélatrice.

**Ce que d'autres disent de vous.** Carnets d'adresses, photos identifiées, témoignages, registres, listes d'appels de vos correspondants. **Vous n'en avez aucun contrôle**, et c'est la porte par laquelle se reconstituent les profils de gens qui n'ont eux-mêmes rien publié.

## Le mécanisme central : la ré-identification

C'est le résultat qui a fondé toute la discipline, et il est contre-intuitif.

Une base « anonymisée », dont on a retiré les noms, ne l'est presque jamais. Il suffit de la croiser avec une autre base qui partage quelques attributs pour retrouver les identités.

Les ordres de grandeur, tirés de travaux devenus classiques :

- **Code postal, date de naissance et sexe suffisent à identifier de manière unique environ 87 % de la population** des États-Unis. Trois champs qu'on donne partout sans y penser.
- **Quatre points de position dans le temps** — quatre fois « vous étiez là, à peu près à cette heure » — ré-identifient plus de 90 % des individus dans une base de déplacements.
- Des jeux de données de notations de films, publiés anonymisés, ont été ré-identifiés en les croisant avec des avis publics signés.

Le principe général : **plus un comportement est riche, plus il est unique.** L'anonymat d'un individu dans une foule vient de la pauvreté de ce qu'on sait de lui, pas d'une propriété de la foule.

## Ce qui identifie sans identifiant

**L'empreinte de navigateur.** La combinaison de la résolution, des polices installées, du fuseau horaire, de la langue, des extensions et de la façon dont la carte graphique dessine un texte suffit à distinguer un navigateur parmi des millions — **sans aucun cookie et sans compte.**

**Les réseaux sans fil connus.** Un appareil qui cherche ses réseaux favoris annonce en clair la liste des endroits où il est allé.

**Le style.** L'analyse stylométrique identifie un auteur à partir de la fréquence des mots courants, de la ponctuation et des fautes récurrentes, sur des textes de quelques milliers de mots. Ce n'est pas du vocabulaire rare : ce sont les mots qu'on ne choisit pas.

**Le rythme.** Heures de connexion, de sommeil, de déplacement. Un emploi du temps est une signature.

## La métadonnée contre le contenu

Le contenu d'un message est une phrase : il faut le lire et le comprendre. La métadonnée — qui, à qui, quand, d'où, combien de temps — est **structurée**, donc triable, croisable et analysable en masse.

C'est pourquoi les systèmes d'analyse s'y intéressent d'abord. Savoir qu'un numéro a appelé un cabinet d'oncologie, puis un proche, puis un employeur, dans cette séquence, est plus informatif que la transcription des trois conversations. **Le chiffrement protège le contenu et laisse la métadonnée entièrement lisible.**

## La rétention : qui garde quoi, et combien de temps

C'est la partie qu'on ignore et qui décide de tout.

- **L'opérateur** conserve les données de connexion — pas le contenu — pendant une durée fixée par la loi, de l'ordre de l'année dans l'Union européenne.
- **La banque** conserve les mouvements pendant des années au titre des obligations comptables et de lutte contre le blanchiment.
- **L'administration** conserve à peu près indéfiniment.
- **Les services en ligne** conservent selon leur politique, c'est-à-dire souvent au-delà de ce qu'ils annoncent, et les sauvegardes survivent aux suppressions.
- **Les courtiers en données** agrègent et revendent des profils constitués de sources publiques, de fuites et d'achats. Vous n'avez jamais eu de relation avec eux.

D'où une asymétrie qui gouverne tout le sujet : **la collecte est instantanée, l'effacement est lent, partiel et révocable.** Une donnée qui n'a pas été produite est le seul cas propre.

## Le facteur qui décide vraiment

Pas la technique. **L'intensité de la recherche.**

Retrouver quelqu'un coûte du temps, de l'accès à des bases et des réquisitions. Personne ne dépense ça pour quelqu'un que personne ne cherche. Les mêmes traces, exactement les mêmes, sont invisibles dans un cas et décisives dans l'autre.

C'est la variable que les discussions sur le sujet oublient systématiquement, et c'est celle qui explique pourquoi deux personnes aux pratiques identiques ont des résultats opposés.

## Ce qu'il faut retenir

**Un identifiant seul ne vaut rien ; c'est la jointure qui identifie.** Protéger une donnée isolée n'a donc pas beaucoup de sens : ce qu'on protège, ce sont les points de recoupement.

**Le comportement identifie mieux que les papiers.** Un faux nom ne change ni vos horaires, ni votre façon d'écrire, ni les gens que vous appelez.

**La biométrie ne se change pas.** C'est la seule catégorie d'identifiant qui n'a pas de version révocable, et elle se répand.

**Et la dissymétrie fondamentale :** il est facile de produire une trace, très difficile de la retirer, et impossible de retirer ses copies. Voir [[SIG-COM-007]] pour les conséquences pratiques.
