def extract_vowels(text):
    """
    Extracts vowels from the given text and returns them as a list.

    :param text: The text from which to extract vowels.
    :return: A list of vowels found in the text.
    """
    # Define a string of vowels
    vowels = 'aeiouAEIOU'

    # Use list comprehension to extract vowels from the text
    vowels_found = [char for char in text if char in vowels]
    return vowels_found


# User input for text
user_text = input('Enter text: ')

# Extract vowels from the input text
vowels_list = extract_vowels(user_text)

# Print the list of vowels and their count
print('List of vowels:', vowels_list)
print('Number of vowels found:', len(vowels_list))
