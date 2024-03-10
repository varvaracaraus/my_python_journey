import datetime
import random

# This program generates a log file with random error and success messages.

# Number of lines in the file can be controlled by changing 'NUM_LINES'
NUM_LINES = 80

error_types = ['ValueError', 'ArithmeticError', 'AssertionError', 'ImportError', 'NameError', 'OSError']

with open('work_logs.txt', 'w', encoding='utf8') as log_file:
    for _ in range(NUM_LINES):
        if random.randint(1, 10) == 5:
            error_message = 'ERROR: ' + random.choice(error_types) + ' ' + str(datetime.datetime.today())
            log_file.write(error_message + '\n')
        else:
            success_message = 'COMPLETE: Data successfully transferred.'
            log_file.write(success_message + '\n')
