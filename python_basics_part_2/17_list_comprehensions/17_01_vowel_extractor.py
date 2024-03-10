# Vowel Extractor
# This script extracts and counts vowels from a user-entered text string.

def extract_vowels(text: str) -> list:
    """
    Extracts all vowels from the provided text.

    Args:
        text (str): The text from which vowels are to be extracted.

    Returns:
        list: A list of vowels found in the text.
    """
    vowels = 'aeiouAEIOU'
    vowels_found = [char for char in text if char in vowels]
    return vowels_found


# Taking user input for text
user_text = input('Enter text: ')

# Extracting vowels from the entered text
vowels_list = extract_vowels(user_text)

# Displaying the results
print('List of vowels:', vowels_list)
print('Number of vowels found:', len(vowels_list))
