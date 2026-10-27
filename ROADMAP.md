# Roadmap — Realistic Production

Mise à jour : 27 oct. 2026 · Cible : Factorio 2.1 · Extension Space Age prévue plus tard

Objectif : des chaînes de production plus réalistes — roche brute → minerais → lingots → pièces → produits finis, avec fluides, broyage, multiblocs et nouveaux packs de science.

## Principes de conception

- **Le monde ne contient que ce qui existe naturellement sur Terre** : roches, minerais, fluides et gaz. Les éléments artificiels sont fabriqués par le joueur et servent à la recherche.
- **Extraction progressive** : au début, certaines roches ne sont pas extractibles. Le raffinage basique d'une roche ne garde que son élément principal et le reste devient des scories. Il n'existe qu'**un seul type de scorie**, inerte, comme des cendres : elle ne sert qu'à faire du ciment, du béton ou d'autres matériaux inertes. Les autres éléments s'obtiennent avec des procédés avancés appliqués à la roche brute. Détails dans `RoadMap/Item.md`.
- **Gisements mixtes** : un patch peut contenir plusieurs minerais ou roches souvent associés dans la réalité (`associated_with`).
- **Bâtiments débloqués par la recherche** : chaque machine est liée à une technologie. Certains bâtiments demanderont d'autres bâtiments pour fonctionner ; ce sujet est reporté jusqu'à ce que l'assemblage des prototypes fonctionne (voir `RoadMap/machine.md`).
- **Noms** : tirets (`-`), jamais de `_`. Les noms des prototypes créés par le mod portent le préfixe `rp-` ; les IDs vanilla réutilisés ne sont pas préfixés. Les tables de données conservent les noms courts et le loader applique le préfixe.
- **Alliages simplifiés** : acier, bronze, laiton, duralumin, acier inoxydable.
- **Ressources vanilla** : `iron-ore` et `copper-ore` restent les IDs du jeu de base, comme produits du raffinage de l'hématite et de la malachite ; les sept ressources déjà présentes dans le jeu sont réutilisées, pas recréées (voir `RoadMap/Item.md`, section 8).
- **Space Age** : hors périmètre tant que les phases 1 à 5 ne sont pas stables.

## Architecture (5 repos + dev-docs)

| Repo     | Mod                               | Rôle                                                         | Avancement                                              |
| -------- | --------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------- |
| assets   | `realistic_production_assets`   | graphismes, sons                                              | ◐ images de test (`graphics/dev/`), README à jour, pas d'icône définitive |
| utils    | `realistic_production_utils`    | fonctions communes                                            | ◐ `general.lua` (6 fonctions) et `ore.lua` (11 fonctions, correctifs ciblés vérifiés), 3 modules vides |
| ore      | `realistic_production_ore`      | roches, minerais, fluides, éléments, alliages               | ◐ `data.lua` crée items, fluides et groupes (non testé dans Factorio) |
| building | `realistic_production_building` | machines, multiblocs                                          | ▫ vide                                                 |
| core     | `realistic_production_main`     | charge les autres, adapte le vanilla                          | ▫ vide                                                 |
| dev-docs | (documentation)                   | roadmap, TODO, rapport, notes de conception, `proto_table/` | ✓                                                      |

Dépendances : `assets` et `utils` ne dépendent que de `base` ; `ore` et `building` dépendent d'`assets` et d'`utils` ; `main` dépend des quatre autres.

## Phase 0 — Fondations *(presque terminée)*

- [X] Découpage en 5 mods et dépendances, tous en 2.1
- [X] Fonctions générales utils (`normalize_name`, `icon_path`, `icons`, `add_proto`, `copy_proto`, `get_settings`)
- [X] Modèle de données : 88 ressources, 118 éléments, 5 alliages, 32 matériaux, groupes et sous-groupes, 498 lignes de composition (script Python)
- [X] Niveaux (`level`) et quantités d'alliages remplis
- [X] Nettoyage : faute `buidling`, versions 2.1, `bool = {}` retiré des settings de building
- [X] **Convention de noms décidée** (23 oct.) : tirets et préfixe `rp-`
- [X] Normaliser les noms du générateur en tirets et régénérer les tables ; convention `rp-` décidée pour les prototypes non-vanilla
- [X] **Scorie unique** décidée (23 oct.)
- [X] **Définition du `level`** d'un élément : palier du premier procédé qui le libère ; Al/Si `advanced`, Th/U `experimental`, Sn `basic`
- [X] Ressources disponibles au départ : les 8 ressources de `Item.md`, section 7 ; fer et cuivre viennent de l'hématite et de la malachite (`iron-ore` / `copper-ore` sont des produits, décision du 25 oct.)
- [X] Colonnes `primary` (composition), `tech` et `world` (resources), `volatile` et `vanilla` (elements) dans le tableur et le générateur (27 oct.)
- [X] Tableur complété : 88 ressources avec composition, 88 éléments naturels avec au moins une source (voir `proto_table/COMPOSITIONS.md`)
- [X] Option de génération de gisements mixtes compatibles (`rp-mixed-ore-patches`, startup, activée par défaut) ; son branchement à l'autoplace reste à faire
- [ ] Confirmer le niveau du plomb (`advanced`, alors que la galène est `basic`)

## Phase 1 — Ore jouable *(en cours : validation dans Factorio à faire)*

Jalon : le jeu démarre avec le mod ore ; items et fluides apparaissent dans le menu de craft avec leurs noms FR/EN et des icônes de test.

- [X] `data.lua` d'ore charge les données et crée les prototypes d'items et de fluides
- [X] Générateurs `create_item`, `create_fluid`, groupes et sous-groupes (`utils/ore.lua`)
- [X] `create_fluid` fournit `default_temperature = 15` par défaut, surchargeable dans la définition
- [X] `create_recipe` conserve `ingredients` avant la normalisation des champs typés
- [ ] Icônes de test teintées par famille : aujourd'hui les 236 icônes d'items/fluides sont identiques (pas de colonne `tint`)
- [X] Locale générée depuis `name_en` / `name_fr` par `generate_elements.py`
- [X] Settings renommés (`rp-…`) avec leur locale
- [ ] **Premier lancement dans Factorio** avec assets + utils + ore (jalon de la phase)
- [X] Compositions manquantes (44 ressources complétées le 27 oct.)

## Phase 2 — Ressources et raffinage

Jalon : on peut miner des roches et des minerais et obtenir les éléments de base.

- [~] `create_resource` : le helper existe, mais aucune ressource n'est encore posée ; autoplace, densité, nodes purs et gisements mixtes via `associated_with` restent à faire
- [ ] Roches verrouillées au départ (technologie de prospection par roche)
- [ ] Raffinage basique : élément principal + scories (`create_recipe`, `ing` / `res`)
- [ ] Gaz de l'air (machine) et fluides (gisements)
- [ ] Alliages simplifiés (acier, bronze, laiton, acier inox, duralumin)
- [ ] Recettes de ciment et de béton à partir des scories
- [ ] Procédés avancés : extraction des éléments secondaires depuis la roche brute
- [ ] Technologies de déblocage par niveau : Basic → Advanced → Experimental

## Phase 3 — Bâtiments

Jalon : chaque étape de la chaîne de démarrage (extraction, concassage, préparation, première fusion) a sa machine, débloquée par une technologie.

- [X] Utilitaires `create_building`, `create_machine`, catégories de craft, `fluid_boxes` ; les prototypes de machines restent à créer
- [ ] Première version : machines autonomes reliées par tapis et tuyaux
- [ ] Dépendances entre bâtiments : reportées, à reprendre quand l'assemblage des prototypes fonctionne (voir `machine.md`)
- [ ] Multiblocs (ex. raffinerie : tour de distillation, tour catalytique, séparateur pétrole/eau salée)
- [ ] Sprites et animations (assets) ; modèles 3D suivis dans `blender_models_checklist.md`

## Phase 4 — Intégration au jeu de base

- [X] Helpers `remove_resource`, remplacement d'ingrédients et masquage des recettes ; leur intégration aux mods reste à faire
- [X] Helpers de correction des prérequis et effets de technologies
- [X] Helper `scale_recipe` disponible ; équilibrage des quantités à faire

## Phase 5 — Science

- [ ] Packs de science vanilla rendus plus complexes
- [ ] Nouveaux packs (éléments artificiels fabriqués par le joueur)
- [ ] Chaînes manufacturières avancées (inspiration Galloc manufacturing)

## Phase 6 — Space Age *(plus tard)*

- [ ] Extension séparée, après stabilisation des phases 1 à 5

## Ordre de travail conseillé

1. Phase 0 : terminée côté tableur ; reste à confirmer le niveau du plomb.
2. Phase 1 : teintes d'icônes, puis premier lancement dans Factorio (les bugs `create_fluid` et `create_recipe` sont corrigés).
3. Phase 2 : ressources, puis raffinage basique, puis ciment/béton et procédés avancés.
4. Phases 3 et 4 en parallèle.
5. Phase 5.

À chaque phase, lancer le jeu et vérifier le chargement avant de passer à la suivante.