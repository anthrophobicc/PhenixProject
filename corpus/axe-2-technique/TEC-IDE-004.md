---
id: TEC-IDE-004
titre: Les caméras de surveillance
axe: 2
categorie: Information et Données
temps: Court
contexte: 1
risque: Discret
materiel: Technique
priorite: normale
origine: officielle
tags: [camera, surveillance, video, infrarouge, securite, reseau]
sources: ["Norme EN 62676-4, systèmes de vidéosurveillance, lignes directrices d'application", "CNIL, fiches pratiques sur la vidéoprotection et la vidéosurveillance", "Documentation technique des codecs H.264 et H.265 (ITU-T)"]
---

::Une caméra ne voit pas mieux que vous. Elle voit plus longtemps, sans cligner, et elle garde tout. C'est sa seule force, et ses faiblesses viennent de la même place.::

## Ce qu'il y a dedans

Une caméra de surveillance est un appareil photo qui prend 15 à 30 images par seconde, sans arrêt.

**L'objectif** concentre la lumière. Sa focale décide de tout : courte, elle voit large mais les détails sont petits ; longue, elle voit loin mais étroit. Une caméra ne peut pas tout voir en détail à la fois.

**Le capteur** transforme la lumière en pixels. Plus il y en a, plus on peut agrandir l'image, mais seulement si l'objectif et la lumière suivent.

**Le filtre infrarouge.** Le jour, un petit filtre bloque l'infrarouge pour garder des couleurs justes. La nuit, il s'escamote avec un petit clic, la caméra passe en noir et blanc et s'éclaire elle-même avec des **LED infrarouges**.

**Le processeur** compresse l'image et l'envoie. Il fait souvent aussi la détection de mouvement, parfois la reconnaissance de personnes ou de véhicules.

## La vision de nuit

Les LED infrarouges à **850 nm** donnent une lueur rouge sombre, visible à l'œil quand on regarde la caméra dans le noir. Celles à **940 nm** sont invisibles, mais portent moins loin.

Cet éclairage a une portée limitée, souvent 20 à 30 m. Au-delà, l'image est noire. Voir [[TEC-NUI-001]] pour la vision nocturne en général.

**Un appareil photo de téléphone voit l'infrarouge** : filmez la caméra dans le noir, ses LED apparaissent comme des points violets ou blancs.

## Analogique ou IP

**Les caméras analogiques** (et leurs versions modernes HD sur câble coaxial) envoient un signal vidéo brut à un enregistreur, le **DVR**. Tout reste dans le bâtiment.

**Les caméras IP** sont de petits ordinateurs sur le réseau. Elles envoient un flux numérique vers un enregistreur réseau (**NVR**), un serveur ou un cloud. Beaucoup sont alimentées par le câble réseau lui-même (**PoE**, Power over Ethernet).

**Les caméras WiFi grand public** envoient presque toujours leurs images vers les serveurs du fabricant. Sans internet, beaucoup ne font plus rien, ou seulement enregistrer sur leur carte mémoire.

## Pourquoi la compression compte

Une vidéo brute remplirait un disque en quelques heures. Les codecs **H.264** et **H.265** ne gardent que ce qui change d'une image à l'autre. Un parking vide ne coûte presque rien ; une rue sous la pluie ou un arbre au vent coûte beaucoup, parce que tout bouge.

Conséquence pratique : un enregistreur garde souvent **une à quatre semaines**, puis écrase les images les plus anciennes. **Si vous avez besoin d'une image, demandez-la vite.**

## Détecter, reconnaître, identifier

La norme européenne EN 62676-4 fixe ce qu'on peut attendre d'une image selon le nombre de pixels qui couvrent un mètre de scène :

| Objectif | Pixels par mètre | Ce qu'on peut dire |
|---|---|---|
| Détecter | 25 | Il y a quelqu'un |
| Observer | 62 | Ce qu'il fait, ses vêtements |
| Reconnaître | 125 | C'est une personne qu'on connaît |
| Identifier | 250 | On peut établir qui c'est |

Une caméra 4K qui filme un parking de 40 m de large donne environ 100 pixels par mètre : elle reconnaît peut-être, elle n'identifie pas. **C'est pour cela que les images de journaux télévisés sont si floues.**

## Ce qui trompe une caméra

- **Le contre-jour** : une silhouette devant une porte vitrée ou des phares devient noire. Les caméras dites WDR compensent en partie.
- **Les reflets de vitre** : une caméra derrière une fenêtre, la nuit, ne voit que le reflet de ses propres LED.
- **La pluie, la neige, les toiles d'araignée** devant l'objectif déclenchent la détection de mouvement sans fin, ou aveuglent l'image la nuit.
- **L'angle** : une caméra placée trop haut ne voit que des sommets de crânes et des visières de casquettes.
- **Le réseau** : une caméra IP mal protégée, avec son mot de passe d'usine, est accessible depuis internet. Des sites entiers recensent des caméras ouvertes.

## Installer la sienne

1. Décidez **ce que vous voulez voir** : l'entrée, une allée, une boîte aux lettres. Une caméra par besoin, pas une caméra pour tout.
2. Placez-la entre **2,5 et 3 m de haut**, assez basse pour voir les visages, assez haute pour ne pas être arrachée.
3. Évitez le contre-jour : pas face à l'est ou l'ouest, pas face à une lampe.
4. **Changez le mot de passe** dès l'installation, mettez à jour, et si possible gardez-la sur un réseau séparé.
5. Préférez un enregistrement **local** (carte, NVR) : il marche sans internet.

**Le droit.** En France, un particulier ne peut filmer que chez lui. La voie publique, le jardin ou les fenêtres du voisin sont interdits. Un salarié doit être informé, et les images ne se gardent pas plus d'un mois. Les caméras de la ville suivent d'autres règles, voir [[TEC-IDE-005]].
