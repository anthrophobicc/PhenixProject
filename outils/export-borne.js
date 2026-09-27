// La borne Phenix sans carte SD : l'appli complète, compressée, écrite dans le programme de l'ESP32.
// Écrit materiel/phenix-001-v0/borne-sans-sd/app.h
// Usage : node outils/export-borne.js
"use strict";
const fs = require("fs");
const path = require("path");
const zlib = require("zlib");

const RACINE = path.join(__dirname, "..");
const gz = zlib.gzipSync(fs.readFileSync(path.join(RACINE, "app", "phenix.html")), { level: 9 });
const lignes = [];
for (let i = 0; i < gz.length; i += 24) lignes.push(Array.from(gz.subarray(i, i + 24)).join(","));
const h = `// Généré par outils/export-borne.js : ne pas modifier à la main.
#pragma once
#include <stdint.h>
static const uint8_t APP_GZ[] = {
${lignes.join(",\n")}
};
static const uint32_t APP_GZ_TAILLE = ${gz.length};
`;
const sortie = path.join(RACINE, "materiel", "phenix-001-v0", "borne-sans-sd", "app.h");
fs.mkdirSync(path.dirname(sortie), { recursive: true });
fs.writeFileSync(sortie, h);
console.log(`appli compressée : ${(gz.length / 1e6).toFixed(2)} Mo → ${path.relative(RACINE, sortie)}`);
