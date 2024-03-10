from game import Game
from player import Player

# Initialize and start the game
player1 = Player("Player 1")
player2 = Player("Player 2")
game = Game(player1, player2)

while True:
    if not game.play_game():
        break
