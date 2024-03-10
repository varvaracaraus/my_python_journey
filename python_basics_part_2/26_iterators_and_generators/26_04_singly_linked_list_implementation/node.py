from typing import Iterator


class Node:
    """A node in a singly linked list.

    Attributes:
        data: The data stored in the node.
        next: A pointer to the next node in the list, or None.
    """

    def __init__(self, data: int):
        """Initialize the node with data and set next as None."""
        self.data = data
        self.next = None


class LinkedList:
    """A singly linked list."""

    def __init__(self):
        """Initialize the linked list with a head node set to None."""
        self.head = None

    def append(self, data: int) -> None:
        """Add a node with the given data to the end of the list."""
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def get(self, index: int) -> int:
        """Return the data of the node at the given index."""
        current = self.head
        for i in range(index):
            if current is None:
                raise IndexError("Index out of bounds.")
            current = current.next
        if current is None:
            raise IndexError("Index out of bounds.")
        return current.data

    def remove(self, index: int) -> None:
        """Remove the node at the given index from the list."""
        if self.head is None:
            raise IndexError("Index out of bounds.")
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        previous = None
        for i in range(index):
            if current.next is None:
                raise IndexError("Index out of bounds.")
            previous = current
            current = current.next
        if previous is not None and current is not None:
            previous.next = current.next

    def __iter__(self) -> Iterator[int]:
        """Iterate through the nodes in the list."""
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __str__(self) -> str:
        """Return a string representation of the list."""
        data = []
        current = self.head
        while current:
            data.append(str(current.data))
            current = current.next
        return '[' + ' '.join(data) + ']'
