# Day-wise Participant Selection
# This script selects every second participant from the original list for the first day's event.

# List of all participants
participants = ['Gabriel', 'Alain', 'Jean', 'Louis', 'Beau', 'Laurent', 'Pierre', 'Benoit']

# Initialize an empty list for first-day participants
firstDayParticipants = []

# Loop through the participants list and select every second participant
for i in range(len(participants)):
    if i % 2 == 0:
        firstDayParticipants.append(participants[i])

# Print the list of first-day participants
print('Day 1:', firstDayParticipants)
