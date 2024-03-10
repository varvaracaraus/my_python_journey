# Sorted List Merger
# This script merges two pre-sorted lists into one sorted list without duplicates.

def merge_sorted_lists(list1: list, list2: list) -> list:
    """
    Merges two sorted lists into one sorted list without duplicates.

    Args:
        list1 (list): The first sorted list.
        list2 (list): The second sorted list.

    Returns:
        list: The merged and sorted list without duplicates.
    """
    # Copying the first list to preserve its original state
    merged = list(list1)

    # Merging and sorting without duplicates
    for item in list2:
        if merged.count(item) == 0:
            for i in range(len(merged)):
                if item < merged[i]:
                    merged.insert(i, item)
                    break
            else:
                merged.append(item)
    return merged


# Predefined sorted lists
first_list = [1, 3, 5, 7, 9]
second_list = [2, 4, 5, 6, 8, 10]

# Merging the two lists
final_list = merge_sorted_lists(first_list, second_list)
print(final_list)
