# Even Index and Modulo 5 Generator
# This script generates a list of length N where each element is 1 if its index is even,
# otherwise it's the modulo 5 of the index.

# Reading the length of the list from user input
N = int(input('Enter the length of the list: '))

# Generating the list based on specified conditions
result = [1 if index % 2 == 0 else index % 5 for index in range(N)]

# Displaying the result
print('Result:', result)
