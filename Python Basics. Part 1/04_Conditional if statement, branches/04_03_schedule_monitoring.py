# Schedule Monitoring
# This script determines whether today is a workday or a day off based on the date.

# Input for today's date
today_date = int(input('What date is today? '))

# Determine if it's a workday or day off
if today_date % 2 == 0:
    print("Let's go to work!")
else:
    print('Hooray, today is a day off!')
