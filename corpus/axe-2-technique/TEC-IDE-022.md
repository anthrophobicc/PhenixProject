---
id: TEC-IDE-022
titre: Le sans contact, badges et cartes
axe: 2
categorie: Information et Données
temps: Court
contexte: 1
risque: Discret
materiel: Rien
priorite: normale
origine: officielle
tags: [sans contact, nfc, rfid, carte bancaire, badge, paiement mobile, antenne, securite, portefeuille]
sources: ["Norme ISO/IEC 14443, cartes à puce sans contact", "Banque de France, Observatoire de la sécurité des moyens de paiement, rapport annuel", "ANSSI, recommandations de sécurité pour les usages numériques"]
---

::Une carte sans contact n'a pas de pile : c'est le terminal qui l'alimente, par une petite antenne cachée dans le plastique, quand on l'approche à quelques centimètres. C'est ce qui la rend pratique, et c'est aussi pourquoi le « vol à distance » dont on parle tant est rare : il faut coller un lecteur à votre poche, et ce qu'il lit ne suffit presque jamais à payer ailleurs.::

## Comment ça marche

- **Une puce et une antenne** dans la carte, le badge, le téléphone.
- **Le lecteur** crée un champ qui alimente la puce le temps d'un échange, à **quelques centimètres**.
- **Le paiement** utilise des codes à usage unique : ce qu'on intercepte ne se rejoue pas.

## Les limites de sécurité

- **Les paiements sans code** sont plafonnés par transaction ; au bout de plusieurs paiements, le terminal redemande le code.
- **Le vrai risque** est le vol de la carte ou du téléphone : quelques paiements rapides avant qu'on fasse opposition. On fait opposition **tout de suite**. Voir [[TEC-IDE-015]].
- **Les étuis anti-ondes** protègent contre la lecture à distance, rare. Ils ne protègent pas du vol.
- **Les vieux badges** d'immeuble ou de parking sont souvent faciles à copier. Pour ce qui compte vraiment, un badge récent ou une vraie clé.

## Le téléphone

- **Le paiement mobile** : protégé par l'empreinte ou le code du téléphone, souvent plus sûr que la carte.
- **Le lecteur NFC** du téléphone lit certaines cartes de transport, étiquettes, passeports (avec leur clé).

À lire aussi : [[SURV-CRI-013]], [[TEC-IDE-021]].
