# Fiches en anglais

Chaque fichier traduit une fiche du dossier `corpus/` et porte **le même identifiant**. Il est rangé dans le même axe. Exemple : `corpus/axe-3-survie/URG-EAU-001.md` devient `traductions/en/axe-3-survie/URG-EAU-001.md`.

Quand l'application est en anglais, la traduction remplace le texte de la fiche. Une fiche sans traduction reste en français, avec la mention « FR » dans la liste.

## Règles

**Ce qui se traduit :**
- le titre ;
- le texte ;
- les balises (`tags`), pour que la recherche anglaise trouve la fiche ;
- les sources, sauf les titres d'ouvrages et les noms propres.

**Ce qui ne bouge pas :**
- `categorie`, `temps`, `contexte`, `risque`, `materiel`, `priorite` et `origine` gardent les valeurs françaises du corpus : l'application les traduit à l'affichage ;
- les liens `[[ID]]` restent tels quels ;
- les chiffres, doses et durées sont identiques à la fiche d'origine ; on ajoute seulement l'équivalent impérial entre parenthèses quand il aide (2 000 m, soit 6 500 ft).

**Titres de section :** `## ACT`, `## UNDERSTAND` et `## ADAPT` remplacent `AGIR`, `COMPRENDRE` et `ADAPTER`.

**Deux caractères sont interdits**, parce que les fiches sont recopiées telles quelles dans le code : l'accent grave isolé (caractère U+0060) et la suite `${`.

## Après chaque modification

```
node traductions/synchroniser.js
```

Le script vérifie que chaque traduction correspond à une fiche existante et que ses liens mènent quelque part. Il recopie ensuite toutes les traductions dans `app/phenix.html`, `app/index.html` et `site/phenix.html`.

Une traduction reste une traduction : si la fiche française change sur le fond, la version anglaise doit suivre.
