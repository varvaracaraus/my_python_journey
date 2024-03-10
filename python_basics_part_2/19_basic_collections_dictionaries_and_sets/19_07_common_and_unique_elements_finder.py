# Common and Unique Elements Finder
# This script finds common and unique elements in three arrays,
# demonstrating solutions with and without using sets.

def find_common_elements(array1: list, array2: list, array3: list) -> tuple:
    """
    Finds common elements in three arrays using methods with and without sets.

    Args:
        array1 (list): The first array.
        array2 (list): The second array.
        array3 (list): The third array.

    Returns:
        tuple: Two lists containing common elements, one found without sets and the other with sets.
    """
    # Finding common elements without using sets
    com_elements_no_set = [element for element in array1 if element in array2 and element in array3]

    # Finding common elements using sets
    com_elements_with_set = list(set(array1) & set(array2) & set(array3))

    return com_elements_no_set, com_elements_with_set


def find_unique_elements(array1: list, array2: list, array3: list) -> tuple:
    """
    Finds unique elements in the first array compared to the other two arrays using methods with and without sets.

    Args:
        array1 (list): The first array.
        array2 (list): The second array.
        array3 (list): The third array.

    Returns:
        tuple: Two lists containing unique elements, one found without sets and the other with sets.
    """
    # Finding unique elements without using sets
    uni_elements_no_set = [element for element in array1 if element not in array2 and element not in array3]

    # Finding unique elements using sets
    uni_elements_with_set = list(set(array1) - (set(array2) | set(array3)))

    return uni_elements_no_set, uni_elements_with_set


# Defining arrays
array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

# Task 1: Finding common elements
print("Task 1:")
common_elements_no_set, common_elements_with_set = find_common_elements(array_1, array_2, array_3)
print("Solution without sets:", common_elements_no_set)
print("Solution with sets:", common_elements_with_set)

# Task 2: Finding unique elements
print("\nTask 2:")
unique_elements_no_set, unique_elements_with_set = find_unique_elements(array_1, array_2, array_3)
print("Solution without sets:", unique_elements_no_set)
print("Solution with sets:", unique_elements_with_set)
