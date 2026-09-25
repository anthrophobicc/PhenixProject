/* =========================================================================
   PHENIX LAB — envoi d'une proposition
   Remplacez les deux valeurs ci-dessous par celles de votre projet Supabase.
   Elles se trouvent dans Supabase → Project Settings → API.
   La clé « anon » est publique par nature : c'est prévu pour, à condition
   que les règles de sécurité soient bien celles décrites dans BACKEND.md.
   ========================================================================= */
const SUPABASE_URL = "https://VOTRE-PROJET.supabase.co";
const SUPABASE_ANON = "VOTRE_CLE_ANON";

const form = document.getElementById("form");
const retour = document.getElementById("retour");
const bouton = document.getElementById("submit");

let sb = null;
try {
  if (!SUPABASE_URL.includes("VOTRE-PROJET")) {
    sb = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON);
  }
} catch (e) { /* la bibliothèque n'a pas chargé : on le gère à l'envoi */ }

function message(type, html) {
  retour.innerHTML = `<div class="msg ${type}">${html}</div>`;
  retour.scrollIntoView({ behavior: "smooth", block: "center" });
}

/* Un identifiant lisible, du type SUB-2026-0042.
   Le numéro définitif est attribué par la base ; celui-ci sert d'accusé
   de réception immédiat pour la personne. */
function referenceProvisoire() {
  const an = new Date().getFullYear();
  const n = Math.floor(Math.random() * 9000 + 1000);
  return `SUB-${an}-${n}`;
}

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  // Piège à robots : si ce champ est rempli, on fait semblant d'accepter.
  if (document.getElementById("site").value) {
    message("ok", "Contribution reçue.");
    return;
  }

  const titre = document.getElementById("titre").value.trim();
  const contenu = document.getElementById("contenu").value.trim();

  if (titre.length < 4) return message("ko", "Le titre est trop court.");
  if (contenu.length < 200) {
    return message("ko",
      "La fiche fait moins de 200 caractères. Une proposition doit être suffisamment " +
      "développée pour être évaluée — reprenez l'aide au-dessus si besoin.");
  }

  bouton.disabled = true;
  bouton.textContent = "Envoi en cours…";

  const proposition = {
    titre,
    contenu,
    resume: document.getElementById("resume").value.trim() || null,
    axe: document.getElementById("axe").value ? Number(document.getElementById("axe").value) : null,
    categorie: document.getElementById("categorie").value.trim() || null,
    langue: document.getElementById("langue").value,
    urgence: document.getElementById("urgence").value === "urgence",
    sources: document.getElementById("sources").value.trim() || null,
    note_editeur: document.getElementById("note").value.trim() || null,
    auteur: document.getElementById("auteur").value.trim() || null,
    contact: document.getElementById("contact").value.trim() || null,
    statut: "submitted"
  };

  // --- Si le backend n'est pas encore branché, on n'abandonne pas la personne :
  //     on lui rend son travail sous forme de fichier.
  if (!sb) {
    const fichier = construireMarkdown(proposition);
    telecharger(fichier, (titre.replace(/\W+/g, "-").toLowerCase() || "fiche") + ".md");
    bouton.disabled = false;
    bouton.textContent = "Envoyer ma proposition";
    return message("info",
      "<strong>L'envoi automatique n'est pas encore actif.</strong><br>" +
      "Votre fiche vient d'être téléchargée sur votre appareil au format .md. " +
      "Rien n'est perdu : envoyez ce fichier par le canal indiqué sur la page d'accueil.");
  }

  try {
    const { data, error } = await sb.from("propositions").insert(proposition).select("reference").single();
    if (error) throw error;

    // Images, une fois la proposition créée (elles y sont rattachées).
    const fichiers = document.getElementById("images").files;
    let envoyees = 0, ratees = 0;
    for (const f of fichiers) {
      if (f.size > 5 * 1024 * 1024) { ratees++; continue; }
      const chemin = `${data.reference}/${Date.now()}-${f.name.replace(/[^\w.\-]/g, "_")}`;
      const { error: eImg } = await sb.storage.from("propositions").upload(chemin, f);
      if (eImg) ratees++; else envoyees++;
    }

    form.reset();
    message("ok",
      `<strong>Contribution reçue.</strong><br>` +
      `Référence : <strong>${data.reference}</strong> — notez-la si vous souhaitez en reparler.<br>` +
      (envoyees ? `${envoyees} image(s) jointe(s).<br>` : "") +
      (ratees ? `<em>${ratees} image(s) n'ont pas pu être envoyées.</em><br>` : "") +
      `Elle sera examinée avant toute intégration au corpus Phenix.`);
  } catch (err) {
    // On ne laisse jamais quelqu'un perdre ce qu'il vient d'écrire.
    const fichier = construireMarkdown(proposition);
    telecharger(fichier, (titre.replace(/\W+/g, "-").toLowerCase() || "fiche") + ".md");
    message("ko",
      "<strong>L'envoi a échoué.</strong><br>" +
      "Votre fiche vient d'être téléchargée sur votre appareil pour que rien ne soit perdu. " +
      "Réessayez plus tard, ou envoyez le fichier par un autre canal.<br>" +
      `<span class="small">Détail : ${err.message || err}</span>`);
  } finally {
    bouton.disabled = false;
    bouton.textContent = "Envoyer ma proposition";
  }
});

/* Reconstruit une fiche au format Phenix, prête à être ouverte dans l'application. */
function construireMarkdown(p) {
  const sources = (p.sources || "").split("\n").map(s => s.trim()).filter(Boolean);
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
sources: [${sources.map(s => '"' + s.replace(/"/g, "'") + '"').join(", ")}]
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
