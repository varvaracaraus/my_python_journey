class SquaresIterator:
    """
    An iterator class for generating square numbers up to a specified limit.
    """

    def __init__(self, limit: int):
        """
        Initializes the iterator with an upper limit.
        :param limit: The upper limit for generating squares of numbers.
        """
        self.limit = limit
        self.current = 1

    def __iter__(self):
        """
        Returns the iterator object itself.
        """
        return self

    def __next__(self):
        """
        Generates the next square number in the sequence. Raises StopIteration when the limit is reached.
        """
        if self.current > self.limit:
            raise StopIteration
        square = self.current ** 2
        self.current += 1
        return square


def squares_generator(limit: int):
    """
    A generator function for generating square numbers up to a specified limit.
    :param limit: The upper limit for generating squares of numbers.
    """
    for number in range(1, limit + 1):
        yield number ** 2


def squares_expression(limit: int):
    """
    A generator expression for generating square numbers up to a specified limit.
    :param limit: The upper limit for generating squares of numbers.
    """
    return (number ** 2 for number in range(1, limit + 1))
