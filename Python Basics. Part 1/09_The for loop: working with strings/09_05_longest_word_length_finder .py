# Longest Word Length Finder
# This script takes a string of text as input and calculates the length of the longest word in the text.

# Input for the text
input_text = input("Enter the text: ")

# Initialize variables to track the maximum length and the current word length
max_word_length = 0
current_word_length = 0

# Loop through each character in the text
for char in input_text:
    if char != ' ':
        current_word_length += 1
    else:
        max_word_length = max(max_word_length, current_word_length)
        current_word_length = 0

# Check for the last word in the text
max_word_length = max(max_word_length, current_word_length)

# Print the length of the longest word
print(f"Longest word has {max_word_length} letters.")
