from cell import Cell


class Board:
    """Represents the Tic-Tac-Toe game board."""

    def __init__(self):
        """
        Initialize a new board with empty cells.
        """
        self.cells = [Cell(i) for i in range(1, 10)]
        self.winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]

    def display(self) -> None:
        """Display the current state of the board."""
        for i in range(0, 9, 3):
            print("|".join([self.cells[i].symbol, self.cells[i + 1].symbol, self.cells[i + 2].symbol]))
            if i < 6:
                print("-" * 5)

    def check_winner(self, symbol: str) -> bool:
        """
        Check for a winning combination on the board.

        Args:
            symbol (str): The symbol to check ('X' or 'O').

        Returns:
            bool: True if a winning combination is found, False otherwise.
        """
        for combo in self.winning_combinations:
            if all(self.cells[i].symbol == symbol for i in combo):
                return True
        return False
