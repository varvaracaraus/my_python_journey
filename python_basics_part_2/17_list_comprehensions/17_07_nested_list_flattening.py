# Nested List Flattening
# This script flattens a deeply nested list into a single-level list by extracting each element.

# Defining a deeply nested list
nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

# Flattening the nested list using list comprehension
disclosed_list = [element for sublist in nice_list
                  for section in sublist
                  for element in section]

# Displaying the flattened list
print('Answer:', disclosed_list)
