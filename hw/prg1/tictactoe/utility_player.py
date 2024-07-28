# Import libraries
from board import Board
from conditional_player import ConditionalPlayer
from argmax import argmax
import numpy as np


# Represents a tic-tac-toe agent evaluating moves with a utility function
# Note: this agent inherits from a conditional player
# Note: it uses it's conditional logic for making decisive moves
class UtilityPlayer(ConditionalPlayer):

    # Gets the next move using an utility function
    # and conditional logic for decisive moves
    def get_next_move(self, board: Board) -> int:
        # find a winning move for the AI
        win_move = self.ai_opponent_winning_move(board)

        # if there is a winning move for the AI
        if win_move  != None and board.is_open_space(win_move):
            return win_move

        if board.is_empty():
            return 0

        utility_of_lines = self.get_utility_of_lines(board)
        utility_of_space = self.get_utility_of_spaces(board, utility_of_lines)

        utility_occuppied = self.get_utility_of_spaces(board, [0]*8)
        move = np.argmax(np.array(utility_occuppied) + np.array(utility_of_space))
        return move
        
    def get_line_utility(self, board, line):
        return 3*self.get_mark_count(board, line, self.mark) - self.get_mark_count(board,line, self.opponent_mark)

    def get_utility_of_lines(self, board: Board):
        return [self.get_line_utility(board, line) for line in board.lines]
    
    def get_mark_count(self, board, line, mark):
        count = 0
        for space in line:
            if board.spaces[space] == mark:
                count += 1
        return count


    def is_line_empty(self, board: Board, line) -> int:
        for space in line:
            if not board.is_open_space(space):
                return False
        return True

    def is_line_full(self, board: Board, line) -> int :
        for space in line:
            if board.is_open_space(space):
                return False
        return True

    def get_utility_of_spaces(self, board, utility_of_lines) -> list:
        utilityList = [0] * 9
        if utility_of_lines == [0]*8:
            for space in range(len(board.spaces)):
                if not board.is_open_space(space):
                    utilityList[space] = -99
        else:
            for line, utility in zip(board.lines, utility_of_lines):
                for space in line:
                    utilityList[space] += utility 
        return utilityList
