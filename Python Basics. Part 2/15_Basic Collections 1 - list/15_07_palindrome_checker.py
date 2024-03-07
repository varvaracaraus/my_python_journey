# Palindrome Checker
# This script checks whether the entered word is a palindrome (reads the same forward and backward).

# User input for a word
word = input('Enter a word: ')

# Convert the word into a list of characters
word_list = list(word)

# Calculate the length of the word
length = len(word_list)

# Check if the word is a palindrome
for i in range(length // 2):
    if word_list[i] != word_list[length - i - 1]:
        print('Word is not a palindrome')
        break
else:
    # The else block executes if the for loop completes without breaking, indicating a palindrome
    print('Word is a palindrome')
