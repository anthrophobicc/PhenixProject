// La version officielle de la bibliothèque, telle que l'application l'embarque (app/phenix.html) :
// CORPUS pour le français, CORPUS_EN pour les traductions. Elle sort au format « phenix-version »,
// celui que Phenix Base sait ouvrir, exporter et publier. C'est ce que Phenix Hub propose au téléchargement.
"use strict";
const crypto = require("crypto");

// Mêmes règles de lecture que l'application (parseYaml et parseFiche dans app/phenix.html).
function parseYaml(t) {
  const o = {};
  t.split(/\r?\n/).forEach((l) => {
    if (!l.trim() || /^\s*#/.test(l)) return;
    const i = l.indexOf(":");
    if (i < 0) return;
    const k = l.slice(0, i).trim();
    let v = l.slice(i + 1).trim();
    if (v.startsWith("[") && v.endsWith("]")) {
      v = v.slice(1, -1).split(/,(?=(?:[^"]*"[^"]*")*[^"]*$)/).map((s) => s.trim().replace(/^["']|["']$/g, "")).filter(Boolean);
    } else v = v.replace(/^["']|["']$/g, "");
    o[k] = v;
  });
  return o;
}
function parseFiche(raw) {
  const m = raw.match(/^\s*---\r?\n([\s\S]*?)\r?\n---\r?\n?([\s\S]*)$/);
  if (!m) return null;
  const y = parseYaml(m[1]);
  if (!y.id) return null;
  const liste = (v) => (Array.isArray(v) ? v : v ? String(v).split(/[,\s]+/).filter(Boolean) : []);
  const f = {
    id: String(y.id).toUpperCase(),
    titre: y.titre || y.id,
    axe: parseInt(y.axe, 10) || 3,
    categorie: y.categorie || "",
    temps: y.temps || "",
    contexte: String(y.contexte || ""),
    risque: y.risque || "",
    materiel: y.materiel || "",
    priorite: (y.priorite || "normale").toLowerCase(),
    tags: liste(y.tags),
    sources: Array.isArray(y.sources) ? y.sources : y.sources ? [y.sources] : [],
  };
  if (y.sommaire) f.sommaire = y.sommaire;
  if (y.parcours) f.parcours = y.parcours;
  if (y.parent) f.parent = String(y.parent).toUpperCase();
  if (y.chapitre) f.chapitre = parseInt(y.chapitre, 10) || 0;
  f.corps = m[2].trim();
  return f;
}
const blocs = (src) => src.split(/\n(?=---\r?\nid:)/).map((s) => s.trim()).filter(Boolean)
  .map((b) => parseFiche(b.startsWith("---") ? b : "---\n" + b)).filter(Boolean);

function versionOfficielle(appHtml) {
  const fr = appHtml.match(/const CORPUS=String\.raw`([\s\S]*?)`;/);
  const en = appHtml.match(/const CORPUS_EN=String\.raw`([\s\S]*?)`;/);
  if (!fr || !en) throw new Error("app/phenix.html : CORPUS ou CORPUS_EN introuvable");
  // L'empreinte suit le texte exact embarqué : même empreinte, même bibliothèque.
  const empreinte = crypto.createHash("sha256").update(fr[1] + "\n" + en[1]).digest("hex").slice(0, 12);
  const fiches = blocs(fr[1]);
  const trad = {};
  for (const t of blocs(en[1])) trad[t.id] = t;
  return {
    empreinte,
    fr: fiches.map((f) => ({ ...f, langue: "fr" })),
    // En anglais : la traduction quand elle existe, sinon l'original français, marqué comme tel.
    en: fiches.map((f) => {
      const t = trad[f.id];
      return t ? { ...f, titre: t.titre, tags: t.tags, sources: t.sources, corps: t.corps, langue: "en" } : { ...f, langue: "fr" };
    }),
  };
}

module.exports = { versionOfficielle };
