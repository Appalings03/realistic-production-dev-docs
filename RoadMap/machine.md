# Machines et procédés

> Proposition de conception pour Factorio 2.1. Les machines ci-dessous forment une progression possible ; leurs dimensions, coûts, vitesses, catégories et recettes restent à concevoir et équilibrer.

## Principes

- Chaque machine doit correspondre à une étape identifiable de la chaîne : préparation, séparation, raffinage, fabrication ou recherche.
- La complexité vient de chaînes interconnectées et de sous-produits, pas d’une machine différente pour chaque élément.
- Réutiliser une même machine pour plusieurs recettes lorsque le procédé est similaire.
- Les machines nécessitant des fluides doivent avoir des entrées/sorties compréhensibles et permettre une implantation logistique lisible.
- La direction artistique visée est réaliste et industrielle, adaptée à la perspective et à la lisibilité de Factorio. Les silhouettes doivent rester reconnaissables à petite échelle.
- Les gisements et machines statiques peuvent avoir une animation minimale ; les machines de traitement gagneront en lisibilité avec une animation de mouvement, de chaleur ou de flux.

## Chaîne de production suggérée

### 1. Extraction et préparation

| Machine                       | Rôle et procédés                                                                                                                                           |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Foreuse minière              | Extrait les gisements de minerai et les ressources solides ; silhouette de foreuse industrielle, animation de tête de forage.                                |
| Carrière / excavatrice       | Variante visuelle ou machine spécialisée pour les grandes formations rocheuses ; à retenir seulement si elle apporte un gameplay différent de la foreuse. |
| Concasseur à mâchoires      | Réduit les roches et minerais en morceaux ; première étape après extraction.                                                                              |
| Broyeur à boulets            | Produit une poudre plus fine à partir des fragments, avec consommation d’énergie.                                                                          |
| Crible vibrant                | Sépare les matériaux par granulométrie et renvoie les morceaux trop gros au broyage.                                                                       |
| Laveur de minerai             | Utilise de l’eau pour retirer les impuretés et produire des boues ou des rejets.                                                                            |
| Séparateur magnétique       | Récupère les minerais ferreux ou magnétiques à partir d’un mélange.                                                                                     |
| Cellule de flottation         | Sépare des minéraux fins avec eau et réactifs ; peut créer un concentré et des résidus.                                                                 |
| Épaississeur / filtre-presse | Déshydrate les boues et récupère une partie de l’eau de procédé.                                                                                        |

### 2. Raffinage et métallurgie

| Machine                        | Rôle et procédés                                                                            |
| ------------------------------ | ---------------------------------------------------------------------------------------------- |
| Four de grillage / calcination | Chauffe les concentrés avant réduction ou lixiviation.                                       |
| Four de fusion                 | Produit des métaux ou des lingots à partir de minerais préparés et de fondants.            |
| Haut fourneau                  | Produit notamment de la fonte puis de l’acier, avec combustible et carbone.                   |
| Four électrique à arc        | Procédé avancé de fusion/recyclage, consommateur d’électricité.                          |
| Cellule d’électrolyse        | Raffine ou extrait certains métaux à partir d’une solution ou d’un bain fondu.             |
| Fonderie / machine de coulée  | Transforme un métal raffiné en lingots, billettes ou formes intermédiaires.                 |
| Laminoir                       | Produit plaques, tôles, bandes et barres à partir de métal brut ou de billettes.            |
| Presse d’extrusion            | Produit des profilés, tuyaux et barres de section définie.                                   |
| Presse d’emboutissage         | Fabrique des pièces formées à partir de tôles.                                             |
| Centre d’usinage              | Produit engrenages, arbres et composants mécaniques à partir de barres ou de pièces brutes. |

### 3. Chimie, pétrole et séparation

| Machine                                  | Rôle et procédés                                                                                                               |
| ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| Réacteur chimique                       | Synthèses générales : acides, bases, solvants, polymères et précurseurs.                                                     |
| Colonne de distillation                  | Sépare le pétrole brut et d’autres mélanges liquides en fractions. C’est la « tour de distillation » de la liste initiale. |
| Réacteur catalytique                    | Craquage, reformage ou conversion sélective à l’aide d’un catalyseur.                                                         |
| Unité de séparation de l’air          | Produit azote, oxygène et gaz rares à partir d’air comprimé/refroidi ; consomme de l’électricité.                          |
| Cristalliseur / précipitateur           | Récupère un solide depuis une solution, notamment pour certains sels et éléments.                                             |
| Centrifugeuse                            | Sépare des mélanges fins ou des produits nucléaires lorsque la recherche le permet.                                            |
| Unité de lixiviation                    | Dissout sélectivement certains métaux depuis un minerai ou un concentré.                                                       |
| Tour de lavage / séparateur gaz-liquide | Traite les gaz et récupère les produits solubles ou les sous-produits.                                                          |

### 4. Fabrication et recherche

| Machine                     | Rôle et procédés                                                                                                            |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| Assembleuse mécanique      | Assemble les composants de base et remplace progressivement les recettes d’assemblage direct vanilla.                         |
| Assembleuse électronique   | Fabrique les circuits et composants avancés à partir de matériaux raffinés.                                                |
| Laboratoire d’analyse      | Produit des échantillons ou des données de recherche à partir de minerais, matériaux et procédés chimiques.              |
| Installation expérimentale | Fabrique les éléments artificiels et matériaux de fin de partie ; coûteuse, lente et réservée aux technologies tardives. |

## Architecture en plusieurs blocs

Pour une première version, chaque étape peut être une entité Factorio distincte. Les installations « multiblocs » sont une évolution possible, pas un prérequis. Exemples de lignes visuelles/logiques :

- **Raffinerie pétrochimique** : colonne de distillation + réacteur catalytique + stockage de fluides.
- **Complexe de traitement minéral** : concasseur + crible + laveur/flottation + filtre-presse.
- **Aciérie** : haut fourneau + convertisseur/réacteur + coulée continue + laminoir.

N’introduire une mécanique de multibloc que si elle est réalisable et lisible avec les contraintes de Factorio. La version initiale peut représenter chaque poste par une machine autonome reliée par des tapis et des tuyaux.

## Dépendances entre bâtiments

> Décision du 23 oct. 2026 : reporté. Ce sujet sera repris quand l'assemblage des prototypes fonctionne ; la première version utilise des machines autonomes (option A).

Idée : certains bâtiments ne fonctionnent que si d'autres bâtiments sont présents (une raffinerie qui demande une colonne de distillation, un réacteur catalytique et un séparateur pétrole/eau salée). Trois façons de l'implémenter, de la plus simple à la plus coûteuse :

| Option                              | Principe                                                                                                                                    | Avantages                                              | Limites                                                                                                                         |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| A. Dépendance par la chaîne       | Chaque poste est une machine autonome ; elle « dépend » des autres parce que sa recette consomme un fluide ou un solide produit ailleurs | aucun script, lisible, compatible avec tapis et tuyaux | n'impose ni la présence ni la proximité d'un bâtiment                                                                        |
| B. Grand bâtiment unique           | Une seule entité, grande, dont le sprite représente plusieurs unités, avec plusieurs entrées et sorties de fluides                      | aucun script, robuste, aspect de multibloc             | les blocs ne sont pas séparés ni déplaçables                                                                                |
| C. Bâtiment principal + satellites | La machine principale n'est active que si ses satellites sont posés à proximité ; un script de contrôle vérifie leur présence         | vrai multibloc                                         | script `control.lua`, événements de construction et de destruction, fantômes et plans de construction, tests de sauvegarde |

**Proposition** : option A pour la première version (comme annoncé plus haut), option B pour les quelques installations phares (raffinerie, aciérie), option C seulement si le gameplay l'exige. Pour l'option C, vérifier lors de la pose et de la destruction plutôt qu'à chaque tick.

Règles associées :

- Un bâtiment requis est débloqué avant ou avec le bâtiment qui en dépend (même technologie ou prérequis).
- Chaque bâtiment correspond à un item, une entité, une recette et une technologie de déblocage (`tech.md`).
- Le bâtiment requis doit rester utile seul si possible, pour éviter une machine inerte tant que l'autre manque.

Une feuille `buildings` du tableur (nom, niveau, technologie, taille, bâtiments requis, catégorie de recette) pourra alimenter ces fiches. Ne pas figer ses colonnes avant d'avoir conçu les premières recettes.

## Familles et paliers

- **De base** : foreuse, concasseur, crible, laveur, four de fusion, assembleuse mécanique.
- **Avancé** : broyeur, flottation, séparation magnétique, haut fourneau, électrolyse, laminoir, réacteur chimique et distillation.
- **Expérimental** : four électrique à arc, centrifugeuse, réacteur catalytique spécialisé et installation de synthèse artificielle.

Les paliers sont indicatifs et doivent être alignés sur l’accès aux packs de science dans `tech.md`.

## Détails à définir pour chaque prototype

Avant implémentation, documenter pour chaque machine : catégorie de recette, dimensions, consommation électrique/combustible, vitesse, nombre d’emplacements d’entrée/sortie, fluid boxes, animation, portée sonore, recettes disponibles, technologie de déblocage, niveau (basic, advanced ou experimental), bâtiments requis le cas échéant et icône.

## Priorités de conception

1. Fixer une chaîne de démarrage jouable : extraction, concassage, préparation et première fusion.
2. Ajouter la séparation des minerais et ses sous-produits.
3. Ajouter les formes intermédiaires (lingots, tôles, fils, pièces) et les machines qui les produisent.
4. Ajouter pétrole/catalyse et traitement avancé.
5. Réserver les machines expérimentales aux branches tardives.

La liste complète des modèles 3D, animations, icônes et variantes est suivie dans `blender_models_checklist.md`.