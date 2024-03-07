def merge_sorted_lists(list1, list2):
    """
    Merges two sorted lists into one sorted list without duplicates.

    :param list1: The first sorted list.
    :param list2: The second sorted list.
    :return: A new sorted list with elements from both input lists, excluding duplicates.
    """
    # Copy the first list to avoid modifying the original
    merged = list(list1)

    # Iterate through each item in the second list
    for item in list2:
        # Check if the item is not already in the merged list
        if merged.count(item) == 0:
            # Find the correct position for the item in the merged list
            for i in range(len(merged)):
                if item < merged[i]:
                    merged.insert(i, item)
                    break
            else:
                # If item is greater than all elements in merged, append it
                merged.append(item)
    return merged


# Define the sorted lists
first_list = [1, 3, 5, 7, 9]
second_list = [2, 4, 5, 6, 8, 10]

# Merge the lists and print the final sorted list
final_list = merge_sorted_lists(first_list, second_list)
print(final_list)
