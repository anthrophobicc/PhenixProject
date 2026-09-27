---
id: TEC-MEC-009
titre: Driving a metro train
axe: 2
categorie: Mécanique et Transport
temps: Court
contexte: 1
risque: Exposé
materiel: Technique
priorite: normale
origine: officielle
tags: [metro, subway, train, rail, third rail, signalling, driving, tunnel, transport]
sources: ["RATP (Paris transport authority), press files on the automation of lines 1, 4 and 14", "Pyrgidis C., Railway Transportation Systems: Design, Construction and Operation, CRC Press", "Transport for London, public documentation on the network and its power supply", "UITP, World Report on Metro Automation"]
---

::A metro train is driven with a single lever. Everything else, the power, the signals, the control room, sits around the train, and that's what makes it run.::

## What moves a train

**Power comes through the track.** On most metros, a **third rail** laid beside the running rails carries direct current, **750 volts** in Paris, 630 in London. A metal shoe under the train slides along it. Other networks use an overhead line, at 1,500 volts.

**Substations** along the lines convert grid power into direct current. **If they go down, everything stops**: a metro train has no engine of its own, only batteries for emergency lighting, doors and the radio.

**The electric motors** are spread under several cars. When braking, they become generators and send current back into the rail: that's electric braking. Friction brakes take over at low speed and to stop.

## The cab

A metro driver has far fewer controls than you'd think:

- **The master controller**, a single lever: pushed, the train accelerates; in neutral, it coasts; pulled, it brakes; all the way, **emergency braking**.
- **The dead man's device**: the driver must keep constant pressure, or release and press again at regular intervals. If not, because they've fainted, the train brakes by itself. In France it's called the **VACMA**.
- **The door controls**, left side and right side, which only open when stopped at a platform.
- **The cab key or badge**, which switches the cab on. A train has a cab at each end; only one is active at a time.
- **The train radio** to the control centre.
- **Screens** showing the permitted speed, faults, door status.

## Signalling: why you can't just floor it

Two trains must never be on the same section. The track is divided into **blocks**, and an occupied block is protected by signals and, above all, by an **automatic train protection system** that brakes the train if it goes over the permitted speed or passes a red signal.

On modern lines, this system is continuous (**CBTC**): the train knows at all times where the one ahead is and adjusts its speed to the metre. That's what allows a train every 85 to 90 seconds at rush hour.

On **driverless lines** (1, 4 and 14 in Paris, Lille, Copenhagen, Dubai, Singapore), there's no driver at all. The central control room runs each train, and platform screen doors close off the platform.

## The control room

A metro is run first of all from a **central control room**: a large room with the layout of the lines, the position of every train, the status of substations, points, tunnel ventilation and pumps. The controllers decide departures, power cuts for maintenance work, the evacuation of a train. The driver carries it out.

## Tips from people who know the tunnels

- **The third rail is always live until proven otherwise.** Even when trains have stopped running. It's often protected by a wooden or plastic cover, but not everywhere. Contact kills. Never step on it, or on its supports.
- **Tunnels have emergency exits** at regular intervals, connected to the surface by stairs and ventilation shafts. They're shown by lit signs and arrows painted on the walls, giving the direction and distance of the nearest station or exit.
- **A train evacuated in a tunnel** is emptied from the front or the back, on orders, once the power is cut. The side doors often open onto the wall or the live rail.
- **Pumps** constantly drain water from the tunnels. Without power for days, the low parts of a network flood, especially near a river.
- **Tunnels have been used as shelters.** In London during the Blitz, up to 177,000 people slept in them on some nights of 1940. They protect from blast and fragments, not from water or stale air once ventilation stops. See [[TEC-CON-009]].
- **A train without power weighs several hundred tonnes.** Without the grid, it doesn't move. Maintenance draisines, small diesel or battery vehicles, and hand trolleys, on the other hand, do run on the rails.

Driving a car and a boat is in [[TEC-VOI-001]] and [[TEC-NAV-001]]. How a station works, and what you find there, is in [[SURV-REC-012]].
