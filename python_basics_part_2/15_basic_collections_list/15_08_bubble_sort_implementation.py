# Bubble Sort Implementation
# This script implements the bubble sort algorithm to sort a list of numbers input by the user.

# Reading the number of elements
elements = int(input('How many numbers: '))

# Creating an empty list to store elements
initial_list = []

# Collecting numbers for the list
for index in range(elements):
    element = int(input(f'Enter {index + 1} number: '))
    initial_list.append(element)
print("The unsorted list is:", initial_list)

# Original Bubble Sort Algorithm
for outer_index in range(len(initial_list) - 1):
    for inner_index in range(len(initial_list) - 1):
        if initial_list[inner_index] > initial_list[inner_index + 1]:
            # Swapping elements
            temp = initial_list[inner_index]
            initial_list[inner_index] = initial_list[inner_index + 1]
            initial_list[inner_index + 1] = temp

print("The sorted list is:", initial_list)
