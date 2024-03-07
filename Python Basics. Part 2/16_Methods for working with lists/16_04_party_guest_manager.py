# Party Guest Manager
# This script manages the list of guests at a party, allowing for additions and removals based on user input.

# Initial list of guests
guests = ['Louis', 'Adele', 'Alain', 'Jean', 'Alice']

# Main loop to manage guests
while True:
    print(f'\nThere are {len(guests)} people at the party right now:')
    update = input('Has the guest arrived or left? ')

    # Handling the arrival of a guest
    if update == 'arrived':
        name = input('Guest name: ')
        # Check if there is room for the guest
        if len(guests) < 6:
            print(f'Hello, {name}!')
            guests.append(name)
        else:
            print(f"Sorry, {name}, but there's no room.")

    # Handling the departure of a guest
    elif update == 'left':
        name = input('Guest name: ')
        # Bid farewell and remove the guest from the list
        print(f'Bye, {name}!')
        guests.remove(name)

    # Handling the end of the party
    elif update == 'time to sleep':
        print('The party was over, everyone went to bed.')
        break

# Final state of the guest list
print('Final list of guests:', guests)
