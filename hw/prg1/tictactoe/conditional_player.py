# Import libraries
from player import Player
from board import Board

from itertools import combinations
import numpy as np

# Represents a tic-tac-toe agent that evaluates moves using conditional logic
class ConditionalPlayer(Player):

    # 
    def winning_move(self, board: Board, mark):
        for line in board.lines:
            combs = list(combinations(line, 2))
            print(board.lines)
            for comb in combs:
                if board.spaces[comb[0]] == mark and board.spaces[comb[1]] == mark:
                    move = set(line) - set(comb)
                    return next(iter(move))
        return -1

    # Returns the next move given the current board state
    def get_next_move(self, board: Board) -> int:
        # find a winning move for the AI
        ai_move = self.winning_move(board, self.mark)

        # if there is a winning move for the AI
        if ai_move != -1 and board.is_open_space(ai_move):
            return ai_move

        # find a winning move for the opponent
        opponent_move = self.winning_move(board, self.opponent_mark)

        print("opponent move:", opponent_move)
        if opponent_move != -1 and board.is_open_space(opponent_move):
            return opponent_move

        if board.is_empty() or board.is_open_space(4):
            # take the center first
            if board.is_open_space(4):
                return 4

        ai_move = self.take_corner(board)

        if ai_move != -1 and board.is_open_space(ai_move):
            return ai_move

        ai_move = self.take_random_move(board)

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
            if not board.is_open_space(move):
                move = -1
        return move
