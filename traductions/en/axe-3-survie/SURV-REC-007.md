---
id: SURV-REC-007
titre: Repairing a cable, a plug, a contact
axe: 3
categorie: Récupération
temps: Court
contexte: 1
risque: Discret
materiel: Technique
priorite: normale
origine: officielle
tags: [electricity, repair, cable, wire, salvage]
sources: []
---

::Most electrical failures aren't dead components. They're broken wires and dirty contacts.::

## UNDERSTAND

A circuit only works if it's **closed**: the current goes out, passes through the load, and comes back. A break anywhere produces exactly the same symptom — nothing works — whether the fault is on the way out or on the way back.

The breaking points are always the same, and this list covers almost everything: **where the cable moves**, meaning where it leaves a plug or a device; **where two metals touch**, meaning the connections; **where moisture sits**.

A degraded contact isn't a clean break: it's resistance appearing. It heats up, oxidizes further, heats up more. **A warm contact is a dying contact** — the mechanism is detailed in [[TEC-ENE-003]].

## ACT

**Find the fault before you repair anything.**

1. **Cut the power and check that there's no voltage.** Always, and with a tester, never by deduction.
2. **Look and bend.** A cable breaks near its ends: bend it gently along its whole length; a sheath that's hard, cracked, soft or locally deformed shows you the spot.
3. **Test continuity** from end to end, wire by wire, with the cable unplugged at both ends — see [[TEC-ENE-008]]. Move the cable while you measure: that's how an intermittent fault gives itself away.
4. **Check both conductors.** The return wire breaks as often as the outgoing one.

**Repairing a break.**

5. **Cut cleanly on both sides** of the doubtful area. Don't repair right at the fault: the cable is fatigued for several centimeters around it.
6. **Strip without nicking the copper.** A nick creates a weak point that will break at the first movement. Rotate the blade around the insulation instead of slicing into it.
7. **Stagger the joints.** Never join both conductors at the same spot: offsetting them by a few centimeters keeps them from touching if the insulation gives way.
8. **Make it mechanically sound first.** Twist tightly in the direction of the strands, or better, wrap one wire around the other in tight coils. **The joint has to hold on its own when you pull on it, before you insulate it.**
9. **Solder if you can.** Solder brings contact resistance down to almost nothing. Otherwise, a terminal block or a crimped connector does the job.
10. **Insulate each conductor separately**, then the whole thing. Several crossed turns, overlapping well on each side.
11. **Add strain relief.** A loop, a knot or a cable tie that takes the pull before it reaches the joint: without it, your repair will break at the same spot.

**Cleaning a contact.**

12. **Scrape off the oxidation** with fine sandpaper, a blade or an eraser. A dull contact conducts poorly.
13. **Tighten it.** Copper creeps under pressure, and a terminal loosens by itself over time.
14. **Protect it** with a trace of grease once the contact is clean and tight, if the air is damp — see [[TEC-COR-001]].

## ADAPT

**The cable cuts in and out.** It's almost always a broken strand under the insulation, at a bending point. Cut generously on both sides: a repair that's too short leaves the fatigued part in place.

**You have no electrical tape.** Heat-shrink tubing is better; failing that, thick adhesive tape, inner-tube rubber cut into a strip and stretched on in tight turns, or dipping the joint in melted plastic.

**You have no tools at all.** Scrape with whatever you have: a house key, the edge of a coin, a stone, sand on a rag. A loose battery clamp sits on a tapered post: push it all the way down, tap it with a stone, then twist it to lock it. As a last resort, a strip of aluminium (a gum wrapper, a cut-up can) slipped between the clamp and the post takes up the slack long enough to get going. **Never bridge the two terminals with anything metal**: a car battery can push hundreds of amps and the metal turns red-hot.

**You have nothing to solder with.** A well-made mechanical joint works for years. What counts is the tightness, the contact surface and protection from moisture, not the solder itself.

**The wires aren't the same metal.** Copper and aluminum in direct contact corrode — see [[TEC-COR-001]]. Use a connector designed for it, or put a suitable part between them.

**It's the cable of a device you want to power some other way.** Check voltage, polarity and power before connecting anything. Reversing polarity on direct current destroys things instantly — see [[TEC-ENE-001]] and [[TEC-ENE-002]].

**It's on a vehicle.** Vehicles are full of cables, flexible and in every size: they're the best source of raw material — see [[SURV-REC-003]].
