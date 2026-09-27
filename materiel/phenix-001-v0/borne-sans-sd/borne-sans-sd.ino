// Phenix borne, sans carte SD : l'appli complète est dans le programme (app.h, généré par outils/export-borne.js).
// L'ESP32 ouvre un WiFi « Phenix » sans mot de passe ; le téléphone qui s'y connecte ouvre toute la bibliothèque, sans internet.
// Arduino : carte ESP32C3 Dev Module · Tools > Partition Scheme : Huge APP (3MB No OTA/1MB SPIFFS).
#include <WiFi.h>
#include <WebServer.h>
#include <DNSServer.h>
#include "app.h"

const IPAddress IP(192, 168, 4, 1);
WebServer serveur(80);
DNSServer dns;

void envoyerApp() {
  serveur.sendHeader("Content-Encoding", "gzip");
  serveur.send_P(200, "text/html; charset=utf-8", (const char*)APP_GZ, APP_GZ_TAILLE);
}

void setup() {
  WiFi.mode(WIFI_AP);
  WiFi.softAPConfig(IP, IP, IPAddress(255, 255, 255, 0));
  WiFi.softAP("Phenix");
  dns.start(53, "*", IP);  // toutes les adresses mènent à la borne : le téléphone ouvre la page tout seul
  serveur.on("/", envoyerApp);
  serveur.on("/phenix.html", envoyerApp);
  serveur.onNotFound([]() {
    serveur.sendHeader("Location", "http://192.168.4.1/", true);
    serveur.send(302, "text/plain", "");
  });
  serveur.begin();
}

void loop() {
  dns.processNextRequest();
  serveur.handleClient();
}
