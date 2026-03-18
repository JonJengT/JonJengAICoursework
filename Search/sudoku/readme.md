Sudoku is described as a constraint satisfaction problem. 

For sudoku, we will be using the backtracking algorithm. The backtracking algorithm tries a possible entry, and keeps on going until it finds an inconsistency. In sudoku, this inconsistency could mean, maybe two 5's in a row when there should only be one 5 in each row.

We have also added a minimum values heuristic to decrease the search time. 

In order to run the sudoku, you can change the puzzle in sudoku.py as needed, and run, inside of the sudoku file:

python3 sudoku.py

The current puzzle is set to (sudoku.py (Lines 3-11)):

puzzle = [[0, 0, 9, 5, 8, 6, 0, 0, 0],
          [0, 0, 0, 0, 2, 0, 0, 0, 0],
          [4, 0, 0, 0, 0, 0, 6, 8, 3],
          [9, 0, 0, 6, 5, 0, 0, 3, 2],
          [0, 6, 0, 7, 0, 0, 0, 9, 8],
          [0, 3, 0, 2, 0, 0, 7, 0, 4],
          [0, 0, 3, 0, 0, 0, 0, 0, 0],
          [6, 2, 0, 0, 1, 5, 0, 4, 0],
          [0, 0, 0, 4, 0, 0, 0, 5, 0]]

The output also prints the number of searches visited after printing the solution.