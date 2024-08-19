# Import libraries
from random_player import RandomPlayer
from conditional_player import ConditionalPlayer
from utility_player import UtilityPlayer
from minimax_player import MinimaxPlayer
#from alpha_beta_player import AlphaBetaPlayer
from human_player import HumanPlayer
from game import Game

# Set the players for the game
# Note: Change these players to test different agents
player1 = HumanPlayer(1)
player2 = MinimaxPlayer(2)
# Loop until the user chooses to exit the program
while True:
    print("Choose your difficulty: ")
    player_choice = input("0 - Random Move (Easy) \n1 - Utility Based (Medium) \n2 - Goal Based (Medium) \n3 - MiniMax (Hard)\nYour choice: ")

    if player_choice == 0:
        player2 = RandomPlayer(2)
    elif player_choice == 1:
        player2 = UtilityPlayer(2)
    elif player_choice == 2:
        player2 = ConditionalPlayer(2)
    elif player_choice == 3:
        player2 = MinimaxPlayer(2)

    # Create a new game using the two players
    game = Game(player1, player2)

    # Play the game to it's conclusion
    game.play()

    # Ask the user if they want to continue
    choice = input("Play another game? Y/N: ")

    # Exit the program if the user doesn't want to play anymore
    if choice != "Y":
        break




