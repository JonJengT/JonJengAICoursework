from typing import Tuple
from copy import deepcopy

class TicTacToe:
    def __init__(self, start_state=None, currentTurn="O"):
        if start_state is not None:
            self.board = start_state
        else:
            self.board = [" "," "," "," "," "," "," "," "," "]
        self.turn = currentTurn

    def welcome(self):
        print("Welcome to Tic-Tac-Toe")
        print("To make a move, select a number 0-8")
        print("Numbers correspond to spots as follows")
        print()
        print(" 0 | 1 | 2 ")
        print("---+---+---")
        print(" 3 | 4 | 5 ")
        print("---+---+---")
        print(" 6 | 7 | 8 ")
        print("-------------------")
        print()


    def display(self):
        print("Current Board State")
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("---+---+---")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("---+---+---")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")

    def toMove(self):
        return self.turn
    
    def actions(self):
        return [x for x in range(len(self.board)) if self.board[x] == " "]
    
    def state(self):
        return deepcopy(self.board)

    def move(self, move):
        if move < 0 or move > 8:
            print("ERROR: Moves must be in valid board coordinates")
        elif self.board[move] != " ":
            print(f"ERROR: location {move} is occupied")
        else:
            self.board[move] = self.turn
            if self.turn == "O":
                self.turn = "X"
            else:
                self.turn = "O"

    def isTerminal(self) -> Tuple[bool, str]:
        for i in range(3):
            if self.board[i*3] != " " and self.board[i*3] == self.board[i*3+1] and self.board[i*3+1] == self.board[i*3+2]:
                return True, self.board[i*3]
            if self.board[i] != " " and self.board[i] == self.board[i+3] and self.board[i+3] == self.board[i+6]:
                return True, self.board[i]
        if self.board[0] != " " and self.board[0] == self.board[4] and self.board[4] == self.board[8]:
            return True, self.board[0]
        if self.board[2] != " " and self.board[2] == self.board[4] and self.board[4] == self.board[6]:
            return True, self.board[2]
        if all([x != " " for x in self.board]):
            return True, 'Tie'
        
        return False, " "