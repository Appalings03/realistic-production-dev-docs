# TODO — Realistic Production

Mis à jour le 22 oct. 2026 · @Martin

Légende : `[x]` fait · `[~]` fait mais à corriger · `[ ]` à faire

## 0. Bloquants (à régler avant tout)

- [X] `ore` : créer un `data.lua` (aucun fichier ne charge les prototypes aujourd'hui)
- [X] Remplacer les faux `icon.png` (fichiers texte « PLACEHOLDER ») par de vrais PNG
- [X] Corriger `settings copy.lua` : `local bool = {}` passé à `data:extend` → erreur au chargement
- [X] Corriger la faute `buidling` (nom du mod + dépendance dans `main`) **avant** toute publication
- [X] Déplacer/supprimer `migrations.lua` : Factorio lit un dossier `migrations/`, pas un fichier à la racine

## 1. Utils (`realistic_production_utils`)

### Général — `utils/general.lua`

- [X] `normalize_name(name)`
- [X] `icon_path(name)` : variable globale `folder` jamais déclarée, paramètre `mod` inutilisé, chemin plat `graphics/<nom>.png` ≠ arborescence réelle `graphics/ores/<nom>/icon.png` => à modifier comletement
- [X] `add_proto(proto)` (TODO disait `add_prototype`)
- [X] `copy_proto(type, name, overrides)` (TODO disait `copy_prototype`)
- [X] `get_settings(name)` (TODO disait `get_setting`)
- [X] `trancate(name)` : fonction vide (faute de frappe ?) → implémenter ou supprimer
- [ ] Fixer la convention de noms (tirets vs underscores, préfixe du mod) et la documenter

### Ore — `utils/ore.lua` (vide)

- [ ] `load_data(path)` : lecture des `*_data.lua` générés par `generate_elements.py`
- [ ] `create_item{...}` : un seul générateur d'items, qui appelle `add_proto`
- [ ] `create_fluid{...}` : gaz et saumures
- [ ] `create_group` et `create_subgroup` (les données existent déjà dans `groups_data.lua`)
- [ ] `make_icons(name, tint)` : icône de base par forme, teintée par famille
- [ ] `create_resource{...}` : entité `resource` avec autoplace et densité
- [ ] `ing(name, amount, type)` et `res(...)` : `type` obligatoire en 2.x
- [ ] `create_recipe{...}` : extraction, raffinage, séparation
- [ ] `create_technology{...}` : prérequis, recettes débloquées, coût en science

### Assets — `utils/assets.lua` (vide)

- [ ] `sound_path(name)`
- [ ] Helper de sprites et d'animations pour les bâtiments

### Building — `utils/building.lua` (vide)

- [ ] `create_building{base, ...}`
- [ ] `create_recipe_category` et `create_crafting_category`
- [ ] `fluid_boxes(...)`
- [ ] `kw(n)`
- [ ] `create_machine{...}`
- [ ] `function/multi.lua` : helpers multiblocs (fichier vide, absent de l'ancien TODO)
- [ ] `function/world.lua` : helpers monde (fichier vide, absent de l'ancien TODO)

### Main — `utils/main.lua` (vide)

- [ ] `remove_resource(name)`
- [ ] `find_recipes_using(item)`
- [ ] `replace_ingredient(recipe, old, new)`
- [ ] `hide_prototype` et `remove_recipe`
- [ ] `remove_tech_effect` et `fix_prerequisites`
- [ ] `scale_recipe(recipe, factor)`

## 2. Ore (`realistic_production_ore`)

### Données (générées par `generate_elements.py`)

- [X] `resources_data` (88 entrées), `elements_data` (118), `alloys_data` (5), `groups_data`, `composition_data`
- [ ] `materials_data` et `components_data` : tables vides
- [ ] Compléter `composition_data` : manquent bauxite, wolframite, pentlandite, laterite, lepidolite, coltan, monazite, bastnasite, carnotite, apatite, charbons/tourbe, bitumes, fluides (eau, pétrole, saumures…) et toutes les roches
- [ ] Ajouter `origin` à astatine et francium
- [ ] Versionner `generate_elements.py` et le tableur source dans un repo (absents des fichiers fournis)
- [ ] Rendre cohérents les niveaux : étain `advanced` mais cassitérite et bronze `basic` ; thorium/uranium `advanced` mais minerais `experimental`

### Prototypes

- [ ] `data.lua` qui charge les `*_data.lua` et crée items, fluides, groupes, sous-groupes
- [ ] Remplir `prototypes/item.lua`, `entity.lua`, `recipe.lua`, `technologie.lua` (renommer en `technology.lua`), ou les supprimer au profit du `data.lua`
- [ ] Supprimer `prototypes/globals.lua` et `prototypes/util.lua` (remplacés par les données générées et le mod utils)
- [ ] Vérifier les collisions avec Space Age (`carbon`, `lithium`, `fluorine`, `sulfur`…), car `add_proto` ignore les doublons en silence

### Settings et locale

- [~] `settings.lua` : noms « Allow pure ore nodes » / « Ore density multiplier » → ids préfixés (`rp-…`) + sections `[mod-setting-name]` / `[mod-setting-description]`

- [ ] Brancher ces settings dans `create_resource` (rien ne les lit encore)
- [ ] Générer `locale/en` et `locale/fr` depuis `name_en` / `name_fr` (tous les `config.cfg` sont vides)

## 3. Assets (`realistic_production_assets`)

- [ ] Vrais PNG (64×64 recommandé en 2.x) ; icônes de base par forme : roche, minerai, lingot, fluide, gaz
- [ ] Mettre à jour `graphics/README.md` (obsolète, mentionne `prototypes/util.lua` et du 32×32)
- [ ] Choisir **une** arborescence (`graphics/ores/<nom>/icon.png` ou plat) et aligner `icon_path`
- [ ] Ajouter dossiers sons / sprites quand nécessaire

## 4. Building (`realistic_production_buidling` → `building`)

- [ ] Corriger le nom du mod (faute) tant que rien n'est publié
- [ ] Tout le contenu : `data.lua`, machines, catégories de craft, multiblocs (voir utils/building)

## 5. Core / Main (`realistic_production_main`)

- [ ] `info.json` : `factorio_version` 2.0 → 2.1, `base >= 2.1`, description copiée de assets à réécrire
- [ ] Corriger la dépendance `buidling`
- [ ] Logique d'intégration vanilla (voir utils/main) dans `data-updates.lua` / `data-final-fixes.lua`
- [ ] Unifier le nom : repo `core` ↔ mod `main`

## 6. Hygiène transverse

- [ ] Supprimer les stubs vides inutiles dans chaque repo (`control.lua`, `settings-*.lua`, `data-*.lua`…)
- [X] Supprimer `settings copy.lua` (en double) et le préfixe `RM-stp-order` incohérent
- [X] Fusionner `CHANGELOGS.md` (contient juste `---`) dans `changelog.txt` ; mettre à jour la date du changelog ore (2025-11-05)
- [X] Un `changelog.txt` valide par repo, ou aucun
