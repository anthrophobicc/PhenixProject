// Liste les sujets d'un portail Wikipédia et signale ceux que le corpus couvre déjà.
// Sert de matière première : chaque sujet retenu est réécrit en fiche Phenix (comprendre, agir, adapter), jamais copié.
// Usage : node outils/portail-wikipedia.js "Portail:Agriculture et agronomie" [fr|en]
//   → outils/portails/<portail>.json, et le tableau des sujets pas encore couverts
const fs = require("fs");
const path = require("path");

const [portail, langue = "fr"] = process.argv.slice(2);
if (!portail) { console.log('usage : node outils/portail-wikipedia.js "Portail:Nom" [fr|en]'); process.exit(1); }
const API = `https://${langue}.wikipedia.org/w/api.php`;
const ENTETES = { "User-Agent": "PhenixProject/1.0 (https://github.com/anthrophobicc/PhenixProject)" };
const RACINE = path.join(__dirname, "..");

const api = async (params) => {
  const url = API + "?" + new URLSearchParams({ format: "json", formatversion: "2", ...params });
  for (let essai = 0; essai < 3; essai++) {
    const r = await fetch(url, { headers: ENTETES });
    if (r.ok) return r.json();
    await new Promise((ok) => setTimeout(ok, 1500 * (essai + 1)));
  }
  throw new Error("Wikipédia ne répond pas : " + url);
};

// Titres et mots-clés du corpus, sans accents ni majuscules, pour repérer les sujets déjà traités.
const norm = (s) => s.toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/[^a-z0-9 ]/g, " ").replace(/\s+/g, " ").trim();
const deja = [];
for (const axe of fs.readdirSync(path.join(RACINE, "corpus"), { withFileTypes: true }).filter((e) => e.isDirectory())) {
  for (const f of fs.readdirSync(path.join(RACINE, "corpus", axe.name)).filter((f) => f.endsWith(".md"))) {
    const t = fs.readFileSync(path.join(RACINE, "corpus", axe.name, f), "utf8");
    const titre = (t.match(/^titre:\s*(.+)$/m) || [])[1] || "";
    const tags = ((t.match(/^tags:\s*\[(.*)\]$/m) || [])[1] || "").split(",");
    deja.push({ id: f.replace(/\.md$/, ""), mots: [titre, ...tags].map(norm).filter(Boolean) });
  }
}
const couvert = (titre) => {
  const n = norm(titre.replace(/\s*\(.*\)$/, ""));
  const f = deja.find((d) => d.mots.some((m) => m === n || (n.length > 4 && (m.includes(n) || (m.length > 5 && n.includes(m))))));
  return f ? f.id : null;
};

(async () => {
  // 1. Tous les liens vers des articles, sur la page du portail et ses sous-pages incluses.
  const p = await api({ action: "parse", page: portail, prop: "links", redirects: "1" });
  if (p.error) throw new Error(p.error.info);
  const titres = [...new Set(p.parse.links.filter((l) => l.ns === 0 && l.exists).map((l) => l.title))];
  // 2. Description courte et longueur de chaque article, par lots de 50.
  const infos = [];
  for (let i = 0; i < titres.length; i += 50) {
    const q = await api({ action: "query", titles: titres.slice(i, i + 50).join("|"), prop: "description|info", redirects: "1" });
    for (const pg of q.query.pages) if (!pg.missing) infos.push({ titre: pg.title, description: pg.description || "", taille: pg.length });
  }
  // 3. Les personnes, lieux, dates et listes ne font pas des fiches.
  const horsSujet = /\b(né|née|homme politique|femme politique|agronome|botaniste|ingénieur|écrivain|chanteu|acteur|actrice|commune|département|région|ville|pays|village|entreprise|société|organisation|institut|école|université|journal|revue|film|année|siècle|liste|ministère|personnalité|footballeur|rivière|fleuve)\b/i;
  const sujets = infos
    .filter((s) => !horsSujet.test(s.description) && !/^(Liste|Année|\d)/.test(s.titre))
    .map((s) => ({ ...s, couvert: couvert(s.titre) }))
    .sort((a, b) => b.taille - a.taille);
  const dossier = path.join(__dirname, "portails");
  fs.mkdirSync(dossier, { recursive: true });
  const f = path.join(dossier, norm(portail).replace(/ /g, "-") + ".json");
  fs.writeFileSync(f, JSON.stringify(sujets, null, 1));
  const libres = sujets.filter((s) => !s.couvert);
  console.log(`${portail} : ${titres.length} liens, ${sujets.length} sujets, ${sujets.length - libres.length} déjà couverts, ${libres.length} à écrire`);
  libres.forEach((s) => console.log(`${String(s.taille).padStart(7)}  ${s.titre}${s.description ? "  · " + s.description : ""}`));
  console.log("→", path.relative(RACINE, f));
})().catch((e) => { console.error(e.message); process.exit(1); });
