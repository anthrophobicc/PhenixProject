---
id: TEC-MOT-001
titre: Boat engines — the complete guide
axe: 2
categorie: Mécanique et Transport
temps: Long
contexte: 1
risque: Discret
materiel: Technique
priorite: normale
origine: officielle
tags: [engine, boat, mechanics, transport]
sources: []
---

::A marine engine isn't different from a land engine in its mechanics, but in what it goes through.::

Three constraints define every marine engine, and they explain every technical choice that follows.

**The load never lets up.** A car engine spends most of its life at part load. A boat engine pushes a mass of water continuously, with no idle time and no downhill. It works close to its peak-torque speed for hours. That's why a car engine transplanted into a boat breaks: it was never built for that. What both have in common is described in [[TEC-MOTH-001]].

**Cooling uses the water you're sailing on.** It's free, unlimited, and corrosive. All marine design revolves around that compromise.

**A breakdown isn't a stop on the hard shoulder.** Redundancy and repairability aren't luxuries.

## By where the engine sits

**Outboard.** A complete unit — engine, transmission, propeller — hung on the transom. It tilts up to lift the propeller, comes off entirely, and can be swapped in a few minutes. It's the most repairable and interchangeable engine there is on the water. Its weakness is where the weight sits: high and at the back.

**Inboard.** The engine is inside the hull, a shaft passes through the hull via a stern gland, and the propeller sits under the hull. The weight is low and central, so the boat handles the sea much better. In exchange: a hull opening to keep watertight at all times, a shaft to align to a tenth of a millimetre, cramped access, and a shaft line that fixes the propeller's angle.

**Sterndrive, or Z-drive.** Engine inside, transmission outside on a steerable leg. A compromise between the two: the propeller efficiency of an outboard, the inboard weight of an inboard. Clearly more mechanically complex, and a rubber bellows through the hull whose failure sinks the boat.

**Jet drive.** A pump sucks water in and blasts it out. Nothing sticks out under the hull, so it runs in very shallow water and there's no risk of propeller injuries. Poor efficiency at low speed, and sensitive to floating debris being sucked in.

**Electric pod.** An electric motor submerged in a pod that turns through 360 degrees. Full manoeuvrability without a bow thruster. On large vessels, diesel generators produce electricity and the pods provide propulsion: that separates power generation from propulsion, and lets generators be shut down when demand drops.

## By cycle

**Two-stroke.** One explosion per turn. High power for low weight, very few moving parts, exceptional repairability. It uses more fuel, smokes, and releases some unburned oil. Emissions regulations have pushed it back everywhere, but when you have to repair things yourself, its simplicity becomes decisive again. On direct-injection models, much of the fuel-consumption penalty disappears.

**Four-stroke.** Economical, clean, quiet, with good torque at low revs. A separate oil circuit means oil changes, more parts, and more to understand before you work on it.

**Diesel.** Huge torque at low revs, exactly what a propeller asks for. No ignition system to corrode — a considerable advantage in salty air. A much longer service life. In exchange: heavy weight, high-pressure injection that can't tolerate water, and hard starting in severe cold.

**Electric.** Maximum torque from a standstill, total silence, no vibration, no exhaust. The limit is the energy on board, and how to calculate it is in [[TEC-ENE-001]]. For slow, short use — fishing, canals, tenders — it already beats everything else.

**Steam.** Marginal today, but mentioned for one specific reason: it's the only type that accepts **any solid fuel**. Wood, coal, waste. If refined fuel supplies are cut off, it's the only engine that can be kept fed indefinitely.

## Cooling, where everything is decided

**Open circuit.** The water you sail in runs straight through the engine. Simple, light, few parts. It leaves salt, it corrodes, it scales. An open-circuit engine used at sea is flushed with fresh water after every outing, or it slowly destroys itself from the inside.

**Closed circuit.** An internal coolant circuit gives its heat to seawater in a heat exchanger. Salt water never touches the engine. Heavier, more expensive, and incomparably more durable.

In both cases, **the rubber water-pump impeller is the critical wear part**. It's destroyed in seconds if the engine runs out of the water, because it's lubricated and cooled by the water it pumps. It's the first spare part to own, before any other.

## The propeller

Two numbers define it: the **diameter**, which sets the area of water it moves, and the **pitch**, the theoretical distance travelled in one turn. High pitch and small diameter for speed, low pitch and large diameter for thrust.

An oversized propeller stops the engine from reaching its maximum speed and makes it work permanently overloaded: it's the most common cause of slow destruction of a marine engine. An undersized propeller lets the engine over-rev without producing thrust.

**{{Cavitation|Vapour bubbles forming where pressure drops on the blades, which eat into the metal and cost thrust.}}** — vapour bubbles forming where the pressure drops on the back of the blades — physically erodes the metal and costs thrust. It always points to a problem of geometry, depth or engine speed.

## Identifying a marine engine

1. **Look where it is.** Outside, inside or halfway: you already know how to reach it and what to take apart.
2. **Look for the spark plug.** Present: petrol. Absent: diesel.
3. **Look for the oil dipstick.** Present: four-stroke. Absent, with mixed fuel: two-stroke.
4. **Follow the water circuit from the intake under the hull.** Straight to the block: open circuit. Through a heat exchanger: closed circuit.
5. **Find the tell-tale water outlet at the exhaust.** No trickle of water at start-up: switch off immediately, the impeller is dying.
6. **Note the plate.** Power, maximum speed, year, serial number.

## How to choose

**You have to pick an engine to build with or salvage.** An inboard diesel if you want endurance and torque. A two-stroke outboard if you want repairability and interchangeability. Electric if your trips are short and you already produce electricity.

**You've run out of refined fuel.** A diesel accepts filtered vegetable oils with some adaptations. Steam accepts anything that burns. Petrol engines accept almost nothing but petrol.

**You have to handle the boat yourself.** Manoeuvres, buoyage and the rules of the helm are in [[TEC-NAV-001]].

**You're cannibalising.** An outboard travels whole, fits any hull with a transom, and swaps like a part. It's the closest thing to a universal standard on the water.
