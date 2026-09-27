---
id: TEC-IDE-007
titre: The green screen
axe: 2
categorie: Information et Données
temps: Court
contexte: 1
risque: Discret
materiel: Technique
priorite: normale
origine: officielle
tags: [green screen, chroma key, compositing, video, film, lighting, editing]
sources: ["Foster J., The Green Screen Handbook: Real-World Production Techniques, Sybex", "OBS Studio and DaVinci Resolve documentation, keying filters", "Brinkmann R., The Art and Science of Digital Compositing, Morgan Kaufmann"]
---

::A green screen doesn't replace the set. It replaces a colour. All the work is making sure that colour only exists behind you.::

## The principle

The camera films a person in front of a single, even colour. The software finds every pixel of that colour and makes it transparent. Another image slides in behind. That's **keying**, or *chroma key*.

It's the same idea as the TV weather map, film special effects, or the background of any video creator.

## Why green, and why sometimes blue

**Green** is the colour furthest from human skin, whatever its tone. And camera sensors have twice as many green pixels as red or blue: green is the most detailed colour, so the easiest to cut out cleanly.

**Blue** is used when the subject wears green, for night scenes, and gives less coloured reflection on skin. But it needs more light.

Absolute rule: **no clothing, accessory or object in the colour of the screen.** It would become transparent. Watch out for shiny things too, glasses, watches, jewellery: they reflect the screen.

## The three laws of lighting

Lighting makes 80% of the result. Software can't save a badly lit screen.

1. **The screen must be even.** No darker corners, no creases, no glare. Two soft lights at 45 degrees on either side of the screen, rather than one in front.
2. **Light the subject separately**, with their own lights, as for any video.
3. **Keep the subject away from the screen: at least 1.5 to 2 metres** (5 to 6.5 ft). Too close, the green reflects onto shoulders and hair, that's *spill*, and the subject's shadow falls on the screen.

## Camera settings

- **Fast shutter speed** (1/100 s or faster): motion blur mixes subject and green, and the key gets messy.
- **Focus on the subject.** A slightly blurred screen keys even better.
- **Don't overexpose**: a blown-out green becomes almost white.
- **The highest resolution possible**, and a lightly compressed format if the camera offers one.

## The software

Free software is enough: OBS for live, DaVinci Resolve, CapCut or Shotcut for editing. The setting always goes in the same order:

1. pick the colour to remove with the eyedropper, on a mid-tone area of the screen;
2. raise the tolerance until the whole screen disappears, no more;
3. soften the edges a little;
4. turn on **spill suppression**, which removes the green reflection on the outlines.

## Tips from people who do it every day

- **Iron the fabric**, or stretch it on a frame. Every crease makes a shadow, and every shadow is another shade of green. A wall painted matte green beats a creased cloth.
- **Frame wide, crop later.** If the subject goes off the screen, even by a finger, it's lost. Frame the shot, then mask everything outside the screen with a rough mask (*garbage matte*).
- **Fine hair** is the real test. A light placed behind the subject, towards the top of the head, separates hair from the screen and makes the key much cleaner.
- **The final background decides the lighting.** If the new background is a sunset, light the subject warm and from the side. A subject lit like an office, dropped onto a beach, fools no one.
- **No green screen?** A blue sheet, a plain wall, a clear sky behind you. The software accepts any colour, as long as it's even and absent from the subject.
- **New AI tools** cut out subjects without a green screen. They get hands and hair wrong when moving: the green screen stays more reliable as soon as you move.
