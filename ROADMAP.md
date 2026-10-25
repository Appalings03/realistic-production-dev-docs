
# Roadmap — Realistic Production

Mise à jour : 24 oct. 2026 · Cible : Factorio 2.1 · Extension Space Age prévue plus tard

Objectif : des chaînes de production plus réalistes — roche brute → minerais → lingots → pièces → produits finis, avec fluides, broyage, multiblocs et nouveaux packs de science.

## Principes de conception

- **Le monde ne contient que ce qui existe naturellement sur Terre** : roches, minerais, fluides et gaz. Les éléments artificiels sont fabriqués par le joueur et servent à la recherche.
- **Extraction progressive** : au début, certaines roches ne sont pas extractibles. Le raffinage basique d'une roche ne garde que son élément principal et le reste devient des scories. Il n'existe qu'**un seul type de scorie**, inerte, comme des cendres : elle ne sert qu'à faire du ciment, du béton ou d'autres matériaux inertes. Les autres éléments s'obtiennent avec des procédés avancés appliqués à la roche brute. Détails dans `RoadMap/Item.md`.
- **Gisements mixtes** : un patch peut contenir plusieurs minerais ou roches souvent associés dans la réalité (`associated_with`).
- **Bâtiments débloqués par la recherche** : chaque machine est liée à une technologie. Certains bâtiments demanderont d'autres bâtiments pour fonctionner ; ce sujet est reporté jusqu'à ce que l'assemblage des prototypes fonctionne (voir `RoadMap/machine.md`).
- **Noms** : tirets (`-`), jamais de `_`. Tout prototype créé par le mod porte le préfixe `rp-` (à valider) ; les ids du jeu de base réutilisés ne sont pas préfixés.
- **Alliages simplifiés** : acier, bronze, laiton, duralumin, acier inoxydable.
- **Ressources vanilla** : `iron-ore` et `copper-ore` restent comme minerais génériques ; les sept ressources déjà présentes dans le jeu sont réutilisées, pas recréées (voir `RoadMap/Item.md`, section 8).
- **Space Age** : hors périmètre tant que les phases 1 à 5 ne sont pas stables.

## Architecture (5 repos + dev-docs)

| Repo     | Mod                               | Rôle                                                         | Avancement                                              |
| -------- | --------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------- |
| assets   | `realistic_production_assets`   | graphismes, sons                                              | ◐ images de test (`graphics/dev/`), README obsolète |
| utils    | `realistic_production_utils`    | fonctions communes                                            | ◐ `general.lua` fait (6 fonctions), 4 modules vides  |
| ore      | `realistic_production_ore`      | roches, minerais, fluides, éléments, alliages               | ◐ données générées, `data.lua` vide              |
| building | `realistic_production_building` | machines, multiblocs                                          | ▫ vide                                                 |
| core     | `realistic_production_main`     | charge les autres, adapte le vanilla                          | ▫ vide                                                 |
| dev-docs | (documentation)                   | roadmap, TODO, rapport, notes de conception, `proto_table/` | ✓                                                      |

Dépendances : `assets` et `utils` ne dépendent que de `base` ; `ore` et `building` dépendent d'`assets` et d'`utils` ; `main` dépend des quatre autres.

## Phase 0 — Fondations *(presque terminée)*

- [X] Découpage en 5 mods et dépendances, tous en 2.1
- [X] Fonctions générales utils (`normalize_name`, `icon_path`, `icons`, `add_proto`, `copy_proto`, `get_settings`)
- [X] Modèle de données : 88 ressources, 118 éléments, 5 alliages, groupes et sous-groupes, 115 lignes de composition (script Python)
- [X] Niveaux (`level`) et quantités d'alliages remplis
- [X] Nettoyage : faute `buidling`, versions 2.1, `bool = {}` retiré des settings de building
- [X] **Convention de noms décidée** (23 oct.) : tirets et préfixe `rp-`
- [ ] Appliquer la convention : `norm` du générateur (une ligne), régénérer, renommer les settings
- [X] **Scorie unique** décidée (23 oct.)
- [ ] **Définition du `level`** d'un élément et alignement des 5 cas incohérents (à décider)
- [ ] Roches disponibles au départ (proposition dans `Item.md`, section 7)
- [ ] Colonnes `primary` (composition), `tech` (resources) et `vanilla` (elements) dans le tableur et le générateur

## Phase 1 — Ore jouable *(prochaine étape)*

Jalon : le jeu démarre avec le mod ore ; items et fluides apparaissent dans le menu de craft avec leurs noms FR/EN et des icônes de test.

- [ ] `data.lua` d'ore + loader des `*_data.lua`
- [ ] Générateurs `create_item`, `create_fluid`, groupes et sous-groupes
- [ ] Icônes de test teintées par famille (`make_icons`, setting « Dev assets »)
- [ ] Locale générée depuis `name_en` / `name_fr`
- [ ] Settings renommés (`rp-…`) avec leur locale
- [ ] Compositions manquantes (44 ressources sur 88 : bauxite, pentlandite, latérite, apatite, roches…)

## Phase 2 — Ressources et raffinage

Jalon : on peut miner des roches et des minerais et obtenir les éléments de base.

- [ ] `create_resource` (autoplace, densité, nodes purs, gisements mixtes via `associated_with`)
- [ ] Roches verrouillées au départ (technologie de prospection par roche)
- [ ] Raffinage basique : élément principal + scories (`create_recipe`, `ing` / `res`)
- [ ] Gaz de l'air (machine) et fluides (gisements)
- [ ] Alliages simplifiés (acier, bronze, laiton, acier inox, duralumin)
- [ ] Recettes de ciment et de béton à partir des scories
- [ ] Procédés avancés : extraction des éléments secondaires depuis la roche brute
- [ ] Technologies de déblocage par niveau : Basic → Advanced → Experimental

## Phase 3 — Bâtiments

Jalon : chaque étape de la chaîne de démarrage (extraction, concassage, préparation, première fusion) a sa machine, débloquée par une technologie.

- [ ] `create_building`, `create_machine`, catégories de craft, `fluid_boxes`
- [ ] Première version : machines autonomes reliées par tapis et tuyaux
- [ ] Dépendances entre bâtiments : reportées, à reprendre quand l'assemblage des prototypes fonctionne (voir `machine.md`)
- [ ] Multiblocs (ex. raffinerie : tour de distillation, tour catalytique, séparateur pétrole/eau salée)
- [ ] Sprites et animations (assets) ; modèles 3D suivis dans `blender_models_checklist.md`

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

1. Phase 0 : appliquer la convention de noms, trancher la définition des niveaux et les roches de départ, ajouter les colonnes `primary` / `tech` / `vanilla` (quelques heures).
2. Phase 1 : loader, générateurs, icônes de test, locale.
3. Phase 2 : ressources, puis raffinage basique, puis ciment/béton et procédés avancés.
4. Phases 3 et 4 en parallèle.
5. Phase 5.

À chaque phase, lancer le jeu et vérifier le chargement avant de passer à la suivante.
