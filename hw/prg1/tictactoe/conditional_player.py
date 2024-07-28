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
        win_move = self.ai_opponent_winning_move(board)

        # if there is a winning move for the AI
        if win_move  != None and board.is_open_space(win_move):
            return win_move

        non_decisive_move = self.non_decisive_move(board)

        if non_decisive_move != None:
            return non_decisive_move

    # select the winning move dependent on either mark
    def winning_move(self, board: Board, mark):
        for line in board.lines:
            combs = list(combinations(line, 2))
            for comb in combs:
                if board.spaces[comb[0]] == mark and board.spaces[comb[1]] == mark:
                    move = set(line) - set(comb)
                    return next(iter(move))
        return None

    def ai_opponent_winning_move(self, board: Board):
        # check if AI wins first
        #ai_move = None
        #opponent_move = None

        ai_move = self.winning_move(board, self.mark)
        if ai_move != None and board.is_open_space(ai_move):
            return ai_move

        # check if opponent wins second
        opponent_move = self.winning_move(board, self.opponent_mark)
        if opponent_move != None and board.is_open_space(opponent_move):
            return opponent_move
        return None

    # take the corners next
    def take_space(self, board: Board, spaces : list) -> int:
        for space in spaces:
            if board.is_open_space(space):
                print("SPACE:", space)
                return space
        return None

    def take_random_move(self, board: Board) -> int:
        move = -1
        while move == -1 and not board.is_full():
            move = np.random.randint(0, 8)
            if not board.is_open_space(move):
                move = -1
        return move

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

