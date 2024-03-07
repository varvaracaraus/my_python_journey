# Shop Inventory Calculator
# This script searches for a specified item in a list of products and calculates
# the total count and cost of that item.

# Define the list of products in the shop
shop = [['carriage', 1200], ['crank', 1000], ['saddle', 300],
        ['pedal', 100], ['saddle', 1500], ['frame', 12000],
        ['rim', 2000], ['crank', 200], ['saddle', 2700]]

# User input for the item to search
item = input('Item name: ')

# Initialize count and cost variables
count = 0
cost = 0

# Iterate over the list of products
for product in shop:
    # Check if the current product matches the specified item
    if product[0] == item:
        count += 1  # Increment the count for each matching item
        cost += product[1]  # Add the cost of the matching item

# Print the total count and cost of the specified item
print(f'Number of parts: {count}')
print(f'Total cost: {cost}')
