---
id: TEC-ELN-003
titre: The electronic ink screen
axe: 2
categorie: Électronique et Numérique
temps: Court
contexte: 1
risque: Discret
materiel: Technique
priorite: normale
origine: officielle
parent: TEC-ELN-001
chapitre: 2
tags: [e-ink, electronic paper, e-reader, screen, electrophoresis, low power]
sources: ["Comiskey B., Albert J., Yoshizawa H., Jacobson J., An electrophoretic ink for all-printed reflective electronic displays, Nature, 1998", "E Ink Holdings, datasheets for Carta, Kaleido and Spectra displays", "Heikenfeld J. et al., Review Paper: A critical review of the present and future prospects for electronic paper, Journal of the SID, 2011"]
---

::An e-reader with a dead battery still shows its last page. A screen that keeps its picture without power is exactly what a device built to last needs.::

## The principle

The screen is filled with **microcapsules** thinner than a hair. Each holds a clear liquid and thousands of **pigment particles**: white ones charged one way, black ones charged the other.

Electrodes above and below each dot create an electric field. Depending on its direction, it pulls the white or the black particles to the surface. The dot turns white or black. This is **electrophoresis**, the movement of charged particles in a liquid.

The invention came out of MIT in the late 1990s; the company E Ink industrialised it, and the first consumer e-reader used it in 2004.

## What makes it unique

**It is bistable.** Once moved, the particles stay where they are, without power. The screen only uses energy **while the picture changes**. A page displayed for a week costs nothing.

**It is reflective.** Like paper, it bounces ambient light back. It reads perfectly in full sun, from every angle, and tires the eyes less than a lit screen. In the dark, it needs a front light: a row of LEDs along the edge lighting the surface from above.

## Its limits

- **Slow**: a picture changes in a few tenths of a second. No video, jerky animations.
- **Ghosting**: the previous picture leaves a faint trace. The screen regularly "cleans" itself by flashing all black then all white: that flash is normal.
- **Cold**: below about 0 °C (32 °F), the liquid thickens and picture changes become slow or incomplete. Many displays are rated for 0 to 50 °C. **The picture already shown, however, stays.**
- **Colour** exists in two versions: with colour filters over the black-and-white screen (pale colours, fast), or with pigments of several colours in each capsule (vivid colours, but a picture change takes several seconds).
- **Price**: for the same size, more expensive than an LCD.

## Where you find it

- E-readers and some writing tablets.
- **Electronic shelf labels** in supermarkets: each one is a small electronic ink display with a button cell that lasts years, updated by radio.
- Timetable displays at some solar-powered bus stops.
- Watches and badges with very long battery life.

## Why it's the survival screen

A reading device that must work for weeks far from any socket has three needs: use almost nothing, be readable in daylight, and **show something even when its battery is empty**. Electronic ink is the only technology that ticks all three. That's why it is considered for offline reading devices, see [[TEC-IDE-009]].

## Tips

- **A dead e-reader keeps its last page**: if you leave a map, a list of frequencies or an emergency sheet on it before it dies, the information stays readable.
- **A screen frozen halfway** after a cold snap often recovers if you warm it against your body, then force a full refresh.
- **For a build**, electronic ink modules from 1.5 to 7.5 inches driven over SPI cost from about ten to a few tens of euros. You send the whole picture, then let the screen refresh, often 2 to 15 seconds depending on the model.
- **Don't leave an electronic ink screen in full sun behind a window**: heat and ultraviolet eventually yellow and damage the capsules.
