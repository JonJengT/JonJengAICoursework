import argparse
from puzzle import PuzzleGame
from typing import List, Tuple
import copy

def bfs(puzzle:PuzzleGame):
    frontier = [(puzzle.state(), [])]
    #This line creates a queue data structure called the frontier that contains the current board

    visited = set()
    #Create a set type variable of visited states. 
    while frontier:
        s_cur, path = frontier.pop(0)
        #Assigns the first item in the queue to s_cur and path.
        cur_puzzle = PuzzleGame(s_cur)
        #Creates a puzzle object with the current puzzle state

        if cur_puzzle.is_solved(): 
        #Checks if the current puzzle and the solution are the same
            print("Visited:",len(visited))
            #When the current and solution are the same it prints the numbers visited
            return path
            #Returns the path
        
        for move in cur_puzzle.get_valid_moves():
            #iterates through the paths adjacent to the current spot.
            new_puzzle = PuzzleGame(copy.deepcopy(s_cur))
            #Creates a copy of the puzzle
            new_puzzle.move_number(move)
            #makes a move for each of the adjacent spots individually.
            
            state_str = new_puzzle.linearize()
            #Creates a string of the puzzle

            if state_str not in visited:
                #If the string of the current puzzle has not been visited
                visited.add(state_str) 
                #Add it to a list of visited puzzle in the form of a list of strings.
                new_path = path + [move]
                #makes new_path which is a list of the previous moves.
                frontier.append((new_puzzle.state(), new_path))
                #Add the new states to the frontier 
    
    return None


def astar(puzzle:PuzzleGame, heuristic, weight):
    frontier = [(puzzle.state(), 0 , [])]

    visited = set()

    while frontier:
        frontier.sort(key=lambda x: x[1])
        s_cur, c_heur, path = frontier.pop(0)
        
        cur_puzzle = PuzzleGame(s_cur)

        if cur_puzzle.is_solved(): 
            print("Visited:",len(visited))  
            return path
        
        for move in cur_puzzle.get_valid_moves():
            new_puzzle = PuzzleGame(copy.deepcopy(s_cur))
            new_puzzle.move_number(move)
            
            state_str = new_puzzle.linearize()

            if state_str not in visited:
                visited.add(state_str) 
                new_path = path + [move]
                if heuristic == "inc":
                    new_heur = (c_heur + calculate_incorrect(new_puzzle))*weight
                elif heuristic == "dist":
                    new_heur = (c_heur + calculate_distance(new_puzzle))*weight
                frontier.append((new_puzzle.state(), new_heur, new_path))

    return None

def distanceF(x1, y1, item):
    if item == 0:
        x2, y2 = (0,0)
    elif item ==1:
        x2, y2 = (0,1)
    elif item ==2:
        x2, y2 = (0,2)
    elif item == 3:
        x2, y2 = (1,0)
    elif item == 4:
        x2, y2 = (1,1)
    elif item == 5:
        x2, y2 = (1,2)
    elif item == 6:
        x2, y2 = (2,0)
    elif item == 7:
        x2, y2 = (2,1)
    elif item == 8:
        x2, y2 = (2,2)
    else:
        print("error")
    return abs(x2-x1)+abs(y2-y1)

def calculate_distance(game: PuzzleGame):
    board = game.state()
    goalBoard = game.goalState()

    distance = 0

    for i in range(0,9):
        for row in range(0,3):
            for col in range(0,3):
                if i == board[row][col]:
                    #this finds the row and col of the item
                    #we need to compare this to the actual location of the item. 
                    distance += distanceF(row, col, i)
                    
    return distance


def calculate_incorrect(game: PuzzleGame):
    board = game.state()
    goalBoard = game.goalState()
    #I created this function in the puzzle file to make a goal state to compare it with the board.
    """
    self.goal = [[0, 1, 2], 
                 [3, 4, 5], 
                 [6, 7, 8]]
    """
    numIncorrect = 0

    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] != goalBoard[i][j]:
                numIncorrect += 1

    return numIncorrect

    

####################################################################################
# DO NOT EDIT BELOW

parser = argparse.ArgumentParser("HW-1")
parser.add_argument("--search", "-s", required=True, help="Which search to run", choices=["bfs", "astar","human"])
parser.add_argument("--debug", action="store_true", help="Turns on debug mode")
parser.add_argument("--depth", help="Value for iterative deepening depth", type=int, default=5)
parser.add_argument("--heuristic", help="Which heuristic to use for A*", choices=["dist", "inc"])
parser.add_argument("--weight", help="Weight for A* heuristic", type=float, default=1)

if "__main__":
    args = parser.parse_args()

    game = PuzzleGame([[3,5,1],[7,0,6],[4,8,2]])
    #switch to: "game = PuzzleGame()" if you want a randomized map


    print("Try to get the blank space (.) to the top-left and numbers 1-8 in order!")
    game.display()   

    if args.search == "bfs":
        solution = bfs(game)
    elif args.search == "astar":
        solution = astar(game, args.heuristic, args.weight)
    else:
        solution = []

    print("Solution:", solution)

    if solution:
        for move in solution:
            if args.debug:
                game.display()
            game.move_number(move)

        if game.is_solved():
            if args.debug:
                game.display()
            print(f"Congratulations! Your search solved the puzzle in {len(solution)} moves!")
        else:
            print("There are no moves left and the game is not solved.")
    else:
        while not game.is_solved():
            try:
                choice = int(input("Enter number to move (1-8): "))
                if not game.move_number(choice):
                    print("(!) That number isn't next to the blank space.")
            except ValueError:
                print("(!) Please enter a valid number.")
            game.display()