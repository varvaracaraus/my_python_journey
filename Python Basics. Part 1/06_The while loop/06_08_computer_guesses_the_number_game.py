# "Computer Guesses the Number" Game
# In this game, the player thinks of a number between 1 and 100, and the computer tries to guess it.
# The player gives hints whether the computer's guess is too high, too low, or correct. The game
# continues until the computer guesses the number of uses up its allotted attempts.

# Define the range for the guess
min_num = 1
max_num = 100

# Initialize the number of attempts
attempt_counter = 0

print('Think of a number from 1 to 100, I will try to guess it.')

# Game loop
while True:
    attempt_counter += 1
    guess = (min_num + max_num) // 2
    response = int(input(f'Is your number {guess}? (Enter: 1 - if yes, 2 - if higher, 3 - if lower): '))

    if response == 1:
        print(f'I guessed your number {guess} in {attempt_counter} attempts!')
        break
    elif response == 2:
        min_num = guess + 1
    elif response == 3:
        max_num = guess - 1
    else:
        print('Please enter: 1 - if correct, 2 - if higher, 3 - if lower')

    if attempt_counter >= 7:
        print("I've used all 7 attempts, but couldn't guess the number :( ")
        break
