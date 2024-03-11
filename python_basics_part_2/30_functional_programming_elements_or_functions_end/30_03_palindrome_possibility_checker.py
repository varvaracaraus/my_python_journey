from collections import Counter


def can_be_poly(s: str) -> bool:
    """
    Checks whether the given string s can be rearranged to form a palindrome.

    Args:
    s (str): The string to check.

    Returns:
    bool: Returns True if a palindrome can be formed, otherwise False.
    """
    counter = Counter(s)
    odd_count = sum(map(lambda char_count: char_count % 2 != 0, counter.values()))
    return odd_count <= 1


print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))
