# Import libraries
from player import Player
from board import Board

from itertools import combinations

# Represents a tic-tac-toe agent that evaluates moves using conditional logic
class ConditionalPlayer(Player):

    # 
    def winning_move(self, board: Board, mark):
        for line in board.lines:
            combs = list(combinations(len(line), 2))
            for comb in combs:
                if board.spaces[comb[0]] == mark and board.spaces[comb[1]] == mark:
                    move = set(line) - set(comb)
                    return move
                else:
                    return -1

    # Returns the next move given the current board state
    def get_next_move(self, board: Board) -> int:
        if board.is_empty():
            # take the center first
            if board.is_open_space(4):
                return 4
        # find a winning move for the AI
        ai_move = winning_move(board, self.mark)

        # if there is a winning move for the AI
        if ai_move != -1 and board.is_open_space(ai_move):
            return ai_move

        # find a winning move for the opponent
        opponent_move = winning_move(board, self.opponent_mark)

        if opponent_move != -1 and board.is_open_space(opponent_move):
            return opponent_move

    def check_diagonals(self, board: Board) -> int:
        if board.is_open_space

