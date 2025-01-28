# Map of city part of the game


def quit_game():
    # if player_stats['hp'] <= 0:
    #     print("You have died, game over")
    #     exit()
    action = input("Are you sure you want to quit? Y/N: ")
    if action.lower() == 'y':
        print("you have quit the game")
        exit()
    elif action.lower() == 'n':
        print("You have chosen to continue playing")
        return False
    
explored_segments = set()
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
    print("You have entered the library. You can read books here.")
    
def enter_goonCave():
    print("You have entered the goon cave. You feel your legs sticking to the ground, there's a foul smell in the air. You pick up some of the white liquid and start gulping it down.")
    print("you start gooning... you can't stop gooning, you feel your life sapping out of you as you goon, YOU DIE")

def enter_shop():
    print("You have entered the shop. You can buy items here.")

def enter_tavern():
    print("You have entered the tavern. You can rest here.")

def enter_blacksmith():
    print("You have entered the blacksmith. You can forge weapons here.")

def enter_guild():
    print("You have entered the guild. You can take quests here.")


location_actions = {
    "library": enter_library,
    "shop": enter_shop,
    "tavern": enter_tavern,
    "blacksmith": enter_blacksmith,
    "guild": enter_guild,
    "goon_cave": enter_goonCave,
}

player_x, player_y = 4, 2
explored_segments.add((player_x, player_y))

# x and y co-ordinates are flipped, change it later
# move direction function
def move_player(direction):
    global player_x, player_y
    new_x, new_y = player_x, player_y

    if direction == "up" and player_y > 0 and player_x < len(Hima_city_grid[player_y - 1]) > 0:
        new_y -= 1
        if Hima_city_grid[new_y][new_x] == "wall":
            print("You can't move in that direction. There's a wall.")
            new_y += 1
    elif direction == "down" and player_y < len(Hima_city_grid) - 1 and player_x < len(Hima_city_grid[player_y + 1]):
        new_y += 1
        if Hima_city_grid[new_y][new_x] == "wall":
            print("You can't move in that direction. There's a wall.")
            new_y -= 1
    elif direction == "left" and player_x > 0:
        new_x -= 1
        if Hima_city_grid[new_y][new_x] == "wall":
            print("You can't move in that direction. There's a wall.")
            new_x += 1
    elif direction == "right" and player_x < len(Hima_city_grid[player_y]) - 1:
        new_x += 1
        if Hima_city_grid[new_y][new_x] == "wall":
            print("You can't move in that direction. There's a wall.")
            new_x -= 1
    else:
        print("Invalid move")
        return
    
    print(f"player_y:{player_y} and new_y: {new_y}")
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
             print(f"{direction.capitalize()} ({i}, {j}): {Hima_city_grid[i][j]}")

    
    current_location = Hima_city_grid[x][y]
    if current_location in location_actions:
        choice = input(f"Do you want to enter the {current_location}? (enter/skip): ").strip().lower()
        if choice == "enter":
            location_actions[current_location]()
            for direction, (i, j) in surroundings.items():
                if 0 <= i < rows and 0 <= j < len(Hima_city_grid[i]):
                    print(f"{direction.capitalize()} ({i}, {j}): {Hima_city_grid[i][j]}")
        # make an else statement for invalid input

def check_map(grid, player_x, player_y, explored_segments):
    for j, row in enumerate(grid):
        for i, cell in enumerate(row):
            if (i, j) == (player_x, player_y):
                 print(f"{cell}/Player", end=" | ")
            elif (i, j) in explored_segments:
                print(cell, end=" | ")
            else:
                print("???", end=" | ")
        print()


while True:
    action = input("Which direction: ").strip().lower()
    if action in ["up", "down", "left", "right"]:
        move_player(action)
    # action = input("which direction: ")
    # if action == "up":
    #     direction = "up"
    #     move_player(direction)
    # elif action == "down":
    #     direction = "down"
    #     move_player(direction)
    # elif action == "right":
    #     direction = "right"
    #     move_player(direction)
    # elif action == "left":
    #     direction = "left"
    #     move_player(direction)
        
    if action.lower() in ["check map", "map", "check_map"]:
        check_map(Hima_city_grid, player_x, player_y, explored_segments)

    if action.lower() == "quit":
        quit_game()
# Add a map feature
# Add logic to the location functions, like library, tavern, guild, etc
# Add secret areas for the lollsss
# remove the goon cave