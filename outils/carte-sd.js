// Prépare la carte SD de la borne Phenix (materiel/phenix-001-v0/borne) dans sortie-sd/ :
// une page d'accueil, l'application complète compressée, et la version officielle de la bibliothèque (Phenix Hub).
// Ensuite : copier tout le contenu de sortie-sd/ à la racine d'une carte SD formatée en FAT32.
// Usage : node outils/carte-sd.js   (lancer après outils/construire-site.js pour avoir les fichiers du Hub à jour)
"use strict";
const fs = require("fs");
const path = require("path");
const zlib = require("zlib");

const RACINE = path.join(__dirname, "..");
const SORTIE = path.join(RACINE, "sortie-sd");
fs.rmSync(SORTIE, { recursive: true, force: true });
fs.mkdirSync(path.join(SORTIE, "hub"), { recursive: true });

const gz = (source, cible) => {
  const donnees = zlib.gzipSync(fs.readFileSync(source), { level: 9 });
  fs.writeFileSync(path.join(SORTIE, cible + ".gz"), donnees);
  return donnees.length;
};
let total = gz(path.join(RACINE, "app", "phenix.html"), "phenix.html");
for (const f of fs.readdirSync(path.join(RACINE, "site", "hub"))) total += gz(path.join(RACINE, "site", "hub", f), path.join("hub", f));

const accueil = `<!DOCTYPE html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Phenix</title>
<style>
body{margin:0;background:#040806;color:#C8FFD6;font:17px/1.5 system-ui,sans-serif;padding:28px 18px}
main{max-width:460px;margin:0 auto}
h1{color:#39FF6A;font:700 30px/1.15 Georgia,serif;margin:0 0 6px}
p{margin:0 0 18px;color:#93E8AA}
a.b{display:block;text-decoration:none;border:1px solid #39FF6A;border-radius:10px;padding:16px;margin:0 0 12px;color:#39FF6A;font-weight:700;font-size:19px}
a.b span{display:block;font-weight:400;font-size:14px;color:#93E8AA;margin-top:3px}
a.b.p{background:#39FF6A;color:#040806}a.b.p span{color:#0B2A14}
small{color:#56A36E;display:block;margin-top:22px}
</style></head><body><main>
<h1>Phenix</h1>
<p>Une bibliothèque de savoirs pratiques, lisible sans internet.<br>A library of practical knowledge, readable without internet.</p>
<a class="b p" href="/phenix.html">Ouvrir la bibliothèque<span>Open the library · toutes les fiches, les cartes, les modules</span></a>
<a class="b" href="/hub/phenix-officielle-fr.json" download>Emporter la version officielle<span>Take the official version · un fichier que Phenix ouvre partout</span></a>
<small>Cette borne n'est reliée à rien : tout vient de sa carte SD. This hotspot is connected to nothing: everything comes from its SD card.</small>
</main></body></html>
`;
fs.writeFileSync(path.join(SORTIE, "index.html"), accueil);
total += Buffer.byteLength(accueil);
console.log(`sortie-sd/ prête : ${(total / 1e6).toFixed(1)} Mo à copier à la racine de la carte SD (FAT32).`);
