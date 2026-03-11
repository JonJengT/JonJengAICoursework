from connect4 import Connect4
from typing import Tuple, List

    #Heuristic Functions


def threeInRow(game:Connect4, player:str) -> Tuple[bool, str]:
    piece = "X" if player == "max" else "O"
    for row in game.board:
        for i in range(0, game.cols-2):
            if row[i] != piece:
                continue
            if all(x == piece for x in row[i:i+3]):
                return True, player
    return False, player

def threeInCol(game:Connect4, player:str) -> Tuple[bool, str]:
    for c_i in range(0, game.cols):
        for r_i in range(0, game.rows-2):
            if game.board[r_i][c_i] == ".":
                continue
            start_piece = game.board[r_i][c_i]
            is_win = True
            for i in range(1, 3):
                is_win = is_win and (start_piece == game.board[r_i+i][c_i])
            
            if is_win:
                return True, player
    
    return False, player

def threeInDiag(game: Connect4, player: str) -> Tuple[bool, str]:
    if player == "max":
        piece = "X" 
    else:
        piece = "O"
        
    for r in range(game.rows - 2):
        for c in range(game.cols - 2):
            if game.board[r][c] == piece and \
               game.board[r+1][c+1] == piece and \
               game.board[r+2][c+2] == piece:
                return True, player
    for r in range(game.rows - 2):
        for c in range(2, game.cols):
            if game.board[r][c] == piece and \
               game.board[r+1][c-1] == piece and \
               game.board[r+2][c-2] == piece:
                return True, player
    return False, player

def getBotMiddle(game:Connect4, player:str) -> Tuple[bool, str]:
    piece = "X" if player == "max" else "O"
    midCol = game.cols//2
    row = game.rows-1
    if game.board[row][midCol] == piece:
        return True, player
    return False, player

def getTwoMiddle(game:Connect4, player:str) -> Tuple[bool, str]:
    piece = "X" if player == "max" else "O"
    midCol = game.cols//2
    row = game.rows-2
    if game.board[row][midCol] == piece:
        return True, player
    return False, player

def getThreeMiddle(game:Connect4, player:str) -> Tuple[bool, str]:
    piece = "X" if player == "max" else "O"
    midCol = game.cols//2
    row = game.rows-3
    if game.board[row][midCol] == piece:
        return True, player
    return False, player

def getFourMiddle(game:Connect4, player:str) -> Tuple[bool, str]:
    piece = "X" if player == "max" else "O"
    midCol = game.cols//2
    row = game.rows-4
    if game.board[row][midCol] == piece:
        return True, player
    return False, player
            

def heuristic(game:Connect4, player:str) -> int:
    heurVal = 0
    botMid, _ = getBotMiddle(game, player)
    twoMid, _ = getTwoMiddle(game, player)
    threeMid, _ = getThreeMiddle(game, player)
    fourMid, _ = getFourMiddle(game, player)

    threeCol, _ = threeInCol(game, player)
    threeRow, _ = threeInRow(game, player)
    threeDiag, _ = threeInDiag(game, player)

    if threeCol:
        if player == "max":
            heurVal += 100
        elif player == "min":
            heurVal += -100
    if threeRow:
        if player == "max":
            heurVal += 100
        elif player == "min":
            heurVal += -100
    if threeDiag:
        if player == "max":
            heurVal += 100
        elif player == "min":
            heurVal += -100
    
    if botMid:
        if player == "max":
            heurVal += 50
        elif player == "min":
            heurVal += -50
    if twoMid:
        if player == "max":
            heurVal += 50
        elif player == "min":
            heurVal += -50
    if threeMid:
        if player == "max":
            heurVal += 50
        elif player == "min":
            heurVal += -50
    if fourMid:
        if player == "max":
            heurVal += 50
        elif player == "min":
            heurVal += -50
            
    
    return heurVal

def minimax(game:Connect4, player:str, alpha:float = float("-inf"), beta:float = float("inf"), max_depth:int = 5, cur_depth:int = 0) -> Tuple[int, int]:
    is_over, winner = game.is_terminal()

    if is_over:
        if winner == "O":
            return 1000, None
        elif winner == "X":
            return -1000, None
        elif winner == "Tie":
            return 0, None
    elif cur_depth == max_depth:
            if player == "max":
                return heuristic(game, "max"), None
            elif player == "min":
                return heuristic(game, "min"), None
    
    if player == "max":
        max_eval = float("-inf")
        max_action = None

        for a in game.actions():
            sub_game = Connect4(game.state(), game.to_move())
            sub_game.make_move(a)

            c_eval, _ = minimax(sub_game, "min", alpha, beta, max_depth, cur_depth+1)

            if c_eval > max_eval:
                max_eval = c_eval
                max_action = a

            alpha = max(alpha, c_eval)
            if beta <= alpha:
                break

        return max_eval, max_action
    
    elif player == "min":
        min_eval = float("inf")
        min_action = None

        for a in game.actions():
            sub_game = Connect4(game.state(), game.to_move())
            sub_game.make_move(a)

            c_eval, _ = minimax(sub_game, "max", alpha, beta,  max_depth, cur_depth+1)
            if c_eval < min_eval:
                min_eval = c_eval
                min_action = a

            beta = min(beta, c_eval)
            if beta <= alpha:
                break

        return min_eval, min_action
    



