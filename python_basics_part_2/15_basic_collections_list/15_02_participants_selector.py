# Participants Selector
# This script selects every other participant from a list of names and assigns them to the first day of an event.

# List of participants
participants = ['Alexandre', 'Bernard', 'Charles', 'Denis', 'Étienne', 'François', 'Gustave', 'Henri']

# List to store participants assigned to the first day
first_day_participants = []

# Selecting every other participant for the first day
for i in range(len(participants)):
    if i % 2 == 0:
        first_day_participants.append(participants[i])

# Displaying participants for Day 1
print('Day 1:', first_day_participants)
