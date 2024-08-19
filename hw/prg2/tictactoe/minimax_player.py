# Import libraries
from player import Player
from board import Board
from argmax import argmax
import math


# Represents a brute-force minimax agent
class MinimaxPlayer(Player):

    # Gets the next move given the current board state
    def get_next_move(self, board: Board) -> int:
        self.best_move = -1
        best_score = -math.inf
        for space in range(9):
            if board.is_open_space(space):
                board.mark_space(space, self.mark)
                score = self.get_minimax(board, False)
                board.mark_space(space, board.empty)
                if score > best_score:
                    best_score = score
                    self.best_move = int(space)
        return self.best_move

    def get_minimax(self, board: Board, is_maximizing: bool) -> int:
        score = self.get_score(board)

        if score is not None:
            return score

        # asssume the AI is the maximizing player 
        if is_maximizing:
            best_score = -math.inf
            for space in range(9):
                if board.is_open_space(space):
                    board.mark_space(space, self.mark)
                    score = self.get_minimax(board, False)
                    board.mark_space(space, board.empty)
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = math.inf
            for space in range(9):
                if board.is_open_space(space):
                    board.mark_space(space, self.opponent_mark)
                    score = self.get_minimax(board, True)
                    board.mark_space(space, board.empty)
                    best_score = min(score, best_score)
            return best_score


    def get_score(self,board):
        if board.has_win(self.mark):
            return 10
        elif board.has_win(self.opponent_mark):
            return -10
        elif board.is_full():
            return 0
        return None