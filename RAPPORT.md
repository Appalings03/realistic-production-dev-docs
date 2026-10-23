# Rapport d'état — 23 oct. 2026

Fondé sur la lecture des fichiers de chaque repo au 23 oct. 2026 (commits : assets `46be2ab`, utils `1c73544`, ore `475408a`, building `b2f605b`, core `f8ceb39`, dev-docs `939e9a2`) et sur l'analyse du tableur `proto_table/elements.xlsx`.

**Limites** : rien n'a été lancé dans Factorio et `verify.lua` n'a pas été exécuté. Les erreurs de chargement annoncées sont déduites du code, pas testées. Ce fichier remplace toutes les versions précédentes du rapport.

## En bref

- Le projet est en phase de **fondations**. Les cinq mods ne définissent encore aucun prototype de jeu (items, entités, recettes) : seuls ore et building déclarent des settings.
- Aucun bloquant de chargement n'a été trouvé. L'ancien bloquant (`building/settings.lua` avec `local bool = {}`) est corrigé.
- Le manque principal est le **loader** : `ore/data.lua` est vide, donc les 6 fichiers de données générés ne sont lus par personne.
- Les données sont complètes dans leur structure mais incomplètes dans leur contenu : 44 ressources sur 88 ont une composition.
- Trois décisions bloquent l'écriture du code d'ore : la convention de noms, la mécanique des scories et la cohérence des niveaux (voir « Décisions à prendre »).

## État par repo

| Repo | Mod | Avancement | Contenu réel |
| --- | --- | --- | --- |
| assets | `realistic_production_assets` | ◐ | 4 icônes 64×64 et 4 images 256×256 de test (1x1, 2x2, 3x3, 3x5) dans `graphics/dev/` |
| utils | `realistic_production_utils` | ◐ | `general.lua` (6 fonctions) ; `data.lua` charge 5 modules dont 4 sont vides |
| ore | `realistic_production_ore` | ◐ | 6 fichiers de données générés ; `data.lua` vide |
| building | `realistic_production_building` | ▫ | rien : 6 fichiers `prototypes/` vides, pas de `data.lua` |
| core | `realistic_production_main` | ▫ | rien : stubs vides, pas de `data.lua` |
| dev-docs | (documentation) | ✓ | roadmap, TODO, rapport, notes de conception, `proto_table/` |

Tous les `info.json` sont en `factorio_version` 2.1 avec `base >= 2.1`, et `building` est correctement orthographié partout.

## assets

- Contenu sain : les images de test servent de support aux icônes teintées et aux entités.
- `graphics/README.md` est obsolète : il parle de 32×32, de `prototypes/util.lua` (qui n'existe pas) et de dossiers `realistic-iron-ore/icon.png`. Ta note « Not right anymore / `Graphics/mod_part/part/part.png` » n'est pas une convention rédigée.
- `thumbnail.png` est un vrai PNG de 720×380, identique dans les 6 repos. Le mod portal affiche des miniatures plus petites (144×144 recommandé).
- À prévoir : une entité `resource` demande des `stages`. Les images 256×256 sont des images uniques, utilisables en test avec une seule variation.

## utils

- Fonctions présentes : `normalize_name`, `icon_path`, `icons`, `add_proto`, `copy_proto`, `get_settings`. La fonction `trancate` n'existe plus.
- **`normalize_name` remplace maintenant les espaces par `-`**, alors que le générateur de données (`generate_elements.py`, fonction `norm`) les remplace par `_`. C'est un conflit de convention, voir « Décisions à prendre ».
- `icon_path` hors mode dev vise `graphics/items/<nom>.png`, un dossier qui n'existe pas dans assets. Le README d'assets ne documente aucune autre arborescence.
- Ménage dans `general.lua` : l'en-tête (« remplace l'ancien… `trancate` ») et le bloc « Utilisation côté ore » sont des commentaires de collage. L'exemple cite un setting `rp-placeholder-icons` alors que le setting réel s'appelle « Dev assets ».
- `data.lua` fait `require` de `utils.general`, `utils.building`, `utils.ore`, `utils.assets` et `utils.main`. Charger un fichier vide ne produit pas d'erreur. `function/multi.lua` et `function/world.lua` (vides) ne sont pas chargés.
- Vides : `utils/ore.lua`, `assets.lua`, `building.lua`, `main.lua`, `function/multi.lua`, `function/world.lua`, `control.lua`, `settings.lua`.
- Les autres mods doivent faire `require("__realistic_production_utils__.utils.general")` : à noter dans un README.

## ore

**Chargement**

- `data.lua` (0 octet), `prototypes/dev.lua` (vide) et tous les stubs (`control`, `data-updates`, `data-final-fixes`, `settings-*`) sont vides.
- Les données sont rangées en `prototypes/resources/` (`resources_data`, `composition_data`, `elements_data`), `prototypes/materials/` (`alloys_data`, `materials_data`), `prototypes/components/` (`components_data`) et `prototypes/groups/` (`groups_data`). `elements_data` est dans `resources/` alors que ce sont des matériaux.
- Locale : les deux `config.cfg` ont des sections vides (`[item-name]`, `[recipe-name]`…), sans entrée et sans `[mod-setting-name]` ni `[mod-setting-description]`. Les `name_en` / `name_fr` sont déjà dans les données.

**Settings** (`settings.lua`)

- Trois settings : « Dev assets », « Allow pure ore nodes », « Ore density multiplier ».
- Ids avec espaces et sans préfixe ; « Dev assets » n'a pas de `order` et utilise `per_user`, qui n'existe pas pour un setting (sans effet à ma connaissance). Les noms sont écrits en dur au lieu de la locale. Proposition : `rp-dev-assets`, `rp-pure-ore-nodes`, `rp-ore-density`.
- Rien ne lit encore ces settings. Les blocs d'exemples commentés peuvent partir.

**Données** (générées par `proto_table/generate_elements.py` depuis `elements.xlsx`)

| Table | Lignes | Remarque |
| --- | --- | --- |
| resources | 88 | 62 minerais, 19 roches, 5 fluides, 2 gaz ; 7 ressources vanilla ; 23 avec `associated_with` |
| elements | 118 | 88 naturels, 28 artificiels, 2 sans `origin` (astate, francium) ; 13 fluides, 105 items |
| composition | 115 | couvre **44 ressources sur 88** |
| alloys | 5 | quantités remplies (acier 3 fer + 1 carbone, bronze 4 cuivre + 1 étain, laiton 3 cuivre + 2 zinc, duralumin 6/2/1/1, acier inox 5/3/1/1) |
| materials | 0 | vide |
| components | 0 | vide |

Les niveaux (`level`) sont remplis partout : ressources 54 basic / 30 advanced / 4 experimental ; éléments 21 / 62 / 35 ; alliages 2 / 2 / 1. Les compositions sont cohérentes (sommes entre 99,5 et 100,5 % pour les 44 ressources couvertes).

*Ressources sans composition (44)*

- 19 roches : granite, basalt, gabbro, diorite, rhyolite, andesite, peridotite, kimberlite, limestone, dolomite, sandstone, clay, shale, chalk, marble, gneiss, quartzite, slate, stone
- 19 minerais : iron-ore, copper-ore, bauxite, wolframite, pentlandite, laterite, lepidolite, coltan, monazite, bastnasite, carnotite, uranium-ore, apatite, coal, lignite, anthracite, peat, oil_sand, oil_shale
- 6 fluides et gaz : crude-oil, water, seawater, lithium_brine, geothermal_water, natural_gas

*Conséquences*

- **47 éléments naturels sur 88 n'ont aucune source** : phosphore, nickel, scandium, vanadium, gallium, germanium, sélénium, brome, rubidium, strontium, yttrium, niobium, ruthénium, rhodium, palladium, cadmium, indium, tellure, iode, césium, baryum, les lanthanides (de lanthane à lutécium, sauf prométhium), hafnium, tantale, rhénium, osmium, iridium, thallium, bismuth, polonium, radon, radium, actinium, protactinium. Monazite, bastnasite, coltan, apatite, pentlandite et latérite en couvriront une partie dès qu'ils auront une composition.
- **Nickel et phosphore** (niveau basic) n'ont aucune source : l'acier inoxydable est impossible aujourd'hui.
- Les 28 éléments artificiels sans source sont normaux : ils viendront de la synthèse.

*Niveaux incohérents*

| Élément | Niveau | Problème |
| --- | --- | --- |
| aluminium | basic | ses seules sources sont `advanced` (spodumène, béryl) ; la bauxite (basic) n'a pas de composition |
| silicium | basic | idem (béryl, spodumène, zircon) ; les roches siliceuses n'ont pas de composition |
| thorium | advanced | sa seule source (thorianite) est `experimental` |
| uranium | advanced | sa seule source (uraninite) est `experimental` |
| étain | advanced | le bronze (basic) en contient 1/5 ; la cassitérite est basic |

**Noms**

- 10 noms avec `_` (`native_gold`, `oil_sand`, `stainless_steel`, `lithium_brine`…) et 4 avec `-` (`iron-ore`, `copper-ore`, `uranium-ore`, `crude-oil`, les ids vanilla).
- Ids déjà présents dans le jeu : `iron-ore`, `copper-ore`, `uranium-ore`, `coal`, `stone`, `crude-oil`, `water`. Probablement aussi `sulfur`, `carbon`, `lithium`, `fluorine` et, si les noms passent en tirets, `lithium-brine` (Space Age). À vérifier dans `data.raw` : `add_proto` ignore les doublons en silence (un `log` seulement).
- À prévoir dans les générateurs : les ingrédients d'alliage sont `{ name, amount }` sans `type` (obligatoire dans les recettes en 2.x), et les fluides exigent `base_color` et `flow_color` (tirables de la teinte).

## building

- Pas de `data.lua`. Les 6 fichiers de `prototypes/` (`entity`, `globals`, `item`, `recipe`, `technologie`, `util`) sont vides, comme les stubs `control` / `data-*` / `settings-*`.
- `settings.lua` déclare un seul setting `RM-stp-order` (chaîne, caché, valeurs `aw` / `dw`) : son préfixe `RM-` est incohérent avec le reste du mod (`rp-`), il n'a pas de locale et rien ne le lit aujourd'hui.
- Locale vide. `info.json` correct (dépend d'assets et d'utils). Le fichier `technologie.lua` garde sa faute (`technology`).

## core (`realistic_production_main`)

- Pas de `data.lua`, tous les stubs vides, `settings.lua` vide, locale vide.
- `info.json` : la description est celle d'assets (« Graphics and sounds… »). Dépendances correctes (assets, building, ore, utils).
- Repo `core` mais mod `main` : à unifier si possible avant publication.

## Décisions à prendre

1. **Convention de noms.** `normalize_name` utilise `-`, le générateur utilise `_`, les ids vanilla utilisent `-`. Si les tirets l'emportent, il faut changer `norm` dans `generate_elements.py` et renommer 10 ressources et alliages, ainsi que leurs références (`composition`, `associated_with`) ; `lithium_brine` deviendrait `lithium-brine`, qui entre probablement en collision avec Space Age.
2. **Scories et extraction progressive** (voir `RoadMap/Item.md`) : colonnes `primary` dans `composition` et `tech` dans `resources`, un type de scorie unique ou par famille, liste des roches disponibles au départ.
3. **Niveaux.** Que signifie `level` pour un élément : le niveau du premier procédé qui le libère, ou celui de sa roche ? La mécanique des scories change la réponse.
4. **Première version des bâtiments.** Machines autonomes reliées par tapis et tuyaux (recommandé dans `machine.md`), ou bâtiments qui demandent d'autres bâtiments pour fonctionner.
5. **Ressources vanilla.** `iron-ore` et `copper-ore` sont gardés comme minerais génériques ; le sort de `coal`, `stone`, `uranium-ore` dépend de leur existence naturelle (à décider un par un).

## Priorités

1. Trancher la convention de noms et mettre `generate_elements.py` et `normalize_name` d'accord.
2. Écrire le loader d'ore (`data.lua`, `utils/ore.lua`) : `load_data`, `create_item`, `create_fluid`, groupes et sous-groupes.
3. Locale générée depuis `name_en` / `name_fr`, et settings renommés (`rp-…`).
4. Compositions manquantes : bauxite, pentlandite, latérite, apatite, wolframite, coltan, monazite, bastnasite, lepidolite, roches siliceuses.
5. Aligner les niveaux (aluminium, silicium, étain, uranium, thorium).
6. assets : README, arborescence des icônes, miniature.