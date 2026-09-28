---
id: TEC-ELN-009
titre: Internet, comment ça marche
axe: 2
categorie: Électronique et Numérique
temps: Court
contexte: 1
risque: Discret
materiel: Rien
priorite: normale
origine: officielle
tags: [internet, cables sous-marins, paquets, adresse ip, dns, antennes, fibre, panne, sms]
sources: ["TeleGeography, Submarine Cable Map", "International Cable Protection Committee, causes des dommages aux câbles sous-marins", "Arcep, rapports sur l'état de l'internet en France"]
---

::Internet ne passe pas par les satellites : presque tout le trafic entre continents voyage dans quelques centaines de câbles posés au fond de la mer, pas plus épais qu'un tuyau d'arrosage. Ils sont coupés plus de cent fois par an, surtout par des ancres et des chaluts.::

## Le principe

Internet, c'est **un réseau de réseaux** : ceux des opérateurs, des entreprises, des universités, reliés entre eux.

1. Un message, une photo, une page sont **découpés en petits paquets**.
2. Chaque paquet porte une **adresse** (l'adresse IP) et part de routeur en routeur, parfois par des chemins différents.
3. À l'arrivée, les paquets sont **remis dans l'ordre**. Si un chemin est coupé, les suivants en prennent un autre.

**Le DNS**, c'est l'annuaire : il traduit « wikipedia.org » en adresse chiffrée.

## Le chemin jusqu'à chez vous

Un serveur dans un centre de données, des câbles terrestres et sous-marins, un nœud de l'opérateur près de chez vous, puis **la fibre, le cuivre ou une antenne 4G ou 5G**. Voir [[TEC-RES-001]].

## Pourquoi ça tombe

- **Le courant** : les antennes relais et les équipements de quartier ne tiennent que **quelques heures sur batterie**.
- **La saturation** : après une catastrophe, tout le monde appelle en même temps.
- **Les câbles** coupés par un chantier, une tempête, une ancre, ou volontairement.

## Ce qui passe quand ça coince

- **Les SMS** passent souvent quand les appels et les données ne passent plus : courts, envoyés quand le réseau a un trou.
- **Le 112** passe par n'importe quel réseau mobile disponible, même celui d'un autre opérateur.
- **Ce qui est déjà téléchargé** reste lisible : cartes, encyclopédie, fiches. Voir [[TEC-ELN-012]].

Les numéros et fréquences utiles : [[SIG-COM-009]].
