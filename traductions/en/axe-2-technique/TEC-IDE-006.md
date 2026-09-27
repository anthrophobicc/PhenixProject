---
id: TEC-IDE-006
titre: The card payment terminal
axe: 2
categorie: Information et Données
temps: Court
contexte: 1
risque: Discret
materiel: Technique
priorite: normale
origine: officielle
tags: [payment terminal, card, payment, contactless, chip, bank, blackout]
sources: ["EMVCo, EMV Integrated Circuit Card Specifications for Payment Systems, books 1 to 4", "Groupement des Cartes Bancaires CB, contactless payment operating rules", "Banque de France, Observatory for the Security of Payment Means, annual report", "ISO/IEC 14443, proximity contactless cards"]
---

::A bank card holds no money. It holds a key that proves it's really that card. The terminal pays nothing: it asks the bank a question, and waits for the answer.::

## What's in the card

The chip is a real little computer, with protected memory. It keeps a **secret key** that it never reveals, even to whoever reads it. For each payment, it uses it to compute a **cryptogram**: a unique code, valid for this transaction, this amount, this day.

That's what makes a chip card hard to copy. You can read its number, not its key; and a stolen cryptogram works only once.

**The magnetic stripe** on the back holds only the number and the expiry date. It's easy to copy: that's why it's hardly used in Europe any more.

## What happens in two seconds

1. **Reading.** The terminal talks to the chip, by contact or by radio.
2. **The PIN.** You type your PIN. In Europe, most of the time **the chip itself checks it**: the PIN never goes to the bank. Three mistakes and it locks.
3. **The request.** The terminal sends the amount and the cryptogram to the merchant's bank (the **acquirer**).
4. **The network.** The acquirer passes it through the card's network (CB, Visa, Mastercard) to **your bank**, the issuer.
5. **The decision.** Your bank checks the cryptogram, the balance or limit, signs of fraud, and answers yes or no.
6. **The receipt.** The answer comes back the same way. All of this takes one to three seconds.

**The money itself doesn't move yet.** In the evening, the terminal sends all the day's transactions in one batch. The banks settle between themselves, and the merchant is credited a day or two later, minus a fee.

## Contactless

The card contains a small antenna. The terminal emits a radio field at **13.56 MHz** that powers the chip from a few centimetres away, with no battery. Payment terminals are designed to read at under about 4 cm (1.5 in).

To go fast, the PIN is skipped below a set amount, **50 euros in France** (the limit varies by country). To limit risk if the card is stolen, it counts payments made without a PIN: past a cumulative amount or a number of transactions, it asks for the PIN on the next payment.

**A phone** works the same way, but the card number is replaced by a substitute number, and your fingerprint or face replaces the PIN.

## Why it can say no

- Spending limit reached (often over a rolling 7 or 30 days).
- Card blocked, expired, or worn chip: try contactless, or the other way round.
- Suspected fraud: unusual purchase, unusual country. Your banking app often flags it.
- **No network.**

## When the network goes down

A terminal needs two things: **power and a link** (landline, internet, or a SIM card for mobile terminals).

Some terminals can accept a payment **offline** under a small amount set by the bank (the floor limit): the chip checks the PIN and the card alone, the transaction is stored and sent later. It's a risk for the merchant, who limits or refuses it.

During a wide blackout, like in Spain and Portugal on 28 April 2025, terminals stop along with everything else: shops still open accept **cash only**. Keep some at home, in small notes. See [[TEC-RES-001]].

## Protecting yourself

- **Cover the keypad** when typing your PIN: a camera or a glance is enough to steal it, and the card gets stolen next.
- **Look at the terminal** of a cash machine or a petrol pump: a front that moves, a thick reader, a raised keypad can hide a skimmer.
- **The amount shown** is the one you agree to: read it before presenting the card.
- **A lost card** must be cancelled immediately, through the app or your bank's number. In France, the interbank card cancellation number is 0 892 705 705.
- A stolen contactless card is limited by its counter; online payment with your numbers is the real risk. Watch your statements.
