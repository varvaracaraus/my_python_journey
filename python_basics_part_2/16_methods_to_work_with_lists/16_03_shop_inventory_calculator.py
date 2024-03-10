# Shop Inventory Calculator
# This script calculates the total number and cost of a specified item in a shop's inventory.

# Shop's inventory list with item names and their costs
shop = [['carriage', 1200], ['crank', 1000], ['saddle', 300],
        ['pedal', 100], ['saddle', 1500], ['frame', 12000],
        ['rim', 2000], ['crank', 200], ['saddle', 2700]]

# Taking user input for item name
item = input('Item name: ')

# Variables for counting items and calculating total cost
count = 0
cost = 0

# Calculating total number and cost of the specified item
for product in shop:
    if product[0] == item:
        count += 1
        cost += product[1]

# Displaying the results
print(f'Number of parts: {count}')
print(f'Total cost: {cost}')
