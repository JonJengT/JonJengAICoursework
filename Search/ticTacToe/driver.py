from tictactoe import TicTacToe
from typing import Tuple
import argparse


def minimax(game:TicTacToe, player:str) -> Tuple[int,int]:
    
    end, winner = game.isTerminal()
    if end:
        if winner == "O":
            return 1, None
        elif winner == "X":
            return -1, None
        else:
            return 0, None

    if player == "max":
        max_eval = float("-inf")
        max_action = None

        for a in game.actions():
            sub_game = TicTacToe(game.state(), game.toMove())
            sub_game.move(a)

            c_eval, _ = minimax(sub_game, "min")
            if c_eval > max_eval:
                max_action = a
                max_eval = c_eval
        return max_eval, max_action
    
    elif player == "min":
        min_eval = float("inf")
        min_action = None

        for a in game.actions():
            sub_game = TicTacToe(game.state(), game.toMove())
            sub_game.move(a)

            c_eval, _ = minimax(sub_game, "max")
            if c_eval < min_eval:
                min_action = a
                min_eval = c_eval
        return min_eval, min_action


parser = argparse.ArgumentParser("MiniMax Example")
parser.add_argument("-x",  choices=["human","ai"], help="Whether x is controlled by human or AI")
parser.add_argument("-o",  choices=["human","ai"], help="Whether o is controlled by human or AI")
parser.add_argument("--debug", action="store_true", help="Turns on debug mode")

if "__main__":
    args = parser.parse_args()
    game = TicTacToe()
    game.welcome()

    done = False
    while not done:
        if game.toMove() == "O" and args.o == "ai":
            score, action = minimax(game, "max")
            game.move(action)
        elif game.toMove() == "X" and args.x == "ai":
            score, action = minimax(game, "min")
            game.move(action)
        else:
            move = input(f"It is {game.toMove()}'s turn. Please select a move:")
            game.move(int(move))

        done, _ = game.isTerminal()
        game.display()
    
    _, res = game.isTerminal()

    if res == "Tie":
        print("It's a tie.")
    else:
        print(f"{res}'s won!")