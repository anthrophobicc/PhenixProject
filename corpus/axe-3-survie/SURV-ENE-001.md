---
id: SURV-ENE-001
titre: Alimenter un circuit sans le réseau
axe: 3
categorie: Feu, Eau et Ressources
temps: Long
contexte: 1
risque: Discret
materiel: Technique
priorite: normale
origine: officielle
tags: [electricite, groupe, batterie, inverseur, retroalimentation, terre, priorite]
sources: ["NF C 15-100, Installations électriques à basse tension, dispositions sur les sources de remplacement", "Enedis, Consignes de sécurité sur le raccordement de groupes électrogènes", "Rapports de sécurité électrique sur les accidents de rétro-alimentation", "Documentation constructeurs d'inverseurs de source et d'onduleurs"]
---

::Une seule règle tue dans ce domaine, et elle tue quelqu'un d'autre que vous : on isole avant d'injecter. Tout le reste n'est que dimensionnement.::

Le fonctionnement du réseau est dans [[TEC-RES-001]], le raisonnement sur le courant dans [[TEC-ENE-002]] et [[TEC-ENE-003]].

## COMPRENDRE

### La rétro-alimentation, et pourquoi c'est la première chose

Si vous injectez du courant dans une installation encore reliée au réseau, ce courant remonte : jusqu'au tableau, jusqu'au branchement, jusqu'au transformateur du quartier. **Et là il fait l'inverse de ce que fait un transformateur en temps normal : il monte la tension.** Quelques centaines de volts deviennent plusieurs milliers sur la ligne.

Deux conséquences, et elles sont toutes les deux graves. **Un agent qui travaille sur une ligne qu'il a consignée comme hors tension se fait électrocuter par votre installation.** Et au retour du courant, votre source et le réseau se retrouvent en opposition : tout ce qui est branché est détruit, souvent avec un incendie.

**C'est pour cela que l'isolement précède toujours l'alimentation.** Ce n'est pas une formalité administrative, c'est le point entier.

### Comment on isole correctement

**L'inverseur de source** est un organe mécanique à deux positions exclusives : réseau, ou source de secours. Il ne peut physiquement pas être dans les deux à la fois. C'est la seule solution propre, et elle existe en version manuelle, simple et peu coûteuse.

**Le disjoncteur de branchement ouvert** est le minimum absolu si vous n'avez pas d'inverseur : on coupe l'arrivée générale, franchement, avant toute chose.

**Et la solution qui évite tout le problème : ne rien injecter dans l'installation du tout.** Une rallonge depuis le groupe ou l'onduleur jusqu'à l'appareil, directement. C'est moins confortable, c'est totalement sûr, et c'est ce qu'il faut faire tant qu'on n'a pas d'inverseur.

### La terre

Une source autonome doit avoir une référence de terre, sinon les protections différentielles ne détectent rien et un défaut ne coupe pas. Beaucoup de groupes portables ont un régime particulier où les deux conducteurs sont isolés de la terre : c'est sûr pour un appareil branché directement, et ça ne l'est plus dès qu'on alimente une installation. **Lisez la plaque du groupe, elle le dit.**

### Le dimensionnement, en deux chiffres

**La puissance de régime**, celle que l'appareil consomme en fonctionnement.

**La puissance de démarrage**, celle qu'il appelle pendant une seconde à l'allumage. Tout ce qui a un moteur — réfrigérateur, congélateur, pompe, compresseur — appelle **trois à huit fois sa puissance nominale** au démarrage. Un réfrigérateur de 150 W peut demander 900 W pendant une seconde.

C'est la cause numéro un des pannes de groupes sous-dimensionnés, et elle ne se voit pas sur l'étiquette.

## AGIR

**1. Faites la liste de ce qui doit vraiment être alimenté**, et dans cet ordre : le froid alimentaire, l'eau si elle demande une pompe, la lumière, la communication, la recharge. Le chauffage électrique est hors de portée de toute source autonome raisonnable.

**2. Additionnez les puissances de régime, et ajoutez la plus grosse puissance de démarrage du lot.** C'est votre besoin réel.

**3. Choisissez où vous branchez.**
- Un ou deux appareils : rallonge directe depuis la source. Rien d'autre à faire.
- Toute l'installation : inverseur de source, et rien d'autre.
- Jamais : une prise mâle-mâle branchée dans une prise murale. Ce montage est ce qui tue les agents et ce qui brûle les maisons, et il n'a aucune excuse.

**4. Mettez le groupe dehors, toujours.** Un moteur thermique produit du monoxyde de carbone, inodore, et il tue dans un garage ouvert, sous un auvent, dans une cave ventilée. Dix mètres d'une ouverture, échappement au vent. Voir [[URG-AIR-001]] et [[TEC-CON-007]].

**5. Soignez les rallonges.** Une section trop faible sur une grande longueur fait chuter la tension et chauffer le câble : l'appareil peine, la rallonge fond. Déroulez complètement un enrouleur avant de tirer dessus — enroulé, il chauffe comme une bobine de chauffage.

**6. Protégez.** Un fusible ou un disjoncteur au départ de la source, toujours. Une batterie de voiture qui se court-circuite fait fondre un outil en quelques secondes et démarre un incendie.

## ADAPTER

**Vous avez une batterie de voiture et rien d'autre.** C'est déjà beaucoup. Éclairage en 12 V direct — voir [[SURV-LUM-001]] —, recharge d'appareils, petit ventilateur, radio. Avec un convertisseur, du 230 V pour les petites puissances. Surveillez la décharge : une batterie de démarrage descendue trop bas ne remonte pas. Voir [[TEC-ENE-004]].

**Vous avez un panneau solaire.** Panneau, régulateur, batterie, puis les usages. **Le régulateur n'est pas optionnel** : sans lui, le panneau détruit la batterie. Voir [[TEC-SOLR-001]].

**Vous voulez alimenter le réfrigérateur.** C'est le meilleur usage d'une source limitée, et il y a une astuce : un congélateur plein tient très longtemps fermé. Alimentez-le par périodes de quelques heures, deux fois par jour, plutôt qu'en continu — vous divisez la consommation par trois sans rien perdre.

**Vous alimentez une pompe.** Regardez la puissance de démarrage avant tout : c'est l'appareil qui fait le plus souvent caler un groupe.

**Vous n'avez qu'un vélo, une perceuse ou un moteur.** Un alternateur de voiture entraîné mécaniquement produit du courant. Le rendement humain est modeste — une centaine de watts soutenus, voir [[MEM-ANT-003]] — mais c'est suffisant pour recharger. Voir [[TEC-ENE-001]].

**Vous êtes tenté de vous raccorder ailleurs qu'à votre propre installation.** Deux faits, sans commentaire moral. C'est un vol, qui se constate à distance par les compteurs du poste. Et c'est, dans tous les pays où c'est pratiqué, **la première cause d'électrocution et d'incendie du travail électrique informel** — les raccordements sauvages tuent surtout ceux qui les font et leurs voisins de palier. Ce corpus n'en traite pas.

**Le courant revient.** Coupez votre source, basculez l'inverseur, et rebranchez progressivement. Tout rallumer d'un coup après une coupure longue fait redisjoncter, chez vous comme sur le quartier.
