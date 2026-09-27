---
id: TEC-IDE-009
titre: The Phenix devices
axe: 2
categorie: Information et Données
temps: Long
contexte: 1
risque: Discret
materiel: Technique
priorite: normale
origine: officielle
tags: [phenix, device, esp32, hotspot, wifi, sd card, prototype, documentation, build]
sources: ["Phenix project repository: materiel/phenix-001-v0/LISEZMOI.md, borne-sans-sd.ino, borne.ino, ecran.ino", "Espressif Systems, ESP32-C3 Series Datasheet and arduino-esp32 documentation", "Andy Brown, Generic Nokia LCD hacking board (pinouts of Nokia phone screens)"]
---

::A Phenix device should be buildable from parts found everywhere, repairable with a soldering iron, and hold the whole library in a pocket. Everything is open: the plans, the code, the mistakes.::

**Everything below is at prototype stage.** Nothing is for sale. The 3D renders of the devices are concepts; only the WiFi hotspot has already worked on a real phone.

## The two devices

**Phenix 001, the small one.** A pocket reader, no bigger than a small remote control, holding the whole library on a memory card and showing it on a small, frugal screen. Common parts, a case you open with a screwdriver, a replaceable battery.

**Phenix 002, the big one.** A larger device, with a colour screen wide enough to read maps. Two memory card slots under a rubber flap: it can **read a Phenix 001's card, check its library and repair damaged sheets**. Modules plug onto pins: solar panel, dynamo, lamp. And a broken Phenix should be able to run again on a salvaged screen, even one from an old payment terminal.

## What already exists: the Phenix hotspot

This is the first prototype that works. An electronic board costing a few euros opens a WiFi network called **Phenix**, with no password. **Any phone that connects to it opens the whole library**, without internet and without installing anything: the page opens by itself, like a hotel WiFi portal.

**The parts**

| Part | Role | Rough price |
|---|---|---|
| ESP32-C3 "Super Mini" | The brain and the WiFi | 3 to 5 € |
| USB-C cable | Power and programming | already at home |
| Power bank | Battery life | already at home |
| Micro SD card module (optional) | For a bigger library | 1 to 2 € |

**Two versions**

- **Without an SD card**: the full app, compressed (under one megabyte), is written straight into the board's memory. Nothing to solder. This is the version that worked.
- **With an SD card**: the library sits on a FAT32 micro SD card, prepared on the computer. Wiring: CS to GPIO7, MOSI to GPIO6, SCK to GPIO4, MISO to GPIO5, plus 3.3 V and ground.

**Building it**

1. Install **Arduino IDE 2**, add Espressif's ESP32 boards, choose the **ESP32C3 Dev Module** board.
2. In the Tools menu: **Partition Scheme: Huge APP**, and **USB CDC On Boot: Enabled**.
3. Open the hotspot program, in the **materiel/phenix-001-v0** folder of the repository, and upload.
4. If the upload won't start: unplug, **hold the BOOT button down**, plug back in, release, try again.
5. On the phone: WiFi settings, network **Phenix**. If the page doesn't open by itself, type **192.168.4.1** in the browser.

## What was tried, and what we learned

**The screen of an old Nokia phone**: the idea was to reuse the colour screen of a dead phone. Two obstacles stopped it: a 24-pin connector with pins 0.4 mm apart, almost impossible to solder without fine equipment, and a backlight needing about 13 volts. **Lesson**: for a device everyone must be able to rebuild, a screen module sold for microcontrollers, already on its small board, beats an exotic salvaged part. See [[TEC-ELN-001]].

**Next planned**: a 2.8-inch colour screen with a built-in SD card reader, or a 2.9-inch **electronic ink** screen, which keeps its page without power and reads in full sun, see [[TEC-ELN-003]].

## The principles behind the design

- **Parts found everywhere**, online and in electronics shops, replaceable one by one.
- **Everything is documented**: schematics, code, parts list, in the public repository. A device whose insides nobody knows can't be repaired.
- **The library stays readable without the device**: they're the same text files as everywhere else. An SD card pulled from a broken Phenix reads on any computer.
- **Energy first**: a device that must last far from sockets picks its components for their consumption before their power.

The project as a whole is presented in [[TEC-IDE-008]].
