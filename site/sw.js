// Phenix hors ligne. Généré par outils/construire-site.js, ne pas modifier à la main.
const CACHE = "phenix-0d39fe786d";
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
