# Generate a list based on index conditions
# Each element is 1 if the index is even, otherwise it's the remainder of the index divided by 5

# User input for the length of the list
N = int(input('Enter the length of the list: '))

# Generate the list with the specified rule
result = [1 if index % 2 == 0 else index % 5 for index in range(N)]

# Print the generated list
print('Result:', result)
