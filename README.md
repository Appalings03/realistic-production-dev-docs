# Dev Docs — Realistic Production

Ce dossier rassemble la documentation de développement du projet Factorio `Realistic Production`.
Il ne contient pas le mod lui-même, mais les notes de conception, le suivi de progression, les analyses de structure, les vérifications et les fichiers de travail utilisés pendant la phase de développement.

## Objectif

Centraliser tout ce qui concerne :

- l'architecture des différents repos du mod ;
- les rapports d'analyse et de validation ;
- la roadmap et les tâches à faire ;
- les conventions de noms et de données ;
- les scripts utiles au développement et à la vérification.

## Structure du dossier

- `README.md` : vue d'ensemble du dossier de dev docs.
- `ROADMAP.md` : plan de développement global du projet, par phases et par repo.
- `TODO.md` : backlog, tâches à faire et points bloquants.
- `RAPPORT.md` : synthèse et analyse technique de l'état actuel des repos.
- `verify.lua` : script de validation rapide des prototypes chargés.
- `jpeg2png.py` : petit utilitaire pour convertir une image JPEG en PNG.
- `RoadMap/` : documents de planification et fichiers de travail liés à la roadmap.
- `proto_table/` : tables de données et références utiles pour la génération de prototypes.

## Contexte du projet

Le projet est réparti en cinq mods Factorio, chacun avec une responsabilité distincte. Les descriptions ci-dessous distinguent le rôle prévu du contenu actuellement présent dans le workspace : plusieurs parties sont encore en construction.

- [`realistic_production_assets`](https://github.com/Appalings03/realistic-production-assets) — Fournit les ressources graphiques et sonores partagées par les autres mods : icônes, images d'entités, sprites et sons. Le dépôt contient actuellement des images de développement dans `graphics/dev/` ; les ressources finales restent à compléter.
- [`realistic_production_utils`](https://github.com/Appalings03/realistic-production-utils) — Regroupe les fonctions communes afin d'éviter de dupliquer les mêmes helpers dans `ore`, `building` et `core`. `utils/general.lua` contient notamment la normalisation des noms, la construction des chemins d'icônes et des helpers pour ajouter ou copier des prototypes et lire les settings. Les autres modules (`ore`, `building`, `assets`, `main`, multiblocs et monde) sont encore des squelettes.
- [`realistic_production_ore`](https://github.com/Appalings03/realistic-production-ore) — Porte les données et, à terme, les prototypes liés aux roches, minerais, fluides, éléments, matériaux et alliages, ainsi que leurs groupes et compositions. Les tables de données sont présentes dans `prototypes/`, mais leur chargement et la génération des prototypes de jeu restent à mettre en place.
- [`realistic_production_building`](https://github.com/Appalings03/realistic-production-building) — Accueillera les machines de production, leurs objets, recettes, technologies, catégories de fabrication et éventuels multiblocs. Les fichiers de prototypes présents sont actuellement vides : cette partie est à développer.
- [`realistic_production_core`](https://github.com/Appalings03/realistic-production-core) — Mod principal destiné à assembler les modules et à intégrer leurs chaînes au jeu de base, notamment en adaptant les recettes, ressources et technologies vanilla. Il déclare les dépendances vers les autres mods, mais sa logique d'intégration est encore à implémenter.

L'objectif fonctionnel est de créer un système de production plus réaliste, avec des chaînes de transformation qui partent des matières brutes pour aller vers les ressources finales, en s'appuyant sur des éléments, des fluides, des recettes et des technologies cohérentes.

## État actuel (à titre de référence)

Les documents de ce dossier montrent que le projet est encore en phase de fondation :

- l'architecture multi-repos est définie ;
- les conventions et les dépendances sont en cours de clarification ;
- les données d'ore sont en cours de préparation ;
- les stubs et erreurs de structure ont été identifiés et certains ont été corrigés ;
- les points bloquants principaux concernent le chargement, le nommage, les settings et les compositions de ressources.

## Utilisation pratique

1. Lire `ROADMAP.md` pour comprendre la vision globale.
2. Consulter `TODO.md` pour la liste des tâches actives / priorisées.
3. Vérifier les dernières conclusions dans `RAPPORT.md`.
4. Lancer `lua verify.lua` depuis ce dossier pour simuler l'enregistrement des définitions de `ore` et afficher les problèmes par prototype. Le script vérifie la structure et les références des données ; il ne remplace pas un lancement dans Factorio.
5. Garder ce dossier comme mémoire technique et historique de développement.

## Priorités de travail

Les priorités les plus importantes actuellement sont :

1. corriger les erreurs de structure et de configuration ;
2. harmoniser les conventions de noms et préfixes ;
3. mettre en place le chargement des données pertinentes dans `ore` ;
4. compléter les compositions et sources des ressources ;
5. développer les modules de bâtiments et d'intégration dans le cœur du mod.

## Note

Ce dossier est un espace de travail de conception et d'analyse. Il doit être maintenu à jour au fil des avancées du projet pour rester utile à la fois comme document de référence et comme outil de coordination.
