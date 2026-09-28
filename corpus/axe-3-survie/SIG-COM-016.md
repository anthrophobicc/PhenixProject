---
id: SIG-COM-016
titre: Les codes et le chiffrement simple
axe: 3
categorie: Signaux et Communications
temps: Court
contexte: 1
risque: Discret
materiel: Rien
priorite: normale
origine: officielle
tags: [chiffrement, code cesar, analyse de frequences, masque jetable, mot de passe familial, arnaque, voix clonee, cryptologie]
sources: ["Singh S., Histoire des codes secrets, Lattès, 1999", "Shannon C.E., Communication theory of secrecy systems, Bell System Technical Journal, 1949", "Loi n° 2004-575 du 21 juin 2004 pour la confiance dans l'économie numérique (liberté de la cryptologie)"]
---

::Jules César décalait chaque lettre de trois rangs dans l'alphabet pour écrire à ses généraux. Au IXe siècle, le savant arabe Al-Kindi a montré comment casser ce genre de code en comptant les lettres les plus fréquentes. Mais il existe un code que personne ne peut casser, prouvé mathématiquement en 1949 : le masque jetable. Et le code le plus utile aujourd'hui tient en un seul mot, connu de votre famille.::

## COMPRENDRE

- **Le code de César** et tous les codes où une lettre est toujours remplacée par la même se cassent en quelques minutes : en français, le **E** est de loin la lettre la plus fréquente, on le repère, puis le reste suit.
- **Le masque jetable** : une clé faite de lettres **tirées au hasard**, **aussi longue que le message**, utilisée **une seule fois** et connue seulement des deux correspondants. Bien utilisé, il est incassable : les espions et la ligne directe entre Moscou et Washington s'en sont servis.
- **En France**, utiliser le chiffrement est libre.

## AGIR

**Le mot de passe familial**

Des escrocs imitent désormais la voix d'un proche avec quelques secondes d'enregistrement : « Maman, j'ai eu un accident, envoie de l'argent. »

- **Choisir un mot secret** connu seulement de la famille, jamais écrit en ligne.
- **Au moindre appel urgent** qui demande de l'argent ou une information : « Quel est notre mot ? » Pas de mot, on raccroche et on rappelle le proche sur son numéro habituel.

**Les mots convenus**

Pour les messages visibles de tous : des phrases anodines dont le sens est convenu à l'avance (« la tante va bien » = on part au point de rendez-vous B). Voir [[SIG-COM-014]].

**Le masque jetable, à la main**
1. Numéroter les lettres de A = 0 à Z = 25.
2. Pour chaque lettre du message, **ajouter** la lettre correspondante de la clé, et retrancher 26 si on dépasse 25.
3. Le destinataire **soustrait** la même clé.
4. **Détruire** la clé après usage.

## ADAPTER

- **Sur les réseaux**, les messageries chiffrées de bout en bout protègent mieux que tous les codes faits main. Voir [[TEC-ELN-008]].
- **Le morse** n'est pas un code secret : tout le monde peut le lire. Voir [[SIG-COM-003]].
