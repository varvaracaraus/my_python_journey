# Conditional Tuple Sorter
# This script sorts the elements of a given tuple if all elements are integers.
# Otherwise, it returns the tuple as is, avoiding shadowing of 'tpl' from the outer scope.

def sort_tuple(input_tuple: tuple) -> tuple:
    """
    Sorts the elements of the input tuple if all elements are integers.

    Args:
        input_tuple (tuple): The tuple to be potentially sorted.

    Returns:
        tuple: A sorted tuple if all elements are integers, otherwise the original tuple.
    """
    # Check if all elements in the tuple are integers
    if all(isinstance(x, int) for x in input_tuple):
        return tuple(sorted(input_tuple))
    else:
        return input_tuple


# Example tuple
tpl = (6, 3, -1, 8, 4, 10, -5)

# Sorting the tuple using the function
sorted_tpl = sort_tuple(tpl)

# Displaying the sorted tuple
print(sorted_tpl)
