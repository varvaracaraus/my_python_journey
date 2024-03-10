# Game Menu: Guess the Number & Rock, Paper, Scissors
# This script provides a menu to choose between two games: 'Guess the Number' and 'Rock, Paper, Scissors'.

def rock_paper_scissors():
    """
    Plays a game of Rock, Paper, Scissors against a robot with a fixed choice.
    """
    print('Rules: input 1 for Rock, 2 for Paper, or 3 for Scissors.')
    robot_choice = 2  # Robot always chooses Paper
    while True:
        user_choice = int(input('Your choice is: '))
        if user_choice == robot_choice:
            print('It\'s a tie, try again.')
        elif user_choice == 1:
            print('You win! Rock beats Paper.')
            break
        elif user_choice == 3:
            print('You lose! Scissors lose to Paper.')
            break
        else:
            print('Input error, try again.')


def guess_the_number():
    """
    Plays a game where the user has to guess the secret number.
    """
    secret_number = 8
    while True:
        guess = int(input('Guess the number: '))
        if guess == secret_number:
            print('Hurray, you guessed it!')
            break
        else:
            print('Wrong guess, try again.')


def main_menu():
    """
    Displays the main menu for game selection.
    """
    while True:
        option = int(input('\nTo choose the game input 1 for Guess the Number or 2 for Rock, Paper, Scissors: '))
        if option == 1:
            guess_the_number()
            break
        elif option == 2:
            rock_paper_scissors()
            break
        else:
            print('Input error, try again.')


# Main loop to run the game menu
while True:
    main_menu()
