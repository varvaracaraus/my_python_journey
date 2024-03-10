import random

from karma_exceptions import KillError, DrunkError, CarCrashError, GluttonyError, DepressionError


def one_day():
    """
    Simulates one day in life. Randomly generates karma points and may raise an exception.

    :return: Random karma points between 1 and 7.
    :raises: KillError, DrunkError, CarCrashError, GluttonyError, DepressionError randomly.
    """
    if random.randint(1, 10) == 1:
        raise random.choice([KillError, DrunkError, CarCrashError, GluttonyError, DepressionError])
    return random.randint(1, 7)


def main():
    """
    Main function to run the karma simulation. Continues until 500 karma points are accumulated.
    Records any exceptions in a log file.
    """
    karma = 0
    karma_goal = 500

    with open('karma.log', 'w') as log_file:
        while karma < karma_goal:
            try:
                karma += one_day()
            except Exception as e:
                log_file.write(f'{e.__class__.__name__}: Caught an exception\n')

        print(f"Congratulations! You have achieved enlightenment with {karma} karma points.")


main()
