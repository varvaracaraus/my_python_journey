# Inventory and Cost Calculator
# This script calculates the total quantity and cost of each product in a store inventory,
# where each product has multiple entries with different quantities and prices.

# Dictionary containing product names and their codes
goods = {
    'Lamp': '12345',
    'Table': '23456',
    'Sofa': '34567',
    'Chair': '45678',
}

# Dictionary representing the store inventory with product codes as keys
store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Calculating and displaying the total quantity and cost for each product
for product, code in goods.items():
    total_quantity = 0
    total_cost = 0

    # Summing up quantities and costs for each product entry
    for entry in store[code]:
        total_quantity += entry['quantity']
        total_cost += entry['quantity'] * entry['price']

    # Displaying the total quantity and cost
    print(f"{product} — {total_quantity} pieces, cost {total_cost:,} dollars.")
