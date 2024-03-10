# Synonym Dictionary Creator and Finder
# This script allows a user to create a synonym dictionary with a specified number of word pairs,
# and then query the dictionary to find synonyms.

def create_synonym_dictionary(n: int) -> dict:
    """
    Creates a dictionary of synonym pairs based on user input.

    Args:
        n (int): The number of synonym pairs to be entered.

    Returns:
        dict: A dictionary mapping each word to its synonym.
    """
    synonyms = {}
    for i in range(n):
        pair = input(f"Enter the {i + 1}-th pair of words separated by '—': ").split("—")
        word1, word2 = pair[0].strip().lower(), pair[1].strip().lower()
        synonyms[word1] = word2
        synonyms[word2] = word1
    return synonyms


def find_synonym(dictionary: dict) -> None:
    """
    Queries the user for a word and prints its synonym if found in the dictionary.

    Args:
        dictionary (dict): The synonym dictionary to query.
    """
    while True:
        query = input("Enter a word: ").strip().lower()
        if query in dictionary:
            synonym = dictionary[query]
            print(f"Synonym: {synonym}")
            break
        else:
            print("The word is not in the dictionary. Please try again.")


# Taking the number of word pairs from the user
num_pairs = int(input("Enter the number of word pairs: "))

# Creating the synonym dictionary
synonym_dictionary = create_synonym_dictionary(num_pairs)

# Finding a synonym in the dictionary
find_synonym(synonym_dictionary)
