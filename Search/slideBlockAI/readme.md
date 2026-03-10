The puzzle.py file was provided by my professor.

We used different types of searches for our AI to play a block puzzle game.

The main type of search we used was the A star search with two different heuristics.

The first heuristic was the calculate_incorrect() (puzzle.py line 119) function that read a possible game board, and returned the number of blocks that were in an incorrect spot.

The second heuristic was calculate_distance() (puzzle.py line 102) function that read a game board and for each block, it calculated the manhattan distance from where it was supposed to be.

The default starting board is shown below: The data structure is a List of a List containing integers.

[[0, 1, 2], 
 [3, 4, 5], 
 [6, 7, 8]]

If you want to randomize the starting board, you can change line 152 in hw-1.py to: 
game = PuzzleGame()

To run the game as a human, you can use the following command in the terminal inside the "slideBlockAI" file: 

python3 hw-1.py --search human

To use the breadth first search algorithm to find a solution, you enter:

python3 hw-1.py --search bfs

Then to use the astar algorithm, you can use:

python3 hw-1.py --search astar

If you would like to use the calculate incorrect heuristic I have described in line 7, you can use:

python3 hw-1.py --search astar --heuristic inc

And lastly if you would like to use the manhattan distance heuristic I have described above in line 9:

python3 hw-1.py --search astar --heuristic dist