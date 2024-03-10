# List Pairing
# This script creates a list of random integers and then pairs consecutive elements into tuples,
# demonstrating two different methods of achieving this.

import random

# First method using zip
# Generating a list of random integers
original_list = [random.randint(0, 100) for _ in range(10)]
# Pairing consecutive elements
paired_list = list(zip(original_list[0::2], original_list[1::2]))

# Displaying the results of the first method
print("Original list:", original_list)
print("New list (Method 1 - zip):", paired_list)

# Second method using list comprehension
# Generating a new list of random integers
original_list = [random.randint(0, 100) for _ in range(10)]
# Pairing consecutive elements
paired_list = [(original_list[i], original_list[i + 1]) for i in range(0, len(original_list), 2)]

# Displaying the results of the second method
print("\nOriginal list:", original_list)
print("New list (Method 2 - list comprehension):", paired_list)
