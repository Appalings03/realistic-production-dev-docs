# Cheat sheet — raccourcis Blender

Fiche rapide pour accompagner la playlist de [Galdoc](https://www.youtube.com/playlist?list=PLV8VrH-TquF7I99ye-BkoDFnK9HHg1cyN). Elle reprend les raccourcis utiles pour l’interface, les transformations, la modélisation de base et les nœuds.

> Référence : keymap Blender par défaut, clavier/souris. Les raccourcis peuvent changer si le keymap a été personnalisé. La plupart des commandes s’appliquent à la zone sous le pointeur; place le curseur dans la vue 3D avant de taper.

## Vue 3D : se déplacer

| Touche / geste | Action |
|---|---|
| Bouton du milieu + glisser | Orbiter autour de la scène |
| Maj + bouton du milieu + glisser | Déplacer la vue sans changer son angle |
| Molette | Zoomer / dézoomer |
| Pavé num. 1 / 3 / 7 | Vues face / côté / dessus |
| Ctrl + pavé num. 1 / 3 / 7 | Vue opposée : arrière / autre côté / dessous |
| Pavé num. . | Centrer la vue sur la sélection |
| Home | Faire cadrer tous les objets visibles |

## Sélection et modes

| Touche | Action |
|---|---|
| Tab | Basculer entre Mode Objet et Mode Édition |
| 1 / 2 / 3 *(rangée du haut)* | En Mode Édition : sélectionner sommets / arêtes / faces |
| A | Tout sélectionner dans la zone active |
| Alt + A | Tout désélectionner |
| Maj + clic sur 1 / 2 / 3 | Activer plusieurs modes de sélection à la fois |
| Maj + A | Ouvrir le menu Ajouter dans la vue 3D ou l’éditeur de nœuds |
| F3 | Rechercher une commande par son nom |

**Repère :** en Mode Objet, on transforme l’objet entier. En Mode Édition, on transforme la géométrie qui le compose.

## Transformations

| Touche | Action |
|---|---|
| G | Déplacer (*Grab*) |
| R | Faire pivoter (*Rotate*) |
| S | Redimensionner (*Scale*) |
| X / Y / Z après G, R ou S | Limiter l’opération à cet axe |
| Taper un nombre après la commande | Donner une valeur précise, p. ex. G puis X puis 2 |
| Entrée / clic gauche | Valider l’opération en cours |
| Échap / clic droit | Annuler l’opération en cours |
| Maj + D | Dupliquer puis déplacer la sélection |
| X ou Suppr | Supprimer la sélection |
| Ctrl + Z | Annuler la dernière action |
| Ctrl + Maj + Z | Rétablir l’action annulée |

## Modélisation en Mode Édition

| Touche | Action |
|---|---|
| E | Extruder la sélection et créer de la géométrie |
| I | Créer un inset à l’intérieur des faces sélectionnées |
| Ctrl + R | Insérer une boucle d’arêtes (*Loop Cut*) |
| Ctrl + B | Biseauter les arêtes sélectionnées |
| F3 puis nom de l’outil | Retrouver une commande sans chercher dans les menus |

Les outils interactifs restent « modaux » jusqu’à validation : bouge la souris ou entre une valeur, puis valide. Échap annule. Pour Inset, Ctrl règle la profondeur pendant l’opération; pour le biseau, la molette règle le nombre de segments.

## Rendu

| Touche | Action |
|---|---|
| F12 | Lancer le rendu de l’image active |
| F11 | Afficher / masquer la fenêtre de rendu |

## Nœuds : raccourcis montrés dans l’épisode 5

Les gestes suivants sont fournis par l’extension **Node Wrangler**. Il faut qu’elle soit installée et activée.

| Geste | Action |
|---|---|
| Maj + D | Dupliquer le nœud sélectionné |
| Ctrl + Maj + clic gauche sur un nœud | Afficher un aperçu de ce nœud |
| Maj + clic droit + glisser sur un lien | Couper le lien |
| Alt + clic droit + glisser | Relier deux prises de nœuds |
| Ctrl + Maj + clic droit + glisser entre deux liens | Insérer un nœud intermédiaire adapté, quand l’extension trouve une opération pertinente |
| Ctrl + X sur un nœud | Supprimer le nœud en essayant de reconnecter le flux |

## Si une touche ne fait rien

1. Mets le pointeur dans la bonne zone (vue 3D, éditeur de nœuds, etc.).
2. Vérifie le mode actif : Mode Objet ou Mode Édition.
3. Vérifie que le keymap Blender par défaut est sélectionné dans les préférences.
4. Utilise F3 pour rechercher la commande et lire son raccourci dans le menu.

## Sources

- [Keymap par défaut — Manuel Blender](https://docs.blender.org/manual/en/latest/interface/keymap/blender_default.html)
- [Modes Objet et Édition — Manuel Blender](https://docs.blender.org/manual/en/latest/editors/3dview/modes.html)
- [Déplacement, rotation et échelle — Manuel Blender](https://docs.blender.org/manual/en/latest/modeling/meshes/editing/mesh/transform/basic.html)
- [Inset Faces — Manuel Blender](https://docs.blender.org/manual/en/5.0/modeling/meshes/editing/face/inset_faces.html)
- [Loop Cut and Slide — Manuel Blender](https://docs.blender.org/manual/en/5.0/modeling/meshes/editing/edge/loopcut_slide.html)
- [Bevel — Manuel Blender](https://docs.blender.org/manual/en/5.2/modeling/meshes/editing/edge/bevel.html)
- [Épisode 5 — Geometry Nodes pt 1, Galdoc](https://www.youtube.com/watch?v=Zt0Q8wfeQZg)
