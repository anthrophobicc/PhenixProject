// Écrans du Phenix 001 pour la story « l'entrepôt » (rendu 3D Blender) : 1116 × 676 px, encre électronique.
// Veille, démarrage, puis compteurs qui montent pendant que les fiches du monde entier arrivent.
// Usage : node ecrans-entrepot.js  → communication/3d/ecrans-entrepot/*.png
const fs = require("fs");
const path = require("path");
const { lancer } = require("../../communication/moteur/cdp");

const SORTIE = path.join(__dirname, "ecrans-entrepot");
const LOGO = "data:image/png;base64," + fs.readFileSync(path.join(__dirname, "logo-hd.png")).toString("base64");
const N = 60; // images de compteurs (une mise à jour partielle toutes les 3 images du film)
const FIN = { fiches: 1284016, cartes: 38420, langues: 112, pays: 194 };
const ARRIVEES = [
  ["Deutschland", 12408], ["Brasil", 9311], ["日本", 7702], ["Россия", 11265], ["Nigeria", 4180], ["España", 8034],
  ["Việt Nam", 3917], ["Ελλάδα", 2210], ["México", 6632], ["Polska", 5105], ["India", 14873], ["Kenya", 2688],
  ["Україна", 7340], ["Türkiye", 5921], ["Québec", 3066], ["Indonesia", 6480], ["Sverige", 2951], ["Maroc", 3377],
  ["Perú", 2742], ["Norge", 1904], ["Egypt", 4019], ["한국", 5213], ["Italia", 7788], ["Chile", 2530],
];

(async () => {
  fs.mkdirSync(SORTIE, { recursive: true });
  const p = await lancer();
  try {
    await p.aller("about:blank", 100);
    await p.eval(`window.logo = new Image(); logo.src = ${JSON.stringify(LOGO)}; logo.decode().then(() => true)`);
    const dessiner = async (nom, e) => {
      const png = await p.eval(`(async () => {
        const c = document.createElement("canvas"); c.width = 1116; c.height = 676;
        const g = c.getContext("2d"), e = ${JSON.stringify(e)}, s = 4;
        const encre = "#1C1B18", gris = "#6E6A62";
        g.fillStyle = "#E4E1D8"; g.fillRect(0, 0, c.width, c.height);
        for (let i = 0; i < 9000; i++) { g.fillStyle = "rgba(0,0,0," + (Math.random() * 0.025) + ")"; g.fillRect(Math.random() * c.width, Math.random() * c.height, 2, 2); }
        const txt = (t, x, y, taille, graisse, couleur, police, align) => { g.fillStyle = couleur || encre; g.textAlign = align || "left";
          g.font = (graisse || 500) + " " + taille * s + "px " + (police || "Arial, sans-serif"); g.fillText(t, x * s, y * s); };
        if (e.veille) {
          g.globalAlpha = 0.85; g.drawImage(logo, c.width / 2 - 36 * s, 34 * s, 72 * s, 72 * s); g.globalAlpha = 1;
          txt("PHENIX", 139.5, 128, 13, 700, encre, "Georgia, serif", "center");
          txt("001", 139.5, 145, 9, 700, gris, "Consolas, monospace", "center");
          return c.toDataURL("image/png").split(",")[1];
        }
        g.fillStyle = encre; g.fillRect(0, 0, c.width, 22 * s);
        txt(e.tete, 9, 15.5, 11.5, 700, "#EDEAE2", "Consolas, monospace");
        txt(e.droite || "", 270, 15.5, 10, 700, "#EDEAE2", "Consolas, monospace", "right");
        if (e.boot !== undefined) {
          txt("Initializing", 10, 50, 19, 700, encre, "Georgia, serif");
          g.strokeStyle = encre; g.lineWidth = 2 * s; g.strokeRect(10 * s, 62 * s, 259 * s, 14 * s); g.fillRect(12 * s, 64 * s, 255 * s * e.boot, 10 * s);
          e.lignes.forEach((l, i) => txt(l, 10, 96 + i * 16.5, 12.5, 500, i === e.lignes.length - 1 ? gris : encre));
          return c.toDataURL("image/png").split(",")[1];
        }
        // quatre compteurs en grille, puis le fil des arrivées
        const cases = [["SHEETS", e.fiches], ["MAPS", e.cartes], ["LANGUAGES", e.langues], ["COUNTRIES", e.pays]];
        cases.forEach(([lib, v], i) => { const x = 10 + (i % 2) * 131, y = 30 + Math.floor(i / 2) * 40;
          txt(lib, x, y + 8, 8.5, 700, gris, "Consolas, monospace"); txt(v.toLocaleString("en-US"), x, y + 29, i === 0 ? 20 : 18, 700, encre, "Georgia, serif"); });
        g.fillStyle = encre; g.fillRect(10 * s, 113 * s, 259 * s, 1 * s);
        e.fil.forEach(([pays, n], i) => { txt("+ " + n.toLocaleString("en-US") + " sheets", 10, 127 + i * 13.5, 10.5, 500, i ? gris : encre);
          txt(pays, 269, 127 + i * 13.5, 10.5, 700, i ? gris : encre, "Arial, sans-serif", "right"); });
        return c.toDataURL("image/png").split(",")[1];
      })()`);
      fs.writeFileSync(path.join(SORTIE, nom + ".png"), Buffer.from(png, "base64"));
    };
    await dessiner("veille", { veille: true });
    const lignesBoot = ["Core library: signed", "Axes 1, 2, 3: verified", "Connecting to the network…"];
    for (let i = 0; i <= 4; i++) await dessiner(`boot-${i}`, { tete: "PHENIX 001", droite: "v1.0", boot: i / 4, lignes: lignesBoot.slice(0, Math.max(1, i - 1)).concat(i === 4 ? [] : []) });
    for (let i = 0; i < N; i++) {
      const k = 1 - Math.pow(1 - (i + 1) / N, 2.4); // montée rapide puis ralentie
      const nb = Math.min(ARRIVEES.length, Math.floor(i / 2.5) + 1);
      const fil = ARRIVEES.slice(0, nb).reverse().slice(0, 3);
      await dessiner(`compte-${String(i).padStart(2, "0")}`, {
        tete: "PHENIX 001 · LIBRARY", droite: i === N - 1 ? "SYNCED" : "SYNCING",
        fiches: Math.round(FIN.fiches * k), cartes: Math.round(FIN.cartes * k),
        langues: Math.max(3, Math.round(FIN.langues * Math.min(1, k * 1.15))), pays: Math.max(1, Math.round(FIN.pays * Math.min(1, k * 1.1))), fil,
      });
    }
    console.log("écrans :", fs.readdirSync(SORTIE).length);
  } finally { await p.fermer(); }
})().catch((e) => { console.error(e); process.exit(1); });
