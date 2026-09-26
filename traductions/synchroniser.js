// Recopie les fiches traduites dans l'application : bloc CORPUS_EN de app/phenix.html, puis sa copie app/index.html.
// site/phenix.html est produit à partir de app/phenix.html par outils/construire-site.js : relancez-le ensuite.
// Usage : node traductions/synchroniser.js && node outils/construire-site.js
const fs = require("fs");
const path = require("path");

const RACINE = path.resolve(__dirname, "..");
const CIBLES = ["app/phenix.html", "app/index.html"].map((f) => path.join(RACINE, f));

// Identifiants du corpus de référence : une traduction doit toujours correspondre à une fiche existante.
const ids = new Set();
(function lire(d) {
  for (const e of fs.readdirSync(d, { withFileTypes: true })) {
    const p = path.join(d, e.name);
    if (e.isDirectory()) lire(p);
    else if (e.name.endsWith(".md")) { const m = fs.readFileSync(p, "utf8").match(/^id:\s*(\S+)/m); if (m) ids.add(m[1]); }
  }
})(path.join(RACINE, "corpus"));

const fichiers = [];
(function parcourir(d) {
  for (const e of fs.readdirSync(d, { withFileTypes: true })) {
    const p = path.join(d, e.name);
    if (e.isDirectory()) parcourir(p);
    else if (e.name.endsWith(".md") && e.name !== "LISEZMOI.md") fichiers.push(p);
  }
})(path.join(__dirname, "en"));

const blocs = fichiers.sort().map((f) => {
  const t = fs.readFileSync(f, "utf8").replace(/\r\n/g, "\n").replace(/\s*$/, "\n");
  const id = (t.match(/^id:\s*(\S+)/m) || [])[1];
  if (!t.startsWith("---\nid: ")) throw new Error("En-tête mal formée : " + f);
  if (!ids.has(id)) throw new Error("Aucune fiche d'origine pour " + id + " (" + f + ")");
  if (/`/.test(t) || /\$\{/.test(t)) throw new Error("Backtick ou ${ interdits dans " + id);
  for (const [, lien] of t.matchAll(/\[\[([^\]]+)\]\]/g)) if (!ids.has(lien.trim())) console.warn(`  ${id} : lien vers ${lien} introuvable`);
  return t;
});

let html = fs.readFileSync(CIBLES[0], "utf8");
const deb = html.indexOf("const CORPUS_EN=String.raw`");
if (deb < 0) throw new Error("Bloc CORPUS_EN absent de l'application");
const fin = html.indexOf("\n`;", deb);
html = html.slice(0, deb) + "const CORPUS_EN=String.raw`\n" + blocs.join("\n") + html.slice(fin);
for (const c of CIBLES) fs.writeFileSync(c, html, "utf8");
console.log(`${blocs.length} fiche(s) anglaise(s) recopiée(s) dans l'application`);
