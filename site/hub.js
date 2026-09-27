/* =========================================================================
   PHENIX HUB : toutes les versions de la bibliothèque.
   La version officielle est écrite dans la page à la construction du site (outils/construire-site.js).
   Ici : les versions des communautés (lues dans la base, fichiers dans son dossier « versions »),
   les fiches écrites par les gens (celles de Phenix Lab), et l'envoi d'une version.
   ========================================================================= */
const PL = window.PHENIX_EN_LIGNE;
const PC = window.PhenixCommunaute;
const M = (en, fr) => (document.documentElement.lang === "fr" ? fr : en);
const esc = PC.esc;
const val = (id) => (document.getElementById(id) ? document.getElementById(id).value.trim() : "");
function message(zone, type, html) {
  zone.innerHTML = `<div class="msg ${type}">${html}</div>`;
  zone.scrollIntoView({ behavior: "smooth", block: "center" });
}
const LANGUES = {
  fr: "Français", en: "English", es: "Español", de: "Deutsch", it: "Italiano", pt: "Português", "pt-br": "Português (Brasil)",
  nl: "Nederlands", pl: "Polski", uk: "Українська", ru: "Русский", ar: "العربية", zh: "中文", ja: "日本語", ko: "한국어",
  hi: "हिन्दी", tr: "Türkçe", br: "Brezhoneg", eu: "Euskara", ca: "Català", oc: "Occitan", co: "Corsu",
};
const nomLangue = (c) => LANGUES[String(c || "").toLowerCase()] || String(c || "").toUpperCase();
const taille = (o) => {
  if (o >= 1e6) { const v = (o / 1e6).toFixed(1); return M(v + " MB", v.replace(".", ",") + " Mo"); }
  return Math.max(1, Math.round(o / 1e3)) + M(" KB", " ko");
};
const slug = (s) => String(s || "").toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "").slice(0, 60);
// Donner un fichier à la personne. Sur le site (pas dans un aperçu), un lien « download » suffit.
function enregistrer(texte, nom, type = "application/json") {
  const u = URL.createObjectURL(new Blob([texte], { type }));
  const a = document.createElement("a");
  a.href = u; a.download = nom; document.body.appendChild(a); a.click(); a.remove();
  setTimeout(() => URL.revokeObjectURL(u), 5000);
}
function copierLien(b, ancre) {
  const lien = location.origin + location.pathname + "#" + ancre;
  const ok = () => { const t = b.textContent; b.textContent = M("Link copied", "Lien copié"); setTimeout(() => (b.textContent = t), 1800); };
  if (navigator.clipboard) navigator.clipboard.writeText(lien).then(ok).catch(() => prompt(M("Copy this link:", "Copiez ce lien :"), lien));
  else prompt(M("Copy this link:", "Copiez ce lien :"), lien);
}
function boutonVote(b, cible, n) {
  const peindre = (k) => { b.querySelector("b").textContent = k; b.classList.toggle("on", PL.aVote(cible)); };
  peindre(n || 0);
  b.onclick = async () => {
    b.disabled = true;
    try { peindre(await PL.voter(cible, PL.aVote(cible))); } catch (e) { alert(e.message); }
    b.disabled = false;
  };
}

/* ---------- Les versions des communautés ---------- */
async function versions() {
  const zone = document.getElementById("hubVersions");
  let l;
  try { l = await PL.versions(); } catch (e) {
    zone.innerHTML = `<div class="lab-vide"><p>${M("Community versions open very soon. You can already prepare yours: start from the official version above.", "Les versions des communautés ouvrent très bientôt. Vous pouvez déjà préparer la vôtre : partez de la version officielle ci-dessus.")}</p></div>`;
    return;
  }
  if (!l.length) {
    zone.innerHTML = `<div class="lab-vide"><p>${M("No community version yet. Yours could be the first: a language, a region, a club, a village.", "Aucune version de communauté pour l'instant. La vôtre peut être la première : une langue, une région, un club, un village.")}</p>
      <a class="btn primary" href="#publier">${M("Publish a version", "Publier une version")}</a></div>`;
    return;
  }
  zone.innerHTML = "";
  for (const v of l) zone.appendChild(carteVersion(v));
  const ancre = decodeURIComponent(location.hash.slice(1));
  if (/^VER-/.test(ancre)) { const c = document.getElementById(ancre); if (c) { c.classList.add("neuve"); c.scrollIntoView({ behavior: "smooth", block: "start" }); } }
}
function carteVersion(v) {
  const art = document.createElement("article");
  art.className = "prop"; art.id = v.reference;
  const meta = [
    v.nb_fiches ? v.nb_fiches + " " + M("sheets", "fiches") : "",
    v.taille ? taille(v.taille) : "",
    (v.telechargements || 0) + " " + M("downloads", "téléchargements"),
    esc(v.auteur || M("Anonymous", "Anonyme")),
    PC.date(v.cree_le),
  ].filter(Boolean).join(" · ");
  art.innerHTML = `
    <div class="prop-vote"><button type="button" class="vote" aria-label="${M("Vote", "Voter")}"><span aria-hidden="true">▲</span><b>0</b></button></div>
    <div class="prop-corps">
      <div class="prop-tete"><span class="tag">${esc(nomLangue(v.langue))}</span>${v.communaute ? `<span class="tag st-com">${esc(v.communaute)}</span>` : ""}</div>
      <h3>${esc(v.nom)}</h3>
      ${v.description ? `<p class="prop-extrait">${esc(v.description)}</p>` : ""}
      <div class="prop-meta small dim">${meta}</div>
      <div class="prop-actions">
        <button type="button" class="btn primary" data-dl>${M("Download", "Télécharger")}</button>
        <button type="button" class="lien" data-ouvrir>${M("Comments", "Commentaires")}</button>
        <button type="button" class="lien" data-partager>${M("Copy the link", "Copier le lien")}</button>
      </div>
      <div class="prop-detail" hidden></div>
    </div>`;
  boutonVote(art.querySelector(".vote"), v.reference, v.votes);
  const dl = art.querySelector("[data-dl]");
  dl.onclick = async () => {
    dl.disabled = true; const t = dl.textContent; dl.textContent = M("Downloading…", "Téléchargement…");
    try {
      enregistrer(await PL.fichierVersion(v.fichier), "phenix-" + (slug(v.nom) || v.reference.toLowerCase()) + ".json");
      PL.compterTelechargement(v.reference);
    } catch (e) { alert(M("The download failed. Try again in a moment.", "Le téléchargement a échoué. Réessayez dans un instant.")); }
    dl.disabled = false; dl.textContent = t;
  };
  art.querySelector("[data-ouvrir]").onclick = () => {
    const d = art.querySelector(".prop-detail");
    d.hidden = !d.hidden;
    if (!d.hidden && !d.dataset.fait) { d.dataset.fait = "1"; PC.bloc(v.reference, d, null, { sansVote: true }); }
  };
  art.querySelector("[data-partager]").onclick = (e) => copierLien(e.currentTarget, v.reference);
  return art;
}

/* ---------- Les fiches écrites par les gens ---------- */
// Une proposition envoyée depuis l'application porte déjà son en-tête (id, axe, balises…) : on le relit.
function entete(texte) {
  const m = String(texte || "").replace(/\r/g, "").match(/^---\n([\s\S]*?)\n---\n?([\s\S]*)$/);
  if (!m) return { meta: {}, corps: String(texte || "").replace(/\r/g, "").trim() };
  const meta = {};
  for (const l of m[1].split("\n")) {
    const i = l.indexOf(":");
    if (i < 0) continue;
    let v = l.slice(i + 1).trim();
    if (v.startsWith("[") && v.endsWith("]")) v = v.slice(1, -1).split(/,(?=(?:[^"]*"[^"]*")*[^"]*$)/).map((s) => s.trim().replace(/^["']|["']$/g, "")).filter(Boolean);
    else v = v.replace(/^["']|["']$/g, "");
    meta[l.slice(0, i).trim()] = v;
  }
  return { meta, corps: m[2].trim() };
}
// La fiche d'une proposition, au format des fiches Phenix. Son identifiant est sa référence (SUB-2026-0001).
function enFiche(p) {
  const { meta, corps } = entete(p.contenu);
  const liste = (v) => (Array.isArray(v) ? v : v ? String(v).split(/[,\n]+/).map((s) => s.trim()).filter(Boolean) : []);
  return {
    id: p.reference, titre: p.titre || meta.titre || p.reference,
    axe: parseInt(meta.axe || p.axe, 10) || 3, categorie: meta.categorie || p.categorie || "",
    temps: meta.temps || "", contexte: meta.contexte || "", risque: meta.risque || "", materiel: meta.materiel || "",
    priorite: meta.priorite || (p.urgence ? "flash" : "normale"),
    tags: liste(meta.tags), sources: meta.sources ? liste(meta.sources) : String(p.sources || "").split(/\n+/).map((s) => s.trim()).filter(Boolean),
    corps, auteur: p.auteur || "", statut: p.statut || "submitted",
  };
}
function enMarkdown(f) {
  const q = (s) => '"' + String(s).replace(/"/g, "'") + '"';
  return `---
id: ${f.id}
titre: ${String(f.titre).replace(/\n/g, " ")}
axe: ${f.axe}
categorie: ${f.categorie}
temps: ${f.temps}
contexte: ${f.contexte}
risque: ${f.risque}
materiel: ${f.materiel}
priorite: ${f.priorite}
origine: communaute
tags: [${f.tags.join(", ")}]
sources: [${f.sources.map(q).join(", ")}]
---

${f.corps}
`;
}
let FICHES = [];
async function fiches() {
  const zone = document.getElementById("hubFiches");
  try {
    const l = (await PL.publiees()).filter((p) => p.type === "fiche");
    const votes = l.length && l[0].votes === undefined ? await PL.votes(l.map((p) => p.reference)).catch(() => ({})) : null;
    FICHES = l.map((p) => ({ ...p, votes: votes ? votes[p.reference] || 0 : p.votes || 0 }))
      .sort((a, b) => b.votes - a.votes || new Date(b.cree_le) - new Date(a.cree_le));
  } catch (e) {
    zone.innerHTML = `<p class="dim">${M("This part needs a connection.", "Cette partie demande une connexion.")}</p>`;
    return;
  }
  if (!FICHES.length) {
    zone.innerHTML = `<div class="lab-vide"><p>${M("No sheet published yet. Write the first one in Phenix Lab.", "Aucune fiche publiée pour l'instant. Écrivez la première dans Phenix Lab.")}</p>
      <a class="btn primary" href="lab.html#ecrire">${M("Write a sheet", "Écrire une fiche")}</a></div>`;
    return;
  }
  const STATUTS = { submitted: ["New", "Nouvelle"], under_review: ["In review", "En relecture"], changes_requested: ["Needs changes", "À reprendre"], community: ["Community", "Communautaire"], verified: ["Verified", "Vérifiée"], official: ["Official", "Officielle"] };
  zone.innerHTML = FICHES.map((p, i) => {
    const st = STATUTS[p.statut] || STATUTS.submitted;
    return `<article class="hub-fiche"><div>
        <h3><a href="lab.html#${esc(p.reference)}">${esc(p.titre)}</a></h3>
        <div class="small dim">${M(st[0], st[1])} · ▲ ${p.votes} · ${esc(p.auteur || M("Anonymous", "Anonyme"))} · ${PC.date(p.cree_le)} · ${esc(p.reference)}</div>
      </div><button type="button" class="btn" data-md="${i}" title="${M("Download this sheet", "Télécharger cette fiche")}">.md</button></article>`;
  }).join("");
  zone.querySelectorAll("[data-md]").forEach((b) => (b.onclick = () => {
    const p = FICHES[+b.dataset.md];
    enregistrer(enMarkdown(enFiche(p)), p.reference + ".md", "text/markdown");
  }));
  const tout = document.getElementById("hubToutes");
  tout.hidden = false;
  tout.onclick = () => {
    const l = FICHES.map(enFiche);
    const jour = new Date().toISOString().slice(0, 10);
    enregistrer(JSON.stringify({
      type: "phenix-fiches", format: 1, nom: M("Sheets written by people", "Fiches écrites par les gens"),
      source: location.origin + location.pathname, date: jour, licence: "CC BY-SA 4.0", nb_fiches: l.length, fiches: l,
    }), `phenix-fiches-communaute-${jour}.json`);
  };
}

/* ---------- Publier une version ---------- */
let LUE = null;   // le fichier choisi : { texte, j, taille }
document.getElementById("vFichier").onchange = async (e) => {
  const f = e.target.files[0], ap = document.getElementById("vApercu");
  LUE = null; ap.textContent = "";
  if (!f) return;
  if (f.size > 26214400) { ap.textContent = M("This file is over 25 MB.", "Ce fichier dépasse 25 Mo."); return; }
  try {
    const texte = await f.text(), j = JSON.parse(texte);
    if (j.type !== "phenix-version" || !Array.isArray(j.fiches) || !j.fiches.length) throw new Error("format");
    LUE = { texte, j, taille: f.size };
    ap.textContent = `${j.fiches.length} ${M("sheets", "fiches")} · ${taille(f.size)}`;
    const remplir = (id, v) => { const el = document.getElementById(id); if (el && !el.value && v) el.value = String(v).slice(0, +el.maxLength || 200); };
    if (!j.officielle) remplir("vNom", j.nom);
    remplir("vLangue", j.langue); remplir("vCommu", j.communaute); remplir("vDesc", j.description);
  } catch (err) {
    ap.textContent = M("This isn't a Phenix version file. Export yours from Phenix Base › Modules › Phenix Hub › Create my version.", "Ce n'est pas un fichier de version Phenix. Exportez la vôtre depuis Phenix Base › Modules › Phenix Hub › Créer ma version.");
  }
};
document.getElementById("formVersion").onsubmit = async (e) => {
  e.preventDefault();
  const retour = document.getElementById("retourVersion");
  if (val("vSite")) return;   // piège à robots
  if (!LUE) { message(retour, "ko", M("Choose the version file first.", "Choisissez d'abord le fichier de la version.")); return; }
  const b = document.getElementById("vEnvoyer"), t = b.textContent;
  b.disabled = true; b.textContent = M("Sending…", "Envoi…");
  try {
    const r = await PL.publierVersion({
      nom: val("vNom"), langue: val("vLangue"), communaute: val("vCommu"), description: val("vDesc"),
      base: String(LUE.j.base || LUE.j.empreinte || "").slice(0, 40), nb_fiches: LUE.j.fiches.length, taille: LUE.taille,
      auteur: val("vAuteur"), contact: val("vContact"),
    });
    await PL.deposerVersion(r.fichier, LUE.texte);
    message(retour, "ok", M(`Received, thank you. Reference <b>${esc(r.reference)}</b>. The team checks it, then it shows up here for everyone.`, `Bien reçue, merci. Référence <b>${esc(r.reference)}</b>. L'équipe la vérifie, puis elle apparaît ici pour tout le monde.`));
    e.target.reset(); LUE = null; document.getElementById("vApercu").textContent = "";
  } catch (err) {
    const pasPret = /publier_version|schema cache|does not exist|404/i.test(err.message);
    message(retour, "ko", pasPret
      ? M("Publishing opens very soon. Keep your file: it will be ready.", "L'envoi ouvre très bientôt. Gardez votre fichier : il sera prêt.")
      : esc(err.message));
  }
  b.disabled = false; b.textContent = t;
};

versions();
fiches();
// Changer de langue réécrit aussi ce que ce script a affiché.
document.querySelectorAll(".lang").forEach((b) => b.addEventListener("click", () => setTimeout(() => { versions(); fiches(); }, 0)));
