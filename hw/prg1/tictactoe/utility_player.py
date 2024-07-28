# Import libraries
from board import Board
from conditional_player import ConditionalPlayer
from argmax import argmax


# Represents a tic-tac-toe agent evaluating moves with a utility function
# Note: this agent inherits from a conditional player
# Note: it uses it's conditional logic for making decisive moves
class UtilityPlayer(ConditionalPlayer):

    # Gets the next move using an utility function
    # and conditional logic for decisive moves
    def get_next_move(self, board: Board) -> int:
        print(board.is_empty())
        # enter code here

    def get_utility_of_lines(self, board: Board):
        print("foo")

    def is_line_empty(self, board: Board, line) -> int:
        for space in line:
            print(space)
            if not board.is_open_space(space):
                return False
        return True

    def is_line_full(self, board: Board, line) -> int :
        for space in line:
            if board.is_open_space(space):
                return False
        return True

    def get_utility_of_spaces(board, utility_of_lines) -> int:
        print("foo")
