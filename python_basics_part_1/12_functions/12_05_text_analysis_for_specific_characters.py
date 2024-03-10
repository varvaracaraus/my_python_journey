# Text Analysis for Specific Characters
# This script analyzes a text input by the user and counts occurrences of a specified digit and a specified letter.

def count_characters(text: str, target_digit: str, target_letter: str) -> None:
    """
    Counts and prints the number of occurrences of the specified digit and letter in the given text.

    :param text: The text to be analyzed.
    :param target_digit: The digit to count in the text.
    :param target_letter: The letter to count in the text.
    """
    count_digit = 0
    count_letter = 0
    for symbol in text:
        if symbol == target_digit:
            count_digit += 1
        elif symbol == target_letter:
            count_letter += 1

    print(f'Number of digits {target_digit}: {count_digit}')
    print(f'Number of letters {target_letter}: {count_letter}')


# Get user input
text_input = input('Input text: ')
search_digit = input('What digit are we looking for? ')
search_letter = input('What letter are we looking for? ')

# Call the function with user input
count_characters(text_input, search_digit, search_letter)
