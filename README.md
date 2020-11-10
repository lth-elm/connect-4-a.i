# I.A Puissance 4

## Présentation

Algorithme d'intelligence artificielle pour un puissance 4 sur un plateau **12x6** limité à **42 jetons** par joueur (paramètres modifiables dans le code) reposant sur l'algorithme **Minimax** avec élagage **Alpha-Beta** et des **heuristiques** permettant de s'arrêter à certaines **profondeur** (- de 10sec pour une profondeur 4).

*Algorithme presque totalement optimisé : la seul manière de gagner et d'avoir 2 coups gagnants différents à un tour d'intervalle et lié.*

## Choix des Heuristiques

Le choix de la meilleur position à jouer va dépendre du **score** renvoyés par les différents chemins calculés par l'algorithme du minimax alpha-beta.

Chaque "sous-setup" vaudra un certain **score** qui sera sommé à d'autre sous-setup pour enfin renvoyer un score total basé sur la configuration entière de notre plateau de jeu.

***On peut illustrer nos heuristiques de la manière suivante :***

Le score s’il y a victoire au prochain tour : **+ 100 000** i.e position suivante accessible et ce sera le tour de l'i.a de jouer.

Dans le test terminal : **+ 5 000 000** afin d’être suffisament à l'abri des score à + 100 000 étant donné que la matrice est assez grande.

### Lignes et Diagonales

* ***2 cases :***

*2 emplacements libres sur une suite de 4 sinon **score += 0**.*

**score += 1 000**

Pour ces setups, score = 2 000.

|   |   |       |       |   |   |       |   |   |   |
|---|---|-------|-------|---|---|-------|---|---|---|
|   |   | 1     | 2     | 3 | 4 |       |   |   |   |
| O | O | **X** | **X** | . | . | **X** | O | . | O |
|   |   |       | 1     | 2 | 3 | 4     |   |   |   |


* ***3 cases :***

*1 emplacement libre sur une suite de 4 sinon **score += 0**.*

**score += 10 000**

Pour ces setups, score = 10 000 (la suite de gauche ne mène à rien car il manque 1 emplacement libre au dessus sur la suite de 4).

|   |       |   |       |   |
|---|-------|---|-------|---|
| 3 | **X** |   | .     | 4 |
| 2 | **X** |   | **X** | 3 |
| 1 | **X** |   | **X** | 2 |
|   | O     |   | **X** | 1 |


* ***Atteindre l'emplacement libre (diagonales)***

Atteignable au prochain tour (1 case) : **-0**

2 cases : **-20**

3 cases : **-40** (ajoutés au précédent -20)

4 cases : **-40** (ajoutés au précédent)

...

Pour ce setup, score = 10 000 - 20 - 40 = 9 940

3 à la suite avec emplacement libre sur la suite de 4 => 10 000.

Puis 3 cases avant d'atteindre cet emplacement libre => -20 + (-40). 

|   |       |       |       |   |   |
|---|-------|-------|-------|---|---|
|   |       |       |       | 1 |   |
|   |       |       | **X** | 2 |   |
|   |       | **X** |       | 3 |   |
|   | **X** |       |       | O |   |


* ***A ne pas considérer***

2 moves de 3 cases qui se gagnent en jouant le jeton à la même position ne doivent être compté qu’une fois, en effet, le premier état nous offre moins de solution que le deuxième.

*score += 10 000*

|   |   |   |   |   |   |
|---|---|---|---|---|---|
| X | X | X | . |   |   |
|   |   |   | X |   |   |
|   |   |   | X |   |   |
|   |   |   | X |   |   |

versus

|   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|
| X | X | X | . |   | . |   |
|   |   |   |   |   | X |   |
|   |   |   |   |   | X |   |
|   |   |   |   |   | X |   |

*score += 10 000 + 10 000*

* ***Exploiter une faille chez l'adversaire***

En jouant exprès à une certaine position on peut influencer l’adversaire à jouer une position lui étant favorable : aligner 3 *O*, or si sa profondeur ne va pas plus loin ou qu’il cherche à gagner avant de se défendre alors on pourra exploiter cette faille pour jouer un coup gagnant.

|   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|
| . | . | . | X | X | X | O |
| . | . | . | O | O | X | O |
| . | O | . | X | O | O | X |

|   |   |       |   |   |   |   |
|---|---|-------|---|---|---|---|
| . | . |   .   | X | X | X | O |
| . | . |   .   | O | O | X | O |
| . | O | **X** | X | O | O | X |

|   |   |       |     |     |   |   |
|---|---|-------|-----|-----|---|---|
| . | . |   .   | X   | X   | X | O |
| . | . | **O** | *O* | *O* | X | O |
| . | O |   X   | X   | O   | O | X |

|   |   |       |     |     |     |   |
|---|---|-------|-----|-----|-----|---|
| . | . | **X** | *X* | *X* | *X* | O |
| . | . |   O   | O   | O   | X   | O |
| . | O |   X   | X   | O   | O   | X |
