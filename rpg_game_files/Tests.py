import time
import sys
# x = time.sleep(1)

# if x is None:
#     print("skibidi")

# def get_player_input(prompt):
#     while True:
#         action = input(prompt)


#         else:
#             return action
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

help_checked = False

def Help():
    global help_checked
    print("-" * 92)
    print ("You are in the inventory menu. You can select items by typing its slot number (1-10)")
    print("typing 'use' to use or equip an item and typing 'check' to check an item.")
    print("Type'remove' or 'rm' to remove an item from your inventory.")
    print ("You can type 'exit' to leave the inventory menu, or 'back' to unselect an item and go to the inventory menu")
    print("You can also type 'invetory' or 'show' to re open the inventory slots")
    print("-" * 92)
    help_checked = True
    check_inventory()

def Item_selected(slot):
    while True:
        action = input(f"Choose an action: ").strip().lower()
        if action == "check":
            print(inventory[slot])
        elif action == "remove" or action == "rm":
            remove_item(int(slot))
            break
        elif action == "use":
            use_item(int(slot))
            break
        elif action == "back":
            #check_inventory()
            break
        else:
            print("Invalid action. Type 'check', 'remove', 'use', or 'back'.")
        # Make the connections to use an item or equip it

def inventory_screen():
        print('\n')
        print(92 * "-")
        print("INVENTORY:")
        if not inventory:
            print("There is nothing in your inventory")
            return 
        for i, item in enumerate(inventory):
            if item is None:
                print(f"Slot {i + 1}: Empty")
            elif isinstance(item, Trinkets):
                print(f"Slot {i + 1}: {item.name}")
            elif isinstance(item, Weapons):
                print(f"Slot {i + 1}: {item.name}")
            elif isinstance(item, Armor):
                print(f"Slot {i + 1}: {item.name}")
            else:
                print(f"Slot {i + 1}: {item.name}")
        print(92 * "-")
        print("type 'help' for instructions for the inventory system")

def armor_inventory_screen():
        print('\n')
        print(92 * "-")
        print("ARMOR INVENTORY:")
        slots = ["Armor", "Weapon", "Trinket 1", "Trinket 2"]
        for i, item in enumerate(armor_inventory):
            if item is None:
                print(f"{slots[i]}: Empty")
            else:
                print(f"{slots[i]}: {inventory[item].name}")
        print(92 * "-")
        print("type 'help' for instructions for the armor inventory system")
        print('\n')

inventory = [None] * 10
armor_inventory = [None, None, None, None]

def check_armor_inventory():
    global isInArmor
    while True:
        action = input("You are in the armor inventory menu, Enter the slot number (1-4) ").strip().lower()
        if action.isdigit():
            action = int(action) - 1
            if  0 <= action < len(armor_inventory):
                if  armor_inventory[action] is not None:
                    item = inventory[armor_inventory[action]]
                    if hasattr(item, 'name'):
                        print(f"item selected is: {item.name}")
                        slot = action
                        slot = int(slot)

                        Item_selected(int(slot))
                    else:
                        print ("It doesnt fucking workkk")
                else: 
                    print("This slot is empty")
            else:
                print("invalid slot")
        elif action == "help":
            Help()
        elif action == "exit" or action == "quit" or action == "exit inventory" or action == "leave":
            return
        elif action == "inventory" or action == "show inventory" or action == "open inventory":
            check_inventory()

def check_inventory():
    global help_checked
    if help_checked == False:
        inventory_screen()
    help_checked = False
    while True:
        action = input("You are in the inventory menu, Choose an action: ").strip().lower()
        if action.isdigit():
            action = int(action) - 1
            if  0 <= action < len(inventory):
                if  inventory[action] is not None:
                    print(f"item selected is: {inventory[action].name}")
                    slot = action
                    slot = int(slot)
                    Item_selected(int(slot))
                else: 
                    print("This slot is empty")
            else:
                print("invalid slot")
        elif action == "help":
            Help()
        elif action == "exit" or action == "quit" or action == "exit inventory" or action == "leave":
            return
        elif action == "inventory" or action == "show inventory" or action == "open inventory":
            inventory_screen()
        elif action == "armor inventory" or action == "armor" or action == "armory" or action == "show armor" or action == "open armor":
            armor_inventory_screen()
            check_armor_inventory()

        else:
            print("Invalid input")

    # when the inventory is shown, be able to leave the inventory by typing back
    # Be able to check, use, and drop items
    # To check, use the number slots of the inventory to be able to decide which item is going to be checked 
     # So it doesnt matter what item is there, since it's not dependent on that
    # this method will be used for the use and drop features as well
    # To do this, the implementation of a while loop might be needed

class Item:
    def __init__(self, name, description, stats, effects, equippable, Class):
        self.name = name
        self.description = description
        self.stats = stats
        self.effects = effects
        self.equippable = equippable
        self.Class = Class

    def __str__(self):    
        if isinstance(self, Armor):
            return f"""{self.name}: 
            Description: {self.description} 
            Defense: {self.stats} 
            Effects: {self.effects}
            Equippable: {self.equippable}"""
        
        elif isinstance(self, Weapons):
            return f"""{self.name}: 
            {self.description} 
            Damage : {self.stats} 
            Effects: {self.effects}
            Equippable: {self.equippable}"""
        
        elif isinstance(self, Trinkets):
            return f"""{self.name}: 
            {self.description} 
            Stats: {self.stats} 
            Effects: {self.effects}
            Equippable: {self.equippable}"""
        
        else: 
            if self.stats is not None:
                return f"""{self.name}: 
                Description: {self.description} 
                Stats: {self.stats} 
                Effects: {self.effects}
                Equippable: {self.equippable}"""
            else:
                return f"""{self.name}: 
                Description: {self.description} 
                Effects: {self.effects}
                Equippable: {self.equippable}"""
            
def add_item(item):
    for i in range(len(inventory)):
        if inventory[i] is None:
            inventory[i] = item
            print(f"Added {item.name} to inventory")
            return
    print("Inventory is full")

def add_to_armor_inventory(slot):
    if inventory[slot].Class == Armor:
        if armor_inventory[0] is None:
            armor_inventory[0] = slot
            print(f"Added {inventory[slot].name} to armor slot")
        else:
            print("Armor slot is already occupied")
    elif inventory[slot].Class == Weapons:
        if armor_inventory[1] is None:
            armor_inventory[1] = slot
            print(f"Added {inventory[slot].name} to weapon slot")
        else:
            print("Weapon slot is already occupied")
    elif inventory[slot].Class == Trinkets:
        if armor_inventory[2] is None:
            armor_inventory[2] = slot
            print(f"Added {slot.name} to trinket slot 1")
        elif armor_inventory[3] is None:
            armor_inventory[3] = slot
            print(f"Added {slot.name} to trinket slot 2")
        else:
            print("Both trinket slots are already occupied")
    else:
        print("Invalid item type for armor inventory")



def remove_item(slot):
    if 0 <= slot < len(inventory):
        if inventory[slot] is not None:
            item_name = inventory[slot].name
            inventory[slot] = None
            print(f"Removed {item_name} from inventory")
        else:
            print("inventory slot is already empty")
    else:        
        print("Invalid inventory slot")

def use_item(slot):
    if inventory[slot].stats is not None:
        if inventory[slot].equippable is True:
            add_to_armor_inventory(slot)
            #remove_item(slot)
            
            # make an armor inventory
            # add the equippaable item to its specific location in the armor inventory
            # remove the item from this inventory
        else:
            print("not so skibidi")
    else:
        print("no stats")

class Trinkets(Item):
    pass


def add_trinket(trinket):
    add_item(trinket)

class Weapons(Item):
    def __init__(self, name, description, damage, special_effects, equippable, Class):
        super().__init__(name, description, damage, special_effects, equippable, Class)


def add_weapon(weapon):
    add_item(weapon)

class Armor(Item):
    def __init__(self, name, description, damage, special_effects, equippable, Class):
        super().__init__(name, description, damage, special_effects, equippable, Class)


def add_armor(armor):
    add_item(armor)

trumpet = Item(
    "Trumpet",
    "Makes a Funny toot sound!",
    None,
    "trumpet sound.mp3",
    False,
    Class=Item
)
epic_sword_of_death = Weapons(
    'Epic sword of death',
    '"This thing is so epic it kills all things to death"',
    1,
    "idkkk it does killy thing",
    True,
    Class=Weapons,
)
super_armor = Armor(
    "Super armor",
    "It is supa armor",
    5,
    "superly defends against everything",
    True,
    Class=Armor,
)
supa_armor = Armor(
    "Supa armor",
    "It is super armor",
    5,
    "supaly defends against everything",
    True,
    Class=Armor
)


add_weapon(epic_sword_of_death) 
add_item(trumpet)
add_armor(super_armor)
add_armor(supa_armor)

def delprint(e1, dell = 0.05): 
    global i
    i = dell
    for c in e1: 
        i += dell
        sys.stdout.write(c) # Write character to console without newline
        sys.stdout.flush() # Force the buffer to write to console immediately
        time.sleep(dell) # Delay for the specified time

check_inventory()
e1 = "skbidiiiiii"
delprint(e1)
print (i)


if time.sleep(i) is None:
    start = input(" Enter to continue:")
    pass
remove_item(trumpet)
check_inventory()




