# Nested List Comprehension Generator
# This script creates a 2D list using nested list comprehensions, where each inner list contains
# elements calculated based on their row and column indices.

# Creating a 2D list using nested list comprehensions
result_list = [[first + 1 + (4 * second) for second in range(3)] for first in range(4)]

# Displaying the generated 2D list
print(result_list)
