# Discount Calculator
# This script calculates the total cost of three items and applies a 10% discount
# if the total cost exceeds 10,000.

# Input for the cost of each item
cost_of_first_item = int(input('Enter cost of 1st item: '))
cost_of_second_item = int(input('Enter cost of 2nd item: '))
cost_of_third_item = int(input('Enter cost of 3rd item: '))

# Calculate the total cost
total_cost = cost_of_first_item + cost_of_second_item + cost_of_third_item

# Apply discount if total cost is over 10,000
if total_cost > 10000:
    discount = total_cost * 0.10  # 10% discount
    # Uncomment below lines to print total cost and discount amount
    # print('Total without discount: ', total_cost)
    # print('Discount 10%: ', discount)
    print('Total with discount: ', total_cost - discount)
else:
    print('Total: ', total_cost)
