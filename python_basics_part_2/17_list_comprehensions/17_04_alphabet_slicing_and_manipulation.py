# Alphabet Slicing and Manipulation
# This script demonstrates various slicing operations on a string of alphabet characters.

# Defining a string of alphabet characters
alphabet = 'abcdefg'

# Displaying different slicing operations
print('Complete alphabet:', alphabet[:])
print('Alphabet in reverse:', alphabet[::-1])
print('Every second character in alphabet:', alphabet[::2])
print('Every second character starting from second character:', alphabet[1::2])
print('First character:', alphabet[:1])
print('Last character:', alphabet[-1:-2:-1])
print('Fourth character:', alphabet[3:4])
print('Last three characters:', alphabet[-3:])
print('Fourth to fifth character:', alphabet[3:5])
print('Fifth to fourth character in reverse:', alphabet[4:2:-1])
