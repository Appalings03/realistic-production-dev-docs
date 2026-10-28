# TODO — Realistic Production

Mis à jour le 28 oct. 2026 · @Martin

Légende : `[X]` fait (vérifié dans les repos au 28 oct.) · `[~]` fait en partie · `[ ]` à faire

Les détails et les chiffres sont dans `RAPPORT.md`.

## 0. Décisions

### Prises le 23 oct. 2026

- [X] **Noms avec `-`**, jamais `_`. `normalize_name` et le générateur normalisent désormais espaces et `_` en `-`. Les noms courts et références des données (`composition`, `associated_with`, alliages) sont normalisés ensemble ; le tableur conserve ses valeurs source.
- [X] **Préfixe `rp-`** : tous les prototypes créés par le mod (items, fluides, groupes, recettes, technologies, entités, settings) prennent `rp-` ; les fichiers de données gardent les noms courts (`hematite`) et le loader applique le préfixe ; les IDs vanilla réutilisés ne sont pas préfixés. Cela évite aussi les collisions avec Space Age (`rp-carbon`, `rp-lithium-brine`).
- [X] **Scories : un seul type**, comme des cendres. Il ne sert qu'à faire du ciment, du béton ou d'autres matériaux inertes ; ce n'est pas une source d'éléments.
- [X] **Bâtiments** : à étudier une fois que l'assemblage des prototypes fonctionne (machines autonomes d'abord, voir `machine.md`).

### Décisions confirmées le 25 oct. 2026

- [X] **Items vanilla** : réutiliser les sept prototypes existants, sans les recréer. `iron-ore` et `copper-ore` restent les IDs vanilla, obtenus comme **produits** du raffinage de l'hématite et de la malachite (pas de gisement posé dans le monde).
- [X] **Ressources disponibles au départ** : `stone`, `clay`, `limestone`, `sandstone`, **hématite**, **malachite**, `coal` et `water` (décision du 25 oct. : roches de départ pour le fer et le cuivre). Magnétite, goethite et sidérite arrivent avec la prospection de base ; les sulfures de cuivre avec la prospection géologique.
- [X] **Éléments volatils** (O, H, C, S) : ils disparaissent au raffinage basique ; seuls les éléments solides non principaux deviennent des scories. Les gaz de procédé (CO₂, SO₂) viendront plus tard.
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
- [X] `create_item{...}` (préfixe `rp-`, icônes de test, vanilla ignoré)
- [X] `create_fluid{...}` : `base_color` et `flow_color` exigés ; `default_temperature` vaut 15 par défaut et peut être surchargée
- [X] `create_group` et `create_subgroup` (données dans `groups_data.lua`)
- [X] `make_icons(name, tint)` : s'appuie sur `icons(name, opts)` de `general.lua`
- [X] `ing(name, amount, type)` et `res(...)` : `type` explicite pour Factorio 2.x

- [~] `create_resource{...}` : création avec `minable.results`, `stages`, `map_color` et `autoplace` fournis par l'appelant ; densité, nodes purs et gisements mixtes à préciser avec les settings et données

- [X] `create_recipe{...}` : conserve `ingredients` avant la normalisation des ingrédients et résultats typés (Factorio 2.x)

- [~] Raffinage basique généré depuis `composition` : `primary`, `volatile` et les compositions complètes sont dans le tableur ; il reste à définir le rendement et la destination des produits (et à écrire la génération)

- [X] `create_technology{...}` : prérequis, recettes débloquées et coût en science via `unit`

### Utilitaires Assets, Building, Main

- [X] `utils/assets.lua` : `sound_path(name)`, helpers de sprites et d'animations
- [X] `utils/building.lua` : `create_building{base, ...}`, `create_recipe_category`, `create_crafting_category`, `fluid_boxes(...)`, `kw(n)`, `create_machine{...}`
- [~] `function/multi.lua` (multiblocs) et `function/world.lua` (monde) : chargés par `utils/data.lua` mais encore vides
- [X] `utils/main.lua` : `remove_resource`, `find_recipes_using`, `replace_ingredient`, `hide_prototype`, `remove_recipe`, `remove_tech_effect`, `fix_prerequisites`, `scale_recipe`
- [ ] **Corriger `utils/main.lua`** (relecture du 28 oct.) : `hide_prototype` pose le drapeau `hidden` sur les items, alors qu'en 2.x il faut `hidden = true` (à confirmer au premier lancement) ; `replace_ingredient` ne cherche le nouvel ingrédient que dans `data.raw.item` (les packs de science, de type `tool`, recevraient un `rp-` à tort) ; `scale_recipe` accepte des facteurs qui donnent des quantités d'items non entières (erreur au chargement)
- [ ] Vérifier que `remove_resource` suffit (références éventuelles dans les `autoplace-control` et les presets de génération de carte)

## 2. Ore (`realistic_production_ore`)

### Données (générées par `proto_table/generate_elements.py`)

- [X] `resources_data` (88), `elements_data` (118), `alloys_data` (5, quantités remplies), `materials_data` (32), `groups_data`, `composition_data` (498 lignes)
- [X] `level` rempli partout ; `generate_elements.py` et `elements.xlsx` versionnés dans dev-docs
- [X] `materials_data` (32 formes de matériaux) généré ; `components_data` reste vide en attendant les décisions de conception
- [X] **44 compositions manquantes** (complétées le 27 oct., voir `proto_table/COMPOSITIONS.md`) : 19 roches, 19 minerais (dont bauxite, pentlandite, latérite, apatite, wolframite, coltan, monazite, bastnasite, lepidolite, carnotite, charbons, tourbe, bitumes), 6 fluides et gaz
- [X] Ajouter `primary` (composition), `tech` et `world` (resources) et `volatile` (elements) dans le tableur et le générateur ; ajouter aussi une colonne indiquant les éléments volatils (ou une liste dans le générateur) pour calculer les scories
- [X] Compositions de départ à compléter d'abord : `stone`, `clay`, `limestone`, `sandstone`, `coal`, `water` (les 8 de départ n'en ont pas, sauf hématite et malachite)
- [X] `iron-ore` et `copper-ore` passés en « produit » (`world = no`) ; goethite et sidérite réattribuées au palier de base (`tech`)

- [~] Colonne `vanilla` ajoutée à la feuille `elements` (vide) : à remplir quand on aura vérifié `data.raw` (`sulfur` est le seul candidat sûr du jeu de base)

- [X] `origin` d'astate et de francium : `artificial`
- [X] Aligner les niveaux selon le premier procédé qui libère l'élément : aluminium et silicium `advanced`, thorium et uranium `experimental`, étain `basic` (cassitérite et bronze `basic`)
- [X] Sources des 47 éléments naturels qui n'en avaient pas : les 88 éléments naturels ont maintenant au moins une source (33 d'entre eux seulement en traces, voir `COMPOSITIONS.md`)
- [ ] Revoir les 23 `associated_with` : les compositions sont maintenant complètes, la revue est possible
- [ ] Ranger `elements_data` hors de `resources/` (ce sont des matériaux) ou le documenter

### Prototypes

- [X] `data.lua` charge les `*_data.lua` et crée items, fluides, groupes, sous-groupes (avec le préfixe `rp-`) : 236 items/fluides + 12 groupes et sous-groupes dans une simulation de l'étape data (pas encore dans Factorio)

- [~] Ressources `vanilla = yes` : le prototype n'est pas créé (fait) ; reste à modifier en `data-final-fixes` ce qui change (sous-groupe, ordre, locale)

- [ ] Supprimer ou remplir `prototypes/dev.lua`
- [ ] Éléments qui existent déjà dans le jeu (`sulfur` probablement, et `carbon`, `lithium`, `fluorine` avec Space Age) : décider de les réutiliser ou de créer `rp-…` (à vérifier dans `data.raw`). Le préfixe supprime les collisions, `add_proto` n'a plus à ignorer de doublons en silence
- [X] Fluides : couleurs (`base_color`, `flow_color`) définies dans `data.lua` pour les 18 fluides
- [ ] Teintes des icônes : aucune colonne `tint` ni conversion de `kind`, donc les 236 icônes d'items/fluides de test sont identiques
- [ ] Confirmer le niveau du plomb (`advanced`, alors que la galène est `basic`)
- [X] Ajouter `world`, `tech` et `volatile` à `INTERNAL_FIELDS` dans `utils/ore.lua` pour éviter de copier ces métadonnées dans les prototypes
- [X] Tables régénérées copiées dans `ore/` : `proto_table/` et `ore/prototypes/` sont identiques (vérifié le 28 oct.)
- [~] Feuille `materials` remplie le 27 oct. (32 formes : lingots, plaques, poudres ; les plaques de fer, cuivre et acier sont celles du jeu de base) ; `components` reste vide (pièces), elle dépend des recettes et des machines

### Settings et locale

- [X] `settings.lua` : trois settings présents, avec ids normalisés (`rp-dev-assets`, `rp-mixed-ore-patches`, `rp-ore-density`), sans `per_user`, et avec un ordre explicite pour chaque option
- [X] Locale des settings : `[mod-setting-name]` et `[mod-setting-description]` présents en EN et FR (générés)
- [ ] Brancher `rp-mixed-ore-patches` et `rp-ore-density` dans la génération des gisements ; le réglage de mélange autorise les ressources compatibles reliées par `associated_with`
- [X] Générer `locale/en` et `locale/fr` depuis `name_en` / `name_fr` et synchroniser les locales du mod
- [X] Blocs d'exemples commentés retirés de `settings.lua`

## 3. Assets (`realistic_production_assets`)

- [X] Images de test : 4 icônes 64×64 et 4 images 256×256 dans `graphics/dev/`
- [X] `thumbnail.png` est un vrai PNG (720×380)
- [X] `graphics/README.md` réécrit (25 oct.) : `graphics/items/<id-prototype>.png`, mode dev
- [X] Une seule arborescence, alignée sur `icon_path`
- [~] Premier test d'icône Blender : `blender_model/plate/brass-plate.png` (64×64, fond transparent). Convention retenue le 27 oct. : **une base blanche/grise à effet métallique par forme, teintée par matériau** (reflets doux, pas de blanc brûlé) ; à valider sur 3 teintes
- [ ] Icônes de base par forme : roche, minerai, lingot, plaque, poudre, fluide, gaz (64×64, à teinter) ; fixer d'abord les conventions de la section « Conventions visuelles » de `blender_models_checklist.md`
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
- [X] Nouveaux documents (27 oct.) : `RoadMap/process.md` (20 grands processus industriels), `interactive_techtree/` (arbres technologiques draw.io, jeu de base et Space Age), `blender_model/` (synthèse de la playlist Blender, aide-mémoire de raccourcis, premier test de plaque)
- [ ] Relier `process.md` aux recettes et machines du mod (quels processus deviennent des multiblocs ou des recettes) et aux technologies de `tech.md`
- [X] Remplacer les fichiers de `dev-docs` par ces nouvelles versions (`ROADMAP`, `TODO`, `RAPPORT`, `RoadMap/Item`, `machine`, `tech`)
- [X] Déplacer ou supprimer `settings copy.lua` à la racine de `dev-docs` => Peu etre ignoré pour l'instant, utiliser code rappel de fonctionnement
- [X] Archiver les fichiers `OLD` de `RoadMap/` (`Liste feature_OLD.xlsx`, `Roadmap — Realistic Production — OLD.md`)
- [ ] Décider des stubs vides (`control.lua`, `data-updates.lua`, `data-final-fixes.lua`, `settings-*.lua`) : supprimer ou garder pour la suite
- [X] Changelogs : les 5 sont identiques (texte générique, 0.0.1 du 22 oct.)
- [~] `.gitignore` : le `__pycache__` n'est plus versionné dans dev-docs, mais aucun `.gitignore` n'existe encore (à ajouter dans chaque repo)
- [ ] `verify.lua` : chemins Windows (`\\`) et ne contrôle que les données ; l'adapter ou le remplacer
- [ ] **Premier lancement dans Factorio** : valider assets + utils + ore, puis les cinq mods

## 7. Idées en attente

- Procédés de raffinage débloqués par la recherche (broyage, flottation, séparation magnétique, lixiviation, électrolyse) : à lier aux machines de `machine.md`
- Nouveaux packs de science (analyse minérale, métallurgie, génie chimique, expérimental) : à confirmer dans `tech.md`
- Catalyseurs et chaîne pétrochimique (règle de récupération à valider)
- Alliages supplémentaires de la liste initiale (invar, monel, stellite, magnalium…) après vérification de leurs éléments
- Modèles Blender et animations
- Extension Space A
