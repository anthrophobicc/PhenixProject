---
id: SURV-ENE-001
titre: Powering a circuit without the grid
axe: 3
categorie: Feu, Eau et Ressources
temps: Long
contexte: 1
risque: Discret
materiel: Technique
priorite: normale
origine: officielle
tags: [electricity, generator, battery, transfer switch, backfeed, grounding, priorities]
sources: ["NF C 15-100 (French wiring standard) — low-voltage installations, provisions for backup sources", "Enedis (French grid operator) — safety instructions for connecting generators", "Electrical safety reports on backfeed accidents", "Manufacturer documentation for transfer switches and inverters"]
---

::Only one rule kills in this field, and it kills someone other than you: isolate before you feed power in. Everything else is just sizing.::

How the grid works is in [[TEC-RES-001]]; the reasoning about current is in [[TEC-ENE-002]] and [[TEC-ENE-003]].

## UNDERSTAND

### Backfeeding, and why it comes first

If you feed current into a building's wiring while it's still connected to the grid, that current flows back: to the panel, to the service connection, to the neighborhood transformer. **And there it does the opposite of what a transformer normally does: it steps the voltage up.** A few hundred volts become several thousand on the line.

Two consequences, both serious. **A line worker on a line they've locked out as dead gets electrocuted by your setup.** And when the power comes back, your source and the grid end up fighting each other: everything plugged in is destroyed, often with a fire.

**That's why isolating always comes before powering anything.** It isn't paperwork, it's the whole point.

### How to isolate properly

**A transfer switch** is a mechanical device with two mutually exclusive positions: grid, or backup source. It physically can't be in both at once. It's the only clean solution, and it exists in a manual version that's simple and cheap.

**An open main breaker** is the absolute minimum if you don't have a transfer switch: you cut the main supply, firmly, before anything else.

**And the solution that avoids the whole problem: don't feed anything into the building's wiring at all.** An extension cord from the generator or the inverter straight to the appliance. It's less convenient, it's completely safe, and it's what you should do for as long as you don't have a transfer switch.

### Grounding

A standalone source needs a ground reference, or the residual-current protections detect nothing and a fault doesn't trip anything. Many portable generators use a special arrangement where both conductors are isolated from ground: that's safe for an appliance plugged in directly, and it stops being safe once you power a building's wiring. **Read the generator's rating plate: it tells you.**

### Sizing, in two numbers

**Running power**: what the appliance draws while it's working.

**Starting power**: what it pulls for a second when it switches on. Anything with a motor — fridge, freezer, pump, compressor — pulls **three to eight times its rated power** when it starts. A 150 W fridge can ask for 900 W for one second.

It's the number one cause of breakdowns on undersized generators, and it doesn't show on the label.

## ACT

**1. List what really needs power**, in this order: food cooling, water if it needs a pump, light, communication, charging. Electric heating is beyond any reasonable standalone source.

**2. Add up the running powers, then add the biggest starting power in the lot.** That's your real need.

**3. Choose where you plug in.**
- One or two appliances: an extension cord straight from the source. Nothing else to do.
- The whole building: a transfer switch, and nothing else.
- Never: a male-to-male cord plugged into a wall outlet. That setup is what kills line workers and burns houses down, and there's no excuse for it.

**4. Keep the generator outside, always.** An engine produces carbon monoxide, which has no smell, and it kills in an open garage, under a porch roof, in a ventilated basement. Ten meters (30 feet) from any opening, exhaust downwind. See [[URG-AIR-001]] and [[TEC-CON-007]].

**5. Take care of your extension cords.** A wire that's too thin over a long run drops the voltage and heats the cable: the appliance struggles, the cord melts. Unroll a cord reel completely before drawing power through it — coiled up, it heats like a heating element.

**6. Protect the circuit.** A fuse or a breaker at the source, always. A shorted car battery melts a tool in seconds and starts a fire.

## ADAPT

**You have a car battery and nothing else.** That's already a lot. Direct 12 V lighting — see [[SURV-LUM-001]] —, charging devices, a small fan, a radio. With an inverter, mains voltage (230 V, or 120 V in North America) for small loads. Watch the discharge: a starter battery run down too low won't come back. See [[TEC-ENE-004]].

**You have a solar panel.** Panel, charge controller, battery, then the loads. **The charge controller isn't optional**: without it, the panel destroys the battery. See [[TEC-SOLR-001]].

**You want to power the fridge.** It's the best use of a limited source, and there's a trick: a full freezer stays cold for a very long time with the door shut. Power it for a few hours, twice a day, rather than all the time — you cut its consumption by a factor of three without losing anything.

**You're powering a pump.** Look at the starting power first: it's the appliance that most often stalls a generator.

**All you have is a bike, a drill or an engine.** A car alternator driven mechanically produces current. Human output is modest — about a hundred watts sustained, see [[MEM-ANT-003]] — but it's enough for charging. See [[TEC-ENE-001]].

**You're tempted to hook up somewhere other than your own wiring.** Two facts, without moral commentary. It's theft, and it's detected remotely by the meters at the substation. And in every country where it happens, it's **the leading cause of electrocution and fire in informal electrical work** — illegal hookups mostly kill the people who make them and their neighbors. This library doesn't cover it.

**The power comes back.** Switch off your source, flip the transfer switch, and reconnect gradually. Turning everything back on at once after a long outage trips the breakers, at your place as well as across the neighborhood.
