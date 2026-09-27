/* Le bloc communautaire sous une fiche ou une proposition : « utile » (un vote par appareil) et commentaires.
   Tout passe par en-ligne.js. Hors connexion, le bloc le dit simplement et la page reste lisible. */
window.PhenixCommunaute = (function () {
  var L = function (en, fr) { return document.documentElement.lang === "fr" ? fr : en; };
  var esc = function (s) { return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#x27;" }[c]; }); };
  var date = function (d) {
    try { return new Date(d).toLocaleDateString(document.documentElement.lang === "fr" ? "fr-FR" : "en-GB", { day: "numeric", month: "short", year: "numeric" }); }
    catch (e) { return ""; }
  };
  var PL = window.PHENIX_EN_LIGNE;

  function boutonVote(cible, n) {
    var b = document.createElement("button");
    b.type = "button";
    b.className = "btn vote" + (PL.aVote(cible) ? " on" : "");
    var peindre = function (k) {
      b.innerHTML = '<span aria-hidden="true">▲</span> ' + L("Useful", "Utile") + ' <b>' + (k || 0) + "</b>";
      b.classList.toggle("on", PL.aVote(cible));
      b.setAttribute("aria-pressed", PL.aVote(cible) ? "true" : "false");
    };
    peindre(n);
    b.onclick = function () {
      b.disabled = true;
      PL.voter(cible, PL.aVote(cible)).then(peindre).catch(function (e) { alerteDans(b.parentNode, e.message); }).then(function () { b.disabled = false; });
    };
    return b;
  }
  function alerteDans(el, t) {
    var m = el.querySelector(".commu-msg") || el.appendChild(document.createElement("p"));
    m.className = "commu-msg small"; m.textContent = t;
  }

  // Monte le bloc dans « conteneur » pour la cible (identifiant de fiche ou référence de proposition).
  function bloc(cible, conteneur, votesConnus, options) {
    options = options || {};
    conteneur.classList.add("commu");
    conteneur.innerHTML = '<div class="commu-barre"></div><div class="commu-liste"></div>' +
      '<form class="commu-form" autocomplete="off">' +
      '<textarea required minlength="2" maxlength="2000" placeholder="' + esc(L("Add something: a tip, a correction, your experience…", "Ajoutez quelque chose : une astuce, une correction, votre expérience…")) + '"></textarea>' +
      '<div class="commu-envoi"><input maxlength="40" placeholder="' + esc(L("Nickname (optional)", "Pseudo (facultatif)")) + '">' +
      '<button class="btn primary" type="submit">' + L("Comment", "Commenter") + "</button></div></form>";
    var barre = conteneur.querySelector(".commu-barre"), liste = conteneur.querySelector(".commu-liste"), form = conteneur.querySelector("form");
    var montrerVotes = function (n) {
      barre.innerHTML = "";
      if (!options.sansVote) barre.appendChild(boutonVote(cible, n));
      var nb = document.createElement("span"); nb.className = "small dim commu-nb"; barre.appendChild(nb);
    };
    if (votesConnus || options.sansVote) montrerVotes(votesConnus ? votesConnus[cible] : 0);
    else PL.votes([cible]).then(function (o) { montrerVotes(o[cible]); }).catch(function () { montrerVotes(0); });
    var charger = function () {
      return PL.commentaires(cible).then(function (l) {
        var nb = conteneur.querySelector(".commu-nb");
        if (nb) nb.textContent = l.length ? l.length + " " + (l.length > 1 ? L("comments", "commentaires") : L("comment", "commentaire")) : "";
        liste.innerHTML = l.map(function (c) {
          return '<div class="commu-com"><div class="small dim"><b>' + esc(c.auteur || L("Anonymous", "Anonyme")) + "</b> · " + date(c.cree_le) + "</div><p>" + esc(c.texte) + "</p></div>";
        }).join("");
      }).catch(function () {
        liste.innerHTML = '<p class="small dim">' + L("Comments need a connection.", "Les commentaires demandent une connexion.") + "</p>";
      });
    };
    charger();
    form.onsubmit = function (e) {
      e.preventDefault();
      var t = form.querySelector("textarea"), a = form.querySelector("input"), b = form.querySelector("button");
      if (t.value.trim().length < 2) return;
      b.disabled = true;
      PL.commenter(cible, t.value.trim(), a.value.trim()).then(function () {
        t.value = ""; return charger();
      }).catch(function (err) { alerteDans(conteneur, err.message); }).then(function () { b.disabled = false; });
    };
  }
  return { bloc: bloc, esc: esc, date: date, L: L };
})();

// Sous une fiche du site : le bloc se monte tout seul dans #communaute[data-cible].
(function () {
  var el = document.getElementById("communaute");
  if (el && el.dataset.cible) window.PhenixCommunaute.bloc(el.dataset.cible, el);
})();
