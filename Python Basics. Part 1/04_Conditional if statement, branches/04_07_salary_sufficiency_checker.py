# Salary Sufficiency Checker
# This script calculates the salary based on the number of worked hours and determines
# if it is sufficient to cover credit and food expenses. It then advises whether more
# work hours are needed or if the user can rest.

# Input for the number of worked hours, credit amount, and food expenses
worked_hours = int(input('Enter the number of worked hours: '))
credit_amount = int(input('Enter the credit amount: '))
food_expenses = int(input('Enter food expenses: '))

# Calculate the salary
salary = ((200 * worked_hours) / (2 ** 3)) + worked_hours

# Check if the salary covers expenses and print the result
if salary >= credit_amount + food_expenses:
    print('There are enough hours. You can rest.')
else:
    print("There aren't enough hours. You'll have to work harder!")
