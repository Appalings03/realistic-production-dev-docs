# Compositions des ressources

Mis à jour le 25 oct. 2026. Ce fichier documente la feuille `composition` de `proto_table/elements.xlsx` : d'où vient chaque composition, quels éléments sont `primary`, et quelles valeurs sont des simplifications.

## Méthode

- **Minéraux** : formule chimique idéale, pourcentages massiques calculés avec les masses atomiques standard. Le calcul a été vérifié sur les 37 compositions déjà présentes dans le tableur (écart maximal inférieur à 0,02 point).
- **Roches** : composition moyenne en oxydes (SiO2, Al2O3, FeO, CaO…) convertie en éléments, puis normalisée à 100 %. Les valeurs de roches, de charbons, de pétrole et d'eaux sont des **moyennes typiques arrondies, entrées de mémoire** : elles sont réalistes mais ne viennent pas d'une table citée. À remplacer par une source précise si tu veux plus de rigueur.
- **Traces** : les éléments naturels qui n'avaient aucune source en ont maintenant une. Ils sont ajoutés en petite quantité dans une ressource où ils existent réellement (voir plus bas), et le reste de la composition est réduit proportionnellement. Les teneurs réelles inférieures à 0,0001 % sont relevées à 0,0001 %.
- Chaque ressource totalise entre 99,99 % et 100,01 %. Les 37 compositions d'origine non modifiées gardent leurs valeurs (bornite 100,01 %, carnallite 100,002 %…).

## Colonne `primary`

- `primary = yes` : élément récupéré au raffinage basique. Les autres éléments **solides** deviennent des scories ; les éléments `volatile` (colonne de la feuille `elements`) disparaissent.
- Par défaut : l'élément le plus abondant qui n'est pas volatil (l'oxygène, l'hydrogène, le carbone, le soufre, les halogènes et les gaz sont volatils). Exceptions choisies à la main : bore (borax, colémanite), lithium (spodumène, lépidolite), béryllium (béryl), phosphore (apatite), nickel (pentlandite, latérite), titane (ilménite), cobalt (cobaltite), aluminium (argile), magnésium (péridotite, kimberlite), carbone (charbons, tourbe, sables et schistes bitumineux).
- Plusieurs `primary` pour les fluides qui se séparent proprement : eau et eau géothermale (hydrogène + oxygène), pétrole brut et gaz naturel (carbone + hydrogène), air (azote + oxygène + argon).
- Le raffinage basique généré depuis `composition` ne concerne que les roches et les minerais (`kind` = rock ou ore). Les fluides et les gaz ont leurs propres procédés.

## Tableau des 88 ressources

| Ressource | Base de calcul | `primary` | Palier |
| --- | --- | --- | --- |
| `granite` | moyenne en oxydes | silicon | base |
| `basalt` | moyenne en oxydes | silicon | base |
| `gabbro` | moyenne en oxydes | silicon | géologique |
| `diorite` | moyenne en oxydes | silicon | géologique |
| `rhyolite` | moyenne en oxydes | silicon | géologique |
| `andesite` | moyenne en oxydes | silicon | géologique |
| `peridotite` | moyenne en oxydes | magnesium | avancé |
| `kimberlite` | oxydes simplifiés (MgO, SiO2, CaO, FeO, CO2, H2O) | magnesium | avancé |
| `limestone` | CaCO3 95 % + SiO2, Al2O3, Fe2O3 | calcium | départ |
| `dolomite` | CaMg(CO3)2 97 % + SiO2, Fe2O3 | calcium | géologique |
| `sandstone` | SiO2 86 % + oxydes | silicon | départ |
| `clay` | kaolinite 92 % + Fe2O3, TiO2, K2O, MgO | aluminium | départ |
| `shale` | moyenne en oxydes (avec H2O, CO2, BaO) | silicon | géologique |
| `chalk` | CaCO3 99 % + SiO2 | calcium | géologique |
| `marble` | CaCO3 99 % + MgCO3 | calcium | base |
| `gneiss` | moyenne en oxydes (gneiss granodioritique) | silicon | géologique |
| `quartzite` | SiO2 98,5 % + oxydes | silicon | base |
| `slate` | oxydes + H2O | silicon | géologique |
| `stone` | croûte continentale supérieure moyenne (oxydes) | silicon | départ |
| `iron-ore` | produit : fer pur | iron | produit |
| `copper-ore` | produit : cuivre pur | copper | produit |
| `hematite` | Fe2O3 | iron | départ |
| `magnetite` | Fe3O4 | iron | base |
| `goethite` | FeOOH | iron | base |
| `siderite` | FeCO3 | iron | base |
| `bauxite` | Al2O3 52 / Fe2O3 11 / SiO2 4 / TiO2 3 / H2O 30 + Ga | aluminium | géologique |
| `chalcopyrite` | CuFeS2 + Se, Te | copper | géologique |
| `bornite` | Cu5FeS4 | copper | géologique |
| `chalcocite` | Cu2S | copper | géologique |
| `malachite` | Cu2CO3(OH)2 | copper | départ |
| `galena` | PbS + Bi | lead | base |
| `sphalerite` | ZnS + Cd, Ge, In | zinc | base |
| `cassiterite` | SnO2 | tin | base |
| `wolframite` | Fe0,5Mn0,5WO4 | tungsten | avancé |
| `scheelite` | CaWO4 | tungsten | avancé |
| `molybdenite` | MoS2 + Re | molybdenum | avancé |
| `pentlandite` | Fe4,5Ni4,5S8 | nickel | avancé |
| `laterite` | FeOOH 78 + NiO, CoO, Al2O3, SiO2, MgO, Cr2O3, MnO, H2O + Sc | nickel | avancé |
| `cobaltite` | CoAsS | cobalt | avancé |
| `chromite` | FeCr2O4 | chromium | géologique |
| `pyrolusite` | MnO2 | manganese | géologique |
| `ilmenite` | FeTiO3 | titanium | géologique |
| `rutile` | TiO2 | titanium | géologique |
| `native-gold` | Au pur | gold | avancé |
| `native-silver` | Ag pur | silver | avancé |
| `native-platinum` | alliage Pt 85,3 / Fe 9 / Pd 2 / Ir 1,5 / Rh 1 / Os 0,8 / Ru 0,4 (simplifié) | platinum | avancé |
| `sperrylite` | PtAs2 | platinum | avancé |
| `cinnabar` | HgS | mercury | avancé |
| `stibnite` | Sb2S3 | antimony | avancé |
| `spodumene` | LiAlSi2O6 | lithium | avancé |
| `lepidolite` | KLi2AlSi4O10F2 + Rb 1 %, Cs 0,05 % | lithium | avancé |
| `beryl` | Be3Al2Si6O18 | beryllium | avancé |
| `coltan` | Fe0,5Mn0,5NbTaO6 | tantalum | avancé |
| `zircon` | ZrSiO4 + Hf 1 % | zirconium | avancé |
| `monazite` | (Ce,La,Nd,Pr,Th,Y…)PO4, terres rares lourdes en traces | cerium | avancé |
| `bastnasite` | (Ce,La,Nd,Pr,Y…)CO3F | cerium | avancé |
| `uraninite` | UO2 + Ra, Po, Ac, Pa | uranium | nucléaire |
| `carnotite` | K2(UO2)2(VO4)2·3H2O | uranium | nucléaire |
| `thorianite` | ThO2 | thorium | nucléaire |
| `uranium-ore` | U3O8 | uranium | nucléaire |
| `halite` | NaCl | sodium | base |
| `sylvite` | KCl | potassium | géologique |
| `carnallite` | KMgCl3·6H2O | potassium | géologique |
| `gypsum` | CaSO4·2H2O | calcium | base |
| `anhydrite` | CaSO4 | calcium | géologique |
| `borax` | Na2B4O7·10H2O | boron | avancé |
| `colemanite` | Ca2B6O11·5H2O | boron | avancé |
| `trona` | Na3(CO3)(HCO3)·2H2O | sodium | géologique |
| `nitratine` | NaNO3 + I | sodium | géologique |
| `native-sulfur` | S pur | sulfur | base |
| `pyrite` | FeS2 + Tl | iron | géologique |
| `apatite` | Ca5(PO4)3F | phosphorus | géologique |
| `fluorite` | CaF2 | calcium | avancé |
| `graphite` | C pur | carbon | géologique |
| `diamond` | C pur | carbon | avancé |
| `coal` | analyse élémentaire d'un charbon bitumineux + cendres | carbon | départ |
| `lignite` | analyse élémentaire + cendres | carbon | base |
| `anthracite` | analyse élémentaire + cendres | carbon | géologique |
| `peat` | analyse élémentaire + cendres | carbon | base |
| `oil-sand` | bitume 12 % / quartz 78 % / kaolinite 4 % / eau 6 % | carbon | avancé |
| `oil-shale` | kérogène 20 % / calcite 30 % / dolomite 10 % / quartz 20 % / muscovite 15 % / pyrite 3 % | carbon | avancé |
| `crude-oil` | analyse élémentaire d'un brut moyen + V | carbon,hydrogen | géologique |
| `water` | H2O | oxygen,hydrogen | départ |
| `seawater` | composition moyenne de l'eau de mer | sodium | géologique |
| `lithium-brine` | saumure de salar : eau 72 % + sels (Cl, Na, K, Mg, S, Li…) | lithium | avancé |
| `geothermal-water` | eau 99,6 % + sels dissous | oxygen,hydrogen | avancé |
| `natural-gas` | CH4 90 / C2H6 5 / C3H8 2 / N2 1,5 / CO2 1 / He 0,3 (% molaires) + Rn | carbon,hydrogen | avancé |
| `air` | air sec (valeurs d'origine) | nitrogen,oxygen,argon | géologique |

## Éléments qui n'existent qu'en traces

33 des 88 éléments naturels n'apparaissent que dans une ressource à moins de 0,5 %. Ce sont les cibles des procédés d'extraction secondaire. Leurs hôtes sont réalistes (par exemple le cadmium et l'indium dans la sphalérite, l'iode dans le nitrate du Chili, le rhénium dans la molybdénite). Les teneurs sont arrondies ; celles qui sont en dessous de 0,0001 % sont relevées à cette valeur.

| Élément | Sources (teneur massique) |
| --- | --- |
| helium | `natural-gas` (0,06785 %), `air` (<0,0001 %) |
| neon | `air` (0,001267 %) |
| scandium | `laterite` (0,004 %) |
| gallium | `bauxite` (0,005 %) |
| germanium | `sphalerite` (0,01 %) |
| selenium | `chalcopyrite` (0,01 %) |
| bromine | `seawater` (0,006701 %) |
| krypton | `air` (0,00033 %) |
| strontium | `seawater` (0,0008001 %) |
| ruthenium | `native-platinum` (0,4 %) |
| cadmium | `sphalerite` (0,3 %) |
| indium | `sphalerite` (0,01 %) |
| tellurium | `chalcopyrite` (0,002 %) |
| iodine | `nitratine` (0,05 %), `seawater` (0,0001 %) |
| xenon | `air` (<0,0001 %) |
| caesium | `lepidolite` (0,05 %) |
| barium | `granite` (0,06255 %), `shale` (0,05452 %) |
| europium | `bastnasite` (0,1437 %), `monazite` (0,1264 %) |
| terbium | `monazite` (0,06642 %), `bastnasite` (0,03775 %) |
| dysprosium | `monazite` (0,3389 %), `bastnasite` (0,07645 %) |
| holmium | `monazite` (0,06893 %) |
| erbium | `monazite` (0,1391 %) |
| thulium | `monazite` (0,02118 %) |
| ytterbium | `monazite` (0,07232 %) |
| lutetium | `monazite` (0,02194 %) |
| rhenium | `molybdenite` (0,02 %) |
| thallium | `pyrite` (0,002 %) |
| bismuth | `galena` (0,3 %) |
| polonium | `uraninite` (0,0001 %) |
| radon | `natural-gas` (0,0001 %) |
| radium | `uraninite` (0,0001 %) |
| actinium | `uraninite` (0,0001 %) |
| protactinium | `uraninite` (0,0001 %) |

Cas particuliers :

- **Radium, polonium, actinium, protactinium** (uraninite) et **radon** (gaz naturel) sont relevés à 0,0001 %. Leurs vraies teneurs sont de quelques fois à plusieurs milliers de fois plus faibles ; si tu veux qu'ils soient très rares en jeu, réduis plutôt le rendement du procédé que la composition.
- **Hélium, néon, krypton, xénon** viennent de l'air (déjà présent) ; l'hélium vient aussi du gaz naturel.
- Les **terres rares lourdes** (europium à lutécium) sont des traces de monazite et de bastnasite, avec des proportions typiques simplifiées.

## Autres changements du tableur (25 oct.)

- Noms en tirets partout dans le tableur (`native_gold` devient `native-gold`, etc.) ; la sortie du générateur ne change pas.
- `resources` : colonnes `world` (non pour `iron-ore` et `copper-ore`, qui sont des produits) et `tech` (palier de prospection, vide au départ).
- `elements` : colonnes `volatile` (15 éléments : les 13 gaz et liquides, le carbone et le soufre) et `vanilla` (vide, décision à prendre).
- `composition` : colonne `primary`.
- Niveau du **nickel** : `basic` devient `advanced`, car ses seules sources (pentlandite, latérite) sont `advanced`.
- **Astate** et **francium** : origine `artificial` (ils existent en traces dans la nature, mais ne sont pas extractibles de façon réaliste).
- La première ligne figée de `resources` est maintenant la ligne d'en-tête (elle était figée à la ligne 53).

## Valeurs à discuter

- Plomb : `advanced` alors que la galène est `basic` (même cas que l'étain, qui est `basic`).
- Aluminium : présent à 27,5 % dans la bauxite (`basic`), `advanced` pour son niveau d'élément parce que son procédé est avancé.
- Les roches communes (granite, basalte…) contiennent presque toutes de l'aluminium, du fer et du silicium : le raffinage basique donnera surtout des scories. C'est voulu (« le reste devient des scories »), mais il faudra décider ce que le joueur fait de la roche brute qui n'est pas un minerai.
