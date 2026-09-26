---
id: TEC-ENE-001
titre: Electrical energy in everyday objects
axe: 2
categorie: Énergie et Électricité
temps: Long
contexte: 1
risque: Discret
materiel: Technique
priorite: normale
origine: officielle
tags: [electricity, salvage, equipment]
sources: []
---

::An electrical setup can be read with four values and a single calculation. Everything else follows from them.::

## Reading a setup

It all starts with a rating plate. Four values, and nothing else is needed to decide.

- **The voltage**, in volts. This is the value that destroys. Powering a device at the wrong voltage kills it immediately, sometimes violently.
- **The current**, in amps. What the device draws.
- **The power**, in watts. Often written down; with direct current, it's the voltage multiplied by the current.
- **The type of current.** A straight line for direct current, a wavy line for alternating current. They're not variations of the same thing.

The relationships between voltage, current and resistance, and wiring in series and in parallel, are detailed in [[TEC-ENE-002]].

One calculation is used every day. Power in watts multiplied by a duration in hours gives energy in watt-hours. It's the only unit that lets you compare a need with a reserve. A capacity in amp-hours says nothing on its own: multiply it by the nominal voltage. That's why two batteries advertised with the same capacity can hold very different amounts of energy.

Once you have that calculation, sizing becomes trivial: add up your watt-hours per day, compare them with what you store, and you know how many days you can last. The same calculation decides whether electric propulsion is realistic, see [[TEC-MOT-001]].

## Handling rules

1. **Switch off and check there's no voltage before touching anything.** An unplugged device isn't a safe device.
2. **Read the plate before plugging anything in.** Always.
3. **Respect polarity with direct current.** It has a direction. Reversing it destroys electronics instantly, without warning.
4. **Set aside any deformed lithium cell.** Swollen, punctured, crushed: it can't be repaired and it can't be tested. It can go into {{thermal runaway|A self-sustaining chain reaction inside a damaged lithium cell, which needs no outside oxygen.}}.
5. **Never touch the large capacitors in a switch-mode power supply, a microwave or a camera flash.** They hold a charge that can kill for several minutes after being unplugged, sometimes much longer.

## Where to find what

**You're looking for storage.** Standard cylindrical lithium cells are found in a large share of power-tool and laptop battery packs. A dead pack is rarely dead as a whole: it's almost always one or two cells dragging the rest down, while the others are still good.

**You have no battery-management electronics.** Then prefer lead-acid. Batteries from UPS units and alarm systems keep a residual charge for a long time and can be recharged with basic means. That's their decisive advantage over lithium, which needs precise management or it can catch fire.

**You're looking for power generation.** Solar panels from road signs, garden lights and street furniture are everywhere, rarely watched, and produce power straight away. Sizing a full setup is covered in [[TEC-SOLR-001]].

**You're salvaging on the spot.** Sorting out what can still be used is in [[SURV-REC-002]], and the search method is in [[SURV-REC-001]].

**You want to go further.** Wiring into a system, overcurrent protection, earthing and live work belong in separate sheets. These are subjects where a mistake is deadly, not just expensive: they're covered on their own, never at the end of a sheet.
