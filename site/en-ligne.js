/* Phenix en ligne : envoyer une proposition, voter, commenter, lire ce que la communauté a publié.
   La base est un projet Supabase. La clé ci-dessous est une clé « publishable » : elle est publique par nature.
   La base n'accepte que ce que ses fonctions autorisent (voir supabase/01-propositions.sql) :
   rien ne se lit en dehors des vues publiques, et les contacts ne sortent jamais. */
window.PHENIX_EN_LIGNE = (function () {
  var BASE = "https://ecdyahykwtqdierxlemb.supabase.co";
  var CLE = "sb_publishable_SfcRbMXVNVstCE8eIURTUA_PiLJAu92";

  function appel(chemin, options) {
    options = options || {};
    var entetes = { apikey: CLE };
    if (options.json !== undefined) entetes["Content-Type"] = "application/json";
    for (var k in options.entetes || {}) entetes[k] = options.entetes[k];
    return fetch(BASE + chemin, {
      method: options.methode || "GET",
      headers: entetes,
      body: options.json !== undefined ? JSON.stringify(options.json) : options.corps,
    }).then(function (r) {
      return r.text().then(function (t) {
        var c = null;
        try { c = t ? JSON.parse(t) : null; } catch (e) { c = t; }
        if (!r.ok) throw new Error((c && c.message) || "HTTP " + r.status);
        return c;
      });
    });
  }
  var rpc = function (fonction, args) { return appel("/rest/v1/rpc/" + fonction, { methode: "POST", json: args }); };
  var lire = function (vue, requete) { return appel("/rest/v1/" + vue + "?" + requete); };

  // Un identifiant tiré au hasard et gardé sur l'appareil : un vote par personne, sans compte.
  function appareil() {
    try {
      var a = localStorage.getItem("phenix-appareil");
      if (!a) { a = (crypto.randomUUID ? crypto.randomUUID() : Date.now() + "-" + Math.random().toString(36).slice(2)) + "-phx"; localStorage.setItem("phenix-appareil", a); }
      return a;
    } catch (e) { return "session-" + Date.now() + "-" + Math.random().toString(36).slice(2); }
  }
  function aVote(cible, oui) {
    try {
      var l = JSON.parse(localStorage.getItem("phenix-votes") || "[]");
      if (oui === undefined) return l.indexOf(cible) >= 0;
      l = l.filter(function (x) { return x !== cible; });
      if (oui) l.push(cible);
      localStorage.setItem("phenix-votes", JSON.stringify(l));
    } catch (e) { return false; }
  }

  return {
    proposer: function (p) { return rpc("proposer", { p: p }); },
    signaler: function (p) { return rpc("signaler", { p: p }); },
    commenter: function (cible, texte, auteur) { return rpc("commenter", { p: { cible: cible, texte: texte, auteur: auteur || null } }); },
    voter: function (cible, retirer) {
      return rpc("voter", { cible: cible, appareil: appareil(), retirer: !!retirer }).then(function (n) { aVote(cible, !retirer); return n; });
    },
    aVote: function (cible) { return aVote(cible); },
    votes: function (cibles) {
      if (!cibles.length) return Promise.resolve({});
      return lire("votes_publics", "select=cible,votes&cible=in.(" + cibles.map(encodeURIComponent).join(",") + ")").then(function (l) {
        var o = {}; (l || []).forEach(function (x) { o[x.cible] = x.votes; }); return o;
      });
    },
    nbCommentaires: function (cibles) {
      if (!cibles.length) return Promise.resolve({});
      return lire("commentaires_publics", "select=cible&cible=in.(" + cibles.map(encodeURIComponent).join(",") + ")").then(function (l) {
        var o = {}; (l || []).forEach(function (x) { o[x.cible] = (o[x.cible] || 0) + 1; }); return o;
      });
    },
    commentaires: function (cible) { return lire("commentaires_publics", "select=id,auteur,texte,cree_le&order=cree_le.asc&cible=eq." + encodeURIComponent(cible)); },
    publiees: function () { return lire("propositions_publiques", "select=*&order=cree_le.desc&limit=200"); },
    image: function (reference, fichier) {
      var nom = reference + "/" + Date.now() + "-" + encodeURIComponent(fichier.name.replace(/[^\w.\-]/g, "_"));
      return appel("/storage/v1/object/propositions/" + nom, { methode: "POST", corps: fichier, entetes: { "Content-Type": fichier.type || "application/octet-stream" } });
    },
    // Phenix Hub : les versions publiées par les communautés (voir supabase/03-hub.sql).
    versions: function () { return lire("versions_publiques", "select=*&order=votes.desc,cree_le.desc&limit=100"); },
    publierVersion: function (m) { return rpc("publier_version", { p: m }); },
    deposerVersion: function (chemin, texte) {
      return appel("/storage/v1/object/versions/" + chemin.split("/").map(encodeURIComponent).join("/"), { methode: "POST", corps: texte, entetes: { "Content-Type": "application/json" } });
    },
    fichierVersion: function (chemin) {
      return fetch(BASE + "/storage/v1/object/versions/" + chemin.split("/").map(encodeURIComponent).join("/"), { headers: { apikey: CLE } })
        .then(function (r) { if (!r.ok) throw new Error("HTTP " + r.status); return r.text(); });
    },
    compterTelechargement: function (ref) { return rpc("compter_telechargement", { ref: ref }).catch(function () { return null; }); },
  };
})();
