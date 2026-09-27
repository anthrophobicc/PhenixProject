---
id: TEC-ELN-004
titre: LEDs
axe: 2
categorie: Électronique et Numérique
temps: Court
contexte: 1
risque: Discret
materiel: Technique
priorite: normale
origine: officielle
tags: [led, diode, lighting, resistor, oled, light bulb, electronics]
sources: ["Schubert E. F., Light-Emitting Diodes, Cambridge University Press, 2nd edition", "Nobel Foundation, Nobel Prize in Physics 2014: efficient blue light-emitting diodes (Akasaki, Amano, Nakamura)", "US Department of Energy, LED Lighting Facts and reports on LED lamp lifetime"]
---

::An LED is a piece of crystal that glows when current flows through it the right way. It replaced the filament bulb in fifteen years, because it makes the same light with ten times less energy.::

## What happens inside

An LED (light-emitting diode) is a **diode**: a component that only lets current through in one direction. At its heart, two layers of semiconductor meet. When current flows, electrons drop from one energy level to another, each releasing a grain of light.

**The colour depends on the material**, not on a filter: red and infrared have existed since the 1960s, efficient blue only arrived in the 1990s, which earned its inventors the 2014 Nobel Prize in Physics. **A white LED** is a blue LED coated with a yellow powder (a phosphor): blue and yellow mixed look white.

## Useful numbers

**Each colour needs its own voltage**, called the forward voltage:

| Colour | Typical forward voltage |
|---|---|
| Infrared | 1.2 to 1.5 V |
| Red, orange, yellow | 1.8 to 2.2 V |
| Green, blue, white | 2.8 to 3.4 V |

**A small 3 or 5 mm indicator LED** handles about **20 milliamps**. Beyond that, it heats up and dies.

**Direction matters.** The longer leg is plus (the anode). The flat side of the LED's rim is minus (the cathode). Wired backwards, it doesn't light, and beyond a few volts backwards it can burn out.

## The golden rule: always limit the current

An LED connected straight to a battery that's too strong burns out in a fraction of a second: once past its forward voltage, it lets through as much current as it's given. So you put **a resistor in series**, worked out like this:

**R = (source voltage − LED voltage) ÷ desired current**

Example: a white LED (3 V) on a 5 V USB supply, at 20 mA: (5 − 3) ÷ 0.02 = **100 ohms**. When in doubt, take the next value up: the LED will be a little dimmer, and live longer. See [[TEC-ENE-002]].

## Lighting

- **Efficiency**: an LED bulb produces about 100 lumens per watt or more, against 10 to 15 for a filament bulb. For the same light, **ten times less energy**: that's what makes lighting possible on a small battery or a solar panel.
- **Lifetime**: the LEDs themselves last tens of thousands of hours. In a bulb, it's almost always **the power electronics that fail first**, because of heat. An LED bulb shut inside a sealed ceiling fitting lives much shorter.
- **Heat** is the enemy: a power LED must be mounted on a metal heatsink.

## Screens

- **LCD**: LEDs serve as the backlight, see [[TEC-ELN-002]].
- **OLED**: each sub-pixel is a tiny organic LED making its own light. Perfect blacks and infinite contrast, but pixels wear over time and a still image left for months can leave a mark.
- **Giant screens** in stadiums and on buildings: a mosaic of ordinary LEDs, visible in full sun.

## Tinkerer's tips

- **Testing an LED**: a multimeter on diode mode lights it faintly. Or a 3 V button cell, legs pinched on it: a red, green or white LED lights up with no resistor, because the cell can't supply enough current to burn it.
- **Seeing infrared**: a remote control's LED is invisible to the eye, but a phone camera sees it flash purple. It's the quickest remote test there is.
- **An LED bulb that no longer lights** often has just one dead LED in a chain wired in series: a black burnt dot on its surface gives it away. Bridging that LED with a wire sometimes brings the others back. **Careful: these bulbs run straight off 230 volts mains; only touch them unplugged, with the capacitors discharged.**
- **Squeezing the last drop from a spent battery**: a small circuit called a "joule thief" (a transistor, a resistor, a coil wound on a small ferrite ring) boosts the voltage of a half-dead 1.5 V battery to light a white LED for hours.
- **12 V LED strips** can be cut every three LEDs or so, at the marked points. They connect straight to a car or motorbike battery, with no resistor to add: it's already on the strip.

To light an LED without the grid, see [[SURV-ENE-001]] and [[SURV-ENE-002]].
