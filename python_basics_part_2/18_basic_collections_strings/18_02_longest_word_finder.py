# Longest Word Finder
# This script takes a user-input string and identifies the longest word in it,
# also reporting the length of that word.

# Taking user input for a string
user_input = input('Enter the string: ')

# Splitting the string into words
words = user_input.split()

# Initializing variables to track the longest word and its length
longest_len = 0
longest_word = ''

# Identifying the longest word
for word in words:
    if len(word) > longest_len:
        longest_len = len(word)
        longest_word = word

# Displaying the longest word and its length
print(f'The longest word: "{longest_word}".')
print(f'Length of the longest word: {longest_len} characters.')
