# List Partitioner
# This script partitions a list into three lists: elements less than a pivot, equal to the pivot,
# and greater than the pivot. The pivot is the last element in the input list.

def partition_helper(input_list: list) -> tuple:
    """
    Partitions a list based on the last element as the pivot.

    Args:
        input_list (list): The list to be partitioned.

    Returns:
        tuple: Three lists containing elements less than, equal to, and greater than the pivot.
    """
    pivot = input_list[-1]
    less = []
    equal = []
    greater = []

    for item in input_list:
        if item < pivot:
            less.append(item)
        elif item == pivot:
            equal.append(item)
        else:
            greater.append(item)

    return less, equal, greater


# Example list of numbers
numbers = [4, 9, 2, 7, 5]

# Partitioning the list
partition_result = partition_helper(numbers)

# Displaying the partitioned lists
print("Partitioned lists:", partition_result)
