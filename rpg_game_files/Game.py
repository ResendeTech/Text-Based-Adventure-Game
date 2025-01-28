import sys, time
import random

#variables
enter = ""
F = "farmer"
At = "Attack" or "attack"
It = "Items" or "items"
st = "stats"
slime = False
guard = False
enraged_guard = False

# Player stats
player_stats = {
    'at': 0,
    'df': 0,
    'hp': 0,
    'max_hp': 0,
    'mp': 0,
    'xp': 0,
    'player_lv': 1,
    'character': None,
    'max_xp': 10,
}


#Slime stats
slime_stats = {
    'slime_at': 2,
    'slime_hp': 5,
  
}

#Guard stats
guard_stats = {
    "guard_at": random.randint(3, 5),
    "guard_hp": 12,
    "piercing_strike": 7,
    "armor": 3,
}
#Enraged guard stats
enraged_guard_stats = {
    "guard_at": random.randint(3, 6),
    "guard_hp": 14,
    "piercing_strike": 9,
    "armor": 3,
}


#quit system
def quit_game():
    if player_stats['hp'] <= 0:
        print("You have died, game over")
        exit()
    action = input("Are you sure you want to quit? Y/N: ")
    if action.lower() == 'y':
        print("you have quit the game")
        exit()
    elif action.lower() == 'n':
        print("You have chosen to continue playing")
        return False
    
    


#Player input system
def get_player_input(prompt):
    while True:
        action = input(prompt)
        if action.lower() == 'stats':
            stats()
            return None
        if action.lower() == 'check':
            if guard == True:
                check_guard()
            elif guard == False:
                print("There is nothing to check")
                continue
        elif action.lower() == "quit":
            if not quit_game():
                continue
        else:
            return action

#Guard stat system
def check_guard():
    print('\n')
    print("-" * 92)
    if enraged_guard == True:
        print("Enraged guard's description: A very strong, angry man with enough rage that his eyes literally turned red with anger.")
        print("Enraged guard's health: ", enraged_guard_stats['guard_hp'])
        print("Enraged guard's attack damage: 3-7")
        print("Enraged guard's piercing strike's damage: ", enraged_guard_stats['piercing_strike'])
        print("piercing strike's description: A very dangerous attack that pierces straight through armor")
        return
    elif enraged_guard == False:
        print("Guard's description: A very strong man with years of experience in standing still. A true threat to society!")
        print("Guard's health: ", guard_stats['guard_hp'])
        print("Guard's attack damage: 3-6")
        print("Guard's piercing strike's damage: ", guard_stats['piercing_strike'])
        print("piercing strike's description: A very dangerous attack that pierces straight through armor")
        print("-" * 92)
        print('\n')
        return 

#Stat system

def stats():
    print ('\n')
    print ('-' * 92) 
    print ("Character role: ", player_stats['Character'])
    print ("Attack damage: ", int(player_stats['at']))
    print ("Defense: ", player_stats['df'])
    print ("Health: ", player_stats['hp'])
    print ("Magic: ", player_stats['mp'])
    print ("Player level: ", player_stats['player_lv'])
    print ("player's current xp: ", player_stats['xp'])
    print ("XP needed to level up: ", int(player_stats['max_xp']))
    print ('-' * 92) 
    print ('\n')
    return

# Level up system
def lv_up():
    player_stats['player_lv'] += 1
    player_stats['at'] += 2
    player_stats['df'] += 2
    player_stats['max_hp'] += 4
    if player_stats['xp'] >= player_stats['max_xp']:
        player_stats['xp'] -= player_stats['max_xp']
    elif player_stats['xp'] == player_stats['max_xp']:
        player_stats['xp'] = 0 
    player_stats['max_xp'] *= 1.5
    player_stats['hp'] = player_stats['max_hp']
    print ("You are now level: ", player_stats['player_lv'])
    print("YOU LEVELED UP!!! Your stats were increased and recovered to max health.")

# Player_turn system

def player_turn():
    print('\n')
    print("-" * 92)
    print("Your intention to absolutely demolish the slime frightens the poor fellow, as you swing your rake for the kill, you miss your attack, however, the sheer fright of the attack damaged the slime ")
        
    crit = random.randint(0, 4)

    if crit == 1:
        player_stats['at'] *= 2
        print("critical hit!")

    if slime == True:
        slime_stats['slime_hp'] -= player_stats['at']
        if crit == 1:
            player_stats['at'] /= 2
        print("Slime: YEEOOWWCCHHHHHHH")
        if slime_stats['slime_hp'] >= 0:
            print("Slime's current health:",  slime_stats['slime_hp'])                
        elif slime_stats['slime_hp'] < 0:
            print("Slime's current health:", 0)
        print("-" * 92)

    if guard == True:
        guard_stats["guard_hp"] -= player_stats["at"]
        if crit == 1:
            player_stats["at"] /= 2
        print("Guard: himaOWWWWWWW!!!")
        if guard_stats['guard_hp'] >= 0:
            print("Guard's current health:",  guard_stats['guard_hp'])                
        elif guard_stats['guard_hp'] < 0:
            print("Guard's current health:", 0)
        print("-" * 92)

# Slime turn system
def slime_turn ():
    print('\n')
    print("-" * 92)
    if slime_stats['slime_hp'] > 0:
        print("The slime lived and now is pissed off, it attacks you with all his little might")
        slime_stats['slime_at'] = random.randint(1, 3)
        player_stats['hp'] -= slime_stats['slime_at']
        print ("The slime did", slime_stats['slime_at'], "damage!")
        print('\n')
        print("Youch that hurt! your health is now at: ", player_stats['hp'])
    print("-" * 92)

# Guard turn system
def guard_turn():
    print('\n')
    print("-" * 92)
    if guard_stats["guard_hp"] > 0:
        attack_numba = random.randint(1, 3)
        if attack_numba == 1:
            player_stats['hp'] -= guard_stats["piercing_strike"]
            print("The guard uses his special attack, piercing strike! He did", guard_stats["piercing_strike"], "damage!")
            print('\n')
            print("Godamn that attack pierced through like a mothertrucker! Your health is now at: ", player_stats['hp'])
            print("-" * 92)
        elif attack_numba == 2 or 3:
            player_stats['hp'] -= guard_stats["guard_at"]
            print("The guard attacks! He did", guard_stats["guard_at"], "damage!")
            print('\n')
            print("Godamn that attack pierced through like a mothertrucker! Your health is now at: ", player_stats['hp'])
            print("-" * 92)
   

# Map of city part of the game
# the map    
Hima_city_grid = [
    ["empty",      "shop",  "empty", "wall", "tavern"],
    ["blacksmith", "empty", "guild", "goon_cave"],
    ["empty",      "tavern", "road", "empty"],
    ["empty",      "empty",  "road", "library", "empty"],
    ["wall",       "wall", "entrance", "wall", "wall"],
]

# enter functions
def enter_library():
    print()
    print ("-" * 92)
    print("You have entered the library. You can read books here.")
    # You can book here that will have lore of the game and and the ouside as well
    # maybe secret rooms in the library that you can get cool magic from it
    
def enter_goonCave():
    print("You have entered the goon cave. You feel your legs sticking to the ground, there's a foul smell in the air. You pick up some of the white liquid and start gulping it down.")
    print("you start gooning... you can't stop gooning, you feel your life sapping out of you as you goon, YOU DIE")

def enter_shop():
    print("You have entered the shop. You can buy items here.")
    # make an inventory system
     # In battle, be able to write items, then when in items menu, be able to see the list of items the player has
      # To do this, items should have an array of the lists of items in the game and their description and their abilities
     # Then each item should have the ability to be able to check the item: to see what it does and a small description
     # And as well the ability to use the item
      # For using the item, there will probably be temporary boosts and one off time items
      # so having the variable for counting the turns necessary to calculate how long an item lasts
    
    # Make a system where the player can peruse and choose and buy items 
     # For the store, the items available in the store should be separated in categories: 
      # make the money be taken away when you buy something and that items go into your inventory
      # Potions for kinda miscellaneous magic item effects and healing/boosting mana and maybe health
      # Foods for healing/temporary stat bonuses
      # item accessories that you can equip that you gives you permanent stat upgrade when you have it on
      # When implemeneting equipables, another inventory array needs to made to differentiate between normal items and equipables
       # To specify, equipable items can go into the normal inventory array, however normal items cannot go into equipable invotory array
      # The stats from the armor should be able to be differentiated when the player checks their stats
      # by putting a "(+armor number)" next to the original stat

    # make a currency system
     # Make a variable called money or whatever the currency name is going to be
     # When the player completes a quest, a side quest, kills an enemy, collects treasure, they receive money
     # money is spent in taverns, secret quests, store items, blacksmith upgrades and armor, and library
def enter_tavern():
    print("You have entered the tavern. You can rest here.")
    # in the tavern you should be able to converse with the locals, by writing talk 
     # the tavern people could give the people side quests, secret quests and possibly item trades
      # Secret quests would be able to be accepted and gotten only through very specific ways, like bringing a certain item to someone or something
     # The people should give you monologues and they inform you of things happening in the world or silly thing (like pokemon npcs)
     # Buy and able to drink alcohol
      # secret ending: if player drinks alcohol for 5 days straight every night, FNAF will appear and will kill and end the game. Dont five nights kids 
def enter_blacksmith():
    print("You have entered the blacksmith. You can forge weapons here.")
    #Upgrades to specific weapons, armors and probably accesories
    # Can upgrade only specific weapons, late game items and secret items
    # You can combine certain accessories together to get better accesories
    # Requires to upgrade normal weapons
    # Specific items need specific material where the blacksmith will give you a quest to do 

def enter_guild():
    print("You have entered the guild. You can take quests here.")
    # You can sign up to become a guild member, where you can accept quests and talk with the peeps there
    # The game progresses the more quests, as in time moves forward


location_actions = {
    "library": enter_library,
    "shop": enter_shop,
    "tavern": enter_tavern,
    "blacksmith": enter_blacksmith,
    "guild": enter_guild,
    "goon_cave": enter_goonCave,
}

explored_segments = set()
player_x, player_y = 4, 2
explored_segments.add((player_x, player_y))

# x and y co-ordinates are flipped, change it later
# move direction function
def move_player(direction):
    global player_x, player_y
    new_x, new_y = player_x, player_y

    if direction == "up" and player_x > 0 and player_y < len(Hima_city_grid[player_x - 1]) > 0:
        new_x -= 1
        if Hima_city_grid[new_x][new_y] == "wall":
            print("You can't move in that direction. There's a wall.")
            new_x += 1
    elif direction == "down" and player_x < len(Hima_city_grid) - 1 and player_y < len(Hima_city_grid[player_x + 1]):
        new_x += 1
        if Hima_city_grid[new_x][new_y] == "wall":
            print("You can't move in that direction. There's a wall.")
            new_x -= 1
    elif direction == "left" and player_y > 0:
        new_y -= 1
        if Hima_city_grid[new_x][new_y] == "wall":
            print("You can't move in that direction. There's a wall.")
            new_y += 1
    elif direction == "right" and 0 < player_y < len(Hima_city_grid[player_x]) - 1:
        new_y += 1
        if Hima_city_grid[new_x][new_y] == "wall":
            print("You can't move in that direction. There's a wall.")
            new_y -= 1
    else:
        print("Invalid move")
    
    player_x, player_y = new_x, new_y
    display_surroundings(player_x, player_y)
    explored_segments.add((player_x, player_y))


def display_surroundings(x, y):
    rows = len(Hima_city_grid)
   
    if not (0 <= x < rows and 0 <= y < len(Hima_city_grid[x])):
        print(f"Player position ({x}, {y}) is out of bounds.")
        return
    
    surroundings = {
        "up": (x-1, y),  
        "down": (x+1, y),  
        "left": (x, y-1),  
        "right": (x, y+1)   
    }
    # Define the relative positions for the surroundings

    print(f"Player is at ({x}, {y}): {Hima_city_grid[x][y]}")

    for direction, (i, j) in surroundings.items():
        if 0 <= i < rows and 0 <= j < len(Hima_city_grid[i]):
             print(f"{direction.capitalize()}: {Hima_city_grid[i][j]}")

    
    current_location = Hima_city_grid[x][y]
    if current_location in location_actions:
        choice = input(f"Do you want to enter the {current_location}? (enter/skip): ").strip().lower()
        if choice == "enter":
            location_actions[current_location]()
            for direction, (i, j) in surroundings.items():
                if 0 <= i < rows and 0 <= j < len(Hima_city_grid[i]):
                    print(f"{direction.capitalize()}: {Hima_city_grid[i][j]}")
        # make an else statement for invalid input

def check_map(grid, player_x, player_y, explored_segments):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if (i, j) == (player_x, player_y):
                 print(f"{cell}/Player", end=" | ")
            elif (i, j) in explored_segments:
                print(cell, end=" | ")
            else:
                print("???", end=" | ")
        print()

def delprint(e1, dell = 0.05): 
    for c in e1:      
        sys.stdout.write(c) 
        sys.stdout.flush()
        time.sleep(dell)

# The game
while True:
    role = input("Choose your character: farmer, explorer, scribe ")

    if role.lower() == F.lower():
        e1 = "You have chosen farmer as your character, with this decision made, you shall go on a grand adventure."
        player_stats['at'] = 2
        player_stats['df'] = 3
        player_stats['hp'] = 10
        player_stats['max_hp'] = 10
        player_stats['Character'] = F
        delprint (e1)
        break
    else:
        print("Invalid input, try again")


start = input(" Enter to continue ")
delprint(start)


print("-" * 92)

while True:

    if start == enter:
        def delprint(e2, dell = 0.05): 
            for c1 in e2:      
                sys.stdout.write(c1) 
                sys.stdout.flush()
                time.sleep(dell)
        e2 = "You begin your journey and leave your friends and family behind at the village of farmers. On your way to the populated city of Hima, you go through treacherous woods and you encounter a slime! You decide to beat the living shit out of it!"
        delprint(e2)

        start = input(" Enter to continue ")
        delprint(start)
        break

    else:
        print("Invalid input, try again")
        break

if start == enter:
    def delprint(e3, dell = 0.05): 
        for c2 in e3:      
            sys.stdout.write(c2) 
            sys.stdout.flush()
            time.sleep(dell)   
    e3 = "The slime is so nice that it is letting you attack first! You can Attack, use Items, or you can see your stats by typing stats. "
    delprint(e3)

# Attack and stat system
while True:        
    action = get_player_input("Choose an action: ")
    
    if action is None:
        continue

    if action.lower() == 'attack':
        slime = True
        player_turn()
        input("Press Enter to continue...")
        slime_turn()
        slime = False
        if slime_stats['slime_hp'] <= 0:
            print("You killed the poor slime... But you Won! congrats!")
            player_stats['xp'] += 10
            if player_stats['xp'] >= player_stats['max_xp']:
                lv_up()
            break
        elif player_stats['hp'] <= 0:
            quit_game()
            break
    else:
        print("Invalid input, try again")

action = get_player_input("Enter to continue: ")
if slime_stats['slime_hp'] <= 0:
    
    if action == enter:
        def delprint(e3, dell = 0.05): 
            for c2 in e3:      
                sys.stdout.write(c2) 
                sys.stdout.flush()
                time.sleep(dell)   
        e3 = "After a fierce fight, you have successfully beaten the shit out of the slime! You continue on your epic journey to Hima! You can now always access your stats menu whenever. "
        delprint(e3)

action = get_player_input("Enter to continue: ")


print ("-" * 92)
def delprint(e4, dell = 0.05): 
        for c3 in e4:      
            sys.stdout.write(c3) 
            sys.stdout.flush()
            time.sleep(dell)   
e4 = "As you continue on your journey, you pass through mountains and hills, you encounter many more slimes and fight your best to survive. And finally, after 6 months of blood, sweat and tears of travelling and fighting for your survival, you see on your horizon on a cold autumn night, a glimpse of bright lights!"
delprint(e4)

action = get_player_input(" Press Enter to continue: ")

def delprint(e5, dell = 0.05): 
        for c4 in e5:      
            sys.stdout.write(c4) 
            sys.stdout.flush()
            time.sleep(dell)   
e5 = "You run towards that light and you finally see it, Hima! As you approach the city walls, you realise you need to pass through security to enter the city"
delprint(e5)

action = get_player_input(" Press Enter to continue: ")
print ("-" * 92)

def delprint(e6, dell = 0.05): 
        for c5 in e6:      
            sys.stdout.write(c5) 
            sys.stdout.flush()
            time.sleep(dell)   
e6 = "you have a small mental breakdown as you realise you have no ID on you to enter the city, so now your only way to get inside is to fake it until you make it, or you can try others ways as well. "
delprint(e6)

action = get_player_input("Press Enter to continue: ")
print ("-" * 92)


def delprint(e7, dell = 0.05): 
        for c6 in e7:      
            sys.stdout.write(c6) 
            sys.stdout.flush()
            time.sleep(dell)   
e7 = 'You approach the guard and the guard sees you and says "Hamahimahooo hamahimahaa!" You stand there discombobulated, as you did not understand anything the guard had said (because the people in Hima speak Himanese duhhh)'
delprint(e7)

action = get_player_input(" Press Enter to continue: ")
print ("-" * 92)

def delprint(e7, dell = 0.05): 
        for c6 in e7:      
            sys.stdout.write(c6) 
            sys.stdout.flush()
            time.sleep(dell)   
e7 = "But don't worry, I'll translate for you li'l buddy, as the guard was saying, 'Hey you! You ain't from around these parts, are ya? What's yer business in Hima? I'm gonna need to see some ID before I let ya in!'"
delprint(e7)

print ("-" * 92)

def delprint(e7, dell = 0.05): 
        for c6 in e7:      
            sys.stdout.write(c6) 
            sys.stdout.flush()
            time.sleep(dell) 
e7 = "You gulp and struggle to decide on what to respond with, you come up with a few options in a fraction of a second: 1. Try to lie yourself out of the situation and to get into the city 2. try to beat the shit out of the guard 3. Explain yoself truthfully and hope to god that he'll let you in."
delprint(e7)
print("-" * 92)
action = get_player_input(" Select the option you are going with by writing the number: ")
while True:
    if action == "1":
        luckyy = random.randint(1,3)
        if luckyy == 1:
            print("Your shitty lie somehow pulled through and he belived what you said about you needing to attack those monkey people and swore it was for a good reason")
            break
        
        elif luckyy == 2 or 3:

            e8 = "You tried lying to the big, strong, manly man in front of you, but it did not work on him and now he is furious and ready to fight! You can use 'check' to see your opponent's stats, see your own stats or attack. "
            delprint(e8)
            while True:    
                guard = True
                enraged_guard = True
                action = get_player_input("Choose an action: ")

                if action is None:
                    continue

                if action.lower() == 'attack':
                    player_turn()
                    input("Press Enter to continue...")
                    guard_turn()
                    guard = False
                    enraged_guard = False
                    if guard_stats['guard_hp'] <= 0:
                        print("You defeated the enraged guard! You now can go into the city! albeit illegally, but nonetheless, free entry!")
                        player_stats['xp'] += 45
                        if player_stats['xp'] >= player_stats['max_xp']:
                            lv_up()
                        break
                    elif player_stats['hp'] <= 0:
                        quit_game()
                else:
                  print("Invalid input, try again")
        break
    if action == "2":
        e9 = "you challenge the man to a battle, you said if you win you get into the city. He accepts your challenge!"        
        delprint(e9)
        while True:    
            guard = True
            enraged_guard = False
            action = get_player_input("Choose an action: ")

            if action is None:
                continue

            if action.lower() == 'attack':
                player_turn()
                input("Press Enter to continue...")
                guard_turn()
                guard = False
                enraged_guard = False
                if guard_stats['guard_hp'] <= 0:
                    print("You defeated the guard! You now can go into the city fair and square!")
                    player_stats['xp'] += 45
                    if player_stats['xp'] >= player_stats['max_xp']:
                        lv_up()
                    break
                elif player_stats['hp'] <= 0:
                    quit_game()
            else:
                print("Invalid input, try again")
        break
    if action == "3":
        unluckyy = random.randint(1,5)
        if unluckyy == 5:
            e9 = "You tell the truth to the guards.... and he didn't believe you! He asked you to please leave. However, you feel the heat rise in your face, your teeth gritting in anger as you curl your hand into a fist. You chose to be truthful and the guard did not believe you, now he'll pay for it. As you launch your knuckles into the mans jaw, for a split second you see his eyes twinge in fear. Another second and the man was on the floor, your knuckle bloodied and the guards jaw out of place"
            delprint(e9)
            e10 = "Wow, that was... extreme, you didn't really need to break his jaw and ruin his next 3-5 months of life, but you know... at least you can get into the town now!"
            delprint(e10)
            print("you got 1 xp")
            player_stats['xp'] += 1
            if player_stats['xp'] >= player_stats['max_xp']:
                lv_up()
            break
        else:
            e11 = "You tell the truth to the guards.... and he complimented your honesty and let you in!"
            delprint(e11)
            break
    break
action = get_player_input(" Press Enter to continue: ")
print ("-" * 92)

e12 = "As you enter through the open gates you gaze at the carvings, plated with gold and silver of soldiers standing tall. The ground under your feet turns from soft dirt, the like you have grown used to living in the countryside, to the shaped stone that paves roads and paths in larger cities like Hima."
delprint(e12)
action = get_player_input(" Press Enter to continue: ")
print ("-" * 92)

e13 = "Though it was the darkest part of the night you still saw candles lit outside houses and shops. The shadows played with your eyes and every pillar looked like a gargoyle come to life." 
delprint(e13)
action = get_player_input(" Press Enter to continue: ")

e14 = "Hungering for sleep and desiring for food the only thing weighing on you was the emptiness of your pockets." 
delprint(e14)
action = get_player_input(" Press Enter to continue: ")
print ("-" * 92)

e15 = "In your haste to leave your home you had neglected to bring any money with you, and were forced to sleep outside near the gate for the night... "
delprint(e15)
action = get_player_input(" Press Enter to continue: ")


e16 = "You arise from your slumber at the wake of dawn, as the city begins to move, so does your thinking, and you realise, YOU NEED MONEY BECAUSE THE GROUND WAS SHIT TO SLEEP ON!!! MISSION NUMBER 1, GET MONEY TO SLEEP ON BED!"
delprint(e16)
print ("-" * 92)

print ("You can now explore the city by typing up, down, right or left! And you can type map to see the map")
action = get_player_input(" Press Enter to continue: ")
while True:
    action = get_player_input("which direction: ")
    if action in ["up", "down", "left", "right"]:
        move_player(action)


    if action.lower() in ["check map", "map", "check_map"]:
        check_map(Hima_city_grid, player_x, player_y, explored_segments)
# When The player reaches the town of Hima, give them options to explore the city
# A few ideas being going to the blacksmith for upgrades and buying weapons
# This will be implemented when items are introduced  
# a store for buying stuff (decide on what to sell later) 
# Make an inventory system
# item system (use item, inspect item, etc...)
# in the city there will a library, tavern, quest guild, blacksmith, and maybe a potion place 
 

    if action.lower() == It.lower():
        print("heheheaaa")
        
        skibidi = int(33)
        print (skibidi * 2)


