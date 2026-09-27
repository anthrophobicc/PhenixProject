---
id: TEC-IDE-005
titre: La vidéosurveillance publique
axe: 2
categorie: Information et Données
temps: Court
contexte: 1
risque: Discret
materiel: Technique
priorite: normale
origine: officielle
tags: [camera, videoprotection, ville, droit, surveillance, vie privee]
sources: ["Code de la sécurité intérieure, articles L251-1 à L255-1", "Cour des comptes, Les polices municipales, rapport public thématique, octobre 2020", "Piza E., Welsh B., Farrington D., Thomas A., CCTV surveillance for crime prevention, Criminology & Public Policy, 2019", "Loi n° 2023-380 du 19 mai 2023 relative aux Jeux olympiques et paralympiques, article 10", "Règlement (UE) 2024/1689 sur l'intelligence artificielle, article 5"]
---

::Une caméra de rue n'est presque jamais regardée en direct. Elle sert surtout après coup, à condition que quelqu'un demande les images à temps.::

## Comment fonctionne un réseau de ville

Les caméras d'une commune sont reliées par fibre ou par radio à un **centre de supervision urbain** : une salle, un mur d'écrans, quelques opérateurs. En France, la loi parle de **vidéoprotection** pour la voie publique, et de vidéosurveillance pour les lieux privés.

Un opérateur ne peut suivre vraiment que quelques écrans à la fois. Dans une ville qui a des centaines de caméras, **l'immense majorité des images n'est vue par personne**. Elle est enregistrée, puis effacée.

Trois usages dominent :

- **Le direct** : suivre une manifestation, un match, un incident signalé par radio.
- **L'après-coup** : la police ou la justice demande les images d'un endroit et d'une heure précis. C'est de loin l'usage principal.
- **La lecture de plaques** (LAPI) : des caméras dédiées lisent les immatriculations et les comparent à des fichiers de véhicules recherchés.

Le fonctionnement technique d'une caméra est détaillé dans [[TEC-IDE-004]].

## Ce que dit la loi en France

- Chaque caméra de voie publique demande une **autorisation du préfet**, après avis d'une commission départementale.
- Elle ne doit pas filmer l'intérieur des habitations, ni de façon précise leurs entrées.
- **Des panneaux** doivent signaler la zone filmée et dire à qui s'adresser.
- Les images se gardent **30 jours au plus**, souvent moins. Ensuite elles sont effacées, sauf si une enquête les a réclamées.
- Toute personne peut demander à voir les images où elle figure, auprès du responsable indiqué sur le panneau. Le refus est possible pour des raisons de sécurité ou d'enquête ; il se conteste devant la commission départementale.

**La reconnaissance faciale en temps réel dans la rue n'est pas autorisée en France.** À l'échelle européenne, le règlement sur l'intelligence artificielle de 2024 l'interdit aux forces de l'ordre, sauf exceptions étroites (recherche d'une victime, menace terroriste imminente) encadrées par un juge.

**L'analyse automatique des images**, sans reconnaissance des visages, a été expérimentée pour les Jeux de 2024 : repérer un objet abandonné, un mouvement de foule, une personne au sol. Son avenir fait l'objet de débats et de lois successives : vérifiez l'état du droit au moment où vous lisez.

## Est-ce que ça marche ?

La réponse la plus solide vient de l'analyse de 76 études menées sur quarante ans (Piza et collègues, 2019) :

- une **baisse modeste** de la délinquance là où sont les caméras, de l'ordre de 13 % en moyenne ;
- un effet net sur **les parkings** et les vols liés aux véhicules ;
- **pas d'effet mesurable sur les violences** : on ne réfléchit pas à la caméra au moment d'une bagarre.

En France, la Cour des comptes a relevé en 2020 qu'aucune corrélation globale n'était établie entre l'équipement d'une ville en caméras et son niveau de délinquance. Une étude commandée par la gendarmerie en 2021 a trouvé que les images n'avaient contribué qu'à une petite fraction des enquêtes élucidées.

Ce que les caméras font bien : **retracer un trajet après coup**, confirmer un horaire, retrouver un véhicule. Ce qu'elles font mal : empêcher.

## Ce qui vous sert concrètement

**Vous êtes victime ou témoin.** Portez plainte **dans les jours qui suivent** en donnant le lieu exact et l'heure. C'est la plainte qui permet à la police de réquisitionner les images avant leur effacement. Passé un mois, elles n'existent plus. Notez aussi les commerces du coin : leurs caméras privées ont souvent une meilleure vue que celles de la ville.

**Vous voulez savoir où sont les caméras.** Les panneaux, les délibérations du conseil municipal (l'installation se vote et se finance en public), les données ouvertes de certaines villes, et les cartes collaboratives comme OpenStreetMap, où les caméras sont recensées par des bénévoles.

**Vous voulez voir vos images.** Écrivez au responsable indiqué sur le panneau, dans le délai de conservation, en précisant lieu, date, heure et une description de vous.

**Vous tenez à votre vie privée.** Une caméra de rue est un maillon parmi d'autres ; le téléphone, les paiements et les badges en disent bien plus. Voir [[SIG-COM-007]].

**Pendant une coupure longue.** Un réseau de caméras dépend du courant et des liaisons. Sans eux, il s'éteint comme le reste, voir [[TEC-RES-001]].
