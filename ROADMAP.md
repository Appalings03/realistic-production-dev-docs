# Roadmap — Realistic Production

Mise à jour : 22 oct. 2026 · Cible : Factorio 2.1 · Extension Space Age prévue plus tard

Objectif : des chaînes de production plus réalistes — roche brute → minerais → lingots → pièces → produits finis, avec fluides, broyage, multiblocs et nouveaux packs de science.

## Architecture (5 repos)

| Repo     | Mod                               | Rôle                                           | Avancement                                       |
| -------- | --------------------------------- | ----------------------------------------------- | ------------------------------------------------ |
| assets   | `realistic_production_assets`   | graphismes, sons                                | ▫ squelette, icônes factices                   |
| utils    | `realistic_production_utils`    | fonctions communes                              | ◐ `general.lua` fait, reste vide              |
| ore      | `realistic_production_ore`      | roches, minerais, fluides, éléments, alliages | ◐ données générées, aucun prototype chargé |
| building | `realistic_production_buidling` | machines, multiblocs                            | ▫ vide                                          |
| core     | `realistic_production_main`     | charge les autres, adapte le vanilla            | ▫ vide                                          |

## Phase 0 — Fondations *(en cours)*

- [X] Découpage en 5 mods et dépendances
- [X] Fonctions générales utils (`normalize_name`, `add_proto`, `copy_proto`, `get_settings`)
- [X] Modèle de données : 88 ressources, 118 éléments, 5 alliages, groupes/sous-groupes, compositions (script Python)
- [X] Nettoyage : faute `buidling`, versions 2.0/2.1, stubs vides, `migrations/`
- [ ] Convention de noms et de préfixes, collisions Space Age

## Phase 1 — Ore jouable *(prochaine étape)*

Jalon : le jeu démarre avec le mod ore, les items et fluides apparaissent dans le menu de craft avec leurs noms FR/EN et des icônes.

- [ ] `data.lua` + loader des `*_data.lua`
- [ ] Générateurs `create_item`, `create_fluid`, groupes/sous-groupes
- [ ] Icônes teintées par famille (`make_icons`)
- [ ] Locale générée depuis `name_en` / `name_fr`
- [ ] Compléter les compositions manquantes (aluminium, nickel, silicium, phosphore, terres rares…)

## Phase 2 — Ressources et raffinage

Jalon : on peut miner des roches/minerais et obtenir les éléments de base.

- [ ] `create_resource` (autoplace, densité, nodes purs, gisements mixtes via `associated_with`)
- [ ] Recettes d'extraction, broyage, séparation, raffinage (`create_recipe`, `ing`/`res`)
- [ ] Gaz de l'air (machine) et fluides (gisements)
- [ ] Alliages simplifiés (acier, bronze, laiton, acier inox, duralumin)
- [ ] Technologies de déblocage par niveau : Basic → Advanced → Experimental

## Phase 3 — Bâtiments et multiblocs

- [ ] `create_building`, `create_machine`, catégories de craft, `fluid_boxes`
- [ ] Multiblocs (ex. raffinerie : tour de distillation, tour catalytique, séparateur pétrole/eau salée)
- [ ] Sprites et animations (assets)

## Phase 4 — Intégration au jeu de base

- [ ] Retrait des ressources vanilla remplacées (`remove_resource`)
- [ ] Remplacement des ingrédients, masquage des recettes obsolètes
- [ ] Correction des prérequis et effets de technologies
- [ ] Équilibrage des quantités (`scale_recipe`)

## Phase 5 — Science

- [ ] Packs de science vanilla rendus plus complexes
- [ ] Nouveaux packs (éléments artificiels fabriqués par le joueur)
- [ ] Chaînes manufacturières avancées (inspiration Galloc manufacturing)

## Phase 6 — Space Age *(plus tard)*

- [ ] Extension séparée, après stabilisation des phases 1 à 5

## Ordre de travail conseillé

1. Phase 0 (quelques heures) → 2. Phase 1 → 3. Phase 2 → 4. Phase 3 et 4 en parallèle → 5. Phase 5.
