# Rapport par repo — révisé le 23 oct. 2026

Basé sur la lecture des 5 repos (derniers commits : assets `a6fcc8b`, building `3684125`, core `21c72b6`, ore `f86d8c4`, utils `c7389b8`).
Rien n'a été lancé dans Factorio : les erreurs de chargement annoncées sont déduites du code, pas testées.

## Corrections par rapport à la version du 22 oct.

La première version a été écrite sans avoir lu les repos. Ce qui était faux :

- Pas de faux `icon.png` : assets contient de vrais PNG (`graphics/dev/`).
- Pas de `settings copy.lua`, pas de `migrations.lua`, pas de `trancate`.
- Pas de faute `buidling` : `realistic_production_building` est bien écrit partout.
- `core` est déjà en 2.1 (je le disais en 2.0).
- ore n'a pas de `prototypes/entity|item|recipe|technologie|globals|util.lua`, seulement un `dev.lua` vide.
- building et core n'ont **pas** de `data.lua` (je disais que building en avait un).
- Le setting « Dev assets » est dans le `settings.lua` de **ore** (j'avais écrit main).

Confirmé par l'analyse des données : 88 ressources, 118 éléments, 5 alliages, `materials_data` / `components_data` vides, et la plupart des manques de composition annoncés (détail dans la section ore).

## Bloquant avant un premier lancement

- **`building/settings.lua`** : `local bool = {}` est passé à `data:extend({order, bool})`. Une table sans `type` devrait provoquer une erreur « Missing type » au chargement (à confirmer en lançant le jeu). Comme `core` dépend de building, tout le mod serait touché. À supprimer, ainsi que `RM-stp-order` (nom d'un autre projet, sans locale).

Le reste n'empêche pas le démarrage : un mod sans `data.lua` se charge sans erreur.

## utils

- `icon_path` et `icons` sont en place. Ménage à faire dans `general.lua` : l'en-tête « remplace l'ancien… `trancate` » et le bloc « Utilisation côté ore » sont des commentaires de collage, et le commentaire sur le retour de `add_proto` est peu clair.
- Le commentaire d'exemple lit `rp-placeholder-icons`, mais le setting réel s'appelle « Dev assets » : à aligner (voir ore).
- Le chemin hors mode dev vise `graphics/items/<nom>.png`, un dossier qui n'existe pas dans assets. Le README d'assets note une autre convention (`graphics/mod_part/part/part.png`) : à trancher, les deux ne coïncident pas.
- `normalize_name` ne fait que minuscules + espaces → `_`, alors que les ids vanilla ont des tirets (`iron-ore`) et que les données mélangent les deux.
- **Loader absent** (connu) : rien ne lit les `*_data.lua` d'ore. Les fichiers `utils/ore.lua`, `assets.lua`, `building.lua`, `main.lua`, `function/multi.lua` et `function/world.lua` sont vides. `multi.lua` et `world.lua` ne sont même pas dans le `data.lua` d'utils.
- Les autres mods doivent faire `require("__realistic_production_utils__.utils.general")` : à noter dans un README.

## ore

**Chargement**

- `data.lua` vide (connu) et `prototypes/dev.lua` vide.
- Locale entièrement vide, sans sections `[mod-setting-name]` ni `[mod-setting-description]`. Les noms `name_en` / `name_fr` sont déjà dans les données.

**Settings** (`settings.lua`)

- « Dev assets » : id avec espace, sans préfixe, sans `order`, noms en dur au lieu de la locale, et `per_user` n'existe pas pour un setting (sans effet à ma connaissance). Même chose pour « Allow pure ore nodes » et « Ore density multiplier » (aucun code ne les lit encore). Proposition : `rp-dev-assets`, `rp-pure-ore-nodes`, `rp-ore-density`.
- Les blocs d'exemples commentés peuvent partir.

**Données** (générées par `generate_elements.py`, qui n'est dans aucun des 5 repos)

- 88 ressources (62 minerais, 19 roches, 5 fluides, 2 gaz), 118 éléments (88 naturels, 28 artificiels, 2 sans `origin` : astatine et francium), 5 alliages.
- 115 lignes de composition, qui ne couvrent que **44 ressources sur 88**. Sans composition :
  - roches (19) : granite, basalt, gabbro, diorite, rhyolite, andesite, peridotite, kimberlite, limestone, dolomite, sandstone, clay, shale, chalk, marble, gneiss, quartzite, slate, stone
  - minerais (19) : iron-ore, copper-ore, bauxite, wolframite, pentlandite, laterite, lepidolite, coltan, monazite, bastnasite, carnotite, uranium-ore, apatite, coal, lignite, anthracite, peat, oil_sand, oil_shale
  - fluides (5) et gaz : crude-oil, water, seawater, lithium_brine, geothermal_water, natural_gas
- Conséquences :
  - **nickel** (basic) n'a aucune source, donc l'acier inoxydable est impossible ; pentlandite et laterite sont sans composition ;
  - **phosphore** (basic) n'a aucune source (apatite sans composition) ;
  - **aluminium** et **silicium** (basic) ne viennent que de minéraux `advanced` (spodumène, béryl, zircon), alors que la bauxite (basic) et les roches siliceuses n'ont pas de composition ;
  - 47 éléments naturels n'ont aucune source (lanthanides, platinoïdes, tantale, niobium, vanadium…) ; monazite, bastnasite et coltan en couvriront une partie dès qu'ils auront une composition. Les 28 artificiels sans source sont normaux.
- Niveaux incohérents :
  - étain `advanced`, alors que la cassitérite et le bronze (qui en contient) sont `basic` ;
  - thorium et uranium `advanced`, alors que leurs seules sources (thorianite, uraninite) sont `experimental` ;
  - aluminium et silicium `basic` pour des sources `advanced` (voir plus haut).
- Noms : `iron-ore`, `copper-ore`, `uranium-ore`, `crude-oil` ont des tirets, tout le reste des underscores (`oil_sand`, `native_gold`, `stainless_steel`…). Prévoir une règle et un mapping vers les ids vanilla.
- Ids qui existent déjà dans le jeu : `iron-ore`, `copper-ore`, `uranium-ore`, `coal`, `stone`, `crude-oil`, `water`. Probablement aussi `sulfur`, `carbon`, `lithium`, `fluorine` (Space Age). À vérifier dans `data.raw`, car `add_proto` ignore les doublons en silence (juste un `log`).
- À prévoir dans les générateurs : les ingrédients d'alliage sont `{ name, amount }` sans `type` (obligatoire dans les recettes en 2.x), et les fluides exigent `base_color` et `flow_color` (tirables de la teinte).

## building

- Pas de `data.lua`. Les 6 fichiers de `prototypes/` (`entity`, `globals`, `item`, `recipe`, `technologie`, `util`) sont vides, comme les stubs `control` / `data-*` / `settings-*`.
- `settings.lua` : voir « Bloquant ».
- Locale vide. `info.json` correct (dépend d'assets et d'utils).

## core (`realistic_production_main`)

- Pas de `data.lua`, tous les stubs vides, `settings.lua` vide, locale vide.
- `info.json` : la description est celle d'assets (« Graphics and sounds… »). Dépendances correctes (assets, building, ore, utils).
- Repo `core` mais mod `main` : à unifier si possible avant publication.
- `TODO.md`, `ROADMAP.md` et `RAPPORT.md` sont à la racine du mod, donc empaquetés dans le zip. Les mettre dans `docs/` ou dans `package.ignore`. Les versions déposées contiennent les erreurs listées plus haut.

## assets

- Contenu sain : 4 icônes 64×64 et 4 images 256×256 (1x1, 2x2, 3x3, 3x5), de bons supports pour les teintes.
- `graphics/README.md` obsolète (il parle de `prototypes/util.lua` et de 32×32). Tu y as noté la nouvelle convention `graphics/mod_part/part/part.png` : à réécrire proprement.
- `thumbnail.png` est un JPEG 720×380 renommé en `.png`, et c'est le même fichier dans les 5 repos. Le convertir en vrai PNG (144×144 recommandé).
- À prévoir : une entité `resource` demande des `stages`. Les `_picture` 256×256 sont des images uniques, utilisables en test avec une seule variation.

## Transversal

- Stubs vides : `control.lua`, `data-updates.lua`, `data-final-fixes.lua`, `settings-*.lua` dans building, core et ore (utils : `control.lua` et `settings.lua`). Inoffensifs, à supprimer ou garder pour la suite.
- Les 5 `changelog.txt` sont au bon format mais identiques, avec le texte générique.

## Priorités

1. Corriger `building/settings.lua`.
2. Renommer les settings d'ore (`rp-…`) et aligner l'exemple d'`icon_path`.
3. Loader dans utils et `data.lua` d'ore (en cours).
4. Compositions : bauxite, pentlandite, laterite, apatite, wolframite, coltan, monazite, bastnasite, lepidolite, roches siliceuses.
5. Aligner les niveaux (étain, uranium/thorium, aluminium, silicium) et fixer la convention de noms.
6. assets : README et vrai `thumbnail.png`.

---

Rapport par repo — 22 oct. 2026

Les fichiers vides ne portent pas de nom de repo : je les ai attribués d'après `info.json` et les fichiers uniques (`prototypes/` → ore, `utils/` → utils…). À vérifier si un cas semble mal placé.

## Tous les repos

- Presque tous les fichiers standards sont vides : `control.lua`, `data-updates.lua`, `data-final-fixes.lua`, `settings-*.lua`, `migrations.lua`, tous les `locale/*/config.cfg`. À supprimer tant qu'ils ne servent pas.
- `migrations.lua` à la racine ne sert à rien : Factorio lit un dossier `migrations/`.
- Un `settings copy.lua` (doublon) existe en plusieurs exemplaires. `local bool = {}` passé à `data:extend` fait planter le chargement, et `RM-stp-order` n'a ni préfixe cohérent ni locale.
- `CHANGELOGS.md` ne contient que `---`, doublon de `changelog.txt`.
- Versions : `main` est en 2.0, les autres en 2.1.

## assets

- **Corriger** : les `icon.png` (iron/copper) sont des fichiers texte, pas des PNG. Factorio plantera dès qu'un prototype les référence.
- **Corriger** : `graphics/README.md` est obsolète (cite `prototypes/util.lua`, absent, et du 32×32). Les icônes vanilla sont en 64×64.
- **Corriger** : arborescence `graphics/ores/realistic-iron-ore/icon.png` ≠ chemin attendu par `icon_path`. Les noms `realistic-*` ne correspondent à aucun prototype (`iron-ore` vanilla, `hematite`…).
- **Ajouter** : icônes de base par forme (roche, minerai, lingot, fluide, gaz) à teinter, plutôt que 88+ PNG ; sons et sprites plus tard.
- **Retirer** : `control.lua`, `migrations.lua`, `settings*.lua` inutiles pour un mod de ressources graphiques.

## utils

- **Corriger** `icon_path` : variable globale `folder` jamais déclarée, paramètre `mod` ignoré.
- **Corriger** `trancate` : fonction vide.
- **Aligner** les noms entre TODO et code : `add_proto`, `copy_proto`, `get_settings`.
- **Ajouter** tout ce qui est vide : `utils/ore.lua`, `assets.lua`, `building.lua`, `main.lua`, `function/multi.lua`, `function/world.lua`.
- **Ajouter** un loader des `*_data.lua` générés (c'est le vrai chaînon manquant avec ore).
- Les autres mods l'utilisent via `require("__realistic_production_utils__.utils.general")` : à documenter dans un README.

## ore

C'est le repo le plus avancé, mais rien n'est encore chargé.

- **Bloquant** : pas de `data.lua`. Les fichiers `prototypes/entity|item|recipe|technologie|globals|util.lua` sont tous vides (`technologie` → `technology`).
- **Données incomplètes** :
  - `materials_data` et `components_data` sont vides.
  - Sans composition : bauxite, wolframite, pentlandite, laterite, lepidolite, coltan, monazite, bastnasite, carnotite, apatite, charbons, tourbe, bitumes, tous les fluides sauf l'air, toutes les roches.
  - Conséquences : l'aluminium n'a de source que dans des silicates avancés. Le nickel n'a aucune source, donc pas d'acier inoxydable. Le silicium n'a de source qu'avancée alors qu'il est « basic ». Phosphore, vanadium, niobium/tantale et lanthanides n'ont aucune source.
- **Cohérence** :
  - Étain `advanced` mais cassitérite et bronze `basic`.
  - Thorium/uranium `advanced` mais minerais `experimental`.
  - `astatine` et `francium` sans `origin`.
  - Mélange `iron-ore` / `native_gold` (tirets/underscores).
  - `elements_data` est rangé dans `resources/` alors que ce sont des matériaux.
- **Risques Space Age** : `carbon`, `lithium`, `fluorine`, `sulfur` existent déjà dans le jeu. `add_proto` ignore alors tes versions en silence.
- **Settings** : « Allow pure ore nodes » et « Ore density multiplier » sans préfixe ni locale, et rien ne les lit encore.
- **Hors repo** : `generate_elements.py` et le tableur source n'étaient pas dans les fichiers fournis ; il faut les versionner.
- **Changelog** : daté 2025-11-05, à mettre à jour.

## building

- Tout est à faire : seul `data.lua` existe (vide).
- **Corriger** le nom `realistic_production_buidling` avant publication (renommer un mod plus tard casse les sauvegardes).
- À partir de `utils/building.lua` : `create_building`, catégories de craft, `fluid_boxes`, `create_machine`, multiblocs.

## core (`realistic_production_main`)

- `info.json` : `factorio_version` 2.0 et `base >= 2.0.69` (les autres : 2.1), description copiée d'assets, dépendance `buidling` fautive.
- Aucune logique : `data-updates` / `data-final-fixes` vides. Les fonctions d'intégration vanilla (`remove_resource`, `replace_ingredient`…) n'existent pas non plus.
- Nom du repo (`core`) ≠ nom du mod (`main`) : à unifier.

## Priorités

1. Faux PNG, `settings copy.lua`, faute `buidling`, `migrations/`.
2. `data.lua` d'ore + loader dans utils.
3. Compositions manquantes (aluminium, nickel, silicium, phosphore).
4. Locale générée + icônes teintées.
