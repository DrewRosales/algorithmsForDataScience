# Import libraries
from player import Player
from board import Board

from itertools import combinations
import numpy as np

# Represents a tic-tac-toe agent that evaluates moves using conditional logic

# 1. Take winning move for AI
# 2. Deny winnig move for other agent
# 3. Take center if open
# 4. Take diagonals if available
# 5. Take the other entries in order [1, 3, 5, 7]
class ConditionalPlayer(Player):


    # Returns the next move given the current board state
    def get_next_move(self, board: Board) -> int:
        # find a winning move for the AI
        win_move = self.ai_opponent_winning_move(board)

        # if there is a winning move for the AI
        if win_move  != None and board.is_open_space(win_move):
            return win_move

        non_decisive_move = self.non_decisive_move(board)

        if non_decisive_move != None:
            return non_decisive_move


    # take the corners next
    def take_space(self, board: Board, spaces : list) -> int:
        for space in spaces:
            if board.is_open_space(space):
                return space
        return None

    def non_decisive_move(self, board: Board) -> int:
        if board.is_empty():
            return 0

        # take the center if there are no winning moves
        if board.is_open_space(4):
            # take the center first
            if board.is_open_space(4):
                return 4

        # take a corner if there are no winning values for either side
        ai_move = self.take_space(board, [0, 2, 6, 8])
        if ai_move != None:
            return ai_move

        ai_move = self.take_space(board, [1, 3, 5, 7])
        if ai_move != None:
            return ai_move


        return None

