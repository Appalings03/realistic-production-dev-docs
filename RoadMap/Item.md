
# Items et chaînes de production

> Document de conception pour Realistic Production, ciblant Factorio 2.1. Les propositions ci-dessous ne modifient pas le code. Les noms déjà présents dans `proto_table` sont des données de départ ; les recettes et rendements restent à équilibrer.

## Vision

Le mod remplace les chaînes vanilla par une progression industrielle plus détaillée :

**roche ou gisement naturel → minerai brut → minerai préparé → élément ou matériau → pièce → produit manufacturé.**

Les ressources sont inspirées de roches, minerais et fluides terrestres. Les procédés doivent donner une raison logistique à chaque étape (eau, énergie, sous-produits et transport), sans imposer que chaque élément du tableau périodique soit nécessaire à la progression principale.

## Règles de conception

- Les minerais vanilla remplacés ne restent pas des sources parallèles faciles de fer, cuivre, charbon ou uranium. Leurs recettes, gisements et usages sont intégrés aux chaînes réalistes.
- Une même roche peut contenir plusieurs minerais. Le concassage, le criblage et la séparation donnent des concentrés distincts ainsi que des stériles ou sous-produits.
- Les matériaux ne sont pas tous des minerais : un élément peut être extrait, raffiné, fondu, réduit chimiquement ou produit artificiellement selon sa disponibilité.
- Les fluides et gaz sont transportés dans des tuyaux et traités dans des machines adaptées. Les solides sont utilisés pour les minerais, poudres, lingots et composants.
- Les éléments artificiels sont des objectifs expérimentaux de fin de partie, pas des ressources naturelles ordinaires.
- L’extension Space Age est hors du périmètre initial ; elle pourra ajouter des chaînes dédiées après stabilisation du mod de base.

## 1. Ressources brutes

### Roches et matériaux géologiques

Ces roches peuvent servir de gisements de pierre, de silice, de chaux, d’argiles ou de minerais associés :

granit, basalte, gabbro, diorite, rhyolite, andésite, péridotite, kimberlite, calcaire, dolomie, grès, argile, schiste, craie, marbre, gneiss, quartzite, ardoise et pierre.

### Minerais et minéraux

**Métaux et minerais de base :** minerai de fer vanilla, minerai de cuivre vanilla, hématite, magnétite, goethite, sidérite, bauxite, chalcopyrite, bornite, chalcocite, malachite, galène, sphalérite, cassitérite, wolframite, scheelite, molybdénite, pentlandite, latérite, cobaltite, chromite, pyrolusite, ilménite, rutile.

**Métaux précieux et minerais spécialisés :** or natif, argent natif, platine natif, sperrylite, cinabre, stibine, spodumène, lépidolite, béryl, coltan, zircon, monazite, bastnäsite.

**Minéraux industriels et matières nucléaires :** uraninite, carnotite, thorianite, minerai d’uranium vanilla, halite, sylvite, carnallite, gypse, anhydrite, borax, colémanite, trona, nitratine, soufre natif, pyrite, apatite, fluorite, graphite, diamant.

**Combustibles solides :** charbon vanilla, lignite, anthracite, tourbe, sables bitumineux et schistes bitumineux.

Ces noms reprennent les 88 entrées prévues dans `resources_data.lua`, dont les fluides décrits plus bas. La liste ne signifie pas que chaque roche devra avoir un gisement indépendant : certaines peuvent être des résultats de traitement ou des roches hôtes d’un gisement mixte.

### Fluides et gaz naturels

- Eau et eau de mer.
- Pétrole brut.
- Saumure de lithium.
- Eau géothermale.
- Gaz naturel.
- Air, séparé industriellement en gaz utiles.

À définir ensuite : les gisements, le débit, l’épuisement éventuel, les sous-produits et la place respective des pompes et des machines de séparation de l’air.

## 2. Éléments chimiques

Le registre visé contient les 118 éléments du tableau périodique. Les éléments déjà listés dans `elements_data.lua` servent de référence pour les noms, symboles, états (item ou fluide) et niveaux.

```text
Période 1 : H He
Période 2 : Li Be B C N O F Ne
Période 3 : Na Mg Al Si P S Cl Ar
Période 4 : K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr
Période 5 : Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe
Période 6 : Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn
Période 7 : Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og
```

### Formes d’items à prévoir

- **Gaz et liquides** : éléments gazeux, halogènes et produits de procédé sous forme de fluides lorsqu’ils sont manipulés en phase fluide.
- **Éléments solides** : poudres, granulés ou lingots selon l’étape de traitement ; ne pas créer plusieurs prototypes si un changement d’icône ou de recette suffit.
- **Éléments artificiels** : produits de recherche expérimentale, fabriqués en très petite quantité avec des précurseurs et une installation dédiée.
- **Sous-produits** : éléments minoritaires obtenus lors du traitement d’un minerai polymétallique, pour faire des chaînes secondaires facultatives plutôt que bloquer la progression.

Les 118 éléments ne doivent pas tous être requis pour fabriquer les sciences ou terminer la progression. Les éléments rares, dangereux ou artificiels peuvent rester des objectifs de collection, de recherche et de production avancée.

## 3. Alliages

### Alliages déjà inscrits dans les données

Les cinq recettes de `alloys_data.lua` sont les alliages de base de départ. Leurs proportions sont des ratios de jeu à équilibrer, pas des consignes métallurgiques exactes.

| Alliage          | Ingrédients conceptuels                     | Priorité                                  |
| ---------------- | -------------------------------------------- | ------------------------------------------ |
| Acier            | Fer + carbone                                | Avancée                                   |
| Bronze           | Cuivre + étain                              | De base                                    |
| Laiton           | Cuivre + zinc                                | De base                                    |
| Duralumin        | Aluminium + cuivre + magnésium + manganèse | Expérimentale dans les données actuelles |
| Acier inoxydable | Fer + chrome + nickel + carbone              | Avancée                                   |

### Alliages proposés dans la liste initiale

À ajouter au registre après vérification de leur intérêt ludique et de la disponibilité de leurs éléments :

| Alliage                   | Éléments constitutifs                    |
| ------------------------- | ------------------------------------------ |
| Or blanc                  | Or + nickel et/ou palladium/argent         |
| Amalgame dentaire         | Mercure + argent + étain + cuivre         |
| Magnalium                 | Aluminium + magnésium                     |
| Stellite                  | Cobalt + chrome + tungstène               |
| Invar                     | Fer + nickel                               |
| Monel                     | Nickel + cuivre                            |
| Nichrome                  | Nickel + chrome                            |
| Cupronickel               | Cuivre + nickel                            |
| Étain de potier (pewter) | Étain + cuivre + antimoine                |
| Zamak                     | Zinc + aluminium + magnésium + cuivre     |
| Bêta-titane              | Titane + molybdène + aluminium + vanadium |
| Hastelloy                 | Nickel + molybdène + chrome + fer         |
| Inconel                   | Nickel + chrome + fer                      |
| Tombac                    | Cuivre + zinc                              |
| Électrum                 | Or + argent                                |

**Point de conception :** le mercure et les alliages contenant des substances toxiques doivent apparaître tard dans la progression chimique, avec une représentation et des recettes lisibles, sans ajouter de mécanique de danger obligatoire avant d’avoir une conception claire.

## 4. Pièces et produits intermédiaires

Pour remplacer les recettes vanilla qui consomment directement des minerais ou des plaques, introduire progressivement des formes manufacturées communes :

- **Métallurgie** : lingot, plaque laminée, tôle, barre, fil, tuyau et poudre métallique.
- **Mécanique** : engrenage, axe, ressort, rivet, roulement, plaque renforcée et bâti.
- **Construction** : brique réfractaire, verre, céramique, ciment/chaux, isolant et matériaux de structure.
- **Électricité** : fil conducteur, câble isolé, bobine, électrode, contact et composants électroniques.
- **Chimie** : acide, base, solvant, gaz industriel, polymère, résine, catalyseur et support de catalyseur.
- **Produits de recherche** : échantillon minéralogique, éprouvette d’alliage, analyse chimique et matériau expérimental.

Chaque forme doit avoir une fonction claire. Par exemple, les recettes de câbles utilisent du fil, les machines lourdes des bâtis et des arbres, et les fours réfractaires des briques adaptées à la chaleur.

## 5. Chaîne pétrochimique et catalyse

Proposition de chaîne :

1. Séparer le pétrole brut en fractions (gaz, naphta, distillats et résidus).
2. Traiter certaines fractions par craquage ou reformage pour produire des molécules utiles.
3. Utiliser des catalyseurs spécifiques pour orienter les réactions et augmenter les rendements.
4. Récupérer ou régénérer le catalyseur dans la recette, si l’objectif est qu’il agisse comme un équipement réutilisable plutôt qu’un consommable coûteux.
5. Faire dépendre les procédés avancés de l’eau, de l’énergie, de produits chimiques et de la gestion des sous-produits.

La règle de récupération des catalyseurs reste à valider lors de l’équilibrage ; éviter les recettes où le joueur perd un catalyseur rare à chaque cycle sans indication claire.

## 6. Remplacement des objets vanilla

La refonte doit couvrir les recettes qui utilisent les ressources remplacées, et pas seulement les gisements :

- Fer et cuivre : minerai réel → concentré → métal raffiné/lingot → plaque ou fil → composants.
- Pierre : roche extraite et/ou stériles de traitement → pierre utilisable, agrégat, chaux ou matériaux de construction.
- Charbon : distinguer les usages de combustible, de carbone métallurgique et de matière première chimique selon le type de charbon.
- Pétrole : conserver l’extraction comme fluide, mais faire passer les produits pétrochimiques par la séparation et les procédés catalytiques.
- Uranium : minerai identifié, concentration et raffinage avant les produits nucléaires ; conserver une branche tardive.
- Recettes vanilla : remplacer leurs ingrédients en préservant les paliers de recherche, les usages logistiques et l’équilibre global.

## 7. Extraction progressive et scories

Le joueur ne reçoit pas tout d'une roche dès le départ. La progression se fait en trois temps :

1. **Début de partie** : seules certaines roches sont extractibles. Les autres sont verrouillées par une technologie (colonne `tech` de la feuille `resources` ; vide = disponible dès le départ).
2. **Raffinage basique** : le traitement d'une roche ne donne que son élément principal. Tout le reste devient des **scories**.
3. **Retraitement** : des technologies permettent de retraiter les scories (béton, ciment) et d'extraire les autres éléments de la roche brute.

C'est proche de la métallurgie réelle, où les scories de haut fourneau sont valorisées en ciment.

### Élément principal

Ne pas prendre « l'élément au plus fort pourcentage » : dans les oxydes, les sulfates et les sulfures, l'oxygène ou le soufre arrivent souvent en tête.

| Minéral     | Composition (% en masse)                                           | « Le plus présent » donnerait |
| ------------ | ------------------------------------------------------------------ | -------------------------------- |
| chalcopyrite | soufre 34,94 · cuivre 34,63 · fer 30,43                          | du soufre, pas du cuivre         |
| pyrite       | soufre 53,45 · fer 46,55                                          | du soufre                        |
| gypse        | oxygène 55,76 · calcium 23,28 · soufre 18,62 · hydrogène 2,34 | de l'oxygène                    |
| hématite    | fer 69,94 · oxygène 30,06                                        | du fer (correct)                 |

Il faut donc une colonne **`primary`** (yes/no) dans la feuille `composition`, remplie à la main (ou pré-remplie puis corrigée). Avec la règle actuelle, une ressource a un seul élément `primary` ; à décider si certaines en auront plusieurs (la chalcopyrite pourrait garder cuivre et fer).

### Scories

- À décider : un seul item `slag`, ou une scorie par famille (fer, cuivre, aluminium…). Une scorie par famille permet de récupérer des éléments différents au retraitement.
- Usage de départ : béton et matériaux de construction (voir « Remplacement des objets vanilla », pierre).
- Les éléments secondaires récupérés au retraitement sont ceux de la colonne `composition` qui ne sont pas `primary`.
- Les scories sont des items solides : elles occupent de la place et se stockent, ce qui donne une raison logistique à les valoriser.

### Conséquences sur les données

- Feuille `resources` : colonne `tech` (technologie qui déverrouille la roche).
- Feuille `composition` : colonne `primary`.
- `level` d'un élément : à redéfinir comme le niveau du premier procédé qui le libère. Aujourd'hui, aluminium et silicium sont `basic` alors que toutes leurs sources sont `advanced`, et thorium et uranium sont `advanced` pour des sources `experimental`.
- Les recettes de raffinage basique peuvent être **générées** depuis `composition` et `primary` ; seules les recettes de retraitement demandent un travail à la main.
- Règle de non-blocage : les roches disponibles au départ doivent suffire à fabriquer les premiers packs de science (voir `tech.md`).

## Points restant à décider

- Quelles roches sont disponibles au départ, et lesquelles sont verrouillées.
- Une scorie unique ou une scorie par famille.
- Quantités et rendements de chaque étape, y compris la fréquence des sous-produits.
- Quels minerais doivent être nécessaires à la progression principale et lesquels sont facultatifs.
- Quels éléments sont fluides, poudres ou lingots dans l’interface du jeu.
- Nombre final de composants intermédiaires et recettes de remplacement vanilla.
- Recette, consommation et récupération des catalyseurs.
