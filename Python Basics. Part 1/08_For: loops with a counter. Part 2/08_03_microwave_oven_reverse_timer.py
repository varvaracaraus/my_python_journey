# Microwave Oven Reverse Timer
# This script acts as a countdown timer for a microwave oven, starting from the number of seconds specified by the user.
# The user can interrupt the timer to indicate that the food is ready before the time elapses.

# Input for the countdown time in seconds
countdown_time = int(input('How many seconds? '))

# Countdown loop
for seconds_left in range(countdown_time, 0, -1):
    print(f'{seconds_left} seconds left')
    ready = int(input('Enter 1 if ready or 0 if not: '))
    if ready == 1:
        print('Your food is ready, you can pick it up.')
        break
else:
    print("0 seconds left\nYour food is ready, be careful it's hot!")
