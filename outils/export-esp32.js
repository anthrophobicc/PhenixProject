// La bibliothèque pour le Phenix 001 v0 (ESP32-C3 + écran de Nokia 6300) : toutes les fiches officielles,
// compilées dans la mémoire flash de l'ESP32. Écrit materiel/phenix-001-v0/ecran/fiches.h.
// Les images sont retirées et les signes que les polices de l'écran n'ont pas (tirets longs, apostrophes courbes…)
// sont remplacés : les polices de l'écran s'arrêtent au latin-1.
// Usage : node outils/export-esp32.js [fr|en]   (en : la traduction anglaise quand elle existe, sinon le français)
"use strict";
const fs = require("fs");
const path = require("path");

const RACINE = path.join(__dirname, "..");
const LANGUE = process.argv[2] === "en" ? "en" : "fr";
const SORTIE = path.join(RACINE, "materiel", "phenix-001-v0", "ecran", "fiches.h");

function lire(dossier) {
  const out = {};
  for (const axe of fs.readdirSync(dossier)) {
    const d = path.join(dossier, axe);
    if (!fs.statSync(d).isDirectory()) continue;
    for (const f of fs.readdirSync(d)) {
      if (!f.endsWith(".md") || f === "LISEZMOI.md") continue;
      const src = fs.readFileSync(path.join(d, f), "utf8").replace(/\r\n/g, "\n");
      const m = src.match(/^---\n([\s\S]*?)\n---\n?([\s\S]*)$/);
      if (!m) continue;
      const meta = {};
      for (const l of m[1].split("\n")) {
        const i = l.indexOf(":");
        if (i > 0) meta[l.slice(0, i).trim()] = l.slice(i + 1).trim().replace(/^["']|["']$/g, "");
      }
      if (meta.id) out[meta.id] = { meta, corps: m[2].trim() };
    }
  }
  return out;
}

// Les caractères hors latin-1 que les fiches emploient, et leur équivalent affichable.
const REMPLACE = [[/[‘’ʼ]/g, "'"], [/[“”]/g, '"'], [/[–—]/g, "-"], [/…/g, "..."],
  [/→/g, "->"], [/←/g, "<-"], [/≈/g, "~"], [/≤/g, "<="], [/≥/g, ">="], [/−/g, "-"],
  [/œ/g, "oe"], [/Œ/g, "OE"], [/[   ]/g, " "], [/•/g, "-"]];
function nettoyer(t) {
  t = t.split("\n").filter((l) => !l.trim().startsWith("![")).join("\n");          // les images restent dans l'appli
  t = t.replace(/\{\{([^|}]+)\|[^}]+\}\}/g, "$1").replace(/\{(rouge|vert|bleu|ambre)\|([^}]+)\}/g, "$2");
  for (const [re, par] of REMPLACE) t = t.replace(re, par);
  // tout ce qui reste hors latin-1 (et hors puce) disparaît plutôt que d'afficher un carré vide
  return t.replace(/[^\u0000-ÿ•]/g, "");
}

const FR = lire(path.join(RACINE, "corpus"));
const EN = LANGUE === "en" ? lire(path.join(RACINE, "traductions", "en")) : {};
const fiches = Object.keys(FR).map((id) => {
  const f = EN[id] || FR[id];
  return { id, titre: nettoyer(f.meta.titre || id), axe: parseInt(FR[id].meta.axe, 10) || 3,
    urgence: (FR[id].meta.priorite || "").toLowerCase() === "flash", texte: nettoyer(f.corps) };
});
// Les urgences d'abord : c'est ce qu'on cherche quand on sort l'appareil. Puis par axe et par titre.
fiches.sort((a, b) => (b.urgence - a.urgence) || (a.axe - b.axe) || a.titre.localeCompare(b.titre, LANGUE));

const brut = (s) => {
  if (s.includes(")PHX\"")) throw new Error("délimiteur présent dans le texte");
  return 'R"PHX(' + s + ')PHX"';
};
let h = `// Généré par outils/export-esp32.js (${LANGUE}) : ne pas modifier à la main.
#pragma once
#include <stdint.h>
struct Fiche { const char* id; const char* titre; uint8_t axe; bool urgence; const char* texte; };
`;
fiches.forEach((f, i) => { h += `static const char T${i}[] = ${brut(f.titre)};\nstatic const char C${i}[] = ${brut(f.texte)};\n`; });
h += `static const Fiche FICHES[] = {\n${fiches.map((f, i) => `  {"${f.id}", T${i}, ${f.axe}, ${f.urgence}, C${i}},`).join("\n")}\n};\n`;
h += `static const int NB_FICHES = ${fiches.length};\n`;
fs.mkdirSync(path.dirname(SORTIE), { recursive: true });
fs.writeFileSync(SORTIE, h);
const octets = fiches.reduce((s, f) => s + Buffer.byteLength(f.texte) + Buffer.byteLength(f.titre), 0);
console.log(`${fiches.length} fiches (${fiches.filter((f) => f.urgence).length} urgences), ${(octets / 1e6).toFixed(2)} Mo de texte → ${path.relative(RACINE, SORTIE)}`);
