// Exporte la bibliothèque en fichiers texte simples, pour la lire sur un petit écran (Flipper Zero, prototype Phenix 001).
// Une fiche = un fichier .txt, rangé par langue puis par axe. Le Markdown est aplati : titres en majuscules,
// gras retiré, liens [[ID]] remplacés par « (voir ID) ».
// Usage : node outils/export-flipper.js  → sortie-flipper/phenix/
"use strict";
const fs = require("fs");
const path = require("path");

const RACINE = path.join(__dirname, "..");
const SORTIE = path.join(RACINE, "sortie-flipper", "phenix");
const AXES = { "axe-1-memoire": "1-memory", "axe-2-technique": "2-technique", "axe-3-survie": "3-survival" };

const sansAccents = (s) => s.normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/[’']/g, "").replace(/[^\w -]/g, "").replace(/\s+/g, " ").trim();
function lire(fichier) {
  const brut = fs.readFileSync(fichier, "utf8").replace(/\r/g, "");
  const m = brut.match(/^---\n([\s\S]*?)\n---\n?([\s\S]*)$/);
  if (!m) return null;
  const meta = {};
  for (const l of m[1].split("\n")) { const i = l.indexOf(":"); if (i > 0) meta[l.slice(0, i).trim()] = l.slice(i + 1).trim(); }
  return { meta, corps: m[2] };
}
function aplatir(corps, langue) {
  return corps
    .replace(/::(.+?)::/g, "$1")
    .replace(/^#{1,6}\s*(.+)$/gm, (_, t) => "\n" + t.toUpperCase())
    .replace(/\*\*(.+?)\*\*/g, "$1")
    .replace(/(^|[^*])\*(?!\s)(.+?)\*/g, "$1$2")
    .replace(/\[\[([A-Z0-9-]+)\]\]/g, langue === "en" ? "(see $1)" : "(voir $1)")
    .replace(/\[([^\]]+)\]\((https?:[^)]+)\)/g, "$1")
    .replace(/^\s*[-*]\s+/gm, "- ")
    .replace(/\n{3,}/g, "\n\n")
    .trim();
}

fs.rmSync(path.join(RACINE, "sortie-flipper"), { recursive: true, force: true });
let n = 0;
for (const [langue, base] of [["fr", path.join(RACINE, "corpus")], ["en", path.join(RACINE, "traductions", "en")]]) {
  for (const [dossier, nomAxe] of Object.entries(AXES)) {
    const d = path.join(base, dossier);
    if (!fs.existsSync(d)) continue;
    for (const f of fs.readdirSync(d).filter((x) => x.endsWith(".md")).sort()) {
      const fiche = lire(path.join(d, f));
      if (!fiche || !fiche.meta.id) continue;
      const titre = fiche.meta.titre || fiche.meta.id;
      const texte = `${titre.toUpperCase()}\n${fiche.meta.id}\n\n${aplatir(fiche.corps, langue)}\n`;
      const nom = (fiche.meta.id + " " + sansAccents(titre)).slice(0, 48) + ".txt";
      const cible = path.join(SORTIE, langue, nomAxe);
      fs.mkdirSync(cible, { recursive: true });
      fs.writeFileSync(path.join(cible, nom), texte);
      n++;
    }
  }
}
fs.writeFileSync(path.join(SORTIE, "LISEZMOI.txt"), "PHENIX\nBibliotheque hors ligne.\nfr : toutes les fiches\nen : les fiches traduites\n1 memoire, 2 technique, 3 survie\n");
console.log(`${n} fiches exportées dans ${SORTIE}`);
