---
id: TEC-RAD-001
titre: Building a radio receiver
axe: 2
categorie: Énergie et Électricité
temps: Long
contexte: 1
risque: Discret
materiel: Récupération
priorite: normale
origine: officielle
tags: [radio, electricity, communication, salvage, crystal radio]
sources: ["ARRL — The Radio Amateur's Handbook, detector receivers", "Terman F. E., Radio Engineers' Handbook", "US Army Signal Corps — field expedient receivers, historical documentation"]
---

::A receiver that needs no power source is possible. It draws all its power from the radio wave itself.::

## What a radio wave carries

A transmitter makes a current oscillate in an antenna, which radiates a wave. That wave makes a current oscillate, infinitely weaker, in any other antenna it meets.

So the problem is never picking up a signal: **every station arrives on your wire at the same time**. The problem is isolating one of them and getting the sound out of it.

A wave on its own carries nothing. It's made to carry a signal by varying its strength in time with the sound: that's **amplitude modulation** (AM), the kind used on medium wave and long wave. It's the only kind you can demodulate without active electronics, and that's what makes this build possible.

A detector receiver has four parts, not one more: an **antenna** that picks up, a **tuned circuit** that selects, a **detector** that extracts the sound, and an **earpiece** that plays it.

## The tuned circuit

A coil combined with a capacitor resonates at one precise frequency, like a tuning fork on a note. At that frequency the response is strongest; everywhere else it collapses. That's what separates the stations.

The bigger the coil or the capacitor, the lower the frequency you receive.

**The coil** is made by winding insulated copper wire, turns tight together and even, on an insulating cylinder: a cardboard tube, a bottle, a wooden handle. Around a hundred turns on a diameter of five to seven centimeters (2 to 3 inches) covers medium wave. Enameled wire can be salvaged from any transformer, motor, relay or loudspeaker.

**Tuning** is done in one of two ways. A variable capacitor taken from an old radio is ideal. Failing that, scrape the enamel off in a strip along the coil and slide a contact along the turns: you change the number of active turns, and so the frequency. It's cruder, and it works.

**A capacitor can be made**: two conductive surfaces separated by an insulator. Two sheets of aluminum foil rolled up with paper between them; or two tubes covered in aluminum foil that slide into each other, which gives a variable value.

## The detector, the decisive part

An amplitude-modulated signal swings symmetrically around zero: its average is zero, and an earpiece would get nothing out of it. You need to keep only one half of the oscillation, which brings out the envelope — in other words, the sound. So you need a component that lets current through in one direction only.

**A germanium diode** is the best choice: it conducts at a very low voltage, which matters when the signal is tiny. It can be salvaged from old devices. A silicon diode works, but it needs a stronger signal, and so a better antenna.

**Without a diode, a point contact is enough.** It's the historical principle of the crystal radio: a metal point resting on a semiconducting crystal conducts better in one direction than in the other. Field sets used a blued, oxidized steel blade, with a pencil lead sharpened to a point and pressed on it by a light spring. You move the point until you find the sensitive spot, and you have to find it again after every knock.

The contact must stay **light and exploratory**. Pressed too hard, it conducts both ways and the sound disappears.

## The earpiece

This is where most attempts fail. The available power is tiny: an ordinary low-impedance loudspeaker will produce nothing.

You need a **high-impedance earpiece** — a piezoelectric earpiece, or an old magnetic one. They can be salvaged from old telephones, hearing aids and measuring instruments. Failing that, an ordinary earpiece connected through a small matching transformer — a relay coil, a salvaged transformer — makes things much better.

## The antenna and the ground

This is where reception is won or lost, far more than in the rest of the build.

**The antenna** must be long and high: an insulated wire ten to thirty meters long (30 to 100 feet), strung as high as possible, away from walls and large metal objects. Length matters; height matters more.

**The ground is essential and always neglected.** The circuit has to close. A metal stake driven into damp soil, a metal water pipe, a radiator connected to earth. Without a proper ground, a detector receiver barely works at all.

One rule with no exceptions: **never put up an antenna above, across or near a power line**, and don't leave it up during a thunderstorm. A long, high wire also picks up lightning discharges.

## Assembly and tuning

The antenna goes to one end of the coil; the other end goes to ground. The tuning capacitor goes across the coil's terminals. The detector takes the signal off the coil and sends it to the earpiece, whose other terminal goes back to ground. A small capacitor across the earpiece smooths the result and clearly improves the sound.

Tune in this order: set up a good ground, string the longest antenna you can, find the detector's sensitive spot, and only then sweep the tuning, slowly.

## What this receiver can and can't do

It receives amplitude-modulated broadcasts, on medium wave and long wave. They carry very far, especially at night, and cover huge areas from a few transmitters. It's the kind of broadcasting chosen for safety information, and that's what makes this build useful rather than quaint — see [[URG-EFF-001]].

It doesn't receive FM or digital broadcasts: demodulating them takes active electronics, and so a power supply.

It transmits nothing. Receiving is passive, silent and discreet; transmitting takes power and a tuned antenna, and it occupies frequencies other people need. In a degraded situation, a radio's first job is to listen — see [[SIG-COM-001]].

## Improving an existing radio

If you have a battery radio, three steps beat a complete build. Extend the antenna, by connecting a long wire to the telescopic antenna or wrapping it around it. Connect the radio to a good ground. And keep it away from metal structures and electronic devices, which produce a lot of electrical noise.

A radio uses very little power and runs from any direct-current source at the right voltage: the math is in [[TEC-ENE-001]], the connections in [[TEC-ENE-002]].
