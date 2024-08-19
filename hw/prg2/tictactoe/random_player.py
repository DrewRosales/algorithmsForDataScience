# Import libraries
from player import Player
from board import Board
import random
import numpy as np


# Represents a tic-tak-toe player using purely random moves
class RandomPlayer(Player):

    # Gets the players next random move
    def get_next_move(self, board: Board) -> int:
        move = -1
        while move == -1 and not board.is_full():
            move = np.random.randint(0, 8)
            if not board.is_open_space(move):
                move = -1
        return move