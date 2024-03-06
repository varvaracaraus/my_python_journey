# "Guess the Number" Game
# In this game, the player attempts to guess a secret number. After each guess, the game informs
# the player if their guess is too high or too low. The game continues until the player guesses correctly
# and then reports the number of tries taken.

# Secret number set by the game
secret_number = 8

# Initialize user guess and attempt counter
user_guess = 0
attempts_count = 0

# Game loop
while user_guess != secret_number:
    user_guess = int(input('Enter your number: '))
    if user_guess < secret_number:
        print('The number is less than needed. Try again!')
    elif user_guess > secret_number:
        print('The number is greater than needed. Try again!')
    attempts_count += 1

# Print the successful guess and number of attempts
print('You guessed! Number of tries:', attempts_count)
