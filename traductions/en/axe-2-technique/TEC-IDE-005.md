---
id: TEC-IDE-005
titre: Public CCTV
axe: 2
categorie: Information et Données
temps: Court
contexte: 1
risque: Discret
materiel: Technique
priorite: normale
origine: officielle
tags: [camera, cctv, city, law, surveillance, privacy]
sources: ["French Internal Security Code, articles L251-1 to L255-1", "Cour des comptes (French Court of Audit), Les polices municipales, October 2020", "Piza E., Welsh B., Farrington D., Thomas A., CCTV surveillance for crime prevention, Criminology & Public Policy, 2019", "French law no. 2023-380 of 19 May 2023 on the Olympic and Paralympic Games, article 10", "Regulation (EU) 2024/1689 on artificial intelligence, article 5"]
---

::A street camera is almost never watched live. It is mostly used afterwards, provided someone asks for the footage in time.::

## How a city network works

A town's cameras are linked by fibre or radio to a **control room**: a room, a wall of screens, a few operators. French law calls cameras on public streets **vidéoprotection**, and those in private places vidéosurveillance.

An operator can only really follow a few screens at once. In a city with hundreds of cameras, **the vast majority of footage is seen by no one**. It is recorded, then erased.

Three uses dominate:

- **Live**: following a demonstration, a match, an incident reported by radio.
- **Afterwards**: police or courts request footage of a precise place and time. This is by far the main use.
- **Plate reading** (ANPR): dedicated cameras read number plates and compare them to lists of wanted vehicles.

How a camera works technically is covered in [[TEC-IDE-004]].

## What the law says in France

- Every camera on a public street needs **authorisation from the prefect**, after the opinion of a local commission.
- It must not film inside homes, nor their entrances in detail.
- **Signs** must mark the filmed area and say whom to contact.
- Footage is kept **30 days at most**, often less. Then it is erased, unless an investigation has requested it.
- Anyone can ask to see footage in which they appear, from the person named on the sign. Refusal is possible for security or investigation reasons; it can be challenged before the local commission.

Other countries have their own rules; in the UK, for instance, requests go through a subject access request under data protection law.

**Live facial recognition in the street is not allowed in France.** At European level, the 2024 AI regulation forbids it to law enforcement, except for narrow cases (searching for a victim, an imminent terrorist threat) supervised by a judge.

**Automated video analysis**, without face recognition, was trialled for the 2024 Olympics: spotting an abandoned object, a crowd surge, a person on the ground. Its future is the subject of debates and successive laws: check the law as it stands when you read this.

## Does it work?

The most solid answer comes from an analysis of 76 studies carried out over forty years (Piza and colleagues, 2019):

- a **modest drop** in crime where the cameras are, around 13% on average;
- a clear effect on **car parks** and vehicle-related theft;
- **no measurable effect on violence**: nobody thinks about the camera in the middle of a fight.

In France, the Court of Audit noted in 2020 that no overall link had been established between how many cameras a city has and its crime level. A study commissioned by the gendarmerie in 2021 found that footage had contributed to only a small fraction of solved investigations.

What cameras do well: **retrace a route afterwards**, confirm a time, find a vehicle. What they do badly: prevent.

## What's actually useful to you

**You are a victim or a witness.** Report it **within days**, giving the exact place and time. The complaint is what lets the police request the footage before it is erased. After a month, it no longer exists. Note the shops nearby too: their private cameras often have a better view than the city's.

**You want to know where the cameras are.** Signs, town council minutes (installation is voted and funded in public), some cities' open data, and collaborative maps like OpenStreetMap, where volunteers log cameras.

**You want to see your footage.** Write to the person named on the sign, within the retention period, giving place, date, time and a description of yourself.

**You care about your privacy.** A street camera is one link among many; your phone, your payments and your badges say far more. See [[SIG-COM-007]].

**During a long blackout.** A camera network depends on power and links. Without them, it goes dark like everything else, see [[TEC-RES-001]].
