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
# 5. Pick a random move if everything else fails
class ConditionalPlayer(Player):


    # Returns the next move given the current board state
    def get_next_move(self, board: Board) -> int:
        # find a winning move for the AI
        ai_move = self.winning_move(board, self.mark)

        # if there is a winning move for the AI
        if ai_move != -1 and board.is_open_space(ai_move):
            return ai_move

        # find a winning move for the opponent
        opponent_move = self.winning_move(board, self.opponent_mark)

        if opponent_move != -1 and board.is_open_space(opponent_move):
            return opponent_move

        # take the center if there are no winning moves
        if board.is_empty() or board.is_open_space(4):
            # take the center first
            if board.is_open_space(4):
                return 4

        # take a corner if there are no winning values for either side
        ai_move = self.take_corner(board)

        if ai_move != -1 and board.is_open_space(ai_move):
            return ai_move

        # take a random move if other conditions fail
        ai_move = self.take_random_move(board)
        return ai_move

    # select the winning move dependent on either mark
    def winning_move(self, board: Board, mark):
        for line in board.lines:
            combs = list(combinations(line, 2))
            for comb in combs:
                if board.spaces[comb[0]] == mark and board.spaces[comb[1]] == mark:
                    move = set(line) - set(comb)
                    return next(iter(move))
        return -1

    # take the corners next
    def take_corner(self, board: Board) -> int:
        for corner_space in [0, 2, 6, 9]:
            if board.is_open_space(corner_space):
                return corner_space
            else:
                return -1

    def take_random_move(self, board: Board) -> int:
        move = -1
        while move == -1 and not board.is_full():
            move = np.random.randint(0, 8)
            print(move)
            if not board.is_open_space(move):
                move = -1
        return move
