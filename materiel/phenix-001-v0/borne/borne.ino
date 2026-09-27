// Phenix borne : un ESP32-C3 et une carte SD. Il ouvre un WiFi « Phenix » sans mot de passe ;
// le téléphone qui s'y connecte ouvre toute la bibliothèque (l'appli Phenix complète), sans internet.
// La carte SD se prépare sur l'ordinateur : node outils/carte-sd.js, puis copier sortie-sd/ à la racine de la carte (FAT32).
//
// Arduino IDE 2 :
//   - cartes : « esp32 » d'Espressif ; carte « ESP32C3 Dev Module »
//   - Outils > USB CDC On Boot : Enabled
// Câblage : voir LISEZMOI.md.
#include <WiFi.h>
#include <WebServer.h>
#include <DNSServer.h>
#include <SPI.h>
#include <SD.h>

// La carte SD, en SPI
#define SD_SCK  4
#define SD_MISO 5
#define SD_MOSI 6
#define SD_CS   7

const char* NOM_WIFI = "Phenix";
const IPAddress IP(192, 168, 4, 1);
WebServer serveur(80);
DNSServer dns;

String typeDe(const String& p) {
  if (p.endsWith(".html")) return "text/html; charset=utf-8";
  if (p.endsWith(".json")) return "application/json";
  if (p.endsWith(".js")) return "text/javascript";
  if (p.endsWith(".css")) return "text/css";
  if (p.endsWith(".png")) return "image/png";
  if (p.endsWith(".jpg")) return "image/jpeg";
  if (p.endsWith(".svg")) return "image/svg+xml";
  if (p.endsWith(".txt") || p.endsWith(".md")) return "text/plain; charset=utf-8";
  return "application/octet-stream";
}

// Envoie un fichier de la carte ; s'il existe en version compressée (.gz), c'est elle qui part : quatre fois moins à transmettre.
bool envoyer(String chemin) {
  if (chemin.endsWith("/")) chemin += "index.html";
  const String gz = chemin + ".gz";
  const bool compresse = SD.exists(gz);
  if (!compresse && !SD.exists(chemin)) return false;
  File f = SD.open(compresse ? gz : chemin, FILE_READ);
  if (!f || f.isDirectory()) return false;
  if (compresse) serveur.sendHeader("Content-Encoding", "gzip");
  serveur.sendHeader("Cache-Control", "no-cache");
  serveur.setContentLength(f.size());
  serveur.send(200, typeDe(chemin), "");
  WiFiClient client = serveur.client();
  static uint8_t tampon[4096];
  size_t n;
  while ((n = f.read(tampon, sizeof tampon)) > 0) {
    if (client.write(tampon, n) == 0) break;
  }
  f.close();
  return true;
}

void setup() {
  Serial.begin(115200);
  delay(300);
  SPI.begin(SD_SCK, SD_MISO, SD_MOSI, SD_CS);
  if (SD.begin(SD_CS, SPI, 16000000)) Serial.printf("Carte SD : %llu Mo\n", SD.cardSize() / (1024 * 1024));
  else Serial.println("Carte SD introuvable : vérifier le câblage et le format (FAT32).");
  WiFi.mode(WIFI_AP);
  WiFi.softAPConfig(IP, IP, IPAddress(255, 255, 255, 0));
  WiFi.softAP(NOM_WIFI);
  // Toutes les adresses mènent à la borne : le téléphone affiche la page tout seul en se connectant.
  dns.start(53, "*", IP);
  serveur.onNotFound([]() {
    if (envoyer(serveur.uri())) return;
    // les tests de connexion des téléphones (generate_204, hotspot-detect…) et le reste : vers l'accueil
    serveur.sendHeader("Location", "http://192.168.4.1/", true);
    serveur.send(302, "text/plain", "");
  });
  serveur.begin();
  Serial.println("WiFi « Phenix » ouvert : http://192.168.4.1");
}

void loop() {
  dns.processNextRequest();
  serveur.handleClient();
}
