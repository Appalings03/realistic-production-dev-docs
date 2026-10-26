# Checklist des modèles Blender et des assets graphiques

> Liste de production artistique pour Realistic Production. Toutes les cases sont initialement décochées. « Modèle » signifie ici un modèle 3D Blender destiné à produire les sprites Factorio ; les icônes d’items sont des images 2D rendues ou composées séparément et ne nécessitent pas nécessairement un modèle Blender dédié.

## Conventions visuelles à fixer

- [ ] Définir une palette industrielle cohérente, réaliste mais contrastée à l’échelle du jeu.
- [ ] Définir l’angle de caméra, l’échelle, le cadrage, l’éclairage et les ombres pour tous les rendus.
- [ ] Définir la résolution, le fond transparent, la marge et le format des icônes Factorio.
- [ ] Définir la convention de fichiers et l’arborescence des sources Blender, rendus, icônes et animations.
- [ ] Créer une scène Blender réutilisable avec caméra, éclairage, matériau de référence et réglages de rendu.
- [ ] Créer une planche de comparaison pour vérifier lisibilité et cohérence des icônes à taille réelle.

## Modèles 3D des bâtiments et machines

Créer un modèle distinct seulement lorsque la silhouette ou l’animation représente une fonction de jeu différente. Les niveaux de technologie peuvent réutiliser un modèle avec des détails, couleurs ou modules améliorés.

### Extraction et préparation

- [ ] Foreuse minière de base.
- [ ] Foreuse minière avancée (variante renforcée/électrique).
- [ ] Carrière ou excavatrice, si cette machine reste distincte de la foreuse.
- [ ] Concasseur à mâchoires.
- [ ] Broyeur à boulets.
- [ ] Crible vibrant.
- [ ] Laveur de minerai.
- [ ] Séparateur magnétique.
- [ ] Cellule de flottation (modèle de base).
- [ ] Colonne de flottation (variante industrielle si utile).
- [ ] Épaississeur de boues.
- [ ] Filtre-presse.

### Raffinage et métallurgie

- [ ] Four de grillage/calcination.
- [ ] Four de fusion de base.
- [ ] Haut fourneau.
- [ ] Four électrique à arc.
- [ ] Cellule d’électrolyse.
- [ ] Fonderie et machine de coulée.
- [ ] Laminoir.
- [ ] Presse d’extrusion.
- [ ] Presse d’emboutissage.
- [ ] Centre d’usinage.

### Chimie, pétrole et séparation

- [ ] Réacteur chimique de base.
- [ ] Colonne de distillation pétrolière.
- [ ] Réacteur catalytique.
- [ ] Unité de séparation de l’air.
- [ ] Cristalliseur/précipitateur.
- [ ] Centrifugeuse.
- [ ] Unité de lixiviation.
- [ ] Tour de lavage gaz-liquide.

### Fabrication et recherche

- [ ] Assembleuse mécanique de base.
- [ ] Assembleuse mécanique avancée (variante visuelle, si le palier est distinct).
- [ ] Assembleuse électronique.
- [ ] Laboratoire d’analyse minérale.
- [ ] Installation de synthèse expérimentale.

### Éléments génériques à réutiliser dans les bâtiments

- [ ] Silos et trémies de minerai.
- [ ] Réservoirs de fluides de plusieurs tailles.
- [ ] Tuyauterie, vannes et pompes décoratives réutilisables.
- [ ] Convoyeurs, goulottes et systèmes d’alimentation intégrés aux machines.
- [ ] Cheminées, conduits d’évacuation et filtres de fumées.
- [ ] Armoires électriques, câbles, moteurs et panneaux de commande.
- [ ] Modules de machine de niveau supérieur (moteur, filtre, isolation, blindage).

## Animations et variantes de sprites

- [ ] Foreuse : tête en mouvement, rotation ou percussion.
- [ ] Concasseur : mâchoires mobiles et fragments en entrée/sortie.
- [ ] Broyeur : rotation du tambour.
- [ ] Crible : vibration et flux de matière.
- [ ] Laveur/flottation : mouvement de l’eau, bulles ou agitation.
- [ ] Fours : porte, braises/chaleur et lueur de fonctionnement.
- [ ] Électrolyse : lueur électrique ou bulles en fonctionnement.
- [ ] Coulée : métal liquide ou métal incandescent, sans surcharger le sprite.
- [ ] Laminoir/presse : rouleaux ou piston en mouvement.
- [ ] Réacteur chimique : agitateur, tuyaux et indicateur d’activité.
- [ ] Distillation : animation de vapeur/flux et variantes de fonctionnement.
- [ ] Séparation de l’air : ventilateur/compresseur et indicateur de procédé.
- [ ] Laboratoires : animation sobre d’analyse et variantes au repos/en fonctionnement.
- [ ] Préparer les états repos, actif, désactivé et/ou en panne si l’entité en a besoin.
- [ ] Préparer les directions/orientations requises par chaque prototype Factorio.
- [ ] Vérifier l’alignement des ombres et de la grille de collision sur les prototypes.

## Icônes d’items : roches, minerais et ressources

Une icône dédiée par ressource est préférable. Les icônes d’items peuvent être des rendus Blender ou des illustrations 2D cohérentes ; les icônes de ressources déposées sur la carte sont des sprites distincts, pas des modèles 3D Factorio.

### Roches (19)

- [ ] Granit
- [ ] Basalte
- [ ] Gabbro
- [ ] Diorite
- [ ] Rhyolite
- [ ] Andésite
- [ ] Péridotite
- [ ] Kimberlite
- [ ] Calcaire
- [ ] Dolomie
- [ ] Grès
- [ ] Argile
- [ ] Schiste
- [ ] Craie
- [ ] Marbre
- [ ] Gneiss
- [ ] Quartzite
- [ ] Ardoise
- [ ] Pierre vanilla

### Minerais et minéraux (62)

- [ ] Minerai de fer vanilla
- [ ] Minerai de cuivre vanilla
- [ ] Hématite
- [ ] Magnétite
- [ ] Goethite
- [ ] Sidérite
- [ ] Bauxite
- [ ] Chalcopyrite
- [ ] Bornite
- [ ] Chalcocite
- [ ] Malachite
- [ ] Galène
- [ ] Sphalérite
- [ ] Cassitérite
- [ ] Wolframite
- [ ] Scheelite
- [ ] Molybdénite
- [ ] Pentlandite
- [ ] Latérite
- [ ] Cobaltite
- [ ] Chromite
- [ ] Pyrolusite
- [ ] Ilménite
- [ ] Rutile
- [ ] Or natif
- [ ] Argent natif
- [ ] Platine natif
- [ ] Sperrylite
- [ ] Cinabre
- [ ] Stibine
- [ ] Spodumène
- [ ] Lépidolite
- [ ] Béryl
- [ ] Coltan
- [ ] Zircon
- [ ] Monazite
- [ ] Bastnäsite
- [ ] Uraninite
- [ ] Carnotite
- [ ] Thorianite
- [ ] Minerai d’uranium vanilla
- [ ] Halite
- [ ] Sylvite
- [ ] Carnallite
- [ ] Gypse
- [ ] Anhydrite
- [ ] Borax
- [ ] Colémanite
- [ ] Trona
- [ ] Nitratine
- [ ] Soufre natif
- [ ] Pyrite
- [ ] Apatite
- [ ] Fluorite
- [ ] Graphite
- [ ] Diamant
- [ ] Charbon vanilla
- [ ] Lignite
- [ ] Anthracite
- [ ] Tourbe
- [ ] Sables bitumineux
- [ ] Schistes bitumineux

### Fluides et gaz naturels (7)

- [ ] Pétrole brut
- [ ] Eau
- [ ] Eau de mer
- [ ] Saumure de lithium
- [ ] Eau géothermale
- [ ] Gaz naturel
- [ ] Air comprimé/séparé

### Gisements sur la carte

- [ ] Sprite de gisement pour chaque minerai distinct (reprendre les 62 entrées ci-dessus).
- [ ] Variantes de couleurs et de densité pour chaque ressource effectivement présente sur la carte.
- [ ] Variante de roche hôte pour les gisements mixtes.
- [ ] Sprite de ressource épuisée ou d’emplacement de forage si le gameplay en a besoin.
- [ ] Vérifier que les gisements restent identifiables sans se fier uniquement à la couleur.

## Icônes d’éléments (118)

Prévoir une icône par élément utilisé comme item ou fluide. Convention suggérée : symbole chimique bien lisible, code couleur par famille, texture/formes discrètes ; les variantes solide/gaz/liquide doivent rester différenciables. Les éléments rares ou artificiels peuvent partager un gabarit, mais chaque symbole reste unique.

### Période 1

- [ ] H — Hydrogène
- [ ] He — Hélium

### Période 2

- [ ] Li — Lithium
- [ ] Be — Béryllium
- [ ] B — Bore
- [ ] C — Carbone
- [ ] N — Azote
- [ ] O — Oxygène
- [ ] F — Fluor
- [ ] Ne — Néon

### Période 3

- [ ] Na — Sodium
- [ ] Mg — Magnésium
- [ ] Al — Aluminium
- [ ] Si — Silicium
- [ ] P — Phosphore
- [ ] S — Soufre
- [ ] Cl — Chlore
- [ ] Ar — Argon

### Période 4

- [ ] K — Potassium
- [ ] Ca — Calcium
- [ ] Sc — Scandium
- [ ] Ti — Titane
- [ ] V — Vanadium
- [ ] Cr — Chrome
- [ ] Mn — Manganèse
- [ ] Fe — Fer
- [ ] Co — Cobalt
- [ ] Ni — Nickel
- [ ] Cu — Cuivre
- [ ] Zn — Zinc
- [ ] Ga — Gallium
- [ ] Ge — Germanium
- [ ] As — Arsenic
- [ ] Se — Sélénium
- [ ] Br — Brome
- [ ] Kr — Krypton

### Période 5

- [ ] Rb — Rubidium
- [ ] Sr — Strontium
- [ ] Y — Yttrium
- [ ] Zr — Zirconium
- [ ] Nb — Niobium
- [ ] Mo — Molybdène
- [ ] Tc — Technétium
- [ ] Ru — Ruthénium
- [ ] Rh — Rhodium
- [ ] Pd — Palladium
- [ ] Ag — Argent
- [ ] Cd — Cadmium
- [ ] In — Indium
- [ ] Sn — Étain
- [ ] Sb — Antimoine
- [ ] Te — Tellure
- [ ] I — Iode
- [ ] Xe — Xénon

### Période 6

- [ ] Cs — Césium
- [ ] Ba — Baryum
- [ ] La — Lanthane
- [ ] Ce — Cérium
- [ ] Pr — Praséodyme
- [ ] Nd — Néodyme
- [ ] Pm — Prométhium
- [ ] Sm — Samarium
- [ ] Eu — Europium
- [ ] Gd — Gadolinium
- [ ] Tb — Terbium
- [ ] Dy — Dysprosium
- [ ] Ho — Holmium
- [ ] Er — Erbium
- [ ] Tm — Thulium
- [ ] Yb — Ytterbium
- [ ] Lu — Lutécium
- [ ] Hf — Hafnium
- [ ] Ta — Tantale
- [ ] W — Tungstène
- [ ] Re — Rhénium
- [ ] Os — Osmium
- [ ] Ir — Iridium
- [ ] Pt — Platine
- [ ] Au — Or
- [ ] Hg — Mercure
- [ ] Tl — Thallium
- [ ] Pb — Plomb
- [ ] Bi — Bismuth
- [ ] Po — Polonium
- [ ] At — Astate
- [ ] Rn — Radon

### Période 7

- [ ] Fr — Francium
- [ ] Ra — Radium
- [ ] Ac — Actinium
- [ ] Th — Thorium
- [ ] Pa — Protactinium
- [ ] U — Uranium
- [ ] Np — Neptunium
- [ ] Pu — Plutonium
- [ ] Am — Américium
- [ ] Cm — Curium
- [ ] Bk — Berkélium
- [ ] Cf — Californium
- [ ] Es — Einsteinium
- [ ] Fm — Fermium
- [ ] Md — Mendélévium
- [ ] No — Nobélium
- [ ] Lr — Lawrencium
- [ ] Rf — Rutherfordium
- [ ] Db — Dubnium
- [ ] Sg — Seaborgium
- [ ] Bh — Bohrium
- [ ] Hs — Hassium
- [ ] Mt — Meitnérium
- [ ] Ds — Darmstadtium
- [ ] Rg — Roentgenium
- [ ] Cn — Copernicium
- [ ] Nh — Nihonium
- [ ] Fl — Flérovium
- [ ] Mc — Moscovium
- [ ] Lv — Livermorium
- [ ] Ts — Tennesse
- [ ] Og — Oganesson

## Icônes d’alliages et matériaux (20)

Créer des icônes pour chaque alliage ci-dessous si l’alliage est conservé dans le contenu final. Les 5 premiers sont dans les données actuelles ; les autres viennent de la liste de propositions.

- [ ] Acier
- [ ] Bronze
- [ ] Laiton
- [ ] Duralumin
- [ ] Acier inoxydable
- [ ] Or blanc
- [ ] Amalgame dentaire
- [ ] Magnalium
- [ ] Stellite
- [ ] Invar
- [ ] Monel
- [ ] Nichrome
- [ ] Cupronickel
- [ ] Étain de potier (pewter)
- [ ] Zamak
- [ ] Bêta-titane
- [ ] Hastelloy
- [ ] Inconel
- [ ] Tombac
- [ ] Électrum

## Icônes des produits intermédiaires

- [ ] Lingot métallique générique et variantes de familles visuellement distinctes.
- [ ] Minerai concassé.
- [ ] Concentré de minerai.
- [ ] Poudre métallique.
- [ ] Plaque/tôle.
- [ ] Barre et profilé.
- [ ] Fil et câble.
- [ ] Tuyau.
- [ ] Engrenage, axe, ressort et rivet.
- [ ] Brique réfractaire, verre et céramique.
- [ ] Électrode et composant électronique.
- [ ] Catalyseur et support de catalyseur.
- [ ] Échantillon minéral et échantillon d’alliage.
- [ ] Packs de science ajoutés par le mod, si les propositions de `tech.md` sont retenues.

## Contrôle final des assets

- [ ] Toutes les icônes sont lisibles à la taille d’inventaire Factorio.
- [ ] Les formes de roches, minerais, lingots et composants ne se confondent pas.
- [ ] Les variantes reposent sur une distinction de forme ou de symbole, pas uniquement sur la couleur.
- [ ] Les icônes solides et fluides suivent une convention cohérente.
- [ ] Les sprites de machines sont alignés sur leurs dimensions et boîtes de collision.
- [ ] Les animations ne masquent pas les indicateurs de statut ni les objets transportés.
- [ ] Les sources Blender sont nommées et rangées avec leurs fichiers de rendu.
- [ ] Les exports finaux sont vérifiés en jeu avec les recettes et prototypes réellement retenus.
