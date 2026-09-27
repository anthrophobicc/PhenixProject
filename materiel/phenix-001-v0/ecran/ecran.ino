// Phenix 001, version 0 : un ESP32-C3 et l'écran récupéré d'un Nokia 6300.
// Écran : 2 pouces, 240 × 320, contrôleur MC2PA8201, bus parallèle 8 bits (type 8080), logique en 3,3 V.
// La bibliothèque est compilée dans la mémoire flash de l'ESP32 (fiches.h, généré par outils/export-esp32.js).
// Deux boutons : BAS (GPIO8, vers la masse) et OK (le bouton BOOT de la carte, GPIO9).
//
// Arduino IDE 2 :
//   - cartes : « esp32 » d'Espressif ; carte « ESP32C3 Dev Module »
//   - Outils > USB CDC On Boot : Enabled
//   - Outils > Partition Scheme : Huge APP (3MB No OTA/1MB SPIFFS)
//   - bibliothèques : « Adafruit GFX Library » et « U8g2_for_Adafruit_GFX »
// Câblage : voir LISEZMOI.md.
#include <Adafruit_GFX.h>
#include <U8g2_for_Adafruit_GFX.h>
#include <vector>
#include "soc/gpio_reg.h"
#include "fiches.h"

// D0..D7 de l'écran sur GPIO0..GPIO7 : un octet s'écrit d'un seul coup dans le registre des sorties.
#define PIN_WR    10
#define PIN_RS    20
#define PIN_RESET 21
#define BTN_BAS   8
#define BTN_OK    9

// Si l'image sort en miroir ou à l'envers, essayer 0x00, 0x40 ou 0x80 (les écrans de 6300 existent en plusieurs séries).
#define ORIENTATION 0xC0

constexpr uint16_t rgb(uint8_t r, uint8_t g, uint8_t b) { return ((r & 0xF8) << 8) | ((g & 0xFC) << 3) | (b >> 3); }
const uint16_t PAPIER = rgb(0xF2, 0xEF, 0xE8), ENCRE = rgb(0x1C, 0x1B, 0x18), GRIS = rgb(0x8A, 0x83, 0x78);
const uint16_t VERT = rgb(0x2C, 0x6E, 0x49), ROUGE = rgb(0xA3, 0x2E, 0x22), BANDE = rgb(0x16, 0x18, 0x1A), CLAIR = rgb(0xE3, 0xDF, 0xD6);

// ---------------------------------------------------------------- l'écran
static inline void octet(uint8_t v) {
  REG_WRITE(GPIO_OUT_W1TC_REG, 0xFFu | (1u << PIN_WR));  // bus à zéro, WR bas
  REG_WRITE(GPIO_OUT_W1TS_REG, v);                       // l'octet sur le bus
  __asm__ __volatile__("nop; nop; nop;");
  REG_WRITE(GPIO_OUT_W1TS_REG, 1u << PIN_WR);            // WR remonte : l'écran lit l'octet
}
static void commande(uint8_t c) { digitalWrite(PIN_RS, LOW); octet(c); digitalWrite(PIN_RS, HIGH); }
static void donnee(uint8_t d) { octet(d); }

class Nokia6300 : public Adafruit_GFX {
 public:
  Nokia6300() : Adafruit_GFX(240, 320) {}
  void begin() {
    for (int p = 0; p <= 7; p++) pinMode(p, OUTPUT);
    pinMode(PIN_WR, OUTPUT); pinMode(PIN_RS, OUTPUT); pinMode(PIN_RESET, OUTPUT);
    digitalWrite(PIN_WR, HIGH); digitalWrite(PIN_RS, HIGH);
    digitalWrite(PIN_RESET, HIGH); delay(5);
    digitalWrite(PIN_RESET, LOW); delay(20);
    digitalWrite(PIN_RESET, HIGH); delay(150);
    commande(0x11); delay(10);            // sortie de veille
    commande(0x20);                       // pas d'inversion
    commande(0x38);                       // pas de mode ralenti
    commande(0x13);                       // affichage normal
    commande(0x3A); donnee(0x55);         // 16 bits par pixel (RGB565)
    commande(0x36); donnee(ORIENTATION);  // portrait
    commande(0x33);                       // défilement : tout l'écran
    donnee(0); donnee(0); donnee(0x01); donnee(0x40); donnee(0); donnee(0);
    delay(125);
    commande(0x29);                       // allumage
  }
  void drawPixel(int16_t x, int16_t y, uint16_t c) override {
    if (x < 0 || y < 0 || x >= 240 || y >= 320) return;
    zone(x, y, x, y); donnee(c >> 8); donnee(c & 0xFF);
  }
  void fillRect(int16_t x, int16_t y, int16_t w, int16_t h, uint16_t c) override {
    if (x < 0) { w += x; x = 0; }
    if (y < 0) { h += y; y = 0; }
    if (x + w > 240) w = 240 - x;
    if (y + h > 320) h = 320 - y;
    if (w <= 0 || h <= 0) return;
    zone(x, y, x + w - 1, y + h - 1);
    const uint8_t hi = c >> 8, lo = c & 0xFF;
    for (uint32_t n = (uint32_t)w * h; n; n--) { octet(hi); octet(lo); }
  }
  void writePixel(int16_t x, int16_t y, uint16_t c) override { drawPixel(x, y, c); }
  void writeFillRect(int16_t x, int16_t y, int16_t w, int16_t h, uint16_t c) override { fillRect(x, y, w, h, c); }
  void drawFastHLine(int16_t x, int16_t y, int16_t w, uint16_t c) override { fillRect(x, y, w, 1, c); }
  void drawFastVLine(int16_t x, int16_t y, int16_t h, uint16_t c) override { fillRect(x, y, 1, h, c); }
  void writeFastHLine(int16_t x, int16_t y, int16_t w, uint16_t c) override { fillRect(x, y, w, 1, c); }
  void writeFastVLine(int16_t x, int16_t y, int16_t h, uint16_t c) override { fillRect(x, y, 1, h, c); }
  void fillScreen(uint16_t c) override { fillRect(0, 0, 240, 320, c); }
 private:
  void zone(int16_t x0, int16_t y0, int16_t x1, int16_t y1) {
    commande(0x2A); donnee(0); donnee(x0); donnee(0); donnee(x1);
    commande(0x2B); donnee(y0 >> 8); donnee(y0 & 0xFF); donnee(y1 >> 8); donnee(y1 & 0xFF);
    commande(0x2C);
  }
};

Nokia6300 ecran;
U8G2_FOR_ADAFRUIT_GFX u8;

// ---------------------------------------------------------------- texte
void ecrire(int x, int y, const char* t, const uint8_t* police, uint16_t couleur) {
  u8.setFont(police); u8.setForegroundColor(couleur); u8.setFontMode(1);
  u8.drawUTF8(x, y, t);
}
int largeur(const String& t, const uint8_t* police) { u8.setFont(police); return u8.getUTF8Width(t.c_str()); }

// Une ligne affichée : son style et son texte, déjà coupés à la largeur de l'écran.
enum Style : uint8_t { TITRE, SECTION, SOUS, TEXTE, PUCE, ACCROCHE, BLANC };
struct Ligne { Style style; String texte; };
std::vector<Ligne> lignes;

const uint8_t* policeDe(Style s) {
  switch (s) {
    case TITRE: return u8g2_font_helvB14_tf;
    case SECTION: return u8g2_font_helvB12_tf;
    case SOUS: return u8g2_font_helvB10_tf;
    default: return u8g2_font_helvR10_tf;
  }
}
int hauteurDe(Style s) { return s == TITRE ? 20 : s == SECTION ? 20 : s == BLANC ? 6 : 15; }

// Coupe un paragraphe en lignes de 226 pixels au plus.
void couper(Style s, String t, const String& retrait = "") {
  const uint8_t* p = policeDe(s);
  const int max = 226;
  String ligne;
  while (t.length()) {
    int sp = t.indexOf(' ');
    String mot = sp < 0 ? t : t.substring(0, sp);
    t = sp < 0 ? "" : t.substring(sp + 1);
    String essai = ligne.length() ? ligne + " " + mot : mot;
    if (largeur(essai, p) > max && ligne.length()) {
      lignes.push_back({s, ligne});
      ligne = retrait + mot;
    } else ligne = essai;
  }
  if (ligne.length()) lignes.push_back({s, ligne});
}

// Nettoie une ligne de Markdown : gras, liens [[ID]], surlignage.
String propre(String l) {
  l.replace("**", ""); l.replace("__", ""); l.replace("==", "");
  int a;
  while ((a = l.indexOf("[[")) >= 0) {
    int b = l.indexOf("]]", a);
    if (b < 0) break;
    l = l.substring(0, a) + "(" + l.substring(a + 2, b) + ")" + l.substring(b + 2);
  }
  return l;
}

// Prépare une fiche : titre, puis chaque ligne du texte avec son style.
void preparer(const Fiche& f) {
  lignes.clear();
  couper(TITRE, f.titre);
  lignes.push_back({BLANC, ""});
  const char* p = f.texte;
  while (*p) {
    const char* fin = strchr(p, '\n');
    const size_t n = fin ? (size_t)(fin - p) : strlen(p);
    String l; l.reserve(n);
    for (size_t k = 0; k < n; k++) l += p[k];
    p += n + (fin ? 1 : 0);
    l.trim();
    if (!l.length()) { if (lignes.back().style != BLANC) lignes.push_back({BLANC, ""}); continue; }
    if (l.startsWith("## ")) { lignes.push_back({BLANC, ""}); couper(SECTION, propre(l.substring(3))); continue; }
    if (l.startsWith("### ")) { couper(SOUS, propre(l.substring(4))); continue; }
    if (l.startsWith("::") && l.endsWith("::") && l.length() > 4) { couper(ACCROCHE, propre(l.substring(2, l.length() - 2))); continue; }
    if (l.startsWith("- ") || l.startsWith("* ")) { couper(PUCE, "- " + propre(l.substring(2)), "  "); continue; }
    if (l.startsWith("|")) {
      if (l.indexOf("---") >= 0) continue;
      l.replace("|", "  "); couper(TEXTE, propre(l)); continue;
    }
    couper(TEXTE, propre(l));
  }
}

// ---------------------------------------------------------------- les écrans
int choix = 0, premier = 0, page = 0;
bool lecture = false;
std::vector<int> debutsPages;
const int PAR_ECRAN = 12;

void bandeau(const String& gauche, const String& droite) {
  ecran.fillRect(0, 0, 240, 24, BANDE);
  ecrire(8, 17, gauche.c_str(), u8g2_font_helvB10_tf, rgb(0x79, 0xC7, 0x9A));
  ecrire(232 - largeur(droite, u8g2_font_helvR10_tf), 17, droite.c_str(), u8g2_font_helvR10_tf, CLAIR);
}

void dessinerListe() {
  if (choix < premier) premier = choix;
  if (choix >= premier + PAR_ECRAN) premier = choix - PAR_ECRAN + 1;
  ecran.fillScreen(PAPIER);
  bandeau("PHENIX 001", String(choix + 1) + " / " + NB_FICHES);
  for (int i = 0; i < PAR_ECRAN && premier + i < NB_FICHES; i++) {
    const Fiche& f = FICHES[premier + i];
    const int y = 28 + i * 24;
    const bool sel = premier + i == choix;
    if (sel) ecran.fillRect(0, y, 240, 24, VERT);
    ecran.fillRect(4, y + 7, 4, 10, f.urgence ? ROUGE : (f.axe == 1 ? rgb(0xB0, 0x86, 0x3C) : f.axe == 2 ? rgb(0x28, 0x60, 0x7F) : VERT));
    String t = f.titre;
    while (largeur(t, u8g2_font_helvR12_tf) > 222 && t.length() > 4) t = t.substring(0, t.length() - 4) + "...";
    ecrire(14, y + 17, t.c_str(), u8g2_font_helvR12_tf, sel ? PAPIER : ENCRE);
  }
  ecrire(8, 316, "BAS : suivant (appui long : +10)   OK : ouvrir", u8g2_font_helvR08_tf, GRIS);
}

void paginer() {
  debutsPages.clear();
  int h = 0;
  debutsPages.push_back(0);
  for (int i = 0; i < (int)lignes.size(); i++) {
    const int hl = hauteurDe(lignes[i].style);
    if (h + hl > 276) { debutsPages.push_back(i); h = 0; }
    h += hl;
  }
}

void dessinerPage() {
  const Fiche& f = FICHES[choix];
  ecran.fillScreen(PAPIER);
  bandeau(f.id, String(page + 1) + " / " + debutsPages.size());
  int y = 32;
  const int debut = debutsPages[page], fin = page + 1 < (int)debutsPages.size() ? debutsPages[page + 1] : lignes.size();
  for (int i = debut; i < fin; i++) {
    const Ligne& l = lignes[i];
    y += hauteurDe(l.style);
    if (l.style == BLANC) continue;
    uint16_t c = l.style == SECTION ? VERT : l.style == ACCROCHE ? GRIS : ENCRE;
    if (l.style == TITRE && f.urgence) c = ROUGE;
    ecrire(7, y - 4, l.texte.c_str(), policeDe(l.style), c);
  }
  ecrire(8, 316, "BAS : page suivante   OK : retour", u8g2_font_helvR08_tf, GRIS);
}

// ---------------------------------------------------------------- boutons
// Renvoie 0 (rien), 1 (appui court) ou 2 (appui long, plus de 0,6 s).
int appui(int pin) {
  if (digitalRead(pin) != LOW) return 0;
  const unsigned long t0 = millis();
  delay(20);
  while (digitalRead(pin) == LOW) {
    if (millis() - t0 > 600) { while (digitalRead(pin) == LOW) delay(5); return 2; }
    delay(5);
  }
  return 1;
}

void setup() {
  Serial.begin(115200);
  pinMode(BTN_BAS, INPUT_PULLUP);
  pinMode(BTN_OK, INPUT_PULLUP);
  ecran.begin();
  u8.begin(ecran);
  // premier test : trois bandes de couleur. Si on les voit, l'écran est bien câblé.
  ecran.fillRect(0, 0, 240, 107, ROUGE); ecran.fillRect(0, 107, 240, 106, VERT); ecran.fillRect(0, 213, 240, 107, rgb(0x28, 0x60, 0x7F));
  delay(800);
  dessinerListe();
  Serial.printf("Phenix 001 v0 : %d fiches\n", NB_FICHES);
}

void loop() {
  const int bas = appui(BTN_BAS), ok = appui(BTN_OK);
  if (!lecture) {
    if (bas) { choix = (choix + (bas == 2 ? 10 : 1)) % NB_FICHES; dessinerListe(); }
    if (ok) { lecture = true; page = 0; preparer(FICHES[choix]); paginer(); dessinerPage(); }
  } else {
    if (bas) { page = (page + 1) % debutsPages.size(); dessinerPage(); }
    if (ok) { lecture = false; lignes.clear(); dessinerListe(); }
  }
  delay(10);
}
