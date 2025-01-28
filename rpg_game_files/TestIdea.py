print("-------------Instructions-------------")
print("Collect the Fire Sword, Shield, and Magic key to defeat the Demon King Nox and save Princess Calista. ")
print("Find the Magic Ring and Healing potions to assist you but be careful of the traps King Nox has set up!")
print("To move type: north, south, east, or west.")
print("To stop playing type 'quit'.")
print('-' * 38)


def game_sum():
    print("\n        Text Adventure Game")
    print('-' * 38)
    print("The princess of the kingdom Chrysanthemum was kidnapped by the Demon King, Nox.")
    print("King Nox wants to steal Princess Calista's magic and life force to take over her kingdom.")
    print("Her loyal knight must save the princess from the Demon King before it is too late.")
    print(' ' * 38)

game_sum()



# data setup
rooms = {'Great Hall': {'name': 'Great Hall', 'item': ['none'], 'south': 'Vendetta Room', 'east': 'Kitchen',
                        'north': 'Potion Lab', 'west': 'Armory',
                        'text': 'You are in the Great Hall.'},

         'Armory': {'name': 'the Armory', 'item': ['fire Sword'], 'east': 'Great Hall', 'north': 'Treasure Room',
                    'text': 'You are in the Armory.'},

         'Treasure Room': {'name': 'the Treasure Room', 'item': ['Magic Ring'], 'south': 'Armory',
                           'text': 'You are in the Treasure Room.'},

         'Potion Lab': {'name': 'the Potion Lab', 'item': ['Healing Potion'], 'east': 'Bedroom', 'south': 'Great Hall',
                        'text': 'You are in the Potion Lab.'},

         'Bedroom': {'name': 'the Bedroom', 'item': ['Magic Key'], 'west': 'Potion Lab',
                     'text': 'You are in the Bedroom.'},

         'Kitchen': {'name': 'the Kitchen', 'item': ['Sandwich'], 'south': 'Storage', 'west': 'Great Hall',
                     'text': 'You are in the Kitchen.'},

         'Storage': {'name': 'Storage', 'item': ['Shield'], 'east': 'Mystery Room',
                     'text': 'You are in Storage.'},

         'Mystery Room': {'name': 'the Mystery Room', 'item': ['none'], 'west': 'Storage', 'north': 'Kitchen',
                          'text': 'You are in the Mystery Room.'},

         # villain
         'Vendetta Room': {'name': 'the Vendetta Room', 'item': ['none'], 'west': 'Dungeon', 'north': 'Great Hall',
                           'text': 'You are in the Vendetta Room.'},

         # Princess
         'Dungeon': {'name': 'the Dungeon', 'item': ['none'], 'east': 'Vendetta Room',
                     'text': 'You are in the Dungeon.'}
         }

directions = ['north', 'south', 'east', 'west']
current_room = rooms['Great Hall']
inventory = []

# game loop
while True:

    if current_room['name'] == 'the Dungeon':
        print('Congratulations! You have reached the Dungeon and saved the Princess!')
        break

        # display current location and inventory
    print('You are in {}.'.format(current_room['name']))
    print('Your current inventory: {}\n'.format(inventory))

        # get user input
    command = input('Enter Move:')

    # movement
    if command in directions:
        if command in current_room:
            current_room = rooms[current_room[command]]
        elif command == 'get item':
            if current_room['item'] != 'none':
                inventory.append(current_room['item'])
                print("You acquired : ", current_room['item'])
                print(inventory)
            elif current_room['item'] == 'none':
                print("No items to collect in this room")

        elif command != rooms[current_room[command]]:
            # bad movement
            print('You cannot go that way.')
            # quit game
    elif command == 'quit':
        print('Thanks for playing!')
        break
        # bad command
    else:
        print('Invalid input')