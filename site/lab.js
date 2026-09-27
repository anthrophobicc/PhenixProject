/* =========================================================================
   PHENIX LAB : l'atelier de la communauté.
   Onglets : Propositions (voter, commenter, trier), Proposer une idée, Écrire une fiche.
   L'envoi passe par en-ligne.js (base Supabase du projet). Si l'envoi échoue,
   la personne récupère son texte en fichier .md : on ne perd jamais un travail.
   ========================================================================= */
const REDDIT = "https://www.reddit.com/r/PhenixProject/";
const TICKET = "https://github.com/anthrophobicc/PhenixProject/issues/new?template=proposer-fiche.md";
const PL = window.PHENIX_EN_LIGNE;
const PC = window.PhenixCommunaute;
const M = (en, fr) => (document.documentElement.lang === "fr" ? fr : en);
// D'où vient la personne : ?origine=story sur le lien d'une story Instagram, ?origine=bio sur la bio…
const ORIGINE = (new URLSearchParams(location.search).get("origine") || "site").slice(0, 40);
const val = (id) => (document.getElementById(id) ? document.getElementById(id).value.trim() : "");
function message(zone, type, html, defiler = true) {
  zone.innerHTML = `<div class="msg ${type}">${html}</div>`;
  if (defiler) zone.scrollIntoView({ behavior: "smooth", block: "center" });
}

/* ---------- Onglets ---------- */
const ONGLETS = ["propositions", "idee", "ecrire"];
function montrer(onglet, garderHash) {
  if (!ONGLETS.includes(onglet)) onglet = "propositions";
  ONGLETS.forEach((o) => {
    document.getElementById("o-" + o).hidden = o !== onglet;
    const b = document.querySelector(`[data-onglet="${o}"]`);
    b.classList.toggle("on", o === onglet); b.setAttribute("aria-selected", o === onglet ? "true" : "false");
  });
  if (!garderHash) history.replaceState(null, "", location.pathname + location.search + "#" + onglet);
}
document.querySelectorAll("[data-onglet]").forEach((b) => (b.onclick = () => montrer(b.dataset.onglet)));

/* ---------- Les propositions ---------- */
const TYPES = { fiche: ["Sheet", "Fiche"], idee: ["Idea", "Idée"], correction: ["Correction", "Correction"], message: ["Message", "Message"] };
const STATUTS = {
  submitted: ["New", "Nouvelle", "st-new"], under_review: ["In review", "En relecture", "st-rev"], changes_requested: ["Needs changes", "À reprendre", "st-rev"],
  community: ["Community", "Communautaire", "st-com"], verified: ["Verified", "Vérifiée", "st-ver"], official: ["Official", "Officielle", "st-off"],
};
let TOUTES = [], TRI = "top", FILTRE = "", OUVERTE = null;
const MIENNES = "phenix-mes-propositions";
const miennes = () => { try { return JSON.parse(localStorage.getItem(MIENNES) || "[]"); } catch (e) { return []; } };
function garderMienne(p) { try { const l = miennes().filter((x) => x.reference !== p.reference); l.unshift(p); localStorage.setItem(MIENNES, JSON.stringify(l.slice(0, 50))); } catch (e) {} }
// Le texte d'une proposition, mis en forme simplement (titres, gras, listes), sans jamais interpréter de HTML.
function mdSimple(t) {
  let x = String(t || "").replace(/\r/g, "").replace(/^---\n[\s\S]*?\n---\n?/, "");
  x = PC.esc(x);
  return x.split(/\n{2,}/).map((bloc) => {
    const b = bloc.trim();
    if (!b) return "";
    if (/^#{2,3} /.test(b)) return "<h4>" + b.replace(/^#{2,3} /, "") + "</h4>";
    const lignes = b.split("\n").map((l) => l
      .replace(/\*\*(.+?)\*\*/g, "<b>$1</b>")
      .replace(/^::(.+)::$/, "<i>$1</i>")
      .replace(/^[-*] (.+)$/, "• $1")
      .replace(/\[\[([A-Z0-9-]+)\]\]/g, "<span class='ref'>$1</span>"));
    return "<p>" + lignes.join("<br>") + "</p>";
  }).join("");
}

async function charger() {
  const zone = document.getElementById("liste-communaute");
  try {
    const l = await PL.publiees();
    const refs = l.map((p) => p.reference);
    // Votes et nombre de commentaires : lus à part, pour marcher avec ou sans les compteurs de la vue.
    const [votes, nbCom] = await Promise.all([
      l.length && l[0].votes === undefined ? PL.votes(refs).catch(() => ({})) : Promise.resolve(null),
      l.length && l[0].commentaires === undefined ? PL.nbCommentaires(refs).catch(() => ({})) : Promise.resolve(null),
    ]);
    TOUTES = l.map((p) => ({ ...p, votes: votes ? votes[p.reference] || 0 : p.votes || 0, commentaires: nbCom ? nbCom[p.reference] || 0 : p.commentaires || 0 }));
    const publiques = new Set(TOUTES.map((p) => p.reference));
    for (const m of miennes()) if (!publiques.has(m.reference)) TOUTES.push({ ...m, votes: 0, commentaires: 0, statut: "submitted", _attente: true });
    document.getElementById("nbProps").textContent = TOUTES.length ? " " + TOUTES.length : "";
    afficher();
  } catch (err) {
    zone.innerHTML = `<p class="dim">${M("Phenix Lab needs a connection. The rest of Phenix works without one.", "Phenix Lab demande une connexion. Tout le reste de Phenix marche sans.")}</p>`;
  }
}
function afficher() {
  const zone = document.getElementById("liste-communaute");
  let l = TOUTES.filter((p) => !FILTRE || p.type === FILTRE);
  l.sort(TRI === "top" ? (a, b) => b.votes - a.votes || new Date(b.cree_le) - new Date(a.cree_le) : (a, b) => new Date(b.cree_le) - new Date(a.cree_le));
  l.sort((a, b) => (b._attente ? 1 : 0) - (a._attente ? 1 : 0));
  if (!l.length) {
    zone.innerHTML = `<div class="lab-vide"><p>${M("Nothing here yet. Be the first: an idea takes ten seconds.", "Rien ici pour l'instant. Soyez le premier : une idée prend dix secondes.")}</p>
      <button type="button" class="btn primary" data-aller="idee">${M("Suggest an idea", "Proposer une idée")}</button></div>`;
    zone.querySelector("[data-aller]").onclick = () => montrer("idee");
    return;
  }
  zone.innerHTML = "";
  for (const p of l) zone.appendChild(carte(p));
  if (OUVERTE) { const c = document.getElementById(OUVERTE); if (c) { ouvrir(c, TOUTES.find((x) => x.reference === OUVERTE)); c.scrollIntoView({ behavior: "smooth", block: "start" }); } OUVERTE = null; }
}
function carte(p) {
  const art = document.createElement("article");
  art.className = "prop"; art.id = p.reference;
  const t = TYPES[p.type] || TYPES.fiche, st = p._attente ? ["Yours · awaiting review", "La vôtre · en attente de relecture", "st-new"] : STATUTS[p.statut] || STATUTS.submitted;
  if (p._attente) art.classList.add("attente");
  // L'extrait de la carte : le texte sans les signes de mise en forme.
  const texte = String(p.resume || p.contenu || "").replace(/^---[\s\S]*?\n---/, "").replace(/[#*:]+|\[\[|\]\]/g, "").replace(/^\s*[-•]\s+/gm, "").replace(/\s+/g, " ").trim();
  art.innerHTML = `
    <div class="prop-vote"><button type="button" class="vote${PL.aVote(p.reference) ? " on" : ""}" aria-label="${M("Vote", "Voter")}"${p._attente ? " disabled" : ""}><span aria-hidden="true">▲</span><b>${p.votes}</b></button></div>
    <div class="prop-corps">
      <div class="prop-tete"><span class="tag">${M(t[0], t[1])}</span><span class="tag ${st[2]}">${M(st[0], st[1])}</span></div>
      <h3>${PC.esc(p.titre)}</h3>
      ${texte && texte !== p.titre ? `<p class="prop-extrait">${PC.esc(texte.slice(0, 240))}${texte.length > 240 ? "…" : ""}</p>` : ""}
      <div class="prop-meta small dim">${PC.esc(p.auteur || M("Anonymous", "Anonyme"))} · ${PC.date(p.cree_le)} · ${p.reference}</div>
      <div class="prop-actions">
        <button type="button" class="lien" data-ouvrir>${p._attente ? M("Read", "Lire") : M("Read and comment", "Lire et commenter") + " (" + p.commentaires + ")"}</button>
        ${p._attente ? `<span class="small dim">${M("Only you see it until the team publishes it.", "Vous seul la voyez tant que l'équipe ne l'a pas publiée.")}</span>` : `<button type="button" class="lien" data-partager>${M("Copy the link", "Copier le lien")}</button>`}
      </div>
      <div class="prop-detail" hidden></div>
    </div>`;
  const vb = art.querySelector(".vote");
  vb.onclick = async () => {
    vb.disabled = true;
    try { const n = await PL.voter(p.reference, PL.aVote(p.reference)); p.votes = n; vb.querySelector("b").textContent = n; vb.classList.toggle("on", PL.aVote(p.reference)); }
    catch (e) { message(document.getElementById("retourLab"), "ko", PC.esc(e.message), false); }
    vb.disabled = false;
  };
  art.querySelector("[data-ouvrir]").onclick = () => ouvrir(art, p);
  if (art.querySelector("[data-partager]")) art.querySelector("[data-partager]").onclick = (e) => {
    const lien = location.origin + location.pathname + "#" + p.reference, b = e.currentTarget;
    const ok = () => { b.textContent = M("Link copied", "Lien copié"); setTimeout(() => (b.textContent = M("Copy the link", "Copier le lien")), 1800); };
    if (navigator.clipboard) navigator.clipboard.writeText(lien).then(ok).catch(() => prompt(M("Copy this link:", "Copiez ce lien :"), lien));
    else prompt(M("Copy this link:", "Copiez ce lien :"), lien);
  };
  return art;
}
function ouvrir(art, p) {
  const d = art.querySelector(".prop-detail");
  if (!d.hidden) { d.hidden = true; return; }
  d.hidden = false;
  d.innerHTML = `<div class="prop-texte">${mdSimple(p.contenu)}</div>${p.sources ? `<div class="small dim"><b>Sources</b><br>${PC.esc(p.sources).replace(/\n/g, "<br>")}</div>` : ""}<div class="prop-commu"></div>`;
  if (!p._attente) PC.bloc(p.reference, d.querySelector(".prop-commu"), null, { sansVote: true });
}
document.querySelectorAll("[data-tri]").forEach((b) => (b.onclick = () => {
  TRI = b.dataset.tri; document.querySelectorAll("[data-tri]").forEach((x) => x.classList.toggle("on", x === b)); afficher();
}));
document.getElementById("filtreType").onchange = (e) => { FILTRE = e.target.value; afficher(); };

// Après un envoi : on montre la proposition dans le fil, prête à être partagée.
async function apresEnvoi(ref, p) {
  garderMienne({ reference: ref, type: p.type, titre: p.titre, contenu: p.contenu, resume: p.resume || null, auteur: p.auteur || null, sources: p.sources || null, cree_le: new Date().toISOString() });
  TRI = "new"; document.querySelectorAll("[data-tri]").forEach((x) => x.classList.toggle("on", x.dataset.tri === "new"));
  montrer("propositions");
  OUVERTE = ref;
  await charger();
  const zone = document.getElementById("retourLab");
  const carteNeuve = document.getElementById(ref), publique = TOUTES.some((x) => x.reference === ref && !x._attente);
  if (carteNeuve) carteNeuve.classList.add("neuve");
  if (publique) {
    message(zone, "ok", M(`<strong>It's live.</strong> Reference ${ref}. Share its link so people vote for it.`, `<strong>C'est en ligne.</strong> Référence ${ref}. Partagez son lien pour que les gens votent.`), false);
  } else {
    message(zone, "ok", M(`<strong>Received.</strong> Reference ${ref}. You can see it below; everyone will see it once the team has published it.`, `<strong>C'est reçu.</strong> Référence ${ref}. Vous la voyez ci-dessous ; tout le monde la verra dès que l'équipe l'aura publiée.`), false);
  }
}

/* ---------- L'idée en dix secondes ---------- */
document.getElementById("formIdee").addEventListener("submit", async (e) => {
  e.preventDefault();
  const zone = document.getElementById("retourIdee");
  if (val("idSite")) return message(zone, "ok", M("Thanks, it's in.", "Merci, c'est reçu."));
  const idee = val("ideeTexte");
  if (idee.length < 3) return message(zone, "ko", M("Write at least a few words.", "Écrivez au moins quelques mots."));
  const b = e.target.querySelector("button[type=submit]");
  b.disabled = true;
  try {
    const p = {
      type: "idee", titre: idee.slice(0, 140), contenu: val("ideeDetail") || idee, langue: document.documentElement.lang,
      auteur: val("ideeAuteur") || null, contact: val("ideeContact") || null, origine: ORIGINE,
    };
    const ref = await PL.proposer(p);
    e.target.reset(); zone.innerHTML = "";
    await apresEnvoi(ref, p);
  } catch (err) {
    message(zone, "ko", M("Sending failed: ", "L'envoi a échoué : ") + PC.esc(err.message) + M(`. You can also post it on <a href="${REDDIT}" rel="noopener">r/PhenixProject</a>.`, `. Vous pouvez aussi la poster sur <a href="${REDDIT}" rel="noopener">r/PhenixProject</a>.`));
  } finally { b.disabled = false; }
});

/* ---------- La fiche complète ---------- */
const form = document.getElementById("form");
const retour = document.getElementById("retour");
const bouton = document.getElementById("submit");
form.addEventListener("submit", async (e) => {
  e.preventDefault();
  if (val("site")) return message(retour, "ok", M("Contribution received.", "Contribution reçue."));
  const titre = val("titre"), contenu = val("contenu");
  if (titre.length < 4) return message(retour, "ko", M("The title is too short.", "Le titre est trop court."));
  if (contenu.length < 200) {
    return message(retour, "ko", M(
      "The sheet is under 200 characters. A proposal needs enough substance to be reviewed: see the guide above if needed. For a quick idea, use the Suggest an idea tab.",
      "La fiche fait moins de 200 caractères. Une proposition doit être assez développée pour être relue : reprenez l'aide au-dessus si besoin. Pour une simple idée, utilisez l'onglet Proposer une idée."));
  }
  bouton.disabled = true;
  bouton.textContent = M("Sending…", "Envoi en cours…");
  const proposition = {
    type: "fiche", titre, contenu,
    resume: val("resume") || null, axe: val("axe") || null, categorie: val("categorie") || null,
    langue: val("langue"), urgence: val("urgence") === "urgence",
    sources: val("sources") || null, note_editeur: val("note") || null,
    auteur: val("auteur") || null, contact: val("contact") || null, origine: ORIGINE,
  };
  const nomFichier = (titre.replace(/\W+/g, "-").toLowerCase() || "fiche") + ".md";
  try {
    const ref = await PL.proposer(proposition);
    for (const f of document.getElementById("images").files) {
      if (f.size <= 5 * 1024 * 1024) { try { await PL.image(ref, f); } catch (x) { /* l'image manquante n'empêche rien */ } }
    }
    form.reset(); retour.innerHTML = "";
    await apresEnvoi(ref, proposition);
  } catch (err) {
    telecharger(construireMarkdown(proposition), nomFichier);
    message(retour, "ko", M(
      "<strong>Sending failed.</strong><br>Your sheet was just saved on your device so nothing is lost. Try again later, or ",
      "<strong>L'envoi a échoué.</strong><br>Votre fiche vient d'être enregistrée sur votre appareil pour que rien ne soit perdu. Réessayez plus tard, ou ") +
      M(`post it on <a href="${REDDIT}" rel="noopener">r/PhenixProject</a>, or <a href="${TICKET}" rel="noopener">open a ticket on GitHub</a> and attach it.`,
        `publiez-la sur <a href="${REDDIT}" rel="noopener">r/PhenixProject</a>, ou <a href="${TICKET}" rel="noopener">ouvrez un ticket sur GitHub</a> et joignez-la.`) +
      `<br><span class="small">${M("Detail", "Détail")} : ${PC.esc(err.message || err)}</span>`);
  } finally {
    bouton.disabled = false;
    bouton.textContent = M("Send my proposal", "Envoyer ma proposition");
  }
});

/* ---------- Démarrage : l'onglet ou la proposition demandés par le lien ---------- */
const cible = decodeURIComponent(location.hash.slice(1));
if (/^SUB-\d{4}-\d+$/.test(cible)) { OUVERTE = cible; TRI = "new"; document.querySelectorAll("[data-tri]").forEach((x) => x.classList.toggle("on", x.dataset.tri === "new")); montrer("propositions", true); }
else montrer(cible === "communaute" ? "propositions" : cible, !cible);
charger();

/* Reconstruit une fiche au format Phenix, prête à être ouverte dans l'application. */
function construireMarkdown(p) {
  const sources = (p.sources || "").split("\n").map((s) => s.trim()).filter(Boolean);
  return `---
id: SUB-${Date.now()}
titre: ${p.titre}
axe: ${p.axe || 3}
categorie: ${p.categorie || ""}
temps:
contexte:
risque:
materiel:
priorite: ${p.urgence ? "flash" : "normale"}
origine: communaute
langue: ${p.langue}
tags: []
sources: [${sources.map((s) => '"' + s.replace(/"/g, "'") + '"').join(", ")}]
---

${p.contenu}
`;
}
function telecharger(texte, nom) {
  const b = new Blob([texte], { type: "text/markdown" });
  const u = URL.createObjectURL(b);
  const a = document.createElement("a");
  a.href = u; a.download = nom; a.click();
  URL.revokeObjectURL(u);
}
