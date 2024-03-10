# Deep Dictionary Key Finder
# This script searches for a specific key in a nested dictionary structure, optionally limiting the search
# to a maximum depth.

def find_key_value(dictionary: dict, targ_key: str, max_dep: int = None, current_depth: int = 0):
    """
    Recursively searches for a key in a nested dictionary up to a specified maximum depth.

    Args:
        dictionary (dict): The dictionary to search.
        targ_key (str): The target key to search for.
        max_dep (int, optional): The maximum depth to search. Defaults to None (no limit).
        current_depth (int): The current depth of the search.

    Returns:
        The value of the found key, or None if the key is not found.
    """
    if current_depth == max_dep and max_dep is not None:
        return None

    for key, value in dictionary.items():
        if key == targ_key:
            return value
        elif isinstance(value, dict):
            res = find_key_value(value, targ_key, max_dep, current_depth + 1)
            if res is not None:
                return res

    return None


# Dictionary representing a website structure
site = {
    'html': {
        'head': {
            'title': 'My website'
        },
        'body': {
            'h2': 'Here will be my headline',
            'div': 'Perhaps, some block here',
            'p': 'And here is a new paragraph'
        }
    }
}

# User inputs for target key and maximum search depth
target_key = input("Enter the target key: ")
use_max_depth = input("Do you want to specify the maximum depth? Y/N: ").lower() == 'y'

max_depth = int(input("Enter the maximum depth: ")) if use_max_depth else None

# Searching for the target key
result = find_key_value(site, target_key, max_depth)

# Displaying the result
print(f"Key value: {result if result is not None else 'None'}")
