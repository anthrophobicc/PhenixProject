---
id: SURV-REC-021
titre: Salvaging a laptop
axe: 3
categorie: Récupération
temps: Court
contexte: 1
risque: Discret
materiel: Récupération
priorite: normale
origine: officielle
tags: [salvage, electronics, battery, lithium, signal]
sources: ["Battery University — lithium-ion cells: deep discharge, storage, safety", "INRS (France) — Lithium batteries: fire risks", "iFixit — laptop teardown guides"]
---

::A dead laptop holds a battery, some of the strongest magnets there are, a perfect mirror and a screen. As long as you know what to keep, and what never to puncture.::

## ACT

1. **Try it first.** A laptop that boots, with its charger, is worth far more in one piece: it can hold offline maps, documents, a library like Phenix. Only take apart what's truly dead.
2. **Disconnect the battery before anything else.** It sits under the keyboard or under the bottom cover. Unclip its connector **before** touching anything else.
3. **Look at it.** Swollen, punctured, hot, or smelling of solvent: don't open it, don't bend it. Put it outside, away from anything that burns, on soil or sand.
4. **Keep, in this order:**
   - **the battery**, if healthy: lithium cells for a lamp or a power bank (see ADAPT);
   - **the charger**: a clean 19 to 20 volt power supply;
   - **the hard drive**, if it has one: two neodymium magnets and platters that make mirrors;
   - **the fans, speakers, the webcam, the little coin cell** on the motherboard;
   - **the screws, the thin wires, the case** if it's aluminium.
5. **Store loose cells insulated**, terminals taped over, never loose in a pocket with coins or keys.

## ADAPT

**Making a signal mirror.** Open the hard drive (Torx screws, often one hidden under the label). The platter is an almost perfect mirror. In laptops it's often glass: don't drill it, aim with your outstretched hand, see [[SIG-COM-001]].

**The magnets.** They snap together hard enough to pinch skin until it bleeds. Keep them away from pacemakers, bank cards and compasses. Stuck to a needle or a screwdriver, they magnetise it for life.

**Making a power bank.** Older laptops have cylindrical cells, newer ones flat pouches. A single cell is charged with a small USB charging module made for lithium, never plugged straight into a power supply. Paired with a USB boost module, the cells can charge a phone.

**The cell is nearly empty.** Measure its voltage with a multimeter: below roughly 2.5 volts, it has been over-discharged. Don't recharge it: it can heat up and catch fire while charging.

**The screen.** It won't work on its own, but with a small controller board that matches its model number (label on the back), it becomes a monitor. Even broken, its back layers spread light evenly: put an LED strip behind them for soft, even lighting.

**A battery fire.** Don't lean over it. Move anything flammable away, and drown it in plenty of water, or cover it with sand if it's outside: a powder extinguisher knocks down the flames but the cell often flares up again. See [[URG-INC-002]].

**The data.** The drive holds someone's life. What's useful to everyone, maps, books, manuals, can be kept. The rest is none of your business.

## UNDERSTAND

**Why damaged lithium is so dangerous.** A lithium cell is a very thin sandwich of two electrodes separated by a membrane a few thousandths of a millimetre thick. Punctured, crushed or overheated, the membrane fails: the electrodes touch, the cell heats up, breaks down its own electrolyte and releases what feeds the fire. That's thermal runaway, and it spreads from one cell to the next.

**Why 2.5 volts.** An "empty" cell normally stops around 3 volts: its protection circuit cuts it off first. Left for months without that circuit, it can drop much lower. The copper in one electrode then starts to dissolve, and grows back as needles during the next charge. Those needles can pierce the membrane: an internal short circuit, with no warning. The 2.5 volt threshold keeps a margin.

**Why a hard drive platter makes such a good mirror.** The read heads fly a few nanometres above its surface: it has to be polished almost to the atom, far beyond a bathroom mirror.

**Why such strong magnets in so little space.** The arm that moves the heads has to jump from track to track in a few milliseconds. Neodymium magnets give that force in a few grams, and that's exactly why they're worth salvaging.
