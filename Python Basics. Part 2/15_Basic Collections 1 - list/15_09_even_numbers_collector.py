# Even Numbers Collector
# This script traverses a predefined list in reverse order and collects all the even numbers into a new list.

# Predefined list of numbers
numbers_list = [7, 14, 3, 18, 21, 10, 9, 6]

# Start from the end of the list
index = len(numbers_list) - 1

# Initialize a list to store even numbers
even_numbers = []

# Traverse the list in reverse order
while index >= 0:
    # Check if the current number is even and append to even_numbers list
    if numbers_list[index] % 2 == 0:
        even_numbers.append(numbers_list[index])
    index -= 1

# Print the list of even numbers
print(even_numbers)
