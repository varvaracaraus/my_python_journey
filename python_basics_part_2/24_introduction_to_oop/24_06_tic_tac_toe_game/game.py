from board import Board
from player import Player


class Game:
    """Represents a game of Tic-Tac-Toe."""

    def __init__(self, player1: Player, player2: Player):
        """
        Initialize a new game.

        Args:
            player1 (Player): The first player.
            player2 (Player): The second player.
        """
        self.board = Board()
        self.players = [player1, player2]

    def play_turn(self, player: Player) -> bool:
        """
        Execute a turn for a player.

        Args:
            player (Player): The player who is making the move.

        Returns:
            bool: True if the player won, False otherwise.
        """
        while True:
            move = player.make_move()
            symbol = 'X' if player == self.players[0] else 'O'
            if self.board.cells[move - 1].set_symbol(symbol):
                self.board.display()
                if self.board.check_winner(symbol):
                    return True
                break
            else:
                print("Cell is already occupied. Please choose another cell.")
        return False

    def play_game(self) -> bool:
        """
        Play a complete game of Tic-Tac-Toe.

        Returns:
            bool: True if players want to play again, False otherwise.
        """
        self.board = Board()
        self.board.display()
        for i in range(9):
            if self.play_turn(self.players[i % 2]):
                print(f"\n{self.players[i % 2].name} wins!")
                self.players[i % 2].wins += 1
                break
        else:
            print("\nIt's a draw!")
        print("Score:")
        for player in self.players:
            print(f"{player.name}: {player.wins}")
        return input("\nDo you want to play again? (yes/no): ").lower() == 'yes'
