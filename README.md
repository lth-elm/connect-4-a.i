# A.I Connect 4

## Presentation

Artificial intelligence algorithm for a connect 4 game on a **12x6** board limited to **42 tokens** per player (parameters adjustable in the code) based on the **Minimax** algorithm with **Alpha-Beta** pruning and **heuristics** allowing to stop at a certain **depth** (- 10sec for a depth of 4).

*Algorithm almost perfectly optimized: the only way to win is by having 2 different winning moves at one turn interval and connected.*

## Heuristics selection

Choosing the best position to play will depend on the **score** returned by the different paths calculated by the alpha-beta minimax algorithm.

Each "sub-setup" will be given a certain **score** which will be summed to other sub-setups to finally return a total score based on the entire configuration of our game board.

***Our heuristics can be illustrated as follows :***

The score if next round is assured to be a winner : **+ 100,000** i.e. next position is accessible and it will be the a.i turn to play.

In the final test : **+ 5,000,000** in order to be safe enough from the'+ 100,000' scores since the matrix is relatively large.

### Lines and Diagonals

* ***2 slots :***

*2 spaces on a sequence of 4 otherwise **score += 0**.*

**score += 1,000**

For these setups, score = 2,000.

|   |   |       |       |   |   |       |   |   |   |
|---|---|-------|-------|---|---|-------|---|---|---|
|   |   | 1     | 2     | 3 | 4 |       |   |   |   |
| O | O | **X** | **X** | . | . | **X** | O | . | O |
|   |   |       | 1     | 2 | 3 | 4     |   |   |   |


* ***3 slots :***

*1 space on a sequence of 4 otherwise **score += 0**.*

**score += 10,000**

For these setups, score = 10,000 (the left sequence is useless because there is 1 missing space at the top so we don't sum it with the other valid one).

|   |       |   |       |   |
|---|-------|---|-------|---|
| 3 | **X** |   | .     | 4 |
| 2 | **X** |   | **X** | 3 |
| 1 | **X** |   | **X** | 2 |
|   | O     |   | **X** | 1 |


* ***Reaching the free slot (diagonals)***

Reachable in next round (1 space) : **-0**

2 spaces : **-20**

3 spaces : **-40** (added to the previous -20)

4 spaces : **-40** (added to the previous)

...

For this setup, score = 10,000 - 20 - 40 = 9,940

3 in a row with a free space on a sequence of 4 => 10,000.

Then 3 more cells before reaching this free space => -20 + (-40). 

|   |       |       |       |   |   |
|---|-------|-------|-------|---|---|
|   |       |       |       | 1 |   |
|   |       |       | **X** | 2 |   |
|   |       | **X** |       | 3 |   |
|   | **X** |       |       | O |   |


* ***To be disregarded***

2 moves of 3 filled slots that are won by playing the coin at the same position should be counted only once since the first state offers less solution than the second..

*score += 10,000*

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

*score += 10,000 + 10,000*

* ***Exploiting a weakness in the opponent***

By deliberately playing in a certain position you can trick your opponent into playing a position that is favorable to him : line up 3 *O*, but if his depth does not go any further or if he tries to win before defending himself, then you can exploit this flaw to play a winning move.

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
