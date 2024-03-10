# Menu Formatter
# This script takes a user-input list of dishes separated by semicolons and formats it into a
# comma-separated string, suitable for menu display.

# Taking user input for a list of dishes
menu_input = input('Enter the list of dishes through a semicolon: ')

# Formatting the input string into a comma-separated list
formatted_menu = ', '.join(menu_input.split(';'))

# Displaying the formatted menu
print(f'Now on the menu: {formatted_menu}')
