# Arbres technologiques Factorio

Ces deux diagrammes diagrams.net sont conçus pour être modifiés directement, sans script :

- [Arbre technologique du jeu de base](./Arbre_technologique_jeu_de_base.drawio)
- [Arbre technologique Space Age](./Arbre_technologique_Space_Age.drawio)

## Modifier un arbre

Ouvre un fichier `.drawio` dans diagrams.net (draw.io) ou avec l’extension diagrams.net de VS Code.

- Chaque carte représente une technologie : image, nom français, identifiant du prototype et packs de science.
- Chaque flèche va du prérequis vers la technologie qui en dépend.
- Pour ajouter une technologie, duplique une carte proche, modifie son nom et son identifiant, remplace son image si nécessaire, puis relie-la à chacun de ses prérequis.
- Pour retirer une technologie, supprime sa carte. Vérifie aussi les technologies qui en dépendaient et relie-les à leurs nouveaux prérequis, le cas échéant.
- Les technologies cachées ont un contour en pointillés. Les packs de science sont indiqués par les badges colorés et leur légende en haut du diagramme.

L’arbre Space Age contient aussi les technologies du jeu de base et celles des mods officiels Quality, Elevated Rails et Recycler.

## Version et sources

Les identifiants, prérequis et packs de science sont basés sur les prototypes Factorio 2.1.24 et le [changelog officiel](https://github.com/wube/factorio-data/blob/master/changelog.txt). La comparaison des prototypes confirme que l’arbre du jeu de base est identique à celui de 2.0.77.

Pour Space Age, les différences de 2.1 prises en compte comprennent le prérequis « Inserter capacity bonus 7 » pour « Transport belt capacity 2 », le retrait du prérequis militaire de « Health » et la technologie « Stellar discovery: solar system edge ».

Le verrou de voyage vers les plateformes spatiales jusqu’à la découverte d’une première planète est une règle de jeu, pas une dépendance de recherche ; il n’est donc pas représenté par une flèche supplémentaire.

Les icônes sont intégrées aux fichiers, donc elles restent visibles sans accès aux fichiers du jeu. Elles proviennent de l’installation locale Factorio 2.0.77. Trois images ajoutées après cette version n’y étaient pas disponibles ; leurs cartes signalent une icône approchée :

- Recyclage — icône de productivité du recyclage des déchets.
- Déchargement des plateformes d’atterrissage — icône de plateforme spatiale.
- Découverte stellaire : bord du système solaire — icône d’Aquilo.

## Autres schémas

Le fichier [FactorioMod_techtree.drawio](../RoadMap/FactorioMod_techtree.drawio) reste le schéma d’architecture de progression du mod ; il ne représente pas les technologies vanilla.
