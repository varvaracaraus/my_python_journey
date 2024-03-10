# Palindrome Checker
# This script checks if the entered word is a palindrome. A palindrome is a word that reads the same forwards
# and backwards.

# Taking user input for a word
word = input('Enter a word: ')

# Converting the word to a list for easier manipulation
word_list = list(word)

# Calculating the length of the word
length = len(word_list)

# Checking if the word is a palindrome
for i in range(length // 2):
    if word_list[i] != word_list[length - i - 1]:
        print('Word is not a palindrome')
        break
else:
    print('Word is a palindrome')
