from collections import Counter


def count_unique_characters(s: str) -> int:
    """
    Returns the count of unique characters in a string.

    Args:
    s (str): The string to count unique characters in.

    Returns:
    int: The count of unique characters in the string.
    """
    s = s.lower()
    counter = Counter(s)
    unique_chars = sum(map(lambda char: 1 if counter[char] == 1 else 0, counter))
    return unique_chars


# Example usage
message = "Today is a beautiful day! The sun is shining and the birds are singing."

unique_count = count_unique_characters(message)
print("Number of unique characters in the string:", unique_count)
