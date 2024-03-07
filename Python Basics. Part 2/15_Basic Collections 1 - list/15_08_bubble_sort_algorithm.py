# Bubble Sort Algorithm
# This script sorts a list of integers entered by the user using the bubble sort algorithm.

# User input for the number of elements
elements = int(input('How many numbers: '))

# Initialize an empty list to store the input elements
initial_list = []

# Input and store each element in the list
for index in range(elements):
    element = int(input(f'Enter {index + 1} number: '))
    initial_list.append(element)
print("The unsorted list is:", initial_list)

# Bubble sort algorithm implementation
for outer_index in range(0, len(initial_list) - 1):
    for inner_index in range(len(initial_list) - 1):
        # Swap elements if they are in the wrong order
        if initial_list[inner_index] > initial_list[inner_index + 1]:
            temp = initial_list[inner_index]
            initial_list[inner_index] = initial_list[inner_index + 1]
            initial_list[inner_index + 1] = temp

# Print the sorted list
print("The sorted list is:", initial_list)
