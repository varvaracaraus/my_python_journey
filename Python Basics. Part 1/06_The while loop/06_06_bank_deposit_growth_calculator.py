# Bank Deposit Growth Calculator
# This script calculates the number of years it will take for a bank deposit to reach a target amount 
# given an annual interest rate. The interest is compounded annually.

# Input for initial deposit, interest rate, and target amount
initial_deposit = int(input('The bank deposit is: '))
annual_interest_rate = int(input('Yearly interest rate (%): '))
target_deposit = int(input('Target amount is: '))

# Initialize the years counter
years_to_reach_target = 0

# Compound interest calculation
while initial_deposit < target_deposit:
    initial_deposit += (initial_deposit * annual_interest_rate / 100)
    initial_deposit = int(initial_deposit)  # Round down to nearest whole number
    years_to_reach_target += 1

# Print the result
print('Target amount will be reached in', years_to_reach_target, 'year(s)')
