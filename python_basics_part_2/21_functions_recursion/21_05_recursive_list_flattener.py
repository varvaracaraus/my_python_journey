# Recursive List Flattener
# This script flattens a nested list structure into a single-level list using recursion.

def flatten_recursive(input_list: list) -> list:
    """
    Recursively flattens a nested list into a single-level list.

    Args:
        input_list (list): The nested list to be flattened.

    Returns:
        list: The flattened single-level list.
    """
    result = []
    for item in input_list:
        if isinstance(item, list):
            result.extend(flatten_recursive(item))
        else:
            result.append(item)
    return result


# Example of a nested list
nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]

# Flattening the nested list
flattened_list = flatten_recursive(nice_list)

# Displaying the flattened list
print(flattened_list)
