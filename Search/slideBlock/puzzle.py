# This code was made in part with Google Gemini

import random

class PuzzleGame:
    def __init__(self, init=None):
        # Goal state: 0 (blank) in top-left, then 1-8
        self.goal = [[0, 1, 2], 
                     [3, 4, 5], 
                     [6, 7, 8]]
        
        if init is not None:
            self.board = init
            self.update_blank_pos()
        else:
            self.generate_board()

    def state(self):
        return self.board
    
    def goalState(self):
        return self.goal

    def linearize(self):
        val = ""

        for row in self.board:
            for item in row:
                val += str(item)
        
        return val

    def generate_board(self):
        """Starts with the goal state and scrambles it to ensure solvability."""
        self.board = [row[:] for row in self.goal]
        self.update_blank_pos()
        
        # Scramble the board by making 100 random valid moves
        for _ in range(100):
            possible_moves = self._get_valid_move_coords()
            target_r, target_c = random.choice(possible_moves)
            self._execute_swap(target_r, target_c)

    def update_blank_pos(self):
        """Locates the current coordinates of the blank space (0)."""
        for r in range(3):
            for c in range(3):
                if self.board[r][c] == 0:
                    self.blank_pos = (r, c)
                    return

    def find_number(self, num):
        """Finds the (row, col) of a specific number on the board."""
        for r in range(3):
            for c in range(3):
                if self.board[r][c] == num:
                    return (r, c)
        return None
    
    def get_valid_moves(self):
        r, c = self.blank_pos
        valid_nums = []
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                valid_nums.append(self.board[nr][nc])
        return valid_nums

    def _get_valid_move_coords(self):
        """Returns coordinates of tiles adjacent to the blank space."""
        r, c = self.blank_pos
        valid_coords = []
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                valid_coords.append((nr, nc))
        return valid_coords

    def _execute_swap(self, r, c):
        """Internal helper to swap a coordinate with the blank space."""
        br, bc = self.blank_pos
        self.board[br][bc], self.board[r][c] = self.board[r][c], self.board[br][bc]
        self.blank_pos = (r, c)

    def move_number(self, num):
        """
        The user inputs the number (1-8) they want to slide.
        Returns True if the move was successful, False otherwise.
        """
        if num == 0:
            return False  # Cannot move the blank itself
            
        target_pos = self.find_number(num)
        if target_pos in self._get_valid_move_coords():
            self._execute_swap(target_pos[0], target_pos[1])
            return True
        return False

    def display(self):
        print("\n  Grid:")
        for row in self.board:
            print("  " + " ".join(str(x) if x != 0 else "." for x in row))
        print("-" * 10)

    def is_solved(self):
        return self.board == self.goal

