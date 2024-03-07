# Nested List Generation with List Comprehensions
# This script creates a nested list where each inner list contains numbers calculated
# based on a specific formula using two iterators.

# Generate the nested list using list comprehensions
result_list = [[first + 1 + (4 * second) for second in range(3)] for first in range(4)]

# Print the generated nested list
print(result_list)
