# Reverse Even Number Extractor
# This script extracts even numbers from a predefined list in reverse order and displays the resulting list.

# Predefined list of numbers
numbers_list = [7, 14, 3, 18, 21, 10, 9, 6]

# Index to start from the end of the list
index = len(numbers_list) - 1

# List to store even numbers
even_numbers = []

# Extracting even numbers in reverse order
while index >= 0:
    if numbers_list[index] % 2 == 0:
        even_numbers.append(numbers_list[index])
    index -= 1

# Displaying the list of even numbers
print(even_numbers)
