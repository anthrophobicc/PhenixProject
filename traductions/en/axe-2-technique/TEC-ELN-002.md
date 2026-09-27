---
id: TEC-ELN-002
titre: The liquid crystal display (LCD)
axe: 2
categorie: Électronique et Numérique
temps: Court
contexte: 1
risque: Discret
materiel: Technique
priorite: normale
origine: officielle
parent: TEC-ELN-001
chapitre: 1
tags: [lcd, liquid crystal, screen, polarizer, backlight, tft, ips]
sources: ["Yang D.-K., Wu S.-T., Fundamentals of Liquid Crystal Devices, Wiley, 2nd edition", "Chen J., Cranton W., Fihn M. (eds.), Handbook of Visual Display Technology, Springer", "Castellano J., Liquid Gold: The Story of Liquid Crystal Displays and the Creation of an Industry, World Scientific"]
---

::An LCD makes no light. It's a lamp, and in front of it, millions of shutters opening and closing. Everything you see, you see through them.::

## The principle in three layers

**Light from a lamp** first passes through a **polarizer**: a filter that only lets through light vibrating in one direction.

**Liquid crystals**, sandwiched between two glass plates, have a strange property: their rod-shaped molecules line up on their own, and by lining up in a spiral, they **rotate** the direction of the light passing through them. Apply a small voltage and the molecules stand up straight and stop rotating it.

**A second polarizer**, crossed with the first, only lets through light that has been rotated.

Result: with no voltage, the light rotates and passes, the dot is bright. With voltage, it no longer rotates and is blocked by the second filter, the dot is dark. By adjusting the voltage, you get every shade of grey.

**Colour** comes from tiny red, green and blue filters in front of each sub-pixel. A colour LCD lets through, at best, about a tenth of its lamp's light: the rest is absorbed by the filters and polarizers.

## The families

- **Segment LCDs**: the digits of a calculator, a watch, a thermostat. No lamp, a mirror behind: they are reflective and use a few millionths of a watt.
- **Passive matrix**: old monochrome screens on phones and appliances. Simple, slow, low contrast.
- **Active matrix (TFT)**: a transistor behind each sub-pixel holds its voltage between refreshes. The screen of almost every computer, TV and non-OLED phone.
- **TN, VA, IPS**: three ways of arranging the crystals. TN is fast and cheap but shifts colour as soon as you look from the side; IPS keeps its colours from every angle; VA gives the deepest blacks.

## The backlight

Recent screens are lit by **LEDs**, often placed along one edge: a plastic plate guides the light and spreads it over the whole surface. Screens from before about 2010 used thin **fluorescent tubes** (CCFL), which contain a little mercury and need high voltage to start.

## What damages it

- **Pressure**: pressing hard crushes the crystals and leaves blotches, sometimes permanently.
- **Cold**: below about −20 °C (−4 °F), the crystals turn sluggish and the picture smears. It comes back as it warms up.
- **Strong heat**: a dashboard screen in full sun can turn black. Above a certain temperature, the crystals become an ordinary liquid and lose their effect. That comes back too, as it cools.
- **Dead or stuck pixels**: a failed transistor leaves a dot that is always black or always lit.

## Tips from people who've taken them apart

- **Black screen, device on?** Shine a torch at the screen at an angle, close up. If the picture appears, faintly, only the backlight is dead: the device can still be used to recover data or read a setting.
- **LCD light is polarized.** With polarized sunglasses, a screen can go black when you tilt your head 90 degrees. It isn't broken.
- **The back panel of a broken laptop screen** (the light guide and its LEDs) makes an even, flat light panel, ideal for lighting a room or a workbench, or for tracing. Its LEDs are often wired in series: they need the voltage they were designed for, see [[TEC-ELN-004]].
- **Polarizer sheets** peel off a dead screen. Two crossed sheets show the stresses in clear plastic as rainbows, and a single one works as a polarizing filter for photos.
- **A broken old screen with fluorescent tubes**: don't breathe the dust of shattered tubes, air the room, pick up without a vacuum cleaner.
- **For a build**, small 2 to 3 inch colour LCD modules driven over SPI (ILI9341, ST7789 controllers) cost a few euros and are documented everywhere.
