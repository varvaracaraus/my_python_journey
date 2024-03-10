class Stack:
    """
    A simple implementation of a stack data structure.

    Attributes:
        items (list): The list to store stack items.
    """

    def __init__(self) -> None:
        """Initializes an empty stack."""
        self.items = []

    def push(self, item: any) -> None:
        """
        Adds an item to the top of the stack.

        Args:
            item (any): The item to be added to the stack.
        """
        self.items.append(item)

    def pop(self) -> any:
        """
        Removes and returns the item from the top of the stack.

        Returns:
            The item at the top of the stack or None if the stack is empty.
        """
        return self.items.pop() if not self.is_empty() else None

    def is_empty(self) -> bool:
        """
        Checks if the stack is empty.

        Returns:
            True if the stack is empty, False otherwise.
        """
        return len(self.items) == 0
