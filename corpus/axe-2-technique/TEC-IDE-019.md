---
id: TEC-IDE-019
titre: Le code-barres et le QR code
axe: 2
categorie: Information et Données
temps: Court
contexte: 1
risque: Discret
materiel: Rien
priorite: normale
origine: officielle
tags: [code-barres, ean-13, qr code, prefixe pays, faux qr code, arnaque, denso wave, stockage hors ligne]
sources: ["GS1, standard EAN-13 et préfixes des organisations nationales", "Denso Wave, histoire du QR code (1994)", "Cybermalveillance.gouv.fr, arnaques aux faux QR codes"]
---

::Le 26 juin 1974, dans un supermarché de l'Ohio, la première caisse scanne le premier code-barres : un paquet de chewing-gums. Vingt ans plus tard, au Japon, une filiale de Toyota invente le QR code pour suivre ses pièces détachées. Aujourd'hui, ces petits dessins disent beaucoup de choses, et certains mentent.::

## Le code-barres

- **Les 13 chiffres** écrits sous les barres disent tout : le lecteur ne fait que les lire plus vite.
- **Les premiers chiffres** indiquent le pays **où l'entreprise a enregistré son code**, pas celui où le produit est fabriqué. Un code qui commence par 3 (France) peut très bien désigner un produit fabriqué ailleurs.
- **Le dernier chiffre** est une clé de contrôle : une erreur de lecture est détectée.

## Le QR code

- Un carré de points noirs et blancs qui peut contenir **un lien, un texte, un numéro, des coordonnées GPS**, jusqu'à quelques milliers de caractères.
- Il reste lisible même **abîmé ou en partie caché** (jusqu'à environ un tiers) : c'est pour ça qu'on peut mettre un logo au milieu.
- **Il ne contient pas forcément un lien** : un QR code peut porter un texte entier, lisible sans internet. Pratique pour afficher une consigne, une fiche, un plan.

## Les arnaques

- **Les faux QR codes** collés par-dessus les vrais, sur les horodateurs, les bornes de recharge, les affiches, les avis de passage : ils envoient vers un faux site de paiement.
- **Avant de payer** : regarder l'adresse du site qui s'ouvre, vérifier qu'aucun autocollant n'a été posé sur le code, et **payer plutôt par l'application officielle** ou le terminal.
- **Un QR code reçu par courrier ou par message** qui demande de « régulariser » un paiement ou de « mettre à jour » un compte : arnaque presque à coup sûr. Voir [[TEC-IDE-015]].

## En crise

Une imprimante et un générateur de QR code hors ligne permettent d'afficher des textes, des coordonnées ou des contacts que chacun lit avec son téléphone, sans réseau. Voir [[TEC-ELN-017]].

Reconnaître une fausse information : [[TEC-IDE-010]].
