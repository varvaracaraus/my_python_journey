def reverse_between_h(text):
    """
    Reverses the sequence of characters between the first and last occurrences of 'h' in the given text.

    :param text: The input string to process.
    :return: The reversed sequence between the first and last 'h'.
    """
    first_h = -1
    last_h = -1

    # Find the position of the first 'h'
    for i in range(len(text)):
        if text[i] == 'h':
            first_h = i
            break

    # Find the position of the last 'h'
    for i in range(len(text) - 1, -1, -1):
        if text[i] == 'h':
            last_h = i
            break

    # Extract the sequence between the first and last 'h' and reverse it
    sequence_to_reverse = text[first_h + 1:last_h]
    reversed_sequence = sequence_to_reverse[::-1]

    return reversed_sequence


# User input for the string
input_text = input('Enter a string: ')

# Call the function and display the result
result_text = reverse_between_h(input_text)
print(f"Reversed sequence between the first and last 'h': {result_text}")
