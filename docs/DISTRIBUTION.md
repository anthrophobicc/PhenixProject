# Distribuer Phenix en application de bureau

## Comparaison

| Solution | Taille | Hors ligne | Fichiers locaux | Windows | macOS/Linux | Verdict |
|---|---|---|---|---|---|---|
| **HTML local** | 170 Ko | Oui | Import/export seulement | Oui | Oui | Déjà en place |
| **Electron** | 90–150 Mo | Oui | Complet | Oui | Oui | Trop lourd |
| **Tauri** | 3–8 Mo | Oui | Complet | Oui | Oui | **Recommandé** |
| **PWA** | 200 Ko | Oui | Limité | Partiel | Partiel | Demande un serveur |

## Recommandation : Tauri

Tauri utilise le moteur de rendu déjà présent dans le système au lieu d'embarquer
un navigateur entier. C'est ce qui explique l'écart de taille avec Electron :
quelques mégaoctets contre plus de cent, pour le même code.

Ce que ça apporte à Phenix :

- **Un vrai `.exe`**, un `.dmg` et un `.AppImage` depuis la même base
- **Accès au disque**, donc sauvegarde automatique et fin de la perte de session
- **Aucun serveur**, aucun compte, aucune connexion imposée
- **Démarrage instantané** et empreinte mémoire faible

Le seul coût réel : la compilation demande d'installer Rust une fois. Le code
de l'application, lui, ne change pas.

## Ce qu'il reste à faire

1. Installer Rust et l'outillage Tauri
2. Placer `app/phenix.html` comme page de l'application
3. Remplacer le stockage en mémoire par une écriture dans le dossier de données
4. Signer les binaires — sans signature, Windows affiche un avertissement qui
   fait fuir la moitié des gens

## Sur la signature

Un certificat de signature de code coûte quelques centaines d'euros par an.
Tant qu'il n'est pas en place, indiquez-le franchement dans les notes de version :
l'avertissement de Windows est normal pour un projet non signé, et le dire
à l'avance vaut mieux que de le laisser découvrir.
