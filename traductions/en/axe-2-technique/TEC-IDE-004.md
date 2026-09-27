---
id: TEC-IDE-004
titre: Security cameras
axe: 2
categorie: Information et Données
temps: Court
contexte: 1
risque: Discret
materiel: Technique
priorite: normale
origine: officielle
tags: [camera, cctv, surveillance, video, infrared, security, network]
sources: ["Standard EN 62676-4, video surveillance systems, application guidelines", "CNIL (French data protection authority), practical guides on video surveillance", "Technical documentation of the H.264 and H.265 codecs (ITU-T)"]
---

::A camera doesn't see better than you. It sees longer, without blinking, and it keeps everything. That's its only strength, and its weaknesses come from the same place.::

## What's inside

A security camera is a camera that takes 15 to 30 pictures a second, non-stop.

**The lens** gathers light. Its focal length decides everything: short, it sees wide but details are small; long, it sees far but narrow. A camera cannot see everything in detail at once.

**The sensor** turns light into pixels. More pixels let you zoom into the image, but only if the lens and the light keep up.

**The infrared filter.** By day, a small filter blocks infrared to keep colours right. At night, it slides away with a little click, the camera switches to black and white and lights the scene itself with **infrared LEDs**.

**The processor** compresses the image and sends it. It often also handles motion detection, sometimes recognition of people or vehicles.

## Night vision

Infrared LEDs at **850 nm** give off a dull red glow, visible to the eye when you look at the camera in the dark. Those at **940 nm** are invisible, but reach less far.

This lighting has a limited range, often 20 to 30 m (65 to 100 ft). Beyond it, the image is black. See [[TEC-NUI-001]] for night vision in general.

**A phone camera sees infrared**: film the camera in the dark, its LEDs show up as purple or white dots.

## Analogue or IP

**Analogue cameras** (and their modern HD versions over coaxial cable) send a raw video signal to a recorder, the **DVR**. Everything stays in the building.

**IP cameras** are small computers on the network. They send a digital stream to a network recorder (**NVR**), a server or a cloud. Many are powered by the network cable itself (**PoE**, Power over Ethernet).

**Consumer WiFi cameras** almost always send their footage to the maker's servers. Without internet, many do nothing more, or only record to their memory card.

## Why compression matters

Raw video would fill a disk in a few hours. The **H.264** and **H.265** codecs keep only what changes from one frame to the next. An empty car park costs almost nothing; a street in the rain or a tree in the wind costs a lot, because everything moves.

In practice, a recorder often keeps **one to four weeks**, then overwrites the oldest footage. **If you need a recording, ask for it quickly.**

## Detect, recognise, identify

The European standard EN 62676-4 sets what you can expect from an image according to how many pixels cover one metre of the scene:

| Goal | Pixels per metre | What you can tell |
|---|---|---|
| Detect | 25 | Someone is there |
| Observe | 62 | What they're doing, their clothes |
| Recognise | 125 | It's someone you know |
| Identify | 250 | You can establish who it is |

A 4K camera covering a 40 m (130 ft) wide car park gives about 100 pixels per metre: it may recognise, it doesn't identify. **That's why footage on the TV news is so blurry.**

## What fools a camera

- **Backlight**: a figure in front of a glass door or headlights turns black. So-called WDR cameras partly compensate.
- **Window reflections**: a camera behind a window, at night, sees only the reflection of its own LEDs.
- **Rain, snow, spider webs** in front of the lens trigger motion detection endlessly, or blind the image at night.
- **Angle**: a camera mounted too high sees only the tops of heads and cap peaks.
- **The network**: a poorly protected IP camera, with its factory password, can be reached from the internet. Entire websites list open cameras.

## Installing your own

1. Decide **what you want to see**: the entrance, a driveway, a letterbox. One camera per need, not one camera for everything.
2. Mount it **2.5 to 3 m (8 to 10 ft) high**, low enough to see faces, high enough not to be torn down.
3. Avoid backlight: not facing east or west, not facing a lamp.
4. **Change the password** at install, update it, and if possible keep it on a separate network.
5. Prefer **local** recording (card, NVR): it works without internet.

**The law.** In France, an individual may only film their own property. The public street, the garden or the neighbours' windows are off limits. Employees must be informed, and footage may not be kept more than a month. Rules differ by country. City cameras follow other rules, see [[TEC-IDE-005]].
