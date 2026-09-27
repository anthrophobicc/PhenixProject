---
id: TEC-ENE-011
titre: The circuit breaker
axe: 2
categorie: Énergie et Électricité
temps: Court
contexte: 1
risque: Discret
materiel: Technique
priorite: normale
origine: officielle
tags: [circuit breaker, rcd, fuse, consumer unit, short circuit, overload, safety]
sources: ["French standard NF C 15-100, low-voltage electrical installations", "Standard EN 60898-1, circuit breakers for household installations", "Standards EN 61008 and 61009, residual current devices", "Promotelec, electrical installation guides"]
---

::A circuit breaker doesn't protect your appliances. It protects your wires from fire, and the RCD protects your body. When it trips, it's telling you something: understand what before you switch it back on.::

## What it watches

An electric wire heats up when current flows through it. Too much current and it gets hot enough to melt its insulation and start a fire inside the wall. **The breaker cuts first.** It watches for two different dangers, with two mechanisms:

- **Overload**: too many appliances on the same circuit. The current is a little too high, for a long time. A **bimetallic strip** (two metals bonded together that expand differently) heats, bends and trips the breaker after a few seconds to a few minutes.
- **Short circuit**: two wires touching. The current becomes enormous at once. A **coil** creates a magnetic field that opens the contact within a few milliseconds.

## Reading a breaker

**The rating**, in amps, is printed on it: the current it lets through continuously. In France, the standard ties the rating to the size of the wire it protects (other countries have their own tables, on the same principle):

| Circuit | Wire | Rating |
|---|---|---|
| Lighting | 1.5 mm² | 10 A (16 A allowed) |
| Ordinary sockets | 1.5 mm² or 2.5 mm² | 16 A or 20 A |
| Washing machine, dishwasher, oven | 2.5 mm² | 20 A |
| Hob | 6 mm² | 32 A |

**Never a higher rating than the wire can take.** Replacing a 16 A breaker that keeps tripping with a 32 A one removes the protection: the wire will heat until something burns.

**The letter** in front of the rating (B, C or D) says when it cuts instantly: C for ordinary household use, B for long runs, D for motors with a hard start.

## The RCD: the one that saves lives

Current that leaves by the live wire must come back by the neutral. If some is missing, it's escaping somewhere else: through a wet appliance, a damaged wire, **or a person**. The **residual current device** (RCD) compares the two and cuts as soon as the difference reaches its threshold: **30 milliamps** for those protecting people, within a few tens of milliseconds. Fast enough that an electric shock doesn't become electrocution.

- It has a **test button**: press it once a month, it must cut cleanly.
- It comes as **type AC** and **type A**: in France, type A is required on hob and washing machine circuits, whose electronics produce leaks a type AC can miss.

**The main switch** near the meter cuts the whole house. It is often residual-current too, with a higher threshold and a slight delay, so that the 30 mA devices act first.

## It tripped: read the message

- **It trips again immediately** when switched back on: a **short circuit**. Unplug everything on that circuit, switch on, then plug in one appliance at a time. The culprit trips it when plugged back in.
- **It trips after a few minutes**, when everything runs at once: an **overload**. Spread appliances across other circuits.
- **The RCD trips**: a **leak**. Look for water: an outdoor socket, a bathroom, an appliance that took on moisture, a water heater. Same method: unplug everything, switch on, plug back in one at a time.
- **It trips during storms**: a surge, or water getting in somewhere.

## An electrician's tips

- **Never hold the lever up** to stop a breaker tripping. Modern ones cut anyway, old ones don't, and that's how fires start.
- **A breaker that's warm or smells hot** almost always has a loose terminal screw. A bad contact heats up, see [[TEC-ENE-003]].
- **Label your panel** on a day when everything works. On the day you need to cut the kitchen in the dark, you won't have time to search.
- **Old fuses** are replaced with a fuse of the same rating, never with copper wire or kitchen foil.
- **Before power returns after a long outage**, switch off circuits for fragile or dangerous appliances (heaters, oven, pumps), and switch them back on one by one: the grid often comes back with surges.
- **A generator is never connected to a wall socket** with a cable with two male plugs. It would feed power back into the grid and can kill a technician working on the line hundreds of metres away. It needs a transfer switch, fitted by an electrician. See [[URG-RES-001]].
