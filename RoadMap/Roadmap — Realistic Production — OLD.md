# Roadmap — Realistic Production

Oct 9, 2026 · @Martin

## Vue d'ensemble

L'ordre est : utils, placeholders, ore, building, main, avec un test de chargement dans Factorio à la fin de chaque phase.

Le mod est découpé en quatre mods, du plus bas au plus haut dans la chaîne de dépendances :

1. **assets** : icônes, sons et fonctions utilitaires partagées.
2. **ore** : éléments chimiques, items et fluides, ressources, recettes, technologies.
3. **building** : machines et leurs recettes.
4. **main** : intégration avec le jeu de base, équilibrage, settings globaux.

## Phase 0 : corrections de base

Rien ne se charge tant que ces points ne sont pas corrigés.

- [ ] `globals.lua` : retourner une table à clés (`crustal_rock_deposit = crustal_rock_deposit, ...`) au lieu d'une liste positionnelle
- [ ] Même chemin de `require` partout (`prototypes.globals`) et `prototypes.technologie` devient `prototypes.technology`
- [ ] `info.json` du mod main : `realistic_production_buidling` devient `realistic_production_building`
- [ ] `info.json` du mod ore : corriger le titre et la description, copiés du mod assets
- [ ] Supprimer `settings copy.lua` (le `bool = {}` vide fait planter `data:extend`)
- [ ] Préfixer les settings (`rp-allow-pure-nodes`, `rp-ore-density`) et ajouter leur locale

Test : le jeu démarre sans erreur avec les quatre mods actifs.

## Phase 1 : fonctions utils

Écris seulement les helpers dont ore a besoin tout de suite ; les autres viennent avec les recettes et les technologies.

| Fonction | Rôle | Quand l'écrire |
| --- | --- | --- |
| `normalize_name` | minuscules et `_` à la place des espaces | Maintenant |
| `icon_path` | construit `__realistic_production_assets__/graphics/<nom>.png` | Maintenant |
| `add_prototype` | ignore un item ou fluide déjà déclaré avant `data:extend` | Maintenant |
| `make_item` / `make_fluid` | un seul générateur à la place des trois copies de `item.lua` | Avec les items |
| helpers de recettes et de technologies | catégories, prérequis, ordre | Avec les recettes |

Placement : dans le mod assets, appelés depuis ore et building avec `require("__realistic_production_assets__.prototypes.util")`. Toutes les fonctions sont `local` ou exportées par la table retournée, jamais globales.

## Phase 2 : images placeholder

Une seule icône générique teintée par famille suffit pour tester ; les icônes définitives viennent à la fin.

- Format : PNG de 64 × 64 px (c'est le `icon_size` déjà utilisé dans `item.lua`), fond transparent si ton Paint le permet, sinon fond uni.
- Dossier : `realistic_production_assets/graphics/`.
- Nom : `<nom_normalisé>.png`, par exemple `copper.png`.
- Astuce : dessine un seul `placeholder.png` blanc, puis colorie-le avec la propriété `tint` de `icons` (une couleur par famille). Dix couleurs remplacent plus de cent fichiers.
- Garde le même nom de fichier quand tu remplaces un placeholder par la vraie icône : le code ne change pas.

## Phase 3 : mod ore

Sept étapes, chacune testable seule dans le jeu avant de passer à la suivante.

| Étape | Ce qu'on vérifie |
| --- | --- |
| 1. Registre d'éléments unique (nom, symbole, numéro atomique, item ou fluide) ; les sources référencent des noms | Aucun doublon (cuivre, sodium, lithium…) |
| 2. Groupes et sous-groupes (`item-group`, `item-subgroup`) pour les 10 familles | Les onglets apparaissent dans le menu de craft |
| 3. Items et fluides générés avec `make_item` / `make_fluid` ; gaz et saumures en fluides | Chaque élément est visible avec son icône |
| 4. Entités `resource` avec autoplace, plus les settings de densité et de nodes purs | Les ressources apparaissent dans une nouvelle partie |
| 5. Recettes : extraction, raffinage, séparation | Tout est craftable ou produisible en machine |
| 6. Technologies qui débloquent les recettes | Rien n'est utilisable avant sa technologie |
| 7. Locale EN et FR pour tout ce qui est généré | Aucun nom brut du type `item-name.xxx` |

## Phases 4 et 5 : building puis main

Building se code après ore parce que ses recettes consomment les items d'ore ; main passe en dernier parce qu'il ne fait que relier le reste.

- Building : entités des machines, leurs items, leurs recettes et la technologie qui les débloque.
- Main, `data-final-fixes` : retirer ou remplacer les ressources du jeu de base, ajuster les recettes vanilla qui utilisent le fer, le cuivre ou le charbon.
- Main, settings : réglages globaux (densité, nodes purs) et équilibrage des temps et des quantités.
- Garde un main minimal qui ne fait que déclarer ses dépendances jusqu'à la fin de la phase 3, pour tester le chargement à chaque étape.

## Phase 6 : finitions et tests

Les finitions viennent quand tout le reste charge sans erreur ; la checklist de test se rejoue après chaque phase.

Finitions :

- [ ] Remplacer les placeholders par les vraies icônes
- [ ] Ajouter les éléments manquants (C, S, P, Ba, Ga, In, Cd, Re, Y, Sc)
- [ ] `control.lua` si la génération de minerais l'exige, puis `migrations.lua`
- [ ] Passer la locale FR et EN en revue

Checklist de test :

- [ ] Le jeu démarre sans erreur
- [ ] Les items et fluides sont dans les bons groupes, avec leur icône
- [ ] Les ressources se génèrent dans une nouvelle partie
- [ ] Les recettes fonctionnent et les technologies les débloquent
- [ ] Une ancienne sauvegarde se charge sans casser
