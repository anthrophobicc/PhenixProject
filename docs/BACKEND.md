# Phenix en ligne : propositions, votes, commentaires (Supabase)

Branché le 26/09/2026. Projet Supabase **phenix** (organisation Phenix, offre gratuite, région Europe).
Adresse : `https://ecdyahykwtqdierxlemb.supabase.co`. Tableau de bord : https://supabase.com/dashboard/project/ecdyahykwtqdierxlemb

## Ce qui marche

| Où | Ce que les gens font | Où ça arrive |
|---|---|---|
| Site, page Lab (`lab.html`) | Envoyer une idée de fiche en 10 secondes, ou une fiche complète avec images | table `propositions` (privée) |
| Site, sous chaque fiche | Voter « Utile », commenter | tables `votes` et `commentaires` |
| Application (site et .exe) | « Proposer au corpus » > « Envoyer maintenant » ; « Utile » et commentaires sous les fiches officielles | mêmes tables |
| Story Instagram, bio | Lien `lab.html?origine=story#idee` (ou `?origine=bio`) : on sait d'où vient la personne | colonne `origine` |

## Lire ce qui arrive (sur téléphone aussi)

Tableau de bord > **Table Editor** > `propositions`. Chaque ligne a une référence (`SUB-2026-0001`), le type (fiche, idée, correction, message), le texte, le pseudo, le contact (privé, jamais montré), l'origine.

- **Garder privé** : ne rien faire. Personne d'autre que toi ne voit la ligne.
- **Publier pour tout le monde** : cocher `visible`. La proposition apparaît dans « Ce que la communauté propose » sur la page Lab, où les gens votent et commentent.
- **Suivre** : changer `statut` (submitted, under_review, changes_requested, rejected, community, verified, official) et écrire dans `motif` ou `commentaire` (notes internes).
- **Un commentaire à retirer** : table `commentaires`, décocher `visible`.
- Images jointes : **Storage** > dossier `propositions` > dossier de la référence.

## Sécurité

- Le public ne touche aucune table directement. Il passe par quatre fonctions (`proposer`, `signaler`, `voter`, `commenter`) et trois vues en lecture (`propositions_publiques`, `votes_publics`, `commentaires_publics`). Tout le schéma est dans `supabase/01-propositions.sql`.
- La clé écrite dans le site et l'application est la clé **publishable** : elle est faite pour être publique. La clé **secret** ne doit jamais sortir du tableau de bord.
- Garde-fous : 5 envois par appareil en 10 minutes, 200 propositions et 300 commentaires par heure au total, pas de lien dans les commentaires, images de 5 Mo au plus et seulement juste après une proposition. L'adresse IP n'est jamais gardée (seulement une empreinte qui change chaque jour).
- Le mot de passe de la base a été généré par Supabase à la création. Si un jour il te faut une connexion directe à la base : Project Settings > Database > Reset database password.

## À savoir

- Un projet gratuit se met en pause après une semaine sans aucune activité. Les visites du site suffisent à le garder éveillé. S'il est en pause : tableau de bord > **Restore project**. Pendant la pause, le site continue de marcher ; l'envoi rend la fiche en fichier `.md` pour que rien ne soit perdu.
- Offre gratuite : 500 Mo de base et 1 Go de fichiers. Largement de quoi tenir des milliers de propositions.
- Pour être prévenu à chaque nouvelle proposition (notification sur le téléphone), il faut brancher un service en plus : à décider ensemble.
