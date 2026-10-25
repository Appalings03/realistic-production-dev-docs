# TODO — Realistic Production

Mis à jour le 25 oct. 2026 · @Martin

Légende : `[X]` fait (vérifié dans les repos au 24 oct.) · `[~]` fait en partie · `[ ]` à faire

Les détails et les chiffres sont dans `RAPPORT.md`.

## 0. Décisions

### Prises le 23 oct. 2026

- [X] **Noms avec `-`**, jamais `_`. `normalize_name` et le générateur normalisent désormais espaces et `_` en `-`. Les noms courts et références des données (`composition`, `associated_with`, alliages) sont normalisés ensemble ; le tableur conserve ses valeurs source.
- [X] **Préfixe `rp-`** : tous les prototypes créés par le mod (items, fluides, groupes, recettes, technologies, entités, settings) prennent `rp-` ; les fichiers de données gardent les noms courts (`hematite`) et le loader applique le préfixe ; les IDs vanilla réutilisés ne sont pas préfixés. Cela évite aussi les collisions avec Space Age (`rp-carbon`, `rp-lithium-brine`).

- [X] **Scories : un seul type**, comme des cendres. Il ne sert qu'à faire du ciment, du béton ou d'autres matériaux inertes ; ce n'est pas une source d'éléments.
- [X] **Bâtiments** : à étudier une fois que l'assemblage des prototypes fonctionne (machines autonomes d'abord, voir `machine.md`).

### Décisions confirmées le 25 oct. 2026

- [X] **Items vanilla** : réutiliser les sept prototypes existants, sans les recréer. `iron-ore` et `copper-ore` restent les IDs vanilla des minerais récupérés depuis des roches adaptées ; les constituants secondaires non récupérés deviennent des scories.
- [X] **Ressources disponibles au départ** : `stone`, `clay`, `limestone`, `sandstone`, `iron-ore`, `copper-ore`, `coal` et `water`. Le fer et le cuivre sont récupérables dès le début ; les autres constituants des roches restent des scories jusqu'à de meilleurs procédés.
- [X] **Sens de `level` pour un élément** : palier du premier procédé qui le libère. Al et Si passent à `advanced`, Th et U à `experimental`, et Sn à `basic`.
- [X] **Déblocages de raffinage** : les technologies précises seront définies avec les recettes et les machines ; ce travail est reporté.

## 1. Utils (`realistic_production_utils`)

### Général — `utils/general.lua`

- [X] `normalize_name(name)` (met des `-`)
- [X] `icon_path(name, opts)` : mode dev (`graphics/dev/<taille>_item.png`) et mode normal (`graphics/<folder>/<nom>.png`)
- [X] `icons(name, opts)` avec teinte optionnelle
- [X] `add_proto(proto)`, `copy_proto(type, name, overrides)`, `get_settings(name)`
- [X] `trancate` supprimée
- [X] Vérifier et supprimer les commentaires de collage dans `general.lua` ; aucun bloc obsolète ni exemple de setting n'y subsiste
- [X] Convention normale de `icon_path` : `graphics/items/<id-prototype>.png`, documentée dans le README d'assets
- [X] Documenter le `require("__realistic_production_utils__.utils.general")` dans le README de utils
- [X] Documenter la convention de noms (tirets, préfixe `rp-`) dans le README de utils

### Ore — `utils/ore.lua`

- [X] `load_data(path)` : chargement et validation du retour des fichiers `*_data.lua`
- [X] `create_item{...}` et `create_fluid{...}` (un fluide demande `base_color` et `flow_color`)
- [X] `create_group` et `create_subgroup` (données dans `groups_data.lua`)
- [X] `make_icons(name, tint)` : s'appuie sur `icons(name, opts)` de `general.lua`
- [X] `ing(name, amount, type)` et `res(...)` : `type` explicite pour Factorio 2.x
- [~] `create_resource{...}` : création avec `minable.results`, `stages`, `map_color` et `autoplace` fournis par l'appelant ; densité, nodes purs et gisements mixtes à préciser avec les settings et données
- [X] `create_recipe{...}` : recette 2.x avec ingrédients/résultats typés et IDs préfixés
- [ ] Raffinage basique généré depuis `composition` : ajouter d'abord `primary` et définir le rendement / la destination des produits
- [X] `create_technology{...}` : prérequis, recettes débloquées et coût en science via `unit`

### Assets, Building, Main (fichiers vides)

- [ ] `utils/assets.lua` : `sound_path(name)`, helper de sprites et d'animations
- [ ] `utils/building.lua` : `create_building{base, ...}`, `create_recipe_category`, `create_crafting_category`, `fluid_boxes(...)`, `kw(n)`, `create_machine{...}`
- [ ] `function/multi.lua` (multiblocs) et `function/world.lua` (monde) : vides et non chargés par `data.lua`
- [ ] `utils/main.lua` : `remove_resource`, `find_recipes_using`, `replace_ingredient`, `hide_prototype`, `remove_recipe`, `remove_tech_effect`, `fix_prerequisites`, `scale_recipe`

## 2. Ore (`realistic_production_ore`)

### Données (générées par `proto_table/generate_elements.py`)

- [X] `resources_data` (88), `elements_data` (118), `alloys_data` (5, quantités remplies), `groups_data`, `composition_data` (115 lignes)
- [X] `level` rempli partout ; `generate_elements.py` et `elements.xlsx` versionnés dans dev-docs
- [ ] `materials_data` et `components_data` : tables vides (lingots, plaques, poudres, pièces)
- [ ] **44 compositions manquantes** : 19 roches, 19 minerais (dont bauxite, pentlandite, latérite, apatite, wolframite, coltan, monazite, bastnasite, lepidolite, carnotite, charbons, tourbe, bitumes), 6 fluides et gaz
- [ ] Ajouter `primary` (composition) et `tech` (resources) dans le tableur et le générateur
- [ ] Ajouter `vanilla` à la feuille `elements` si des éléments existent déjà dans le jeu
- [ ] Ajouter `origin` à astatine et francium
- [X] Aligner les niveaux selon le premier procédé qui libère l'élément : aluminium et silicium `advanced`, thorium et uranium `experimental`, étain `basic` (cassitérite et bronze `basic`)
- [ ] Sources des 47 éléments naturels sans source (nickel et phosphore d'abord, puis terres rares, platinoïdes, niobium, tantale…)
- [ ] Revoir les 23 `associated_with` quand les compositions seront complètes
- [ ] Ranger `elements_data` hors de `resources/` (ce sont des matériaux) ou le documenter

### Prototypes

- [ ] `data.lua` qui charge les `*_data.lua` et crée items, fluides, groupes, sous-groupes (avec le préfixe `rp-`)
- [ ] Ressources `vanilla = yes` : ne pas créer le prototype, ne modifier en `data-final-fixes` que ce qui change (sous-groupe, ordre, locale)
- [ ] Supprimer ou remplir `prototypes/dev.lua`
- [ ] Éléments qui existent déjà dans le jeu (`sulfur` probablement, et `carbon`, `lithium`, `fluorine` avec Space Age) : décider de les réutiliser ou de créer `rp-…` (à vérifier dans `data.raw`). Le préfixe supprime les collisions, `add_proto` n'a plus à ignorer de doublons en silence
- [ ] Fluides : couleurs (`base_color`, `flow_color`) tirées de la teinte

### Settings et locale

- [~] `settings.lua` : trois settings présents, mais ids avec espaces et sans préfixe (`Dev assets`, `Allow pure ore nodes`, `Ore density multiplier`), `per_user` inutile, pas de `order` sur le premier

- [ ] Renommer en `rp-dev-assets`, `rp-pure-ore-nodes`, `rp-ore-density` et ajouter `[mod-setting-name]` / `[mod-setting-description]`
- [ ] Brancher les settings dans `create_resource` (rien ne les lit)
- [ ] Générer `locale/en` et `locale/fr` depuis `name_en` / `name_fr` (sections présentes, sans entrées)
- [ ] Retirer les blocs d'exemples commentés de `settings.lua`

## 3. Assets (`realistic_production_assets`)

- [X] Images de test : 4 icônes 64×64 et 4 images 256×256 dans `graphics/dev/`
- [X] `thumbnail.png` est un vrai PNG (720×380)
- [ ] Réécrire `graphics/README.md` (obsolète : 32×32, `prototypes/util.lua`, `realistic-iron-ore/`)
- [ ] Choisir **une** arborescence et aligner `icon_path`
- [ ] Icônes de base par forme : roche, minerai, lingot, fluide, gaz (64×64, à teinter)
- [ ] Miniature à la taille du mod portal
- [ ] Sons et sprites quand nécessaire (voir `blender_models_checklist.md`)

## 4. Building (`realistic_production_building`)

- [~] `settings.lua` valide, mais son seul setting, `RM-stp-order` (caché, sans locale), a un préfixe incohérent avec le reste du mod et ne sert à rien aujourd'hui : le supprimer ou le renommer

- [ ] Créer `data.lua` et remplir `prototypes/` (`entity`, `item`, `recipe`, `technologie` → `technology`) ou supprimer les fichiers inutiles
- [ ] Fiche de chaque machine : catégorie de recette, dimensions, énergie, vitesse, fluid boxes, bâtiments requis, technologie, niveau, icône (voir `machine.md`)
- [ ] Chaîne de démarrage : foreuse, concasseur, crible, laveur, four de fusion, assembleuse mécanique
- [ ] Catégories de craft et technologies de déblocage
- [ ] Multiblocs, après la première version

## 5. Core / Main (`realistic_production_main`)

- [ ] `info.json` : description copiée d'assets, à réécrire
- [ ] Créer `data.lua`, `data-updates.lua` et `data-final-fixes.lua` avec la logique d'intégration vanilla (voir `utils/main`)
- [ ] Unifier le nom : repo `core` ↔ mod `main`
- [ ] Locale et `settings.lua` : vides

## 6. Documentation et hygiène

- [X] Repo `dev-docs` avec roadmap, TODO, rapport, notes de conception et tableur
- [X] Remplacer les fichiers de `dev-docs` par ces nouvelles versions (`ROADMAP`, `TODO`, `RAPPORT`, `RoadMap/Item`, `machine`, `tech`)
- [X] Déplacer ou supprimer `settings copy.lua` à la racine de `dev-docs` => Peu etre ignoré pour l'instant, utiliser code rappel de fonctionnement
- [X] Archiver les fichiers `OLD` de `RoadMap/` (`Liste feature_OLD.xlsx`, `Roadmap — Realistic Production — OLD.md`)
- [ ] Décider des stubs vides (`control.lua`, `data-updates.lua`, `data-final-fixes.lua`, `settings-*.lua`) : supprimer ou garder pour la suite
- [ ] Changelogs : les 5 sont identiques (texte générique, 0.0.1 du 22 oct.)
- [ ] Exécuter `verify.lua` et faire un **premier lancement dans Factorio** avec les cinq mods

## 7. Idées en attente

- Procédés de raffinage débloqués par la recherche (broyage, flottation, séparation magnétique, lixiviation, électrolyse) : à lier aux machines de `machine.md`
- Nouveaux packs de science (analyse minérale, métallurgie, génie chimique, expérimental) : à confirmer dans `tech.md`
- Catalyseurs et chaîne pétrochimique (règle de récupération à valider)
- Alliages supplémentaires de la liste initiale (invar, monel, stellite, magnalium…) après vérification de leurs éléments
- Modèles Blender et animations
- Extension Space A
