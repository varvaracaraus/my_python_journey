# Nested List Sum Calculator
# This script calculates the sum of numbers in nested lists or individual arguments using recursion.

def custom_sum(*args) -> int:
    """
    Sums numbers in nested lists or individual arguments.

    Args:
        *args: Variable length argument list which can include numbers or lists.

    Returns:
        int: The total sum of all numbers.
    """
    total = 0
    for arg in args:
        if isinstance(arg, list):
            total += custom_sum(*arg)
        else:
            total += arg

    return total


# Testing the function with nested lists and individual numbers
result1 = custom_sum([[1, 2, [3]], [1], 3])
result2 = custom_sum(1, 2, 3, 4, 5)

# Displaying the results
print("Sum of nested lists:", result1)
print("Sum of individual numbers:", result2)
