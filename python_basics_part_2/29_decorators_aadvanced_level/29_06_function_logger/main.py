from logger_decorator import LoggerDecorator


@LoggerDecorator
def complex_algorithm(arg1: int, arg2: int) -> int:
    """
    Executes a complex algorithm. For each pair of integers (i, j) in the ranges
    (0, arg1) and (0, arg2), it writes their sum to a file and accumulates these sums.

    Args:
        arg1 (int): The upper limit for the first range.
        arg2 (int): The upper limit for the second range.

    Returns:
        int: The sum of all i + j for each i in range(arg1) and j in range(arg2).
    """
    result = 0
    for i in range(arg1):
        for j in range(arg2):
            with open('test.txt', 'w', encoding='utf8') as file:
                file.write(str(i + j))
                result += i + j
    return result


# Example of calling the function with the decorator applied
res = complex_algorithm(10, 50)
