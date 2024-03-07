# Circular List Shift
# This script allows the user to create a list of integers, then shifts the list's elements
# circularly by a specified number of positions.

# User input for the number of elements in the list
number_of_elements = int(input('Enter how many numbers in the list: '))

# Initialize the list and populate it with user input
input_list = []
for index in range(number_of_elements):
    num = int(input(f'Enter number {index + 1}: '))
    input_list.append(num)

# User input for the number of positions to shift the list by
shift_positions = int(input('By how many positions to shift: '))
print('Initial list:', input_list)

# Perform the circular shift
if shift_positions > 0:
    for i in range(shift_positions):
        input_list.insert(0, input_list.pop())
elif shift_positions < 0:
    for i in range(abs(shift_positions)):
        input_list.append(input_list.pop(0))

# Print the shifted list
print('Shifted list:', input_list)
