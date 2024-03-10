# Party Guest Tracker
# This script tracks the arrival and departure of guests at a party, maintaining a list of guests present.
# Tracking stops when it's time to sleep.

# Initial list of guests
guests = ['Elodie', 'Louis', 'Capucine', 'Adeline', 'Alexandre']

while True:
    # Displaying the current number of people at the party
    print(f'\nThere are currently {len(guests)} people at the party: {guests}')

    # Taking user input for guest update
    update = input('Has the guest arrived or left? ')

    # Handling the arrival of a guest
    if update.lower() == 'arrived':
        name = input('Guest name: ')
        if len(guests) < 6:
            print(f'Hello, {name}!')
            guests.append(name)
        else:
            print(f'Sorry, {name}, but there is no room.')

    # Handling the departure of a guest
    elif update.lower() == 'left':
        name = input('Guest name: ')
        if name in guests:
            print(f'Goodbye, {name}!')
            guests.remove(name)
        else:
            print(f'{name} is not at the party.')

    # Ending the party
    elif update.lower() == 'time to sleep':
        print('The party is over, everyone went to bed.')
        break
