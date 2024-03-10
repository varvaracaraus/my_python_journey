# Dynamic Website Generator
# This script creates multiple versions of a website template, replacing specific content based on user input.

import copy


def copy_site(website: dict) -> dict:
    """
    Creates a deep copy of a website template.

    Args:
        website (dict): The website template to be copied.

    Returns:
        dict: A deep copy of the website.
    """
    return copy.deepcopy(website)


def create_website() -> list:
    """
    Creates a list of websites with different product names.

    Returns:
        list: A list of modified website dictionaries.
    """
    website_list = []
    num_sites = int(input("How many websites: "))

    for i in range(num_sites):
        product_name = input(f"Enter the product name for website {i + 1}: ")
        new_site = copy_site(site)
        replace_element(new_site, 'iPhone', product_name)
        website_list.append(new_site)

    print_site_results(website_list)
    return website_list


def print_site_results(website_list: list) -> None:
    """
    Prints the structure of each website in the list.

    Args:
        website_list (list): The list of websites to be printed.
    """
    for i, site_entry in enumerate(website_list):
        print(f"\nSite {i + 1} for {site_entry['html']['body']['h2'].split()[-1]}:")
        print("site = {")
        print_structure(site_entry, 1)
        print("}")


def print_structure(dictionary: dict, indent: int) -> None:
    """
    Recursively prints the structure of a dictionary.

    Args:
        dictionary (dict): The dictionary to print.
        indent (int): The current indentation level.
    """
    for key, value in dictionary.items():
        if isinstance(value, dict):
            print(' ' * indent + f"'{key}': " + '{')
            print_structure(value, indent + 4)
            print(' ' * indent + '}')
        elif isinstance(value, str):
            print(' ' * indent + f"'{key}': '{value}',")
        elif isinstance(value, list):
            print(' ' * indent + f"'{key}': [")
            for item in value:
                print_structure(item, indent + 4)
            print(' ' * indent + '],')


def replace_element(dictionary: dict, old_value: str, new_value: str) -> None:
    """
    Recursively replaces a value within a nested dictionary.

    Args:
        dictionary (dict): The dictionary where the replacement is to be made.
        old_value (str): The value to be replaced.
        new_value (str): The new value.
    """
    for key, value in dictionary.items():
        if isinstance(value, dict):
            replace_element(value, old_value, new_value)
        elif isinstance(value, str):
            dictionary[key] = value.replace(old_value, new_value)
        elif isinstance(value, list):
            for i, item in enumerate(value):
                if isinstance(item, dict):
                    replace_element(item, old_value, new_value)
                else:
                    value[i] = item.replace(old_value, new_value)


# Template website structure
site = {
    'html': {
        'head': {
            'title': 'Buy/Sell Phones Inexpensively'
        },
        'body': {
            'h2': 'We have the lowest prices on iPhone',
            'div': 'Buy',
            'p': 'Sell'
        }
    }
}

# Generating the list of modified websites
websites = create_website()
