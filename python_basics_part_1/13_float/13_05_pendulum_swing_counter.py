# Pendulum Swing Counter
# This script calculates how many swings a pendulum takes to reduce its amplitude 
# from an initial value to a specified stopping amplitude.

def pendulum_swings(start_amplitude: float, end_amplitude: float) -> None:
    """
    Calculates the number of swings until the pendulum's amplitude decreases to the end amplitude.

    :param start_amplitude: The initial amplitude of the pendulum in cm.
    :param end_amplitude: The amplitude at which the pendulum is considered to have stopped, in cm.
    """
    if start_amplitude <= end_amplitude:
        print('Stop amplitude must be less than initial amplitude.')
        return

    amplitude = start_amplitude
    count = 0

    while amplitude > end_amplitude:
        amplitude -= amplitude * 0.084  # Decrease amplitude by 8.4%
        count += 1

    print(f'The pendulum is considered to have stopped after {count} swings.')


# Get user input
initial_amplitude = float(input('Enter initial amplitude in cm: '))
stop_amplitude = float(input('Enter stop amplitude in cm: '))

# Call the function with user input
pendulum_swings(initial_amplitude, stop_amplitude)
