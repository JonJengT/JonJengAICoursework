The puzzle.py file was provided by my professor.

We used different types of searches for our AI to play a block puzzle game.

The main type of search we used was the A star search with two different heuristics.

The first heuristic was the calculate_incorrect() (puzzle.py line 119) function that read a possible game board, and returned the number of blocks that were in an incorrect spot.

The second heuristic was calculate_distance() (puzzle.py line 102) function that read a game board and for each block, it calculated the manhattan distance from where it was supposed to be.