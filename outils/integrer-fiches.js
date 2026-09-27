// Ajoute à l'application (app/phenix.html) les fiches du corpus et leurs traductions qui n'y sont pas encore.
// L'application embarque tout le corpus dans deux blocs de texte (CORPUS et CORPUS_EN) : c'est ce qui la fait marcher sans réseau.
// Usage : node outils/integrer-fiches.js            (toutes les fiches manquantes)
//         node outils/integrer-fiches.js ID1 ID2     (seulement celles-ci)
"use strict";
const fs = require("fs");
const path = require("path");

const RACINE = path.join(__dirname, "..");
const APP = path.join(RACINE, "app", "phenix.html");
const voulues = process.argv.slice(2);

function lireDossier(base) {
  const out = {};
  for (const axe of fs.readdirSync(base).filter((d) => d.startsWith("axe-"))) {
    for (const f of fs.readdirSync(path.join(base, axe)).filter((x) => x.endsWith(".md"))) {
      const texte = fs.readFileSync(path.join(base, axe, f), "utf8").replace(/\r/g, "").trim();
      const id = (texte.match(/^id:\s*(\S+)/m) || [])[1];
      if (id) out[id] = texte;
    }
  }
  return out;
}
function inserer(html, debutBloc, fiches) {
  const a = html.indexOf(debutBloc);
  if (a < 0) throw new Error("bloc introuvable : " + debutBloc);
  const b = html.indexOf("\n`;", a);
  const bloc = html.slice(a, b);
  const ajout = [];
  for (const [id, texte] of Object.entries(fiches)) {
    if (voulues.length && !voulues.includes(id)) continue;
    if (new RegExp("\\nid: " + id + "\\n").test(bloc)) continue;
    if (texte.includes("`") || texte.includes("${")) throw new Error(id + " contient un accent grave ou ${ : impossible dans le bloc");
    ajout.push(id);
    html = html.slice(0, b) + "\n\n" + texte + html.slice(b);
  }
  return { html, ajout };
}

let html = fs.readFileSync(APP, "utf8");
const fr = inserer(html, "const CORPUS=String.raw`", lireDossier(path.join(RACINE, "corpus")));
const en = inserer(fr.html, "const CORPUS_EN=String.raw`", lireDossier(path.join(RACINE, "traductions", "en")));
fs.writeFileSync(APP, en.html);
fs.copyFileSync(APP, path.join(RACINE, "app", "index.html"));
console.log(`français : ${fr.ajout.length ? fr.ajout.join(", ") : "rien à ajouter"}`);
console.log(`anglais : ${en.ajout.length ? en.ajout.join(", ") : "rien à ajouter"}`);
