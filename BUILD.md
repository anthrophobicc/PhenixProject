# Fabriquer l'application Phenix

Résultat : un `Phenix.exe` installable sous Windows, et les équivalents macOS et
Linux depuis le même code.

Comptez trente minutes la première fois, dont vingt d'installation d'outils.
Les fois suivantes, deux minutes.

---

## Le plus rapide : les deux lanceurs

Sous Windows, vous n'avez rien à taper dans un terminal.

- **`LANCER-PHENIX.bat`** — ouvre Phenix immédiatement. Si l'exécutable a déjà
  été construit, c'est lui qui démarre ; sinon l'application s'ouvre dans votre
  navigateur. Tout fonctionne à l'identique, seule la sauvegarde sur disque
  demande l'exécutable.
- **`CONSTRUIRE-EXE.bat`** — fabrique l'exécutable. Il vérifie que Rust est
  présent, installe `tauri-cli` si besoin, lance la construction, puis ouvre le
  dossier contenant l'installateur.

La suite de ce document décrit la procédure manuelle, utile sous macOS et Linux
ou pour comprendre ce que font les lanceurs.

---

## 1. Installer les outils, une seule fois

### Windows

1. **Rust** — https://rustup.rs → téléchargez `rustup-init.exe`, exécutez-le,
   appuyez sur Entrée pour l'installation par défaut.
2. **Outils de compilation Microsoft** — installez « Visual Studio Build Tools »
   depuis le site de Microsoft, en cochant *Développement Desktop en C++*.
   C'est le plus long, environ 15 minutes.
3. **Node.js** — https://nodejs.org, version LTS.

### macOS

```bash
xcode-select --install
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

### Linux (Debian, Ubuntu)

```bash
sudo apt update
sudo apt install libwebkit2gtk-4.1-dev build-essential curl wget file \
  libxdo-dev libssl-dev libayatana-appindicator3-dev librsvg2-dev
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

**Fermez et rouvrez votre terminal après l'installation de Rust.**

---

## 2. Vérifier

```bash
rustc --version
cargo --version
```

Deux numéros de version doivent s'afficher. Sinon, le terminal n'a pas été
rouvert.

---

## 3. Les icônes

**Rien à faire : elles sont déjà dans `src-tauri/icons/`.**

Tous les formats sont générés à partir du logo Phenix : PNG pour Linux, `.ico` pour
Windows, `.icns` pour macOS, et les gabarits du Windows Store.

Si vous voulez les refaire un jour à partir d'un autre visuel, il faut un PNG carré
d'au moins 1024 pixels et la commande suivante — mais ce n'est pas nécessaire
aujourd'hui :

```bash
cargo install tauri-cli --version "^2"
cd src-tauri
cargo tauri icon ../logo.png
```

> `cargo tauri` n'existe qu'après `cargo install tauri-cli`. Installer le paquet npm
> `@tauri-apps/cli` donne la commande `npx tauri`, pas `cargo tauri` : c'est la cause
> la plus fréquente de blocage à cette étape.

---

## 4. Essayer

```bash
cd src-tauri
cargo tauri dev
```

La fenêtre Phenix s'ouvre. La première compilation prend plusieurs minutes,
c'est normal : Rust compile toutes les dépendances une fois et les garde.

**Vérifiez immédiatement que l'enregistrement fonctionne :** créez une fiche,
fermez la fenêtre, rouvrez avec la même commande. La fiche doit être là.
En haut à droite, l'indicateur doit afficher « Enregistré sur l'ordinateur ».

---

## 5. Fabriquer l'installeur

```bash
cargo tauri build
```

Les fichiers apparaissent dans `src-tauri/target/release/bundle/` :

| Système | Fichier |
|---|---|
| Windows | `nsis/Phenix_0.1.0_x64-setup.exe` |
| Windows | `msi/Phenix_0.1.0_x64_en-US.msi` |
| macOS | `dmg/Phenix_0.1.0_aarch64.dmg` |
| Linux | `appimage/phenix_0.1.0_amd64.AppImage` |

Comptez entre 5 et 10 Mo. C'est cette légèreté qui motive le choix de Tauri
plutôt qu'Electron, où le même logiciel pèserait plus de 100 Mo.

---

## Où sont enregistrées les données

L'application écrit un seul fichier, `sauvegarde.json`, dans le dossier de
données de l'utilisateur :

| Système | Emplacement |
|---|---|
| Windows | `%APPDATA%\org.phenix.bibliotheque\` |
| macOS | `~/Library/Application Support/org.phenix.bibliotheque/` |
| Linux | `~/.local/share/org.phenix.bibliotheque/` |

Ce fichier est la sauvegarde. Copiez-le où vous voulez, il se réimporte par
Paramètres → Importer.

---

## Une chose à savoir avant de distribuer

L'application n'est pas signée numériquement. Au premier lancement, Windows
affichera **« Windows a protégé votre ordinateur »**. Il faut cliquer sur
*Informations complémentaires* puis *Exécuter quand même*.

Ce n'est pas un défaut de votre application : c'est le comportement normal
pour tout logiciel non signé. Un certificat de signature coûte quelques
centaines d'euros par an.

**Dites-le à l'avance dans vos notes de version.** Un avertissement annoncé
inquiète beaucoup moins qu'un avertissement découvert.

---

## Si ça ne compile pas

**`cargo: command not found`** — le terminal n'a pas été rouvert après
l'installation de Rust.

**`link.exe not found` sous Windows** — les outils de compilation Microsoft
manquent, ou la case *Développement Desktop en C++* n'a pas été cochée.

**`webkit2gtk not found` sous Linux** — reprenez la commande `apt install`
de l'étape 1.

**`cargo tauri` : commande inconnue** — les icônes sont déjà fournies, cette commande
n'est pas nécessaire. Si vous y tenez, faites d'abord `cargo install tauri-cli --version "^2"`.

**La fenêtre s'ouvre vide** — vérifiez que `app/index.html` existe bien.
C'est ce fichier que Tauri charge, pas `phenix.html`.
