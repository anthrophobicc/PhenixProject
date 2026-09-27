---
id: TEC-IDE-006
titre: Le terminal de paiement
axe: 2
categorie: Information et Données
temps: Court
contexte: 1
risque: Discret
materiel: Technique
priorite: normale
origine: officielle
tags: [tpe, carte bancaire, paiement, sans contact, puce, banque, coupure]
sources: ["EMVCo, EMV Integrated Circuit Card Specifications for Payment Systems, livres 1 à 4", "Groupement des Cartes Bancaires CB, règles de fonctionnement du paiement sans contact", "Banque de France, Observatoire de la sécurité des moyens de paiement, rapport annuel", "ISO/IEC 14443, cartes sans contact de proximité"]
---

::Une carte bancaire ne contient pas d'argent. Elle contient une clé qui prouve que c'est bien elle. Le terminal ne paie rien : il pose une question à la banque, et attend la réponse.::

## Ce qu'il y a dans la carte

La puce est un vrai petit ordinateur, avec une mémoire protégée. Elle garde une **clé secrète** qu'elle ne révèle jamais, même à celui qui la lit. À chaque paiement, elle s'en sert pour calculer un **cryptogramme** : un code unique, valable pour cette opération, ce montant, ce jour.

C'est ce qui rend une carte à puce difficile à copier. On peut lire son numéro, pas sa clé ; et un cryptogramme volé ne sert qu'une fois.

**La piste magnétique**, au dos, contient seulement le numéro et la date. Elle se copie facilement : c'est pour cela qu'elle ne sert presque plus en Europe.

## Ce qui se passe en deux secondes

1. **Lecture.** Le terminal parle à la puce, par contact ou par radio.
2. **Le code.** Vous tapez votre code. En Europe, c'est le plus souvent **la puce elle-même qui le vérifie** : le code ne part pas vers la banque. Trois erreurs et elle se bloque.
3. **La demande.** Le terminal envoie le montant et le cryptogramme à la banque du commerçant (**l'acquéreur**).
4. **Le réseau.** L'acquéreur transmet par le réseau de la carte (CB, Visa, Mastercard) à **votre banque**, l'émetteur.
5. **La décision.** Votre banque vérifie le cryptogramme, le solde ou le plafond, les signes de fraude, et répond oui ou non.
6. **Le ticket.** La réponse revient par le même chemin. Tout cela dure une à trois secondes.

**L'argent, lui, ne bouge pas encore.** Le soir, le terminal envoie toutes les opérations de la journée en un lot (la **télécollecte**). Les banques compensent entre elles, et le commerçant est crédité un ou deux jours plus tard, moins une commission.

## Le sans contact

La carte contient une petite antenne. Le terminal émet un champ radio à **13,56 MHz** qui alimente la puce à quelques centimètres, sans pile. Les terminaux de paiement sont conçus pour lire à moins de 4 cm environ.

Pour aller vite, on saute le code sous un certain montant, **50 euros en France**. Pour limiter les risques en cas de vol, la carte compte les paiements sans code : passé un montant cumulé ou un nombre d'opérations, elle demande le code au paiement suivant.

**Le téléphone** fonctionne de la même façon, mais le numéro de carte est remplacé par un numéro de substitution, et c'est votre empreinte ou votre visage qui remplace le code.

## Pourquoi ça peut dire non

- Plafond de paiement atteint (souvent sur 7 ou 30 jours glissants).
- Carte bloquée, expirée, ou puce usée : essayez le sans contact, ou l'inverse.
- Soupçon de fraude : achat inhabituel, pays inhabituel. Votre application bancaire le signale souvent.
- **Pas de réseau.**

## Quand le réseau tombe

Un terminal a besoin de deux choses : **du courant et une liaison** (ligne fixe, internet, ou carte SIM pour les terminaux mobiles).

Certains terminaux savent accepter un paiement **hors ligne** sous un petit montant fixé par la banque (le plafond de sol) : la puce vérifie le code et la carte seule, l'opération est stockée et envoyée plus tard. C'est un risque pour le commerçant, qui le limite ou le refuse.

Lors d'une coupure étendue, comme en Espagne et au Portugal le 28 avril 2025, les terminaux s'arrêtent avec le reste : les magasins encore ouverts n'acceptent plus que **les espèces**. Gardez-en un peu chez vous, en petites coupures. Voir [[TEC-RES-001]].

## Se protéger

- **Cachez le clavier** quand vous tapez le code : une caméra ou un regard suffit à le voler, et la carte se vole ensuite.
- **Regardez le terminal** d'un distributeur ou d'une pompe à essence : une façade qui bouge, un lecteur épais, un clavier en relief peuvent cacher un copieur.
- **Le montant affiché** est celui que vous acceptez : lisez-le avant de présenter la carte.
- **Une carte perdue** se fait opposer tout de suite, par l'application ou par le numéro de votre banque. En France, le numéro interbancaire d'opposition est le 0 892 705 705.
- Le sans contact volé est limité par le compteur de la carte ; le paiement en ligne avec vos numéros est le vrai risque. Surveillez vos relevés.
