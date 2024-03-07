# Flatten a Deeply Nested List
# This script flattens a 3-level nested list into a single list using list comprehensions.

# Define a deeply nested list
nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

# Flatten the nested list using list comprehensions
disclosed_list = [element for sublist in nice_list
                  for section in sublist
                  for element in section]

# Print the flattened list
print('Answer:', disclosed_list)
