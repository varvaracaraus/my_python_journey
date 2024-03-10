class Player:
    """Represents a player in the Tic-Tac-Toe game."""

    def __init__(self, name: str):
        """
        Initialize a new player.

        Args:
            name (str): The player's name.
        """
        self.name = name
        self.wins = 0

    def make_move(self) -> int:
        """
        Prompt the player to make a move.

        Returns:
            int: The cell number where the player wants to make a move.
        """
        while True:
            try:
                move = int(input(f"\n{self.name}, enter your move (1-9): "))
                if move < 1 or move > 9:
                    print("Invalid input! Move must be between 1 and 9.")
                    continue
                return move
            except ValueError:
                print("Invalid input! Please enter a number.")
