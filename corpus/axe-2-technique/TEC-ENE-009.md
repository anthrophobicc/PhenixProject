---
id: TEC-ENE-009
titre: L'éolienne industrielle
axe: 2
categorie: Énergie et Électricité
temps: Court
contexte: 1
risque: Discret
materiel: Technique
priorite: normale
origine: officielle
tags: [eolienne, vent, energie, rotor, nacelle, reseau, electricite, betz]
sources: ["Burton T. et al., Wind Energy Handbook, Wiley, 3e édition", "Agence internationale de l'énergie (IEA Wind), rapports annuels", "Manwell J., McGowan J., Rogers A., Wind Energy Explained, Wiley", "RTE, Bilan électrique annuel"]
---

::Une éolienne n'est pas un moulin agrandi. C'est une centrale électrique de 150 mètres qui tourne lentement, qui se pilote seule, et qui a besoin du réseau pour exister.::

## Les dimensions

Une éolienne terrestre récente mesure **100 à 200 mètres** en bout de pale, avec un rotor de **100 à 170 mètres** de diamètre. Sa puissance : **2 à 6 mégawatts**. En mer, les plus grandes dépassent 15 MW, avec des pales de plus de 110 mètres.

Une pale pèse plusieurs dizaines de tonnes, la nacelle plusieurs centaines. La fondation d'une éolienne terrestre est un massif de béton armé de plusieurs centaines de mètres cubes, enterré.

## Comment elle marche

**Les pales** ne sont pas poussées par le vent comme une voile. Elles ont un profil d'aile d'avion : l'air qui les contourne crée une portance qui les fait tourner. Voir [[TEC-AER-001]].

**Le rotor** tourne lentement, 5 à 15 tours par minute. Le bout des pales, lui, file à plus de 250 km/h.

**La nacelle**, en haut du mât, contient :

- **un multiplicateur** (une boîte d'engrenages) qui fait passer de 10 à 1 500 tours par minute pour la génératrice ; ou, sur les modèles « à entraînement direct », une génératrice géante à aimants permanents, sans multiplicateur ;
- **la génératrice** ;
- **le système de freinage** ;
- **l'électronique de puissance** qui adapte le courant à celui du réseau ;
- **un anémomètre et une girouette** sur le toit.

**Deux moteurs la pilotent en permanence** :

- **l'orientation** (*yaw*) tourne toute la nacelle face au vent ;
- **le calage des pales** (*pitch*) fait pivoter chaque pale sur elle-même pour prendre plus ou moins de vent, comme on règle une hélice.

## La courbe de puissance

- En dessous d'environ **3 m/s** (11 km/h), elle ne produit rien.
- Entre 3 et **12 m/s** environ, la puissance augmente très vite : **elle varie comme le cube de la vitesse du vent**. Deux fois plus de vent, huit fois plus d'énergie.
- Au-dessus de 12 m/s, elle plafonne à sa puissance nominale : les pales se mettent en drapeau pour ne pas dépasser.
- Vers **25 m/s** (90 km/h), elle s'arrête et se met en sécurité.

**La limite de Betz** dit qu'aucune éolienne ne peut capter plus de 59,3 % de l'énergie du vent qui la traverse : il faut bien que l'air continue de s'écouler derrière. Les meilleures machines atteignent environ 45 à 50 %.

Sur une année, une éolienne terrestre produit en moyenne **20 à 30 % de sa puissance maximale** (son facteur de charge), une éolienne en mer 35 à 50 %.

## Ce qu'on ne dit pas souvent

**Elle a besoin du réseau.** La plupart des éoliennes ne peuvent pas démarrer seules ni alimenter une maison isolée : leur électronique se cale sur la fréquence du réseau existant, et elles consomment un peu de courant pour tourner, orienter et chauffer. **Pendant un black-out, une éolienne s'arrête**, même en plein vent. Seules des installations spécialement conçues savent fonctionner en îlot.

**Elle se pilote de loin.** Chaque éolienne est surveillée à distance par son constructeur, qui peut l'arrêter, la redémarrer et lire ses capteurs.

**Elle vit 20 à 30 ans.** Les pales en fibre de verre et résine se recyclent mal ; le mât, le cuivre et l'acier se recyclent bien.

## Les astuces de ceux qui y travaillent

- **La glace se projette.** Par temps de givre, des blocs de glace peuvent se détacher des pales et tomber à des dizaines, voire des centaines de mètres. Des panneaux le signalent au pied des machines. Ne restez pas sous une éolienne givrée.
- **On monte à pied.** Beaucoup d'éoliennes n'ont qu'une échelle intérieure avec un rail anti-chute, ou un petit monte-charge. Cent mètres d'échelle : les techniciens sont formés au sauvetage en hauteur et travaillent toujours à deux.
- **La foudre adore les éoliennes.** Les pales ont des récepteurs métalliques et un câble qui descend jusqu'à la terre. Par orage, on s'éloigne.
- **Le bruit** vient surtout des pales, un souffle régulier, et du multiplicateur. À 500 mètres, il se confond avec le vent.
- **Une nacelle contient des centaines de litres d'huile** (multiplicateur, hydraulique), du cuivre en quantité et, sur les machines à entraînement direct, des aimants aux terres rares. C'est aussi une plate-forme d'observation à plus de 100 mètres. Voir [[SURV-REC-016]] pour ce qu'on tire d'une grosse machine immobile.

Le petit éolien, pour une maison ou un bateau, fonctionne sur les mêmes principes mais sans réseau : voir [[TEC-SOLR-001]] pour le stockage sur batteries.
