// Construit le site statique de Phenix dans site/ :
// - les pages principales en anglais, avec la traduction française embarquée dans i18n.js ;
// - une page par fiche, en français (corpus/) et en anglais quand la traduction existe (traductions/en/).
// Usage : node outils/construire-site.js
"use strict";
const fs = require("fs");
const path = require("path");

const RACINE = path.join(__dirname, "..");
const SITE = path.join(RACINE, "site");
const DEPOT = "https://github.com/anthrophobicc/PhenixProject";
// Les dernières fiches parues, montrées en tête de l'accueil (les plus récentes d'abord).
const NOUVELLES = ["URG-VEH-001", "SURV-REC-021", "URG-INC-002", "SURV-REC-020"];
// Adresse publique du site : les aperçus de lien (og:image) exigent une URL absolue.
const ADRESSE = "https://anthrophobicc.github.io/PhenixProject/";
const INSTA = "https://www.instagram.com/phenixprjct/";
const REDDIT = "https://www.reddit.com/r/PhenixProject/";
const EXE = "dl/Phenix_0.1.0_x64-setup.exe";
const EXE_SOURCE = path.join(RACINE, "src-tauri", "target", "release", "bundle", "nsis", "Phenix_0.1.0_x64-setup.exe");
// Tailles affichées sur le site, relues à chaque construction.
const mo = (octets) => { const v = (octets / 1e6).toFixed(1); return [v + " MB", v.replace(".", ",") + " Mo"]; };
const [APP_MB, APP_MO] = mo(fs.statSync(path.join(RACINE, "app", "phenix.html")).size);
const [EXE_MB, EXE_MO] = mo(fs.existsSync(EXE_SOURCE) ? fs.statSync(EXE_SOURCE).size : 1.7e6);

const esc = (s) => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;").replace(/'/g, "&#x27;");

/* ---------- Dictionnaire : chaque texte existe en anglais et en français ---------- */
const D = {};
// Un élément traduisible. Le texte écrit dans la page est celui de la langue de la page.
const tx = (tag, k, en, fr, attrs = "", lang = "en") => {
  D[k] = [en, fr];
  return `<${tag}${attrs ? " " + attrs : ""} data-i18n="${k}">${lang === "fr" ? fr : en}</${tag}>`;
};
const ph = (k, en, fr) => {
  D[k] = [en, fr];
  return `placeholder="${esc(en).replace(/\n/g, "&#10;")}" data-i18n-ph="${k}"`;
};

/* ---------- Lecture des fiches ---------- */
function lireFiches(dossier) {
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
        if (i < 0) continue;
        const k = l.slice(0, i).trim();
        let v = l.slice(i + 1).trim();
        if (v.startsWith("[")) {
          try { v = JSON.parse(v); } catch { v = v.slice(1, -1).split(",").map((s) => s.trim().replace(/^"|"$/g, "")).filter(Boolean); }
        }
        meta[k] = v;
      }
      if (meta.id) out[meta.id] = { meta, corps: m[2].trim() };
    }
  }
  return out;
}
const FR_F = lireFiches(path.join(RACINE, "corpus"));
const EN_F = lireFiches(path.join(RACINE, "traductions", "en"));

// Les fiches du site : la sélection historique, plus toutes celles qui existent en anglais.
const BASE = ["URG-HYPO-001", "URG-HEMO-001", "URG-EAU-001", "SURV-ORI-001", "SURV-FEU-001", "SURV-ABRI-001",
  "SURV-PLUIE-001", "SIG-COM-001", "TEC-MOTH-001", "TEC-MOT-001", "TEC-ENE-001", "MEM-AGR-001", "URG-BRUL-001",
  "TEC-CONS-001", "SURV-TROC-001", "MEM-EFF-001"];
const titre = (id, lang) => (lang === "en" && EN_F[id] ? EN_F[id].meta.titre : FR_F[id] ? FR_F[id].meta.titre : id);
const IDS = [...new Set([...BASE, ...Object.keys(EN_F)])].filter((id) => FR_F[id]);
const flash = (id) => (FR_F[id].meta.priorite === "flash" ? 1 : 0);
IDS.sort((a, b) => flash(b) - flash(a) || Number(FR_F[b].meta.axe) - Number(FR_F[a].meta.axe) || titre(a, "fr").localeCompare(titre(b, "fr"), "fr"));
const fichier = (id, lang) => `fiche-${id.toLowerCase()}${lang === "en" ? "-en" : ""}.html`;

const AXES = { 1: ["Memory", "La Mémoire"], 2: ["Technique", "La Technique"], 3: ["Survival", "La Survie"] };
const CAT_EN = {
  "Protocoles d'urgence": "Emergency protocols", "Feu, Eau et Ressources": "Fire, water and resources",
  "Mouvement et Discrétion": "Movement and stealth", "Signaux et Communications": "Signals and communications",
  "Mécanique et Transport": "Mechanics and transport", "Énergie et Électricité": "Energy and electricity",
  "Les révolutions agricoles": "The agricultural revolutions", "Secourisme": "First aid",
  "Alimentation et Conservation": "Food and preservation", "Psychologie Sociale et Troc": "Social psychology and barter",
  "Ce qui se répète": "What repeats itself", "Récupération": "Salvage",
};
const BALS = {
  temps: [["Time", "Temps"], { Flash: ["Flash", "Flash"], Court: ["Short", "Court"], Long: ["Long", "Long"] }],
  contexte: [["Context", "Contexte"], { 1: ["Alone", "Seul"], 2: ["Two people", "À deux"], "2+": ["Group", "En groupe"] }],
  risque: [["Risk", "Risque"], { Discret: ["Discreet", "Discret"], "Exposé": ["Exposed", "Exposé"] }],
  materiel: [["Gear", "Matériel"], { Rien: ["None", "Aucun"], Aucun: ["None", "Aucun"], "Récupération": ["Salvage", "Récupération"], Technique: ["Technical", "Technique"] }],
};

/* ---------- Markdown des fiches ---------- */
function inline(s, lien) {
  const codes = [], imgs = [], liens = [], glos = [];
  s = s.replace(/`([^`]+)`/g, (_, c) => (codes.push(c), `\u0000${codes.length - 1}\u0000`));
  // Glossaire : {{mot|définition}} devient un mot souligné qui montre sa définition au survol ou au toucher.
  s = s.replace(/\{\{([^|}]+)\|([^}]+)\}\}/g, (_, mot, def) => (glos.push([mot, def]), `\u0003${glos.length - 1}\u0003`));
  s = s.replace(/!\[([^\]]*)\]\(([^)\s]+)\)/g, (_, alt, src) => (imgs.push([alt, src]), `\u0001${imgs.length - 1}\u0001`));
  s = s.replace(/\[\[([A-Za-z0-9-]+)\]\]/g, (_, id) => (liens.push(id), `\u0002${liens.length - 1}\u0002`));
  s = esc(s);
  s = s.replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
  s = s.replace(/(^|[^*\w])\*([^*\n]+)\*(?!\w)/g, "$1<em>$2</em>");
  s = s.replace(/\[([^\]]+)\]\((https?:[^)\s]+)\)/g, '<a href="$2" rel="noopener">$1</a>');
  s = s.replace(/\u0002(\d+)\u0002/g, (_, i) => lien(liens[i]));
  s = s.replace(/\u0001(\d+)\u0001/g, (_, i) => `<img src="${imgs[i][1].replace(/"/g, "%22")}" alt="${esc(imgs[i][0])}" loading="lazy">`);
  s = s.replace(/\u0000(\d+)\u0000/g, (_, i) => `<code>${esc(codes[i])}</code>`);
  s = s.replace(/\u0003(\d+)\u0003/g, (_, i) => `<span class="glo" tabindex="0">${esc(glos[i][0])}<span class="glob">${esc(glos[i][1])}</span></span>`);
  return s;
}

function rendre(corps, lien) {
  const L = corps.split("\n");
  const out = [];
  let para = [];
  const flush = () => { if (para.length) { out.push(`<p>${inline(para.join(" "), lien)}</p>`); para = []; } };
  let i = 0;
  while (i < L.length) {
    const t = L[i].trim();
    let m;
    if (!t) { flush(); i++; continue; }
    if ((m = t.match(/^::(.+)::$/))) { flush(); out.push(`<p class="lede-f">${inline(m[1], lien)}</p>`); i++; continue; }
    if ((m = t.match(/^##\s+(.+)$/))) {
      flush();
      const h = m[1].trim();
      const mot = h.split(/\s+[—–-]\s+/)[0].toUpperCase();
      const cls = /^(AGIR|ACT)$/.test(mot) ? "s-agir" : /^(COMPRENDRE|UNDERSTAND)$/.test(mot) ? "s-comp" : /^(ADAPTER|ADAPT)$/.test(mot) ? "s-adapt" : "";
      out.push(cls ? `<h2 class="step ${cls}">${inline(h, lien)}</h2>` : `<h2>${inline(h, lien)}</h2>`);
      i++; continue;
    }
    if ((m = t.match(/^###\s+(.+)$/))) { flush(); out.push(`<h3>${inline(m[1], lien)}</h3>`); i++; continue; }
    if (t.startsWith("|")) {
      flush();
      const rows = [];
      while (i < L.length && L[i].trim().startsWith("|")) rows.push(L[i++].trim());
      const cells = (r) => r.replace(/^\||\|$/g, "").split("|").map((c) => c.trim());
      let tete = null, corpsT = rows;
      if (rows.length > 1 && /^\|?[\s:|-]+$/.test(rows[1])) { tete = cells(rows[0]); corpsT = rows.slice(2); }
      out.push(`<table>${tete ? `<thead><tr>${tete.map((c) => `<th>${inline(c, lien)}</th>`).join("")}</tr></thead>` : ""}<tbody>${corpsT.map((r) => `<tr>${cells(r).map((c) => `<td>${inline(c, lien)}</td>`).join("")}</tr>`).join("")}</tbody></table>`);
      continue;
    }
    if (/^(\d+[.)]|[-*])\s+/.test(t)) {
      flush();
      const ordonnee = /^\d/.test(t);
      const motif = ordonnee ? /^\d+[.)]\s+(.*)$/ : /^[-*]\s+(.*)$/;
      const items = [];
      while (i < L.length) {
        const u = L[i], ut = u.trim();
        if (!ut) {
          let j = i + 1;
          while (j < L.length && !L[j].trim()) j++;
          if (j < L.length && motif.test(L[j].trim()) && !/^\s/.test(L[j])) { i = j; continue; }
          break;
        }
        const mm = ut.match(motif);
        if (mm && !/^\s{2,}/.test(u)) items.push(mm[1]);
        // Ligne indentée : suite de l'élément ou sous-liste, aplatie dans l'élément courant.
        else if (items.length && /^\s/.test(u)) items[items.length - 1] += " " + ut.replace(/^([-*]|\d+[.)])\s+/, "");
        else break;
        i++;
      }
      const tag = ordonnee ? "ol" : "ul";
      out.push(`<${tag}>${items.map((x) => `<li>${inline(x, lien)}</li>`).join("")}</${tag}>`);
      continue;
    }
    if (t.startsWith(">")) {
      flush();
      const q = [];
      while (i < L.length && L[i].trim().startsWith(">")) q.push(L[i++].trim().replace(/^>\s?/, ""));
      out.push(`<blockquote>${inline(q.join(" "), lien)}</blockquote>`);
      continue;
    }
    if (t.startsWith("![")) { flush(); out.push(`<p>${inline(t, lien)}</p>`); i++; continue; }
    para.push(t);
    i++;
  }
  flush();
  return out.join("\n");
}

const lienPour = (lang) => (id) => {
  const surSite = IDS.includes(id);
  const nom = esc(titre(id, lang));
  if (!surSite) return `<span title="${id}">${nom}</span>`;
  const cible = lang === "en" && EN_F[id] ? fichier(id, "en") : fichier(id, "fr");
  return `<a href="${cible}">${nom}</a>`;
};

/* ---------- Habillage commun ---------- */
function nav(lang) {
  return `<header class="nav">
  <a class="brand" href="index.html"><span class="mark"></span><span>PHENIX</span></a>
  <nav>
    ${tx("a", "nav.explore", "Explore", "Explorer", 'href="explore.html"', lang)}
    ${tx("a", "nav.devices", "Devices", "Appareils", 'href="devices.html"', lang)}
    ${tx("a", "nav.contribute", "Phenix Lab", "Phenix Lab", 'href="lab.html"', lang)}
    ${tx("a", "nav.download", "Download", "Télécharger", 'href="download.html"', lang)}
    <button class="lang" type="button" aria-label="Language">${lang === "fr" ? "EN" : "FR"}</button>
    <span class="themes" role="group" aria-label="Theme">
      <button type="button" data-theme-set="phosphore" title="Phosphor" aria-label="Phosphor theme" style="--c1:#040806;--c2:#39FF6A"></button>
      <button type="button" data-theme-set="ambre" title="Amber" aria-label="Amber theme" style="--c1:#0A0703;--c2:#FFB000"></button>
      <button type="button" data-theme-set="papier" title="Paper" aria-label="Paper theme" style="--c1:#F4F2EC;--c2:#2F6E2A"></button>
    </span>
  </nav>
</header>`;
}
function pied(lang) {
  return `<footer>
  <div class="wrap">
    ${tx("p", "foot.motto", "<strong>Phenix</strong> — knowledge is your only immunity.", "<strong>Phenix</strong> — le savoir est votre seule immunité.", "", lang)}
    <p class="small">
      ${tx("a", "nav.explore", "Explore", "Explorer", 'href="explore.html"', lang)} ·
      ${tx("a", "nav.devices", "Devices", "Appareils", 'href="devices.html"', lang)} ·
      ${tx("a", "nav.contribute", "Phenix Lab", "Phenix Lab", 'href="lab.html"', lang)} ·
      ${tx("a", "nav.download", "Download", "Télécharger", 'href="download.html"', lang)} ·
      ${tx("a", "nav.support", "Support", "Soutenir", 'href="soutenir.html"', lang)} ·
      <a href="${INSTA}" rel="noopener">Instagram</a> ·
      <a href="${REDDIT}" rel="noopener">Reddit</a> ·
      <a href="${DEPOT}" rel="noopener">GitHub</a>
    </p>
    ${tx("p", "foot.licence", "Software under the MIT licence · sheets under CC BY-SA 4.0", "Logiciel sous licence MIT · fiches sous licence CC BY-SA 4.0", 'class="small dim"', lang)}
  </div>
</footer>`;
}
function page({ lang = "en", alt = "", fiche = false, titreHtml, desc = "", css = [], corps, scripts = "" }) {
  return `<!DOCTYPE html>
<html lang="${lang}" data-page-lang="${lang}"${alt ? ` data-alt="${alt}"` : ""}${fiche ? ' data-kind="fiche"' : ""}>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
${titreHtml}
<meta name="description" content="${esc(desc)}">
<meta name="theme-color" content="#040806">
<script>try{var t=localStorage.getItem("phenix-theme");if(t&&t!=="phosphore")document.documentElement.setAttribute("data-theme",t)}catch(e){}</script>
<meta property="og:title" content="Phenix">
<meta property="og:description" content="${esc(desc)}">
<meta property="og:type" content="website">
<meta property="og:image" content="${ADRESSE}img/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="logo.png">
<link rel="manifest" href="manifest.webmanifest">
<link rel="apple-touch-icon" href="img/icone-180.png">
<link rel="stylesheet" href="style.css">
${css.map((c) => `<link rel="stylesheet" href="${c}">`).join("\n")}
</head>
<body>
${nav(lang)}
${corps}
${pied(lang)}
<script src="i18n.js"></script>
${scripts}
</body>
</html>
`;
}

/* ---------- Accueil ---------- */
function accueil() {
  const n = Object.keys(FR_F).length, nEn = Object.keys(EN_F).length;
  const corps = `<main>
  <section class="hero">
    <div class="mark big"></div>
    ${tx("p", "home.kicker", "Phenix Project · free · open · offline", "Phenix Project · libre · ouvert · hors ligne", 'class="kicker"')}
    <h1>Knowledge is the last thing we should lose.<span class="cursor" aria-hidden="true"></span></h1>
    ${tx("p", "home.lede", "A free, participative, open library of knowledge. It works offline, and it's built to run on ultra-resilient devices.", "Une bibliothèque du savoir libre, participative et ouverte. Elle fonctionne hors ligne, et elle est pensée pour tourner sur des appareils ultra-résistants.", 'class="lede"')}
    <div class="actions">
      <a class="act primary wide" href="phenix.html">${tx("b", "home.a0", "Open the app", "Ouvrir l'application")}${tx("span", "home.a0s", "On your phone or your computer, right in the browser. Add it to your home screen and it works without internet.", "Sur téléphone ou sur ordinateur, directement dans le navigateur. Ajoutez-la à l'écran d'accueil et elle marche sans internet.")}</a>
      <a class="act" href="explore.html">${tx("b", "home.a1", "Explore", "Explorer")}${tx("span", "home.a1s", "Read the sheets, nothing to install", "Lire les fiches sans rien installer")}</a>
      <a class="act" href="lab.html">${tx("b", "home.a2", "Phenix Lab", "Phenix Lab")}${tx("span", "home.a2s", "Suggest, vote and comment on the next sheets", "Proposez, votez et commentez les prochaines fiches")}</a>
      <a class="act" href="download.html">${tx("b", "home.a3", "Download", "Télécharger")}${tx("span", "home.a3s", "Phenix Base, the full app, offline", "Phenix Base, l'application complète, hors ligne")}</a>
      <a class="act" href="soutenir.html">${tx("b", "home.a4", "Support", "Soutenir")}${tx("span", "home.a4s", "Help the project last", "Aider le projet à durer")}</a>
    </div>
    ${tx("p", "home.phone", 'On a phone? <a href="download.html#phone">Here is how to install it</a>, no store and no account.', 'Sur téléphone ? <a href="download.html#phone">Voici comment l\'installer</a>, sans store ni compte.', 'class="small dim" style="margin:16px 0 0"')}
  </section>

  <section class="band why">
    <div class="wrap">
      ${tx("h2", "home.why", "Why", "Pourquoi")}
      ${tx("p", "home.why1", "In 2024, the internet was cut 296 times, in 54 countries. Millions of people were left alone with what they already knew. Often, it wasn't enough.", "En 2024, internet a été coupé 296 fois, dans 54 pays. Des millions de personnes livrées à leurs connaissances, souvent insuffisantes.")}
      ${tx("p", "home.why2", "The day access to knowledge is restricted, or erased by a global outage, you won't just be disconnected. You'll be blind.", "Le jour où l'accès à la connaissance sera restreint ou effacé par une panne globale, vous ne serez pas seulement déconnectés. Vous serez aveugles.", 'class="big"')}
      ${tx("p", "home.why3", "Medicine, local maps, technical know-how, history. Think of every question you ever asked the internet. How would you have done without it?", "Médicaments, cartes locales, indications techniques ou histoire. Chaque fois que vous avez posé une question à internet : comment auriez-vous fait sans ?")}
      ${tx("p", "home.why4", "<strong>Participate now, simply. Write down what you know, for everyone.</strong>", "<strong>Participez maintenant, simplement. Inscrivez le savoir pour tout le monde.</strong>")}
      ${tx("p", "home.whysrc", "Source: Access Now, #KeepItOn report on internet shutdowns, 2024.", "Source : Access Now, rapport #KeepItOn sur les coupures d'internet, 2024.", 'class="src"')}
    </div>
  </section>

  <section class="band alt">
    <div class="wrap">
      ${tx("h2", "home.diff", "What makes Phenix different", "Ce qui change avec Phenix")}
      <div class="three">
        <div><div class="num">1</div>${tx("h3", "home.d1", "Open", "Ouvert")}${tx("p", "home.d1p", "Anyone can write a sheet, on any subject. Nobody to ask for permission to get started.", "Tout le monde peut écrire une fiche, sur n'importe quel sujet. Personne à qui demander la permission pour commencer.")}</div>
        <div><div class="num">2</div>${tx("h3", "home.d2", "Participative", "Participatif")}${tx("p", "home.d2p", "Propose, correct, vote, discuss. Experts settle the hard topics, everyone takes care of the rest.", "Proposer, corriger, voter, débattre. Les experts tranchent les sujets pointus, tout le monde s'occupe du reste.")}</div>
        <div><div class="num">3</div>${tx("h3", "home.d3", "Practical", "Pratique")}${tx("p", "home.d3p", "Knowing how an engine works is nice. Knowing how to fix it is better. Every sheet starts with what to do.", "Savoir comment marche un moteur, c'est bien. Savoir le réparer, c'est mieux. Chaque fiche commence par quoi faire.")}</div>
      </div>
      <div class="stats">
        <div class="stat"><b>${n}</b>${tx("span", "home.s1", "sheets written", "fiches écrites")}</div>
        <div class="stat"><b>${nEn}</b>${tx("span", "home.s2", "already in English", "déjà en anglais")}</div>
        <div class="stat">${tx("b", "home.s3v", APP_MB, APP_MO)}${tx("span", "home.s3", "the whole app", "toute l'application")}</div>
        <div class="stat"><b>0</b>${tx("span", "home.s4", "servers needed to read", "serveur pour lire")}</div>
      </div>
    </div>
  </section>

  <section class="band">
    <div class="wrap">
      ${tx("h2", "home.new", "New sheets", "Nouvelles fiches")}
      <div class="list" style="margin-top:14px">${NOUVELLES.filter((id) => FR_F[id]).map((id) => {
        const f = FR_F[id].meta, hrefEn = EN_F[id] ? fichier(id, "en") : fichier(id, "fr");
        D["t." + id] = [esc(titre(id, "en")), esc(f.titre)];
        D["m." + id] = [esc(`Axis ${f.axe} · ${CAT_EN[f.categorie] || f.categorie}`), esc(`Axe ${f.axe} · ${f.categorie}`)];
        return `<a class="item" href="${hrefEn}" data-href-en="${hrefEn}" data-href-fr="${fichier(id, "fr")}"><h3 data-i18n="t.${id}">${D["t." + id][0]}</h3><div class="meta" data-i18n="m.${id}">${D["m." + id][0]}</div></a>`;
      }).join("")}</div>
    </div>
  </section>

  <section class="band">
    <div class="wrap">
      ${tx("h2", "home.dev", "The devices", "Les appareils")}
      <div class="appareil" style="margin-top:6px">
        <div class="visuel"><img src="img/phenix-001.svg" alt="Concept render of Phenix 001, a pocket reader with an e-ink screen"></div>
        <div>
          ${tx("span", "dev.badge", "Prototype · in design", "Prototype · en conception", 'class="concept"')}
          ${tx("p", "home.devp", "Phenix 001 is a pocket reader the size of a Flipper Zero, with an e-ink screen you can read in full sun. Phenix 002 adds a color screen, a keyboard and a long-range radio. Both are built only from common parts, open with a screwdriver, and are meant to cost little enough for every town hall.", "Le Phenix 001 est un lecteur de poche de la taille d'un Flipper Zero, avec un écran à encre électronique lisible en plein soleil. Le Phenix 002 ajoute un écran couleur, un clavier et une radio longue portée. Les deux n'utilisent que des pièces courantes, s'ouvrent au tournevis, et doivent coûter assez peu pour que chaque mairie en ait un.")}
          <p>${tx("a", "home.devb", "See the devices", "Voir les appareils", 'class="btn primary" href="devices.html"')}</p>
        </div>
      </div>
    </div>
  </section>

  <section class="band alt">
    <div class="wrap">
      ${tx("h2", "home.lib", "The library", "La bibliothèque")}
      ${tx("p", "home.libp", "Every sheet is a standalone text file. The software indexes them, links them and filters them, it never locks them in. <strong>If Phenix disappears, the sheets stay readable.</strong>", "Chaque fiche est un fichier texte autonome. Le logiciel les indexe, les relie et les filtre, il ne les enferme pas. <strong>Si Phenix disparaît, les fiches restent lisibles.</strong>")}
      <div class="three">
        <div><div class="num">1</div>${tx("h3", "axe.1", "Memory", "La Mémoire")}${tx("p", "home.x1", "What happened, and what it teaches us.", "Ce qui s'est passé et ce que ça nous apprend.")}</div>
        <div><div class="num">2</div>${tx("h3", "axe.2", "Technique", "La Technique")}${tx("p", "home.x2", "How things work, and the technical data that goes with them.", "Comment les choses fonctionnent, et les données techniques qui vont avec.")}</div>
        <div><div class="num">3</div>${tx("h3", "axe.3", "Survival", "La Survie")}${tx("p", "home.x3", "What to do, right now, when things go wrong.", "Quoi faire, maintenant, en situation dégradée.")}</div>
      </div>
      ${tx("p", "home.note", "Phenix is not just a survival database. A sheet can be about an engine, a plant, a craft, a period of history, a cooking or building method. What matters is quality and structure, not the subject.", "Phenix n'est pas une base de survie. Une fiche peut porter sur un moteur, une plante, une technique manuelle, une période historique, une méthode de cuisine ou d'architecture. Ce qui compte est la qualité et la structure, pas le sujet.", 'class="note"')}
    </div>
  </section>

  <section class="band">
    <div class="wrap">
      ${tx("h2", "home.two", "Two structures, one reason", "Deux structures, une raison")}
      <div class="two">
        <div class="card">
          ${tx("div", "tag.urg", "Emergency", "Urgence", 'class="tag urg"')}
          ${tx("p", "home.seq1", "Act → Adapt → Understand", "Agir → Adapter → Comprendre", 'class="seq"')}
          ${tx("p", "home.seq1p", "The reader has no time. They act first, and understand once things settle down.", "Celui qui lit n'a pas le temps. Il exécute d'abord, il comprend pendant que la situation se stabilise.")}
        </div>
        <div class="card">
          ${tx("div", "tag.sav", "Knowledge", "Savoir", 'class="tag sav"')}
          ${tx("p", "home.seq2", "Act → Understand → Adapt", "Agir → Comprendre → Adapter", 'class="seq"')}
          ${tx("p", "home.seq2p", "The right move comes from the mechanism. Learned the other way round, it breaks outside the case described.", "Le geste juste découle du mécanisme. Appris à l'envers, il ne tient pas hors du cas décrit.")}
        </div>
      </div>
    </div>
  </section>

  <section class="band">
    <div class="wrap">
      ${tx("h2", "home.eco", "The ecosystem", "L'écosystème")}
      <div class="eco">
        <div><b>Phenix Base</b>${tx("p", "home.e1", `The app. One ${APP_MB} file with every sheet inside, readable offline in any browser, even on an old phone or laptop.`, `L'application. Un fichier de ${APP_MO} avec toutes les fiches dedans, lisible hors ligne dans n'importe quel navigateur, même sur un vieux téléphone ou un vieil ordinateur.`)}${tx("span", "st.on", "Available", "Disponible", 'class="state on"')}</div>
        <div><b>Phenix HQ</b>${tx("p", "home.e2", "The community space. Write a sheet in minutes, vote, discuss, translate, correct.", "L'espace communautaire. Écrire une fiche en quelques minutes, voter, débattre, traduire, corriger.")}${tx("span", "st.soon", "Coming", "Bientôt", 'class="state soon"')}</div>
        <div><b><a href="devices.html" style="color:inherit">Phenix 001 · 002</a></b>${tx("p", "home.e3", "Our own devices. A pocket e-ink reader, and a rugged terminal with a keyboard and long-range radio.", "Nos propres appareils. Un lecteur de poche à encre électronique, et un terminal robuste avec clavier et radio longue portée.")}${tx("span", "st.lab", "In design", "En conception", 'class="state lab"')}</div>
        <div>${tx("b", "home.e4t", "Community", "Communauté")}${tx("p", "home.e4", `Every country and every region gets its own version. And so do you. <a href="${INSTA}" rel="noopener">Instagram</a> · <a href="${REDDIT}" rel="noopener">Reddit</a> · <a href="${DEPOT}" rel="noopener">GitHub</a>`, `Chaque pays et chaque région a sa version. Et vous aussi. <a href="${INSTA}" rel="noopener">Instagram</a> · <a href="${REDDIT}" rel="noopener">Reddit</a> · <a href="${DEPOT}" rel="noopener">GitHub</a>`)}${tx("span", "st.open", "Open", "Ouvert", 'class="state on"')}</div>
      </div>
    </div>
  </section>

  <section class="band">
    <div class="wrap center">
      ${tx("h2", "home.start", "Start now", "Commencez maintenant")}
      ${tx("p", "home.startp", "Nothing to install to read.", "Aucune installation pour lire.")}
      <p style="margin-top:22px">
        ${tx("a", "home.b1", "Read a sheet", "Lire une fiche", 'class="btn primary" href="explore.html"')}
        ${tx("a", "home.b2", "Download Phenix Base", "Télécharger Phenix Base", 'class="btn" href="download.html"')}
      </p>
    </div>
  </section>
</main>`;
  return page({
    titreHtml: tx("title", "home.title", "Phenix — Knowledge is the last thing we should lose", "Phenix — Le savoir est la dernière chose à perdre"),
    desc: "A free, participative, open library of knowledge that works offline.",
    corps,
  });
}

/* ---------- Explorer ---------- */
function explorer() {
  const items = IDS.map((id) => {
    const f = FR_F[id].meta, en = EN_F[id];
    const axe = String(f.axe);
    D["t." + id] = [esc(titre(id, "en")), esc(f.titre)];
    D["m." + id] = [esc(`Axis ${axe} · ${CAT_EN[f.categorie] || f.categorie}`), esc(`Axe ${axe} · ${f.categorie}`)];
    const hrefEn = en ? fichier(id, "en") : fichier(id, "fr");
    return `<a class="item" data-axe="${axe}" data-prio="${f.priorite}" href="${hrefEn}" data-href-en="${hrefEn}" data-href-fr="${fichier(id, "fr")}">
  <h3 data-i18n="t.${id}">${D["t." + id][0]}</h3>
  <div class="meta" data-i18n="m.${id}">${D["m." + id][0]}</div>
  <div class="tags" style="margin-top:9px">${f.priorite === "flash" ? tx("span", "tag.urg", "Emergency", "Urgence", 'class="tag urg"') : ""}${tx("span", "tag.off", "Official", "Officielle", 'class="tag off"')}${en ? "" : tx("span", "tag.fronly", "French only", "Français", 'class="tag fr" data-only="en"')}</div></a>`;
  }).join("");
  const corps = `<main class="wrap" style="padding-top:34px;padding-bottom:60px">
  ${tx("h1", "exp.h1", "Explore the library", "Explorer le corpus", 'style="font-size:30px;margin:0 0 10px;color:var(--acc);text-shadow:var(--glow)"')}
  ${tx("p", "exp.lede", `${IDS.length} sheets you can read right here, nothing to install. The app holds all ${Object.keys(FR_F).length}.`, `${IDS.length} fiches lisibles ici, sans rien installer. L'application contient les ${Object.keys(FR_F).length}.`, 'class="lede" style="font-size:17px;margin:0"')}
  <div class="filters" id="filters">
    ${tx("button", "exp.all", "All", "Tout", 'class="on" data-f="tout"')}
    ${tx("button", "exp.urg", "Emergencies", "Urgences", 'data-f="urgence"')}
    ${tx("button", "exp.x1", "Axis 1 — Memory", "Axe 1 — Mémoire", 'data-f="1"')}
    ${tx("button", "exp.x2", "Axis 2 — Technique", "Axe 2 — Technique", 'data-f="2"')}
    ${tx("button", "exp.x3", "Axis 3 — Survival", "Axe 3 — Survie", 'data-f="3"')}
  </div>
  <div class="list" id="list">${items}</div>

  <div class="band" style="margin-top:44px">
    ${tx("h2", "exp.status", "Statuses", "Statuts")}
    <p>${tx("span", "tag.off", "Official", "Officielle", 'class="tag off"')} ${tx("span", "exp.st1", "Reviewed and added to the Phenix library. Versioned, protected against overwriting.", "Relue et intégrée au corpus Phenix. Versionnée, protégée contre l'écrasement.")}</p>
    <p>${tx("span", "tag.ver", "Verified", "Vérifiée", 'class="tag ver"')} ${tx("span", "exp.st2", "Community contribution whose sources have been checked.", "Contribution communautaire dont les sources ont été contrôlées.")}</p>
    <p>${tx("span", "tag.com", "Community", "Communauté", 'class="tag com"')} ${tx("span", "exp.st3", "Published contribution, not yet verified. Readable, and flagged as such.", "Contribution publiée mais non vérifiée. Lisible, signalée comme telle.")}</p>
    ${tx("p", "exp.stnote", "The number of reads or votes is never proof of accuracy. A sheet only becomes official after an explicit review.", "Le nombre de lectures ou de votes n'est jamais une preuve d'exactitude. Une fiche ne devient officielle que par une validation explicite.", 'class="note"')}
  </div>

  <div class="band">
    ${tx("h2", "exp.more", "Go further", "Aller plus loin")}
    ${tx("p", "exp.morep", "The app holds the whole library, offline maps, the bookshelf and the modules, with no connection.", "L'application contient l'intégralité du corpus, les cartes hors ligne, la bibliothèque et les modules, sans connexion.")}
    <p>${tx("a", "home.b2", "Download Phenix Base", "Télécharger Phenix Base", 'class="btn primary" href="download.html"')}</p>
  </div>
</main>`;
  const script = `<script>
const B=document.querySelectorAll("#filters button");
const I=document.querySelectorAll("#list .item");
B.forEach(b=>b.onclick=()=>{
  B.forEach(x=>x.classList.toggle("on",x===b));
  const f=b.dataset.f;
  I.forEach(i=>{
    const ok = f==="tout" || (f==="urgence" ? i.dataset.prio==="flash" : i.dataset.axe===f);
    i.style.display = ok ? "" : "none";
  });
});
</script>`;
  return page({ titreHtml: tx("title", "exp.title", "Explore — Phenix", "Explorer — Phenix"), desc: "Read Phenix sheets online, nothing to install.", corps, scripts: script });
}

/* ---------- Télécharger ---------- */
function telecharger() {
  const corps = `<main class="wrap" style="padding-top:34px;padding-bottom:60px">
  ${tx("h1", "dl.h1", "Download Phenix Base", "Télécharger Phenix Base", 'style="font-size:30px;margin:0 0 10px;color:var(--acc);text-shadow:var(--glow)"')}
  ${tx("p", "dl.lede", "One file. No install. Works offline.", "Un seul fichier. Aucune installation. Il fonctionne hors ligne.", 'class="lede" style="font-size:17px;margin:0"')}

  <div class="act primary" id="phone" style="margin-top:26px">
    ${tx("b", "dl.ph", "On your phone", "Sur votre téléphone")}
    ${tx("span", "dl.phs", "Open the app in your browser, then add it to your home screen. It gets its own icon and keeps working without internet.", "Ouvrez l'application dans votre navigateur, puis ajoutez-la à l'écran d'accueil. Elle a sa propre icône et continue de marcher sans internet.")}
    <p style="margin-top:14px">${tx("a", "dl.phbtn", "Open the app", "Ouvrir l'application", 'class="btn primary" href="phenix.html"')}</p>
    <ol class="etapes">
      ${tx("li", "dl.ph1", "<strong>iPhone</strong>: open it in Safari, tap the Share button, then <em>Add to Home Screen</em>.", "<strong>iPhone</strong> : ouvrez-la dans Safari, touchez le bouton Partager, puis <em>Sur l'écran d'accueil</em>.")}
      ${tx("li", "dl.ph2", "<strong>Android</strong>: open it in Chrome, tap the ⋮ menu, then <em>Install app</em> or <em>Add to Home screen</em>.", "<strong>Android</strong> : ouvrez-la dans Chrome, touchez le menu ⋮, puis <em>Installer l'application</em> ou <em>Ajouter à l'écran d'accueil</em>.")}
      ${tx("li", "dl.ph3", "Open it once with a connection. After that, the sheets, your own sheets and your markers work offline.", "Ouvrez-la une fois avec une connexion. Ensuite, les fiches, les vôtres et vos repères marchent hors ligne.")}
    </ol>
  </div>

  <div class="act" style="margin-top:12px">
    ${tx("b", "dl.card", "Phenix Base — the full app", "Phenix Base — l'application complète")}
    ${tx("span", "dl.cards", "One HTML file with every sheet inside. Download it, open it, that's it.", "Un fichier HTML avec toutes les fiches dedans. Téléchargez-le, ouvrez-le, c'est tout.")}
    <p style="margin-top:14px">${tx("a", "dl.btn", `Download the app (${APP_MB})`, `Télécharger l'application (${APP_MO})`, 'class="btn primary" href="phenix.html" download')}</p>
  </div>

  <div class="band" style="border:none;padding:34px 0 0">
    ${tx("h2", "dl.how", "How it works", "Comment ça marche")}
    <ol>
      ${tx("li", "dl.h1s", `<strong>Download the file.</strong> About ${APP_MB}, every sheet included.`, `<strong>Téléchargez le fichier.</strong> Environ ${APP_MO}, avec toutes les fiches dedans.`)}
      ${tx("li", "dl.h2s", "<strong>Open it</strong> with a double click. It opens in your browser.", "<strong>Ouvrez-le</strong> en double-cliquant dessus. Il s'ouvre dans votre navigateur.")}
      ${tx("li", "dl.h3s", "<strong>Use it.</strong> The sheets need no connection.", "<strong>Utilisez-le.</strong> Les fiches ne demandent aucune connexion.")}
    </ol>

    ${tx("h2", "dl.data", "Your data", "Vos données")}
    ${tx("p", "dl.data1", "Everything stays on your device. Nothing is sent anywhere, there's no account and no server. Your sheets, maps and markers are saved automatically and are still there when you reopen it.", "Tout reste sur votre appareil. Rien n'est envoyé nulle part, il n'y a ni compte ni serveur. Vos fiches, cartes et repères sont enregistrés automatiquement et retrouvés à la réouverture.")}
    ${tx("p", "dl.data2", "<strong>Export your backup regularly</strong> from Settings. That's how you move from one device to another, and how you lose nothing if you clear your browser data.", "<strong>Exportez régulièrement votre sauvegarde</strong> depuis Paramètres. C'est ce qui vous permet de passer d'un appareil à l'autre et de ne rien perdre si vous effacez les données de votre navigateur.")}

    ${tx("h2", "dl.net", "What needs a connection", "Ce qui a besoin d'une connexion")}
    ${tx("p", "dl.netp", "Only loading a new map area and searching for a place. Once an area is saved, it works offline. Everything else, sheets, writing, bookshelf, modules, works without a network.", "Uniquement le chargement d'une nouvelle zone de carte et la recherche d'un lieu. Une fois une zone enregistrée, elle se consulte hors ligne. Tout le reste, fiches, création, bibliothèque, modules, fonctionne sans réseau.")}

    ${tx("h2", "dl.win", "Windows version", "Version pour Windows")}
    ${tx("p", "dl.winp", `The Windows version is available: a ${EXE_MB} installer. macOS and Linux are on the way. <strong>The HTML file stays the main app</strong>: it already does everything, and needs no install.`, `La version Windows est disponible : un installateur de ${EXE_MO}. macOS et Linux sont en préparation. <strong>Le fichier HTML reste l'application principale</strong> : il fait déjà tout, et il ne s'installe pas.`)}
    ${tx("p", "dl.winwarn", "The app isn't signed yet, so Windows may warn you. Click <em>More info</em>, then <em>Run anyway</em>.", "L'application n'est pas encore signée : Windows peut afficher un avertissement. Cliquez sur <em>Informations complémentaires</em>, puis <em>Exécuter quand même</em>.", 'class="small"')}
    <p>${tx("a", "dl.winbtn", "Download for Windows", "Télécharger pour Windows", `class="btn" href="${EXE}" download`)}</p>

    ${tx("h2", "dl.code", "Code and sheets", "Le code et les fiches")}
    ${tx("p", "dl.codep", "Everything is open. The software is under the MIT licence, the sheets under CC BY-SA 4.0. You can copy, modify and share both.", "Tout est ouvert. Le logiciel est sous licence MIT, les fiches sous licence CC BY-SA 4.0. Vous pouvez copier, modifier et redistribuer les deux.")}
    <p>${tx("a", "dl.repo", "See the repository", "Voir le dépôt", `class="btn" href="${DEPOT}" rel="noopener"`)}</p>
  </div>
</main>`;
  return page({ titreHtml: tx("title", "dl.title", "Download — Phenix", "Télécharger — Phenix"), desc: `Download Phenix Base: one ${APP_MB} file, every sheet inside, works offline.`, corps });
}

/* ---------- Contribuer (Phenix Lab) ---------- */
function lab() {
  const corps = `<main class="wrap lab" style="padding-top:34px;padding-bottom:60px">
  ${tx("p", "lab.k", "Phenix Lab · the community workshop", "Phenix Lab · l'atelier de la communauté", 'class="kicker"')}
  ${tx("h1", "lab.h1", "The library is written here.", "La bibliothèque s'écrit ici.", 'class="lab-titre"')}
  ${tx("p", "lab.lede2", "Suggest a sheet, vote for the ones you want, improve them in the comments. The best proposals become official sheets in the app, readable by everyone, offline. No account needed.", "Proposez une fiche, votez pour celles que vous voulez, améliorez-les dans les commentaires. Les meilleures propositions deviennent des fiches officielles dans l'application, lisibles par tous, hors ligne. Sans compte.", 'class="lede"')}
  <ol class="lab-etapes">
    ${tx("li", "lab.e1", "<b>Suggest</b> an idea in ten seconds, or write the whole sheet.", "<b>Proposez</b> une idée en dix secondes, ou écrivez toute la fiche.")}
    ${tx("li", "lab.e2", "<b>The community votes</b> and comments. What people need rises to the top.", "<b>La communauté vote</b> et commente. Ce dont les gens ont besoin monte en tête.")}
    ${tx("li", "lab.e3", "<b>The team checks</b> the sources, the safety and the clarity.", "<b>L'équipe vérifie</b> les sources, la sécurité et la clarté.")}
    ${tx("li", "lab.e4", "<b>It becomes official</b> and ships in the app, readable offline.", "<b>Elle devient officielle</b> et part dans l'application, lisible hors ligne.")}
  </ol>
  <div class="lab-onglets" role="tablist">
    <button type="button" role="tab" data-onglet="propositions">${tx("span", "lab.o1", "Proposals", "Propositions")}<span class="nb" id="nbProps"></span></button>
    <button type="button" role="tab" data-onglet="idee">${tx("span", "lab.o2", "Suggest an idea", "Proposer une idée")}</button>
    <button type="button" role="tab" data-onglet="ecrire">${tx("span", "lab.o3", "Write a sheet", "Écrire une fiche")}</button>
  </div>

  <section class="lab-panneau" id="o-propositions" role="tabpanel">
    <div class="lab-outils">
      <div class="lab-tri" role="group">
        <button type="button" data-tri="top" class="on">Top</button>
        <button type="button" data-tri="new">${tx("span", "lab.new", "New", "Nouveau")}</button>
      </div>
      <select id="filtreType" aria-label="Type">
        ${tx("option", "lab.ft0", "Everything", "Tout", 'value=""')}
        ${tx("option", "lab.ft1", "Ideas", "Idées", 'value="idee"')}
        ${tx("option", "lab.ft2", "Sheets", "Fiches", 'value="fiche"')}
        ${tx("option", "lab.ft3", "Corrections", "Corrections", 'value="correction"')}
      </select>
    </div>
    <div id="retourLab"></div>
    <div id="liste-communaute" class="lab-liste"><p class="dim small">…</p></div>
  </section>

  <section class="lab-panneau" id="o-idee" role="tabpanel" hidden>
    <div class="idee">
      ${tx("h2", "lab.q.h", "Got an idea for a sheet? Ten seconds.", "Une idée de fiche ? Dix secondes.")}
      ${tx("p", "lab.q.p2", "Tell us what you'd want to know how to do. It shows up in Proposals, where people vote for it.", "Dites-nous ce que vous aimeriez savoir faire. Elle apparaît dans Propositions, où les gens votent pour elle.", 'class="help"')}
      <form id="formIdee" autocomplete="off">
        <div class="field"><input id="ideeTexte" required minlength="3" maxlength="140" ${ph("lab.q.i", "e.g. How to purify water with a plastic bottle", "ex : Purifier de l'eau avec une bouteille en plastique")}></div>
        <div class="field"><textarea id="ideeDetail" maxlength="4000" ${ph("lab.q.d", "Details, your situation, what you already know (optional)", "Précisions, votre situation, ce que vous savez déjà (facultatif)")}></textarea></div>
        <div class="row">
          <div class="field"><input id="ideeAuteur" maxlength="60" ${ph("lab.q.a", "Nickname (optional)", "Pseudo (facultatif)")}></div>
          <div class="field"><input id="ideeContact" maxlength="120" ${ph("lab.q.c", "Email or Instagram, to hear back (optional, private)", "E-mail ou Instagram, pour une réponse (facultatif, privé)")}></div>
        </div>
        <div style="position:absolute;left:-9999px" aria-hidden="true"><input id="idSite" tabindex="-1" autocomplete="off"></div>
        <div id="retourIdee"></div>
        <p>${tx("button", "lab.q.b", "Send my idea", "Envoyer mon idée", 'type="submit" class="btn primary"')}</p>
      </form>
    </div>
  </section>

  <section class="lab-panneau" id="o-ecrire" role="tabpanel" hidden>
  ${tx("div", "lab.next2", "<strong>What happens next.</strong> Your sheet shows up in Proposals, where people vote and comment. The team reviews it before anything enters the official library: it can become <em>community</em>, then <em>verified</em>, and only then <em>official</em>.", "<strong>Ce qui se passe ensuite.</strong> Votre fiche apparaît dans Propositions, où les gens votent et commentent. L'équipe la relit avant toute entrée dans la bibliothèque officielle : elle peut devenir <em>communautaire</em>, puis <em>vérifiée</em>, et seulement après <em>officielle</em>.", 'class="msg info"')}

  <details class="aide">
    ${tx("summary", "lab.guide", "How to write a good sheet", "Comment écrire une bonne fiche")}
    <div class="inner">
      ${tx("h3", "lab.g1", "Tone", "Le ton", 'style="margin-top:0;font-size:15px"')}
      ${tx("p", "lab.g1p", "Assertive. Plain words. No filler, no sensationalism. Short sentences in an emergency, longer ones to explain.", "Assertif. Vouvoiement. Aucune phrase pour combler, aucun sensationnalisme. Phrases courtes dans l'urgence, longues dans l'explication.")}
      ${tx("h3", "lab.g2", "The two structures", "Les deux structures", 'style="font-size:15px"')}
      ${tx("p", "lab.g2a", "<strong>Urgent topic</strong> — Act, then Adapt, then Understand. The reader has no time: they act first.", "<strong>Sujet urgent</strong> — Agir, puis Adapter, puis Comprendre. Le lecteur n'a pas le temps : il exécute d'abord.")}
      ${tx("p", "lab.g2b", "<strong>Non-urgent topic</strong>: Understand, then Act, then Adapt. The right move comes from the mechanism.", "<strong>Sujet non urgent</strong> : Comprendre, puis Agir, puis Adapter. Le geste juste découle du mécanisme.")}
      ${tx("p", "lab.g2c", "Write the section titles like this: <code>## ACT</code>, <code>## UNDERSTAND</code>, <code>## ADAPT</code>.", "Écrivez les titres de section ainsi : <code>## AGIR</code>, <code>## COMPRENDRE</code>, <code>## ADAPTER</code>.")}
      ${tx("h3", "lab.g3", "The “Understand” part", "La partie « Comprendre »", 'style="font-size:15px"')}
      ${tx("p", "lab.g3p", "Explain the <strong>mechanism</strong>, not just the fact. The reader should be able to work out what to do in a case your sheet doesn't describe. That's what separates a useful sheet from a list of instructions.", "Expliquez le <strong>mécanisme</strong>, pas seulement le fait. Le lecteur doit pouvoir en déduire quoi faire dans un cas que votre fiche ne décrit pas. C'est ce qui sépare une fiche utile d'une liste d'instructions.")}
      ${tx("h3", "lab.g4", "Tags", "Les balises", 'style="font-size:15px"')}
      ${tx("p", "lab.g4p", "They don't classify the sheet: they guide the reader according to their situation.", "Elles ne classent pas la fiche : elles orientent la lecture selon la situation de celui qui cherche.")}
      <ul>
        ${tx("li", "lab.g4a", "<strong>Time</strong> — Flash (minutes), Short (hours), Long (days or more)", "<strong>Temps</strong> — Flash (minutes), Court (heures), Long (jours et plus)")}
        ${tx("li", "lab.g4b", "<strong>Context</strong> — Alone, Two people, Group", "<strong>Contexte</strong> — Seul, À deux, En groupe")}
        ${tx("li", "lab.g4c", "<strong>Risk</strong> — Discreet, Exposed", "<strong>Risque</strong> — Discret, Exposé")}
        ${tx("li", "lab.g4d", "<strong>Gear</strong> — None, Salvage, Technical", "<strong>Matériel</strong> — Aucun, Récupération, Technique")}
      </ul>
      ${tx("h3", "lab.g5", "Sources", "Les sources", 'style="font-size:15px"')}
      ${tx("p", "lab.g5p", "Prefer primary sources: health agencies, scientific institutions, technical manuals, peer-reviewed papers. On topics where a mistake hurts people, a sheet without sources won't be added.", "Préférez les sources primaires : organismes de santé, institutions scientifiques, manuels techniques, publications évaluées. Sur les sujets où une erreur blesse, une fiche sans source ne sera pas intégrée.")}
      ${tx("h3", "lab.g6", "Links", "Les liens", 'style="font-size:15px"')}
      ${tx("p", "lab.g6p", "Link your sheet to others with the ID between double brackets: <code>[[URG-EAU-001]]</code>. Put them <strong>in the text</strong>, where the reader needs them. A lone sheet is an article; a linked sheet is a path.", "Reliez votre fiche aux autres avec l'identifiant entre doubles crochets : <code>[[URG-EAU-001]]</code>. Placez-les <strong>dans le texte</strong>, là où le lecteur en a besoin. Une fiche isolée est un article ; une fiche reliée est un chemin.")}
      ${tx("h3", "lab.g7", "Topics", "Les sujets", 'style="font-size:15px"')}
      ${tx("p", "lab.g7p", "All of them, as long as the quality is there. Phenix is not just a survival database: an engine, a plant, a craft, a period of history, a cooking or building method all belong here.", "Tous, tant que la qualité y est. Phenix n'est pas une base de survie : un moteur, une plante, une technique manuelle, une période historique, une méthode de cuisine ou d'architecture ont toute leur place.")}
    </div>
  </details>

  <form id="form">
    <div class="field">
      <label for="titre">${tx("span", "lab.f1", "Title", "Titre")} <span class="req">*</span></label>
      ${tx("p", "lab.f1h", "What the sheet covers, plainly. No mysterious titles.", "Ce que la fiche traite, en clair. Pas de titre mystérieux.", 'class="help"')}
      <input id="titre" name="titre" required maxlength="140" ${ph("lab.f1p", "e.g. Purify fresh water", "ex : Purifier une eau douce")}>
    </div>
    <div class="field">
      <label for="contenu">${tx("span", "lab.f2", "The sheet", "La fiche")} <span class="req">*</span></label>
      ${tx("p", "lab.f2h", "The full text. Use <code>## ACT</code>, <code>## UNDERSTAND</code>, <code>## ADAPT</code> for the sections.", "Le texte complet. Utilisez <code>## AGIR</code>, <code>## COMPRENDRE</code>, <code>## ADAPTER</code> pour les sections.", 'class="help"')}
      <textarea id="contenu" name="contenu" class="tall" required ${ph("lab.f2p", "::One hook sentence between double colons.::\n\n## ACT\n\n1. First action.\n\n## ADAPT\n\n## UNDERSTAND", "::Une phrase d'accroche entre doubles deux-points.::\n\n## AGIR\n\n1. Première action.\n\n## ADAPTER\n\n## COMPRENDRE")}></textarea>
    </div>
    <div class="field">
      <label for="resume">${tx("span", "lab.f3", "Short description", "Description courte")}</label>
      ${tx("p", "lab.f3h", "Optional. One or two sentences to frame the sheet.", "Optionnel. Une ou deux phrases pour situer la fiche.", 'class="help"')}
      <textarea id="resume" name="resume" maxlength="400"></textarea>
    </div>
    <div class="row">
      <div class="field">
        <label for="axe">${tx("span", "lab.f4", "Likely axis", "Axe probable")}</label>
        <select id="axe" name="axe">
          ${tx("option", "lab.f4o0", "— I don't know —", "— je ne sais pas —", 'value=""')}
          ${tx("option", "lab.f4o1", "1 — Memory (history, societies)", "1 — La Mémoire (histoire, sociétés)", 'value="1"')}
          ${tx("option", "lab.f4o2", "2 — Technique (how things work)", "2 — La Technique (comment ça marche)", 'value="2"')}
          ${tx("option", "lab.f4o3", "3 — Survival (what to do, now)", "3 — La Survie (quoi faire, maintenant)", 'value="3"')}
        </select>
      </div>
      <div class="field">
        <label for="categorie">${tx("span", "lab.f5", "Suggested category", "Catégorie proposée")}</label>
        <input id="categorie" name="categorie" maxlength="80" ${ph("lab.f5p", "e.g. Mechanics and transport", "ex : Mécanique et Transport")}>
      </div>
    </div>
    <div class="row">
      <div class="field">
        <label for="langue">${tx("span", "lab.f6", "Language of the sheet", "Langue de la fiche")}</label>
        <select id="langue" name="langue">
          <option value="en">English</option>
          <option value="fr">Français</option>
          ${tx("option", "lab.f6o", "Another language", "Une autre langue", 'value="autre"')}
        </select>
      </div>
      <div class="field">
        <label for="urgence">Type</label>
        <select id="urgence" name="urgence">
          ${tx("option", "lab.f7a", "General knowledge", "Savoir général", 'value="savoir"')}
          ${tx("option", "lab.f7b", "Urgent situation", "Situation urgente", 'value="urgence"')}
        </select>
      </div>
    </div>
    <div class="field">
      <label for="sources">Sources</label>
      ${tx("p", "lab.f8h", "One per line. A link, a book title, an organisation.", "Une par ligne. Un lien, un titre d'ouvrage, un organisme.", 'class="help"')}
      <textarea id="sources" name="sources" ${ph("lab.f8p", "WHO — Guidelines for drinking-water quality\nhttps://...", "OMS — Directives sur la qualité de l'eau de boisson\nhttps://...")}></textarea>
    </div>
    <div class="field">
      <label for="note">${tx("span", "lab.f9", "Note to the editor", "Note à l'éditeur")}</label>
      ${tx("p", "lab.f9h", "Why this sheet? What does it add? Anything to avoid or double-check?", "Pourquoi cette fiche ? Qu'apporte-t-elle ? Y a-t-il quelque chose à éviter ou à vérifier ?", 'class="help"')}
      <textarea id="note" name="note"></textarea>
    </div>
    <div class="field">
      <label for="images">${tx("span", "lab.f10", "Images or diagrams", "Images ou schémas")}</label>
      ${tx("p", "lab.f10h", "Optional. You must have the right to share them.", "Optionnel. Vous devez avoir le droit de les partager.", 'class="help"')}
      <input type="file" id="images" name="images" accept="image/*" multiple>
    </div>
    <div class="field">
      <label for="auteur">${tx("span", "lab.f11", "Your name or nickname", "Votre nom ou pseudonyme")}</label>
      ${tx("p", "lab.f11h", "Optional. Leave it empty to stay anonymous: it changes nothing in how your proposal is reviewed.", "Optionnel. Laissez vide pour rester anonyme : cela ne change rien à l'examen de votre proposition.", 'class="help"')}
      <input id="auteur" name="auteur" maxlength="60" ${ph("lab.f11p", "anonymous", "anonyme")}>
    </div>
    <div class="field">
      <label for="contact">Contact</label>
      ${tx("p", "lab.f12h", "Optional. Only if you want to be notified, or to answer a correction request.", "Optionnel. Uniquement si vous voulez être prévenu ou pouvoir répondre à une demande de correction.", 'class="help"')}
      <input id="contact" name="contact" type="email" maxlength="120" ${ph("lab.f12p", "you@example.com", "vous@exemple.fr")}>
    </div>
    <!-- Piège à robots : invisible pour les humains, rempli par les automates. -->
    <div style="position:absolute;left:-9999px" aria-hidden="true">
      <label for="site">Leave empty</label>
      <input id="site" name="site" tabindex="-1" autocomplete="off">
    </div>
    <div id="retour"></div>
    <p style="margin-top:26px">
      ${tx("button", "lab.send", "Send my proposal", "Envoyer ma proposition", 'type="submit" class="btn primary" id="submit" style="font-size:15px;padding:14px 28px"')}
    </p>
    ${tx("p", "lab.cc", "By sending, you agree that your sheet may be published under the CC BY-SA 4.0 licence if it's accepted. You stay free to do whatever you want with it elsewhere.", "En envoyant, vous acceptez que votre fiche puisse être publiée sous licence CC BY-SA 4.0 si elle est retenue. Vous restez libre d'en faire ce que vous voulez par ailleurs.", 'class="small" style="margin-top:16px"')}
  </form>
  </section>
</main>`;
  return page({ titreHtml: tx("title", "lab.title2", "Phenix Lab", "Phenix Lab"), desc: "Phenix Lab: suggest sheets, vote and comment. The best proposals become official sheets in the Phenix library. No account needed.", corps, scripts: '<script src="en-ligne.js"></script><script src="communaute.js"></script><script src="lab.js"></script>' });
}

/* ---------- Soutenir ---------- */
function soutenir() {
  const corps = `<main class="wrap" style="padding-top:34px;padding-bottom:60px">
  ${tx("h1", "sup.h1", "Support Phenix", "Soutenir Phenix", 'style="font-size:30px;margin:0 0 10px;color:var(--acc);text-shadow:var(--glow)"')}
  ${tx("p", "sup.lede", "Today the project costs zero euros to run. That's not luck: it's a design constraint.", "Le projet coûte aujourd'hui zéro euro à faire tourner. Ce n'est pas un hasard : c'est une contrainte de conception.", 'class="lede" style="font-size:17px;margin:0"')}
  <div class="band" style="border:none;padding:30px 0 0">
    ${tx("h2", "sup.best", "The most useful way to help", "La façon la plus utile de soutenir")}
    ${tx("p", "sup.bestp", "<strong>Write a sheet.</strong> The software will be finished long before the library. A good, sourced sheet is worth more than a donation.", "<strong>Écrire une fiche.</strong> Le logiciel sera fini bien avant le corpus. Une bonne fiche sourcée vaut plus qu'un don.")}
    <p>${tx("a", "sup.btn", "Write a sheet", "Proposer une fiche", 'class="btn primary" href="lab.html"')}</p>
    ${tx("h2", "sup.other", "Other ways", "Autrement")}
    <ul>
      ${tx("li", "sup.o1", "Report a mistake in an existing sheet", "Signaler une erreur dans une fiche existante")}
      ${tx("li", "sup.o2", "Translate a sheet into your language", "Traduire une fiche dans votre langue")}
      ${tx("li", "sup.o3", "Review proposals on a subject you know", "Relire les propositions sur un sujet que vous connaissez")}
      ${tx("li", "sup.o4", `Spread the word: <a href="${INSTA}" rel="noopener">@phenixprjct</a> on Instagram, <a href="${REDDIT}" rel="noopener">r/PhenixProject</a> on Reddit`, `Faire connaître le projet : <a href="${INSTA}" rel="noopener">@phenixprjct</a> sur Instagram, <a href="${REDDIT}" rel="noopener">r/PhenixProject</a> sur Reddit`)}
    </ul>
    ${tx("h2", "sup.money", "Money", "Argent")}
    ${tx("p", "sup.m1", "There's no way to donate yet, on purpose: as long as the project costs nothing, asking for money would be dishonest.", "Il n'y a pas encore de moyen de donner, et c'est volontaire : tant que le projet ne coûte rien, demander de l'argent serait malhonnête.")}
    ${tx("p", "sup.m2", "What will cost money, and only with volume: a dedicated map tile server, a signing certificate for the desktop app, a domain name. They'll be announced here, with their real cost, when they come up.", "Ce qui deviendra payant, et seulement avec le volume : un serveur de tuiles cartographiques dédié, un certificat de signature pour l'application de bureau, un nom de domaine. Ces postes seront annoncés ici avec leur montant réel au moment où ils se poseront.")}
  </div>
</main>`;
  return page({ titreHtml: tx("title", "sup.title", "Support — Phenix", "Soutenir — Phenix"), desc: "How to support Phenix.", corps });
}

/* ---------- Appareils ---------- */
// Tout ce qui est dit ici reprend les annonces du post Hardware (communication/posts/23-en-hardware.js).
function appareils() {
  const spec = (k, en, fr, ken, kfr) => `<li><b data-i18n="${k}.k">${ken}</b>${tx("span", k, en, fr)}</li>` + ((D[k + ".k"] = [ken, kfr]), "");
  const corps = `<main class="wrap" style="padding-top:34px;padding-bottom:60px;max-width:900px">
  ${tx("span", "dev.badge", "Prototype · in design", "Prototype · en conception", 'class="concept"')}
  ${tx("h1", "dev.h1", "Phenix devices", "Les appareils Phenix", 'style="font-size:32px;margin:0 0 10px;color:var(--acc);text-shadow:var(--glow)"')}
  ${tx("p", "dev.lede", "Two small, tough devices designed to be cheap and built only from common parts, so they can be repaired with what's left in old electronics.", "Deux petits appareils robustes, pensés pour coûter peu et n'utiliser que des pièces courantes, pour être réparés avec ce qui reste dans les vieux appareils électroniques.", 'class="lede" style="font-size:18px;margin:0"')}

  <section class="appareil">
    <div class="visuel"><img src="img/phenix-001.svg" alt="Concept render of Phenix 001, a pocket reader with an e-ink screen and a D-pad"></div>
    <div>
      ${tx("h2", "dev.001", "Phenix 001 — the pocket reader", "Phenix 001 — le lecteur de poche", 'style="font-size:22px;margin:0 0 10px;color:var(--acc)"')}
      ${tx("p", "dev.001p", "The size of a Flipper Zero, and it holds a whole library. An e-ink screen you can read in full sun, a steel case, a D-pad, and a microSD slot on top.", "La taille d'un Flipper Zero, et une bibliothèque entière dedans. Un écran à encre électronique lisible en plein soleil, un boîtier en acier, une croix directionnelle et un lecteur microSD sur le dessus.")}
      <ul class="specs">
        ${spec("dev.001a", "E-ink, readable in full sun. Color e-ink on the C version.", "Encre électronique, lisible en plein soleil. En couleur sur la version C.", "Screen", "Écran")}
        ${spec("dev.001b", "32 to 64 GB built in (target), plus microSD: room for a whole regional library, its maps and its diagrams.", "32 à 64 Go intégrés (objectif), plus une microSD : de quoi tenir une bibliothèque régionale entière, ses cartes et ses schémas.", "Storage", "Stockage")}
        ${spec("dev.001c", "Steel, with a laser-engraved logo. Five colorways, the same parts inside.", "Acier, logo gravé au laser. Cinq coloris, les mêmes pièces dedans.", "Case", "Boîtier")}
      </ul>
    </div>
  </section>

  <section class="appareil inverse">
    <div class="visuel"><img src="img/phenix-002.svg" alt="Concept render of Phenix 002, a calculator-sized terminal with a color screen and a keyboard" style="max-height:480px"></div>
    <div>
      ${tx("h2", "dev.002", "Phenix 002 — closer to a calculator than a computer", "Phenix 002 — plus proche d'une calculatrice que d'un ordinateur", 'style="font-size:22px;margin:0 0 10px;color:var(--acc)"')}
      ${tx("p", "dev.002p", "About the size of a paperback. A color screen, a real keyboard, and a long-range radio to send messages when there's no network left.", "À peu près la taille d'un livre de poche. Un écran couleur, un vrai clavier, et une radio longue portée pour envoyer des messages quand il n'y a plus de réseau.")}
      <ul class="specs">
        ${spec("dev.002a", "LoRa long-range radio: messages between devices, no network needed.", "Radio longue portée LoRa : des messages entre appareils, sans aucun réseau.", "Radio", "Radio")}
        ${spec("dev.002b", "256 GB built in (target), and room for two or three SD cards at once.", "256 Go intégrés (objectif), et deux ou trois cartes SD en même temps.", "Storage", "Stockage")}
        ${spec("dev.002c", "A diagnostic port to test a salvaged part before you wire it in.", "Un port de diagnostic pour tester une pièce récupérée avant de la brancher.", "Diagnostic", "Diagnostic")}
      </ul>
    </div>
  </section>

  <div class="band">
    ${tx("h2", "dev.built", "Built from what the world already has", "Fait avec ce que le monde a déjà")}
    <div class="quatre">
      <div>${tx("h3", "dev.q1", "Common parts only", "Que des pièces courantes")}${tx("p", "dev.q1p", "No custom parts: every component has a twin in everyday devices. When a screen breaks or a battery dies, the replacement is probably already lying in a drawer somewhere.", "Aucune pièce sur mesure : chaque composant a un jumeau dans les appareils de tous les jours. Quand un écran casse ou qu'une batterie meurt, la pièce de rechange traîne sûrement déjà dans un tiroir.")}</div>
      <div>${tx("h3", "dev.q2", "Opens with a screwdriver", "S'ouvre au tournevis")}${tx("p", "dev.q2p", "No glue, no special screws: every layer comes apart. Cracked screen? Wire in one from an old device with four jumper wires, and it reads again.", "Pas de colle, pas de vis spéciales : chaque couche se démonte. Écran fissuré ? On en branche un autre, récupéré dans un vieil appareil, avec quatre fils, et il relit.")}</div>
      <div>${tx("h3", "dev.q3", "They share everything", "Ils partagent tout")}${tx("p", "dev.q3p", "Plug two together, by cable or magnetic pins, and they swap sheets, maps and notes, checking every signature. Each device becomes another copy of the library.", "Branchez-en deux, par câble ou par leurs broches magnétiques, et ils s'échangent fiches, cartes et notes en vérifiant chaque signature. Chaque appareil devient une copie de plus de la bibliothèque.")}</div>
      <div>${tx("h3", "dev.q4", "Power when there's none", "De l'énergie quand il n'y en a plus")}${tx("p", "dev.q4p", "18650 cells, the most common battery size in the world, in a LiFePO4 pack chosen for safety and long life. It charges over USB-C, magnetic pins, a clip-on crank or a folding solar panel.", "Des cellules au format 18650, le plus répandu au monde, en pack LiFePO4 choisi pour la sécurité et la durée de vie. Recharge par USB-C, broches magnétiques, manivelle à clipser ou panneau solaire pliable.")}</div>
    </div>
  </div>

  <div class="band">
    ${tx("h2", "dev.versions", "Read the version on the logo", "La version se lit sur le logo")}
    ${tx("p", "dev.versionsp", "A painted ring around the engraved logo tells you which model you're holding: none for the base model, yellow for color e-ink, blue for the local AI assistant, both for both.", "Un anneau peint autour du logo gravé indique le modèle : aucun pour la version de base, jaune pour l'encre couleur, bleu pour l'assistant IA local, les deux pour les deux.")}
    <div class="large"><img src="img/phenix-001-versions.svg" alt="The four versions of Phenix 001, told apart by the rings around the logo"></div>
    ${tx("p", "dev.colors", "Five colorways — brushed steel, plain grey, military green, matte black, signal red — and exactly the same parts inside.", "Cinq coloris — acier brossé, gris, vert militaire, noir mat, rouge signal — et exactement les mêmes pièces dedans.")}
    <div class="large"><img src="img/phenix-001-coloris.svg" alt="Phenix 001 in five colorways"></div>
  </div>

  <div class="band">
    ${tx("h2", "dev.price", "A price anyone can pay", "Un prix que tout le monde peut payer")}
    ${tx("p", "dev.pricep", "The goal is a device that's genuinely cheap: cheap enough for every school, village and town hall to have one, like the defibrillator next to the door.", "L'objectif est un appareil vraiment bon marché : assez pour que chaque école, chaque village et chaque mairie en ait un, comme le défibrillateur à côté de la porte.")}
    ${tx("p", "dev.honest", "Concept renders, not the final design. No dates and no prices until a prototype works.", "Rendus de concept, pas le design final. Ni date ni prix tant qu'un prototype ne fonctionne pas.", 'class="note"')}
    ${tx("p", "dev.help", `Want to help build it? Electronics, firmware, case design, testing: come and talk on <a href="${REDDIT}" rel="noopener">r/PhenixProject</a> or open an issue on <a href="${DEPOT}" rel="noopener">GitHub</a>.`, `Envie d'aider à le construire ? Électronique, logiciel embarqué, boîtier, tests : venez en parler sur <a href="${REDDIT}" rel="noopener">r/PhenixProject</a> ou ouvrez un ticket sur <a href="${DEPOT}" rel="noopener">GitHub</a>.`)}
    <p>${tx("a", "dev.follow", "Follow the build on Instagram", "Suivre la construction sur Instagram", `class="btn primary" href="${INSTA}" rel="noopener"`)}</p>
  </div>
</main>`;
  return page({ titreHtml: tx("title", "dev.title", "Devices — Phenix", "Appareils — Phenix"), desc: "Phenix 001 and 002: small, tough, repairable devices that carry the library offline.", corps });
}

/* ---------- Pages des fiches ---------- */
function pageFiche(id, lang) {
  const i = lang === "fr" ? 1 : 0;
  const src = lang === "en" ? EN_F[id] : FR_F[id];
  const f = FR_F[id].meta;
  const axe = String(f.axe);
  const alt = lang === "en" ? fichier(id, "fr") : EN_F[id] ? fichier(id, "en") : "";
  const cat = lang === "en" ? CAT_EN[f.categorie] || f.categorie : f.categorie;
  const bals = ["temps", "contexte", "risque", "materiel"].map((k) => {
    const v = String(f[k] || "").trim();
    if (!v) return "";
    const [lab, table] = BALS[k];
    return `<div><span>${lab[i]}</span><b>${esc(table[v] ? table[v][i] : v)}</b></div>`;
  }).join("");
  const sources = (src.meta.sources && src.meta.sources.length ? src.meta.sources : f.sources) || [];
  const retours = IDS.filter((o) => o !== id && FR_F[o].corps.includes(`[[${id}]]`));
  const lienRetour = (o) => {
    const cible = lang === "en" && EN_F[o] ? fichier(o, "en") : fichier(o, "fr");
    return `<a class="item" href="${cible}"><h3>${esc(titre(o, lang))}</h3><div class="meta">${lang === "fr" ? "Axe" : "Axis"} ${FR_F[o].meta.axe}</div></a>`;
  };
  const seulFr = lang === "fr" && !EN_F[id];
  const corps = `<main class="wrap fiche">
  <p class="fil">${tx("a", "nav.explore", "Explore", "Explorer", 'href="explore.html"', lang)} › ${esc(AXES[axe][i])} › ${esc(cat)}</p>
  ${seulFr ? tx("p", "fiche.onlyfr", 'This sheet is only in French for now. <a href="lab.html#ecrire">Help translate it →</a>', "Cette fiche n'existe qu'en français pour l'instant.", 'class="onlyfr" data-only="en" hidden', lang) : ""}
  <div class="tags">
    ${f.priorite === "flash" ? tx("span", "tag.urg", "Emergency", "Urgence", 'class="tag urg"', lang) : ""}
    ${tx("span", "tag.off", "Official", "Officielle", 'class="tag off"', lang)}
  </div>
  <h1>${esc(src.meta.titre)}</h1>
  <p class="meta">${lang === "fr" ? "Axe" : "Axis"} ${axe} · ${esc(AXES[axe][i])} · ${esc(cat)}</p>
  <div class="bals">${bals}</div>
  <article class="prose">${rendre(src.corps, lienPour(lang))}</article>
  ${sources.length ? `<div class="blk"><h4>Sources</h4>${sources.map((s) => `<div class="src">${esc(s)}</div>`).join("")}</div>` : ""}
  ${retours.length ? `<div class="blk">${tx("h4", "fiche.back", "Sheets that lead here", "Fiches qui mènent ici", "", lang)}${retours.map(lienRetour).join("")}</div>` : ""}
  <section class="blk">
    ${tx("h4", "fiche.commu", "Useful? Anything to add?", "Utile ? Quelque chose à ajouter ?", "", lang)}
    <div id="communaute" data-cible="${id}"></div>
  </section>
  <div class="blk cta">
    ${tx("p", "fiche.cta", "<strong>This sheet is part of Phenix.</strong> The app holds the whole library, the maps and the bookshelf, and works offline.", "<strong>Cette fiche fait partie de Phenix.</strong> L'application contient tout le corpus, les cartes et la bibliothèque, et fonctionne hors ligne.", "", lang)}
    <p>${tx("a", "home.b2", "Download Phenix Base", "Télécharger Phenix Base", 'class="btn primary" href="download.html"', lang)}
       ${tx("a", "sup.btn", "Write a sheet", "Proposer une fiche", 'class="btn" href="lab.html#ecrire"', lang)}</p>
  </div>
</main>`;
  const desc = `${src.meta.titre} — Phenix`;
  return page({ lang, alt, fiche: true, titreHtml: `<title>${esc(src.meta.titre)} — Phenix</title>`, desc, css: ["fiche.css"], corps, scripts: '<script src="en-ligne.js"></script><script src="communaute.js"></script>' });
}

/* ---------- Script de langue ---------- */
function i18n() {
  return `/* Généré par outils/construire-site.js : ne pas modifier à la main. */
(function () {
  var D = ${JSON.stringify(D)};
  var h = document.documentElement;
  var pageLang = h.getAttribute("data-page-lang") || "en";
  var alt = h.getAttribute("data-alt");
  var estFiche = h.getAttribute("data-kind") === "fiche";
  function lire() {
    try { var s = localStorage.getItem("phenix-lang"); if (s === "fr" || s === "en") return s; } catch (e) {}
    return /^fr/i.test(navigator.language || "") ? "fr" : "en";
  }
  function garder(l) { try { localStorage.setItem("phenix-lang", l); } catch (e) {} }
  var lang = lire();
  if (lang !== pageLang && alt) { location.replace(alt); return; }
  function appliquer(l) {
    var i = l === "fr" ? 1 : 0;
    h.lang = estFiche ? pageLang : l;
    document.querySelectorAll("[data-i18n]").forEach(function (el) {
      var v = D[el.getAttribute("data-i18n")]; if (v) el.innerHTML = v[i];
    });
    document.querySelectorAll("[data-i18n-ph]").forEach(function (el) {
      var v = D[el.getAttribute("data-i18n-ph")]; if (v) el.placeholder = v[i];
    });
    document.querySelectorAll("[data-only]").forEach(function (el) {
      el.hidden = el.getAttribute("data-only") !== l;
    });
    document.querySelectorAll("a[data-href-fr]").forEach(function (a) {
      a.href = l === "fr" ? a.getAttribute("data-href-fr") : (a.getAttribute("data-href-en") || a.getAttribute("data-href-fr"));
    });
    document.querySelectorAll(".lang").forEach(function (b) { b.textContent = l === "fr" ? "EN" : "FR"; });
  }
  document.querySelectorAll(".lang").forEach(function (b) {
    b.addEventListener("click", function () {
      var n = lang === "fr" ? "en" : "fr";
      garder(n);
      if (alt && n !== pageLang) { location.href = alt; return; }
      lang = n; appliquer(n);
    });
  });
  appliquer(lang);
  // Thèmes : phosphore (par défaut), ambre, papier. Le choix est gardé d'une page à l'autre.
  function marquerTheme() {
    var t = h.getAttribute("data-theme") || "phosphore";
    document.querySelectorAll("[data-theme-set]").forEach(function (b) { b.classList.toggle("on", b.getAttribute("data-theme-set") === t); });
  }
  document.querySelectorAll("[data-theme-set]").forEach(function (b) {
    b.addEventListener("click", function () {
      var t = b.getAttribute("data-theme-set");
      if (t === "phosphore") h.removeAttribute("data-theme"); else h.setAttribute("data-theme", t);
      try { localStorage.setItem("phenix-theme", t); } catch (e) {}
      marquerTheme();
    });
  });
  marquerTheme();
})();
`;
}

/* ---------- Liens (le lien de la bio Instagram) ---------- */
function liens() {
  const lien = (href, k, en, fr, ks, ens, frs, cls = "act") =>
    `<a class="${cls}" href="${href}"${/^https?:/.test(href) ? ' rel="noopener"' : ""}>${tx("b", k, en, fr)}${tx("span", ks, ens, frs)}</a>`;
  const corps = `<main class="wrap liens">
  <div class="mark big"></div>
  ${tx("p", "ln.lede", "A free library of practical knowledge that works without internet. Written by everyone, for everyone.", "Une bibliothèque libre de savoirs pratiques, qui marche sans internet. Écrite par tout le monde, pour tout le monde.", 'class="lede"')}
  <div class="pile">
    ${lien("phenix.html", "ln.app", "Open the app", "Ouvrir l'application", "ln.apps", "On your phone or your computer. Nothing to install to try it.", "Sur téléphone ou sur ordinateur. Rien à installer pour l'essayer.", "act primary")}
    ${lien("download.html#phone", "ln.inst", "Put it on your phone", "La mettre sur votre téléphone", "ln.insts", "Home screen icon, works offline. No store, no account.", "Une icône sur l'écran d'accueil, marche hors ligne. Sans store ni compte.")}
    ${lien("explore.html", "ln.exp", "Read the sheets", "Lire les fiches", "ln.exps", "First aid, water, repairs, energy, memory of the world", "Secours, eau, réparation, énergie, mémoire du monde")}
    ${lien("lab.html?origine=bio#idee", "ln.idee", "Suggest a sheet", "Proposer une fiche", "ln.idees", "Ten seconds, no account. The best ideas become sheets.", "Dix secondes, sans compte. Les meilleures idées deviennent des fiches.")}
    ${lien("lab.html#propositions", "ln.com", "Phenix Lab", "Phenix Lab", "ln.coms", "Vote and comment on what readers propose", "Votez et commentez ce que proposent les lecteurs")}
    ${lien("devices.html", "ln.dev", "The devices", "Les appareils", "ln.devs", "Phenix 001 and 002, pocket readers in design", "Phenix 001 et 002, des lecteurs de poche en conception")}
    ${lien("lab.html#ecrire", "ln.lab", "Write a sheet", "Écrire une fiche", "ln.labs", "Share what you know. No account needed.", "Partagez ce que vous savez. Aucun compte nécessaire.")}
    ${lien("download.html", "ln.win", "Windows version", "Version Windows", "ln.wins", "The full app, installed on your PC", "L'application complète, installée sur votre PC")}
    ${lien(REDDIT, "ln.red", "Reddit", "Reddit", "ln.reds", "Discuss the project on r/PhenixProject", "Discuter du projet sur r/PhenixProject")}
    ${lien(DEPOT, "ln.git", "GitHub", "GitHub", "ln.gits", "Code and sheets, open to everyone", "Le code et les fiches, ouverts à tous")}
  </div>
</main>`;
  return page({ titreHtml: tx("title", "ln.title", "Links — Phenix", "Liens — Phenix"), desc: "Phenix: open the app, install it on your phone, read the sheets, see the devices.", corps });
}

/* ---------- Application web : installable sur téléphone et utilisable hors ligne ---------- */
const APP_SRC = path.join(RACINE, "app", "phenix.html");
const TETE_APP = `<link rel="manifest" href="manifest.webmanifest">
<meta name="theme-color" content="#040806">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Phenix">
<meta name="apple-mobile-web-app-status-bar-style" content="black">
<link rel="apple-touch-icon" href="img/icone-180.png">
<link rel="icon" href="img/icone-192.png">
<script>if("serviceWorker"in navigator&&location.protocol==="https:")addEventListener("load",function(){navigator.serviceWorker.register("sw.js").catch(function(){})})</script>`;
const MANIFESTE = {
  name: "Phenix",
  short_name: "Phenix",
  description: "A free library of practical knowledge that works without internet.",
  lang: "en",
  start_url: "phenix.html",
  scope: "./",
  display: "standalone",
  background_color: "#040806",
  theme_color: "#040806",
  icons: [
    { src: "img/icone-192.png", sizes: "192x192", type: "image/png" },
    { src: "img/icone-512.png", sizes: "512x512", type: "image/png" },
    { src: "img/icone-masque-512.png", sizes: "512x512", type: "image/png", purpose: "maskable" },
  ],
};
// Le service worker garde l'application (un seul fichier) sur le téléphone. Il sert la copie en cache
// tout de suite et va chercher la nouvelle version en arrière-plan : elle s'affiche à l'ouverture suivante.
const SW = (version) => `// Phenix hors ligne. Généré par outils/construire-site.js, ne pas modifier à la main.
const CACHE = "phenix-${version}";
const BASE = ["phenix.html", "manifest.webmanifest", "img/icone-192.png", "img/icone-512.png", "img/icone-180.png"];
self.addEventListener("install", (e) => {
  e.waitUntil(caches.open(CACHE).then((c) => c.addAll(BASE)).then(() => self.skipWaiting()));
});
self.addEventListener("activate", (e) => {
  e.waitUntil(caches.keys().then((ks) => Promise.all(ks.filter((k) => k !== CACHE).map((k) => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener("fetch", (e) => {
  const req = e.request;
  const url = new URL(req.url);
  // Tuiles de carte, recherche de lieux, installateur Windows : toujours le réseau.
  if (req.method !== "GET" || url.origin !== location.origin || url.pathname.includes("/dl/")) return;
  const reseau = fetch(req).then((r) => {
    if (r.ok) { const copie = r.clone(); caches.open(CACHE).then((c) => c.put(req, copie)); }
    return r;
  });
  e.respondWith(
    caches.match(req, { ignoreSearch: true }).then((enCache) => {
      if (enCache) { e.waitUntil(reseau.catch(() => {})); return enCache; }
      return reseau.catch(() => (req.mode === "navigate" ? caches.match("phenix.html") : Response.error()));
    })
  );
});
`;

/* ---------- Écriture ---------- */
const ecrire = (nom, html) => fs.writeFileSync(path.join(SITE, nom), html);
ecrire("index.html", accueil());
ecrire("explore.html", explorer());
ecrire("download.html", telecharger());
ecrire("lab.html", lab());
ecrire("soutenir.html", soutenir());
ecrire("devices.html", appareils());
ecrire("links.html", liens());
const faites = new Set();
for (const id of IDS) {
  ecrire(fichier(id, "fr"), pageFiche(id, "fr"));
  faites.add(fichier(id, "fr"));
  if (EN_F[id]) { ecrire(fichier(id, "en"), pageFiche(id, "en")); faites.add(fichier(id, "en")); }
}
// Les anciennes pages de fiches qui ne sont plus générées disparaissent.
for (const f of fs.readdirSync(SITE)) if (/^fiche-.*\.html$/.test(f) && !faites.has(f)) fs.unlinkSync(path.join(SITE, f));
ecrire("i18n.js", i18n());
// L'application du site est celle de app/, avec en plus de quoi l'installer sur un téléphone.
const appHtml = fs.readFileSync(APP_SRC, "utf8");
if (!appHtml.includes("<title>PHENIX</title>")) throw new Error("app/phenix.html : balise <title> introuvable");
ecrire("phenix.html", appHtml.replace("<title>PHENIX</title>", "<title>PHENIX</title>\n" + TETE_APP));
ecrire("manifest.webmanifest", JSON.stringify(MANIFESTE, null, 2) + "\n");
// La version du cache suit le contenu de l'application : chaque changement déclenche une mise à jour.
const empreinte = require("crypto").createHash("sha1").update(appHtml).digest("hex").slice(0, 10);
ecrire("sw.js", SW(empreinte));
if (fs.existsSync(EXE_SOURCE)) {
  fs.mkdirSync(path.join(SITE, "dl"), { recursive: true });
  fs.copyFileSync(EXE_SOURCE, path.join(SITE, EXE));
}
console.log(`${IDS.length} fiches (${IDS.filter((id) => EN_F[id]).length} en anglais), ${Object.keys(D).length} textes traduits.`);
