---
id: TEC-ELN-001
titre: Screens
axe: 2
categorie: Électronique et Numérique
temps: Court
contexte: 1
risque: Discret
materiel: Technique
priorite: normale
origine: officielle
sommaire: oui
parcours: Read this sheet first: it explains what all screens have in common. The chapter on liquid crystal displays covers almost everything you own; the one on electronic ink explains why it is the screen of devices that must last weeks on one battery.
tags: [screen, display, pixel, resolution, lcd, oled, e-ink, electronics]
sources: ["Chen J., Cranton W., Fihn M. (eds.), Handbook of Visual Display Technology, Springer, 2nd edition", "Society for Information Display, Display Technology Guide", "E Ink Holdings, technical documentation on electrophoretic displays"]
---

::A screen doesn't show a picture. It lights up, switches off or masks millions of tiny dots fast enough for the eye to take them for a picture.::

This subject reads in three parts: this sheet, which explains what all screens share, then two chapters, [[TEC-ELN-002]] on liquid crystals and [[TEC-ELN-003]] on electronic ink. LEDs, which light most screens and make up some on their own, have their own sheet: [[TEC-ELN-004]].

## The pixel

Every screen is a grid of **pixels**. On a colour screen, each pixel is made of three **sub-pixels**, red, green and blue. By setting the brightness of each, you get every colour: all three at full give white, all three off give black.

**Resolution** is the number of pixels: 1920 × 1080 for "Full HD", 3840 × 2160 for 4K. **Density** is pixels per inch (ppi): beyond about 300 ppi at phone reading distance, the eye can no longer tell the dots apart.

The same number of pixels looks sharp on a phone and coarse on a big TV: density decides sharpness, not resolution alone.

## Three ways of making light

Every screen falls into one of these families.

| Family | Principle | Examples | In sunlight | In the dark |
|---|---|---|---|---|
| Emissive | Each dot makes its own light | OLED, giant LED walls, old tube TVs, plasma | Average | Perfect |
| Transmissive | A lamp behind, shutters in front | Computer, TV and phone LCD screens | Average to poor | Good |
| Reflective | No lamp: they bounce back ambient light, like paper | Electronic ink, calculator and watch LCDs | Perfect | Unreadable without a light |

**This table decides power use.** An emissive or transmissive screen spends energy every second it is on, and the backlight is often the biggest drain in a phone or a laptop. A reflective screen uses almost nothing: an LCD calculator runs for years on a button cell, an e-reader for weeks.

## Refreshing the picture

A computer screen redraws its picture 60 times a second or more (60 Hz, 120 Hz). That's what makes motion smooth. An electronic ink screen only changes the picture when told to, and takes a fraction of a second to do it: perfect for a page, useless for video.

## How a screen gets the picture

- **Large screens** receive the picture through a video cable: HDMI, DisplayPort, and older VGA (analogue, still very common on old monitors and projectors).
- **Small screens** in electronic devices are driven directly by a small controller, through a serial link with a few wires (SPI, I2C) or a parallel bus. This is what you use to build a device yourself with a microcontroller, see [[TEC-IDE-009]].
- **The controller** is a chip bonded behind the panel, which keeps the picture in memory and redraws it on its own. Each model has its own commands: without its documentation, a salvaged screen is very hard to bring to life.

## What you learn by taking them apart

- **Old phone screens are hard to reuse.** Their connectors have pins 0.4 mm apart or less, their controller often has no public documentation, and their backlight sometimes needs more than 10 volts. For a build, a screen module sold for microcontrollers, already mounted on a small board, costs a few euros and saves days.
- **A broken laptop screen** contains a flat, diffusing light panel behind the liquid crystals: an excellent lighting panel once powered. See [[TEC-ELN-002]].
- **A screen that stays black** isn't necessarily dead: often only the backlight has failed. Shine a torch at the screen at an angle, and the picture appears.
- **Touchscreens** are one more layer, glued in front of the panel: you can crack a phone's touch glass without harming the display, and the other way round.
