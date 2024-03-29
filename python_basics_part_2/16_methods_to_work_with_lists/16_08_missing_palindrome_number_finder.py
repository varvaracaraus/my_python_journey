# Missing Palindrome Number Finder
# This script identifies and returns the numbers that need to be added at the beginning of a sequence to
# make it a palindrome.

def find_missing_palindrome_numbers(input_sequence: list) -> list:
    """
    Identifies numbers that need to be added at the start of a sequence to form a palindrome.

    Args:
        input_sequence (list): The sequence of numbers to check.

    Returns:
        list: A list of numbers that need to be added to make the sequence a palindrome.
    """
    missing_numbers = []
    for start_index in range(len(input_sequence)):
        is_palindrome_possible = True
        for current_index in range(start_index, len(input_sequence)):
            left_index = current_index
            right_index = len(input_sequence) - current_index + start_index - 1
            if left_index >= right_index:
                break
            if input_sequence[left_index] != input_sequence[right_index]:
                is_palindrome_possible = False
                break

        if is_palindrome_possible:
            for idx in range(start_index):
                missing_numbers.append(input_sequence[start_index - 1 - idx])
            break

    return missing_numbers


# Collecting user input for the sequence
number_of_elements = int(input('Enter the number of elements: '))
user_input_sequence = []

for index in range(number_of_elements):
    user_input_sequence.append(int(input(f'Enter element {index + 1}: ')))

print('Sequence:', user_input_sequence)

# Finding additional numbers needed to make the sequence a palindrome
additional_numbers = find_missing_palindrome_numbers(user_input_sequence)

# Displaying the result
if additional_numbers:
    print(f'Additional numbers needed: {len(additional_numbers)}')
    print(f'Numbers to be added: {additional_numbers}')
else:
    print('No additional numbers needed.')
