# Import libraries
from board import Board
from itertools import combinations

# Represents an abstract tic-tac-toe player
class Player:

    # Initialize the player
    def __init__(self, number):
        self.number = number
        self.mark = "X" if number == 1 else "O"
        self.opponent_mark = "O" if number == 1 else "X"

    # Get the player's next move
    # Note: This is an abstract method to be implemented in the player subclass
    def get_next_move(self, board: Board) -> int:
        pass

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
