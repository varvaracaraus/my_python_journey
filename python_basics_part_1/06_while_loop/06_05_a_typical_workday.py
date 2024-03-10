# A Typical Workday
# This script simulates a typical 8-hour workday. It tracks the number of tasks completed and
# whether the protagonist picks up calls from his wife. At the end of the day, it summarizes
# the work done and reminds the user to go grocery shopping if they picked up the wife's call.

print('The 8-hour workday has begun')

# Initialize counters
hour = 1
total_tasks_completed = 0
wife_calls_answered = 0

# Workday simulation
while hour <= 8:
    print(f'{hour} hour')
    total_tasks_completed += int(input('How many tasks will Maxim solve? '))
    wife_call = int(input('Wife is calling. Pick up the phone? (1-yes, 0-no) '))
    wife_calls_answered += wife_call
    hour += 1

# End of the workday summary
print('The working day is over. Total completed tasks:', total_tasks_completed)
if wife_calls_answered > 0:
    print('Need to go to the grocery store.')
