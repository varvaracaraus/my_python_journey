class Cell:
    """Represents a cell in the Tic-Tac-Toe board."""

    def __init__(self, number: int):
        """
        Initialize a new cell.

        Args:
            number (int): The cell number.
        """
        self.number = number
        self.symbol = ' '

    def is_empty(self) -> bool:
        """Check if the cell is empty."""
        return self.symbol == ' '

    def set_symbol(self, symbol: str) -> bool:
        """
        Set the symbol of the cell if it's empty.

        Args:
            symbol (str): The symbol to set ('X' or 'O').

        Returns:
            bool: True if the symbol was set, False otherwise.
        """
        if self.is_empty():
            self.symbol = symbol
            return True
        else:
            return False
