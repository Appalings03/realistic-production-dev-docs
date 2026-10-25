---

# Rapport d'état — 25 oct. 2026

Fondé sur la lecture des 6 repos au 25 oct. 2026 (commits : assets `7756b15`, utils `b64f4b6`, ore `e2469a9`, building `b2f605b`, core `f8ceb39`, dev-docs `30286ff`), sur la régénération des tables depuis `proto_table/elements.xlsx` et sur une exécution de `ore/data.lua` dans une **simulation** de l'étape data (voir « Méthode et limites »). Ce fichier remplace toutes les versions précédentes du rapport.

## En bref

- Gros pas en avant depuis le 24 oct. : le **loader d'ore existe**. `utils/ore.lua` (366 lignes) et `ore/data.lua` créent 186 items, 18 fluides, 3 groupes et 9 sous-groupes, avec le préfixe `rp-`, les noms FR/EN et des icônes de test.
- Les décisions de nommage (`-`, `rp-`), de scorie unique, de ressources de départ, de réutilisation des items vanilla et de sens de `level` sont **appliquées dans le code et les données**, pas seulement dans les docs.
- **Deux bugs bloquent un premier lancement ou l'écriture des recettes** (détail plus bas) :
  1. les 18 fluides n'ont pas de `default_temperature`, propriété obligatoire : Factorio refusera de charger le mod ;
  2. `create_recipe` échoue toujours, y compris avec l'exemple du README d'utils.
- Rien n'a été lancé dans Factorio. Ce rapport décrit ce que le code fait dans une simulation, et ce que la documentation de Factorio impose.
- Le jeu n'a toujours aucune entité, recette ni technologie : `building` et `core` sont inchangés (vides).

## Ce qui a été poussé depuis le 24 oct.

| Repo           | Commits                                            | Contenu                                                                                                                                                            |
| -------------- | -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| utils          | `d034e7d`, `b64f4b6`                           | `utils/ore.lua` (11 fonctions), README (convention de noms, exemples), `normalize_name` traite aussi `_`, commentaires de collage retirés                   |
| ore            | `0582011`, `e2469a9`                           | `data.lua` (71 lignes), `settings.lua` réécrit (`rp-dev-assets`, `rp-pure-ore-nodes`, `rp-ore-density`), locales EN/FR remplies, tables régénérées |
| assets         | `7756b15`                                        | `graphics/README.md` réécrit : `graphics/items/<id-prototype>.png`, mode dev                                                                                 |
| dev-docs       | `becc1c4`, `f4d63ce`, `ed424d1`, `30286ff` | générateur : `_` → `-` et génération des locales ; tableur et tables régénérés ; ROADMAP, TODO, `Item`, `tech`, `machine` mis à jour           |
| building, core | aucun                                              | inchangés                                                                                                                                                         |

## Méthode et limites

- **Simulation** : j'ai chargé `ore/data.lua` avec une petite imitation de l'étape data (`data:extend`, `data.raw`, `settings`, `require` à la manière de Factorio) et vérifié ce qui en sort. Cela détecte les erreurs Lua, les doublons et les références cassées. Cela **ne vérifie pas** les propriétés obligatoires que Factorio impose : celles-ci viennent de la documentation de l'API (`FluidPrototype`), pas d'un lancement.
- `verify.lua` n'a pas été exécuté : ses chemins utilisent `\\` (Windows) et il ne contrôle que les tables de données, pas le loader.
- Le générateur a été relancé sur `elements.xlsx` : ses sorties sont **identiques** aux fichiers de dev-docs et à ceux du repo ore (5 tables Lua, 2 locales).

## Résultats de la vérification du code

### Ce qui est correct

- `ore/data.lua` s'exécute sans erreur et crée **204 prototypes** : 81 ressources non vanilla + 118 éléments + 5 alliages. Les 7 ressources vanilla ne sont pas recréées (`rp-water`, `rp-iron-ore`… n'existent pas).
- Les 204 noms commencent par `rp-` et aucun ne contient `_`. Aucun doublon.
- Tous les sous-groupes pointent vers un groupe existant ; tous les items et fluides pointent vers un sous-groupe existant.
- Locales : 186 items, 18 fluides, 3 groupes, 9 sous-groupes et 3 settings, avec exactement les mêmes clés en EN et en FR, et en correspondance un pour un avec les prototypes créés (aucune clé en trop ni manquante).
- Les 18 fluides ont une couleur (`base_color`, `flow_color`) tirée des tables de `data.lua`.
- Les icônes de test (`graphics/dev/1x1_item.png`) existent bien dans assets.
- Les helpers `ing` et `res` exigent un `type` et refusent une quantité nulle ; `create_technology` préfixe les prérequis et les recettes débloquées (testé avec un exemple).

### Bug 1 — fluides sans `default_temperature` (bloquant au lancement)

La documentation de Factorio 2.x marque `default_temperature` comme obligatoire pour un prototype `fluid`. Les 18 fluides créés (13 éléments gazeux ou liquides, plus eau de mer, saumure de lithium, eau géothermale, gaz naturel, air) ont `base_color`, `flow_color`, `icons`, `order`, `subgroup`, mais pas cette propriété. Le mod ne démarrera donc pas. Correction : donner une valeur par défaut dans `create_fluid` (par exemple 15, comme l'eau vanilla), surchargeable par ligne de données.

### Bug 2 — `create_recipe` échoue toujours

Test : l'exemple exact du README d'utils (`crushing-hematite`) produit `create_recipe : ingredients obligatoires`. Cause : `ingredients` figure dans la liste `INTERNAL_FIELDS` (utilisée pour écarter les champs des tables de données, dont les alliages) ; `copy_definition` retire donc le champ avant que `create_recipe` ne le lise. Correction : recopier `definition.ingredients` dans `create_recipe` avant la normalisation (ou ne pas filtrer ce champ pour les recettes). Tant que ce n'est pas fait, la case « `create_recipe` » du TODO ne reflète pas la réalité.

### Autres constats

- **Toutes les icônes sont identiques** : les données générées n'ont pas de colonne `tint`, donc aucun item ni fluide n'est teinté (et `kind` n'est pas converti en teinte). Dans le menu de craft, les 204 entrées auront la même image. Ce n'est pas bloquant, mais ce n'est pas l'objectif de la phase 1.
- `ore.lua` fait `require("utils.general")` alors que les autres mods utilisent `__realistic_production_utils__.utils.general` : le même fichier peut être chargé deux fois sous deux noms (inoffensif ici, `general` n'a pas d'état). La résolution du chemin relatif depuis un autre mod reste à confirmer dans le jeu.
- `create_resource` n'est appelé nulle part : il n'y a encore aucune ressource posée dans le monde, donc aucun gisement ni minage.
- Les alliages gardent `ingredients = { { name, amount } }` sans `type` : pas de problème tant qu'aucune recette n'en est générée, à corriger lors de la génération (voir `ing`).
- Un fichier `.pyc` (`proto_table/__pycache__/`) est versionné dans dev-docs ; ajouter un `.gitignore`.
- Les réglages sont lus par personne, sauf `rp-dev-assets` (icônes). `rp-pure-ore-nodes` et `rp-ore-density` n'ont pas d'effet tant que `create_resource` n'est pas utilisé.

## Données (générateur et tableur)

| Table                 | Lignes | Remarque                                                                                                                          |
| --------------------- | ------ | --------------------------------------------------------------------------------------------------------------------------------- |
| resources             | 88     | 54 basic / 30 advanced / 4 experimental ; 7 vanilla ; 23 avec `associated_with`                                                 |
| elements              | 118    | 88 naturels, 28 artificiels, 2 sans `origin` (astate, francium) ; 13 fluides ; niveaux 20 basic / 61 advanced / 37 experimental |
| composition           | 115    | couvre toujours **44 ressources sur 88**                                                                                    |
| alloys                | 5      | acier, bronze, laiton, duralumin, acier inox ; niveaux 2 basic / 2 advanced / 1 experimental                                      |
| materials, components | 0      | vides                                                                                                                             |

- **Noms** : tous les noms de données sont maintenant en `-`, références comprises (composition, alliages, `associated_with`), sans référence inconnue.
- **Niveaux** : les 5 incohérences du 24 oct. sont résolues par la nouvelle définition (palier du premier procédé qui libère l'élément) : aluminium et silicium `advanced`, thorium et uranium `experimental`, étain `basic`. Un cas reste à confirmer : le **plomb** est `advanced` alors que la galène (sa source) est `basic`. Les gaz rares (hélium, néon, krypton, xénon) sont `advanced` alors que l'air est `basic`, ce qui est cohérent avec un procédé de séparation avancé.
- **47 éléments naturels sur 88 n'ont toujours aucune source** (nickel et phosphore d'abord : l'acier inoxydable reste irréalisable). Les 44 compositions manquantes sont inchangées : 19 roches, 19 minerais, 6 fluides et gaz.
- Colonnes `primary` (composition), `tech` (resources) et `vanilla` (elements) : toujours absentes du tableur et du générateur. Elles sont nécessaires pour générer le raffinage basique et les paliers de prospection.
- Le tableur a été enregistré par un autre outil (29 ko → 22 ko) ; ses 6 feuilles et leurs lignes sont intactes.

## État par repo

| Repo     | Mod                               | Avancement | Contenu réel                                                                                                                        |
| -------- | --------------------------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| assets   | `realistic_production_assets`   | ◐         | 4 icônes et 4 images de test ; README réécrit ; aucune icône définitive                                                         |
| utils    | `realistic_production_utils`    | ◐         | `general.lua` (6 fonctions) et `ore.lua` (11 fonctions, 2 bugs) ; `assets`, `building`, `main`, `multi`, `world` vides |
| ore      | `realistic_production_ore`      | ◐         | `data.lua` fonctionnel (items, fluides, groupes), settings et locales ; ni ressources, ni recettes, ni technologies                |
| building | `realistic_production_building` | ▫         | rien : fichiers de prototypes vides, pas de `data.lua`, setting `RM-stp-order` à renommer ou supprimer                          |
| core     | `realistic_production_main`     | ▫         | rien : stubs vides, description d'`info.json` copiée d'assets                                                                     |
| dev-docs | (documentation)                   | ✓         | roadmap, TODO, rapport, notes de conception, générateur et tableur                                                                 |

Les `info.json` sont tous en 2.1 avec `base >= 2.1` ; les dépendances sont correctes.

## Écarts entre la documentation et la réalité

- **TODO** : `create_recipe` est coché « fait » alors qu'il échoue ; « fluides : couleurs » est décoché alors que les couleurs existent ; les lignes « renommer les settings », « réécrire `graphics/README.md` » et « choisir une arborescence » sont décochées alors que c'est fait ; la ligne « retirer les blocs d'exemples de `settings.lua` » est décochée alors que ce fichier n'en contient plus.
- **ROADMAP** : le tableau d'architecture dit encore « `data.lua` vide » pour ore, « 4 modules vides » pour utils et « README obsolète » pour assets ; la ligne « Générateurs `create_item`, `create_fluid`… » est décochée.
- **RAPPORT** : l'ancienne version cumulait trois états successifs ; elle est remplacée par celle-ci.

Ces points sont corrigés dans les nouvelles versions de `ROADMAP.md` et `TODO.md`.

## Décisions

**Prises** (appliquées) : noms en `-` ; préfixe `rp-` ; scorie unique ; bâtiments reportés ; items vanilla réutilisés ; sens de `level`. **Décidées le 25 oct. après ce rapport** (pas encore dans les données) : les 8 ressources de départ sont `stone`, `clay`, `limestone`, `sandstone`, hématite, malachite, `coal`, `water` ; `iron-ore` et `copper-ore` sont des produits de raffinage, pas des gisements ; les éléments volatils disparaissent au raffinage basique.

**Restent à décider** :

1. Plomb : `basic` (comme la galène) ou `advanced` (actuel) ?
2. Quantité de scories par recette de raffinage basique (rendements de l'hématite et de la malachite en `iron-ore` / `copper-ore`).
3. Éléments déjà présents dans le jeu (`sulfur`, `carbon`, `lithium`, `fluorine`) : réutiliser ou créer `rp-…` (aujourd'hui, tout est créé avec `rp-`).
4. Paliers de prospection : les 5 paliers de `Item.md` restent une proposition ; la colonne `tech` n'existe pas encore.

## Priorités

1. **Corriger les 2 bugs** : `default_temperature` dans `create_fluid`, `ingredients` dans `create_recipe`.
2. **Premier lancement dans Factorio** avec assets + utils + ore : c'est le premier vrai test de tout ce qui précède.
3. Teintes des icônes (colonne `tint` ou table `kind` → couleur) pour distinguer les entrées.
4. Colonnes `primary`, `tech`, `vanilla` dans le tableur et le générateur ; puis compositions manquantes.
5. `create_resource` utilisé par `ore` pour les 8 ressources de départ (sans autre recherche), puis raffinage basique.
6. `.gitignore` pour `__pycache__` ; nettoyage de `RM-stp-order` dans building.

# Rapport d'état — 24 oct. 2026

Fondé sur la lecture des fichiers de chaque repo au 24 oct. 2026 (commits : assets `46be2ab`, utils `1c73544`, ore `475408a`, building `b2f605b`, core `f8ceb39`, dev-docs `911876d`) et sur l'analyse du tableur `proto_table/elements.xlsx`.

**Limites** : rien n'a été lancé dans Factorio et `verify.lua` n'a pas été exécuté. Les erreurs de chargement annoncées sont déduites du code, pas testées. Ce fichier remplace toutes les versions précédentes du rapport.

## Mise à jour — décisions confirmées le 25 oct. 2026

Les quatre décisions de la section 0 du TODO sont désormais tranchées : les sept prototypes vanilla sont réutilisés ; fer et cuivre sont récupérés dès le départ depuis des roches adaptées et les constituants secondaires deviennent des scories ; les huit ressources de départ sont celles listées dans `RoadMap/Item.md` ; `level` désigne le palier du premier procédé qui libère l'élément (Al/Si `advanced`, Th/U `experimental`, Sn `basic`). Les technologies précises de raffinage restent reportées jusqu'à la conception des recettes et des machines.

Le diagnostic ci-dessous décrit l'état observé le 24 oct. 2026 ; ses listes de décisions et incohérences reflètent cet état antérieur.

## En bref

- Le projet est en phase de **fondations**. Les cinq mods ne définissent encore aucun prototype de jeu (items, entités, recettes) : seuls ore et building déclarent des settings.
- Aucun bloquant de chargement n'a été trouvé. L'ancien bloquant (`building/settings.lua` avec `local bool = {}`) est corrigé.
- Le manque principal est le **loader** : `ore/data.lua` est vide, donc les 6 fichiers de données générés ne sont lus par personne.
- Les données sont complètes dans leur structure mais incomplètes dans leur contenu : 44 ressources sur 88 ont une composition.
- Décisions des 23 et 25 oct. : noms avec `-`, préfixe `rp-` pour les prototypes non-vanilla, scorie unique, bâtiments reportés, ressources vanilla et de départ, et sens de `level` (voir les mises à jour ci-dessus).

## État par repo

| Repo     | Mod                               | Avancement | Contenu réel                                                                             |
| -------- | --------------------------------- | ---------- | ----------------------------------------------------------------------------------------- |
| assets   | `realistic_production_assets`   | ◐         | 4 icônes 64×64 et 4 images 256×256 de test (1x1, 2x2, 3x3, 3x5) dans `graphics/dev/` |
| utils    | `realistic_production_utils`    | ◐         | `general.lua` (6 fonctions) ; `data.lua` charge 5 modules dont 4 sont vides           |
| ore      | `realistic_production_ore`      | ◐         | 6 fichiers de données générés ; `data.lua` vide                                     |
| building | `realistic_production_building` | ▫         | rien : 6 fichiers `prototypes/` vides, pas de `data.lua`                              |
| core     | `realistic_production_main`     | ▫         | rien : stubs vides, pas de `data.lua`                                                   |
| dev-docs | (documentation)                   | ✓         | roadmap, TODO, rapport, notes de conception, `proto_table/`                             |

Tous les `info.json` sont en `factorio_version` 2.1 avec `base >= 2.1`, et `building` est correctement orthographié partout.

## assets

- Contenu sain : les images de test servent de support aux icônes teintées et aux entités.
- `graphics/README.md` est obsolète : il parle de 32×32, de `prototypes/util.lua` (qui n'existe pas) et de dossiers `realistic-iron-ore/icon.png`. Ta note « Not right anymore / `Graphics/mod_part/part/part.png` » n'est pas une convention rédigée.
- `thumbnail.png` est un vrai PNG de 720×380, identique dans les 6 repos. Le mod portal affiche des miniatures plus petites (144×144 recommandé).
- À prévoir : une entité `resource` demande des `stages`. Les images 256×256 sont des images uniques, utilisables en test avec une seule variation.

## utils

- Fonctions présentes : `normalize_name`, `icon_path`, `icons`, `add_proto`, `copy_proto`, `get_settings`. La fonction `trancate` n'existe plus.
- **`normalize_name` remplace maintenant les espaces par `-`**, alors que le générateur de données (`generate_elements.py`, fonction `norm`) ne remplace que les espaces par `-` et laisse les `_` du tableur. Les 10 noms avec `_` sortent donc encore avec `_`. Correction d'une ligne, testée : ajouter `.replace("_", "-")` à `norm`.
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

| Table       | Lignes | Remarque                                                                                                                                   |
| ----------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| resources   | 88     | 62 minerais, 19 roches, 5 fluides, 2 gaz ; 7 ressources vanilla ; 23 avec `associated_with`                                              |
| elements    | 118    | 88 naturels, 28 artificiels, 2 sans `origin` (astate, francium) ; 13 fluides, 105 items                                                  |
| composition | 115    | couvre **44 ressources sur 88**                                                                                                      |
| alloys      | 5      | quantités remplies (acier 3 fer + 1 carbone, bronze 4 cuivre + 1 étain, laiton 3 cuivre + 2 zinc, duralumin 6/2/1/1, acier inox 5/3/1/1) |
| materials   | 0      | vide                                                                                                                                       |
| components  | 0      | vide                                                                                                                                       |

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

| Élément | Niveau   | Problème                                                                                             |
| --------- | -------- | ----------------------------------------------------------------------------------------------------- |
| aluminium | basic    | ses seules sources sont `advanced` (spodumène, béryl) ; la bauxite (basic) n'a pas de composition |
| silicium  | basic    | idem (béryl, spodumène, zircon) ; les roches siliceuses n'ont pas de composition                    |
| thorium   | advanced | sa seule source (thorianite) est `experimental`                                                     |
| uranium   | advanced | sa seule source (uraninite) est `experimental`                                                      |
| étain    | advanced | le bronze (basic) en contient 1/5 ; la cassitérite est basic                                         |

**Noms**

- 10 noms avec `_` dans le tableur (`native_gold`, `oil_sand`, `stainless_steel`, `lithium_brine`…) à convertir en `-` (décision du 23 oct.) ; les ids vanilla ont déjà des `-`.
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

## Décisions à prendre au 24 oct. (état antérieur aux décisions ci-dessus)

**Décidées les 23 et 25 oct. :** noms avec `-` ; préfixe `rp-` pour les prototypes non-vanilla (les tables gardent les noms courts et le loader ajoute le préfixe) ; scorie unique et inerte (ciment, béton) ; bâtiments reportés après l'assemblage des prototypes.

**Restent à décider :**

1. **Items déjà présents dans le jeu.** Proposition : les réutiliser sans les recréer (`Item.md`, section 8). À décider : ce que donnent `iron-ore` et `copper-ore` au raffinage.
2. **Roches de départ.** Proposition en 5 paliers, dont 8 ressources au départ (`Item.md`, section 7).
3. **Niveaux.** Que signifie `level` pour un élément : le niveau du premier procédé qui le libère, ou celui de sa roche ? La case « Sens de `level` » du TODO avait été cochée sans décision écrite : elle est rouverte.
4. **Quantité de scories** par recette de raffinage basique.

## Priorités

1. Appliquer la convention : correction de `norm` dans `generate_elements.py`, régénération, settings renommés.
2. Écrire le loader d'ore (`data.lua`, `utils/ore.lua`) : `load_data`, `create_item`, `create_fluid`, groupes et sous-groupes.
3. Locale générée depuis `name_en` / `name_fr`, et settings renommés (`rp-…`).
4. Compositions manquantes : bauxite, pentlandite, latérite, apatite, wolframite, coltan, monazite, bastnasite, lepidolite, roches siliceuses.
5. Aligner les niveaux (aluminium, silicium, étain, uranium, thorium).
6. assets : README, arborescence des icônes, miniature.

---

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

| Repo     | Mod                               | Avancement | Contenu réel                                                                             |
| -------- | --------------------------------- | ---------- | ----------------------------------------------------------------------------------------- |
| assets   | `realistic_production_assets`   | ◐         | 4 icônes 64×64 et 4 images 256×256 de test (1x1, 2x2, 3x3, 3x5) dans `graphics/dev/` |
| utils    | `realistic_production_utils`    | ◐         | `general.lua` (6 fonctions) ; `data.lua` charge 5 modules dont 4 sont vides           |
| ore      | `realistic_production_ore`      | ◐         | 6 fichiers de données générés ; `data.lua` vide                                     |
| building | `realistic_production_building` | ▫         | rien : 6 fichiers `prototypes/` vides, pas de `data.lua`                              |
| core     | `realistic_production_main`     | ▫         | rien : stubs vides, pas de `data.lua`                                                   |
| dev-docs | (documentation)                   | ✓         | roadmap, TODO, rapport, notes de conception, `proto_table/`                             |

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

| Table       | Lignes | Remarque                                                                                                                                   |
| ----------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| resources   | 88     | 62 minerais, 19 roches, 5 fluides, 2 gaz ; 7 ressources vanilla ; 23 avec `associated_with`                                              |
| elements    | 118    | 88 naturels, 28 artificiels, 2 sans `origin` (astate, francium) ; 13 fluides, 105 items                                                  |
| composition | 115    | couvre **44 ressources sur 88**                                                                                                      |
| alloys      | 5      | quantités remplies (acier 3 fer + 1 carbone, bronze 4 cuivre + 1 étain, laiton 3 cuivre + 2 zinc, duralumin 6/2/1/1, acier inox 5/3/1/1) |
| materials   | 0      | vide                                                                                                                                       |
| components  | 0      | vide                                                                                                                                       |

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

| Élément | Niveau   | Problème                                                                                             |
| --------- | -------- | ----------------------------------------------------------------------------------------------------- |
| aluminium | basic    | ses seules sources sont `advanced` (spodumène, béryl) ; la bauxite (basic) n'a pas de composition |
| silicium  | basic    | idem (béryl, spodumène, zircon) ; les roches siliceuses n'ont pas de composition                    |
| thorium   | advanced | sa seule source (thorianite) est `experimental`                                                     |
| uranium   | advanced | sa seule source (uraninite) est `experimental`                                                      |
| étain    | advanced | le bronze (basic) en contient 1/5 ; la cassitérite est basic                                         |

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

## Décisions à prendre au 24 oct. (état antérieur aux décisions ci-dessus)

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
5. Aligner les niveaux (aluminium, silicium, étain, uranium, thorium) — alignement effectué le 25 oct. (voir la mise à jour en tête).
6. assets : README, arborescence des icônes, miniature.
