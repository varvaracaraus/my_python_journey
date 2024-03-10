# Palindrome Permutation Checker
# This script checks if a given string can be rearranged to form a palindrome.

def can_permute_to_palindrome(s: str) -> bool:
    """
    Determines if the given string can be rearranged to form a palindrome.

    Args:
        s (str): The string to be checked.

    Returns:
        bool: True if the string can be permuted to a palindrome, False otherwise.
    """
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Counting characters with odd occurrences
    odd_count = sum(1 for count in char_count.values() if count % 2 != 0)

    # A string can form a palindrome if it has at most one character with an odd count
    return odd_count <= 1


def main():
    # Taking user input
    user_input = input("Enter a string: ")

    # Checking for palindrome permutation possibility
    if can_permute_to_palindrome(user_input):
        print("Can be permuted to a palindrome")
    else:
        print("Cannot be permuted to a palindrome")


# Running the main function
main()
