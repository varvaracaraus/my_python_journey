# Reverse Between 'h' Characters
# This script reverses the sequence of characters in a string that are between the first and last occurrences of 'h'.

def reverse_between_h(text: str) -> str:
    """
    Reverses the characters between the first and last occurrence of 'h' in the given text.

    Args:
        text (str): The string in which the reversal is to be performed.

    Returns:
        str: The substring reversed between the first and last 'h'.
    """
    first_h = -1
    last_h = -1

    # Finding the position of the first 'h'
    for i in range(len(text)):
        if text[i] == 'h':
            first_h = i
            break

    # Finding the position of the last 'h'
    for i in range(len(text) - 1, -1, -1):
        if text[i] == 'h':
            last_h = i
            break

    # Reversing the sequence between the first and last 'h'
    sequence_to_reverse = text[first_h + 1:last_h]
    reversed_sequence = sequence_to_reverse[::-1]

    return reversed_sequence


# Taking input from the user
input_text = input('Enter a string: ')

# Getting the reversed sequence result
result_text = reverse_between_h(input_text)

# Displaying the result
print(f"Reversed sequence between the first and last 'h': {result_text}")
