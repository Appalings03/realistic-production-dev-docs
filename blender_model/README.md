# Blender — synthèse de la playlist de Galdoc

**Playlist :** [Blender Tutorial for Absolute Beginners](https://www.youtube.com/playlist?list=PLV8VrH-TquF7I99ye-BkoDFnK9HHg1cyN)  
**Chaîne :** [Galdoc’s Tutorials](https://www.youtube.com/@galdocstutorials)  
**Périmètre vérifié :** 6 vidéos, de l’épisode 0 à l’épisode 5. La série vise à faire passer un débutant complet aux bases nécessaires pour continuer vers une spécialité 3D.

Ce document résume les idées pratiques et les notions à retenir; ce n’est pas une transcription. Pour les épisodes 0 à 4, la synthèse s’appuie sur les descriptions et les chapitres publiés par Galdoc. Pour l’épisode 5, elle s’appuie aussi sur la transcription disponible.

## Parcours en bref

| Épisode | Sujet | Durée approx. | Résultat attendu |
|---|---|---:|---|
| [0 — Introduction](https://www.youtube.com/watch?v=ksL9PwniqK8) | Objectif du cours et installation | 4 min 27 s | Préparer Blender et comprendre le parcours |
| [1 — Basic Interface](https://www.youtube.com/watch?v=LXZQn-tNMNE) | Interface, navigation, transformations, caméra, lumière et rendu | 30 min | Se repérer et produire un premier rendu |
| [2 — Edit Mode](https://www.youtube.com/watch?v=ryj7qbx5gs4) | Outliner, mode Édition et distinction avec le mode Objet | 18 min | Comprendre où se modifie l’objet et où se modifie son maillage |
| [3 — Edit Mode Tools](https://www.youtube.com/watch?v=mkD-h_HW0ss) | Inset, boucles d’arêtes et extrusion | 19 min | Façonner une géométrie avec les outils de base |
| [4 — Materials](https://www.youtube.com/watch?v=IGP_ixFV4eY) | Matériaux, shaders, textures et UV | 33 min | Donner une apparence à un modèle |
| [5 — Geometry Nodes pt 1](https://www.youtube.com/watch?v=Zt0Q8wfeQZg) | Répétition procédurale de rivets avec des Geometry Nodes | 16 min | Construire un petit réseau de nœuds réutilisable |

## Résumé vidéo par vidéo

### Épisode 0 — Introduction

Galdoc présente l’objectif de la série — partir de zéro et acquérir des bases pour poursuivre ensuite dans la direction de son choix — puis passe par quelques repères et le téléchargement de Blender.

**À retenir :** l’objectif est d’apprendre un flux de travail général et des notions transférables, pas de mémoriser chaque commande avant de commencer à créer.

### Épisode 1 — Interface de base

Tour de l’espace de travail, navigation dans la vue 3D, commandes de transformation les plus courantes, puis aperçu des modificateurs, matériaux, caméra, éclairage et rendu.

**À retenir :** une scène 3D suit déjà un petit cycle complet : organiser et déplacer des objets, définir leur apparence, cadrer avec une caméra, éclairer, puis lancer le rendu. Les modificateurs permettent d’ajouter des changements au modèle sans retravailler immédiatement sa géométrie à la main.

### Épisode 2 — Mode Édition

L’épisode introduit l’Outliner, le Mode Édition et la différence entre le Mode Objet et le Mode Édition. Il revient aussi sur matériaux, éclairage indirect et rendu.

**À retenir :**

- **Mode Objet :** agir sur l’objet entier dans la scène (position, rotation, échelle).
- **Mode Édition :** modifier les éléments du maillage qui compose l’objet.
- **Outliner :** retrouver et organiser les objets de la scène.

Bien choisir le mode évite de transformer tout un objet quand on voulait seulement retoucher sa forme, ou l’inverse.

### Épisode 3 — Outils du Mode Édition

Approfondissement des menus contextuels et commandes modales, avec trois outils de modélisation centraux : **Inset**, boucles d’arêtes (**Edge Loops**) et **Extrude**.

**À retenir :** ces outils créent et réorganisent des faces et des arêtes pour faire évoluer la silhouette d’un maillage. La sélection active et le contexte déterminent souvent le résultat; il faut donc observer ce qui est sélectionné avant d’appliquer une commande.

### Épisode 4 — Matériaux

Après quelques détails de modélisation, Galdoc présente les shaders, les textures et les coordonnées UV, puis montre des générateurs, l’ajout de teinte et des ajustements non uniformes.

**À retenir :**

- Un matériau décrit la façon dont la surface réagit et apparaît; les nœuds servent à combiner et régler ses propriétés.
- Les UV établissent comment une image 2D se projette sur la surface 3D.
- Les générateurs et autres réglages procéduraux permettent de faire varier l’apparence sans peindre chaque détail manuellement.

### Épisode 5 — Geometry Nodes, première partie

Exercice pratique : modéliser une base circulaire (une bride) puis créer une couronne de rivets avec un réseau de Geometry Nodes. Une Mesh Circle à huit sommets fournit les points; **Instance on Points** place un rivet sur chacun; **Join Geometry** réunit les rivets et la base; **Transform Geometry** règle leur position. L’épisode couvre également l’arrondi/lissage, les matériaux, l’éclairage et un défi de mise en pratique.

**À retenir :**

- Un réseau de Geometry Nodes se lit comme un flux : la géométrie entre, passe par des opérations, puis ressort. Si le fil entre l’entrée et la sortie est interrompu, la géométrie ne ressort plus.
- Une instance permet de réutiliser une géométrie à plusieurs endroits en évitant de fabriquer chaque copie séparément.
- Les paramètres exposés sur le groupe de nœuds rendent le résultat réglable depuis le modificateur.
- La géométrie générée peut nécessiter ses propres nœuds de lissage ou d’affectation de matériau.
- Garder séparées la création des rivets et la transformation globale rend le réseau plus facile à réutiliser.
- Attention aux échelles et aux niveaux de subdivision : ils peuvent modifier l’espacement apparent ou faire croître très vite le nombre de polygones.

Cet épisode est explicitement la **première partie** sur les Geometry Nodes : il construit les bases avec un exemple simple et annonce que la suite approfondira le sujet.

## Les notions essentielles à retenir

1. **Une scène est une chaîne d’étapes.** Modèle, matériaux, caméra, lumière et rendu se complètent; régler un seul élément ne remplace pas les autres.
2. **Le Mode Objet et le Mode Édition ont des rôles différents.** Vérifie lequel est actif avant de transformer ou de modéliser.
3. **Commence par les formes et les outils simples.** Inset, boucle d’arêtes et extrusion suffisent déjà à construire beaucoup de volumes de base.
4. **Les modificateurs et les Geometry Nodes sont procéduraux.** Ils ajoutent des transformations réglables et facilitent les changements; garde leurs paramètres compréhensibles.
5. **Les matériaux et les UV relient l’apparence à la géométrie.** Les nœuds définissent le shader, tandis que les UV servent à placer une texture 2D sur un objet 3D.
6. **La pratique consolide les raccourcis.** Refaire de petites scènes et varier quelques paramètres aide davantage que regarder passivement les démonstrations.

## Ordre conseillé pour apprendre

1. Suivre les épisodes dans l’ordre et reproduire les manipulations dans Blender.
2. À chaque épisode, refaire une petite variante sans suivre exactement la démonstration.
3. Pour la modélisation, vérifier régulièrement le mode, le type de sélection et l’échelle de l’objet.
4. Pour les nœuds, suivre visuellement le trajet entrée → opérations → sortie et tester un paramètre à la fois.
5. Enregistrer des versions successives de son fichier pour pouvoir comparer et revenir en arrière.

## Sources

- [Playlist complète sur YouTube](https://www.youtube.com/playlist?list=PLV8VrH-TquF7I99ye-BkoDFnK9HHg1cyN)
- [Épisode 0 — Introduction](https://www.youtube.com/watch?v=ksL9PwniqK8)
- [Épisode 1 — Basic Interface](https://www.youtube.com/watch?v=LXZQn-tNMNE)
- [Épisode 2 — Edit Mode](https://www.youtube.com/watch?v=ryj7qbx5gs4)
- [Épisode 3 — Edit Mode Tools](https://www.youtube.com/watch?v=mkD-h_HW0ss)
- [Épisode 4 — Materials](https://www.youtube.com/watch?v=IGP_ixFV4eY)
- [Épisode 5 — Geometry Nodes pt 1](https://www.youtube.com/watch?v=Zt0Q8wfeQZg)
