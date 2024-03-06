# Debt Collector Simulator
# This script simulates a debt payment process. It asks for the debtor's name and the debt amount,
# then repeatedly asks for payments until the debt is fully paid.

# Input for the debtor's name and the debt amount
debtor_name = input('Enter your name: ')
debt_amount = int(input('Enter your debt amount: '))

# Debt payment process
while True:
    payment = int(input('Enter your payment: '))
    if payment == debt_amount:
        print(f'Great, {debtor_name}. You have paid your debt. Thank you!')
        break
    else:
        print(f"Not enough, {debtor_name}. Let's do it again.")
