# String Slicing Demonstrations
# This script demonstrates various slicing techniques on the string 'abcdefg',
# showcasing how different slicing parameters affect the output.

alphabet = 'abcdefg'

# Print the entire alphabet
print(alphabet[:])  # 'abcdefg'

# Print the alphabet in reverse
print(alphabet[::-1])  # 'gfedcba'

# Print every second character of the alphabet
print(alphabet[::2])  # 'aceg'

# Print every second character of the alphabet, starting from the second character
print(alphabet[1::2])  # 'bdf'

# Print the first character of the alphabet
print(alphabet[:1])  # 'a'

# Print the last character of the alphabet
print(alphabet[-1:-2:-1])  # 'g'

# Print the fourth character of the alphabet
print(alphabet[3:4])  # 'd'

# Print the last three characters of the alphabet
print(alphabet[-3:])  # 'efg'

# Print characters from the fourth to the fifth of the alphabet
print(alphabet[3:5])  # 'de'

# Print characters from the fifth to the third in reverse order
print(alphabet[4:2:-1])  # 'ed'
