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
    print("Or if you are in the armor inventory, then 'remove' moves it out of the armor inventory and into the normal inventory")
    print ("You can type 'exit' to leave the inventory menu, or 'back' to unselect an item and go to the inventory menu")
    print("You can also type 'invetory' or 'show' to re open the inventory slots")
    print("-" * 92)
    help_checked = True
    check_inventory()

def Item_selected(slot):
    item = inventory[slot]
    while True:
        action = input("Choose an action: ").strip().lower()
        if action == "check":
            print(item)
        elif action == "remove" or action == "rm":
            if item.isInArmorInv:
                remove_armor_item(slot)
                break
            else:
                remove_item(slot)
                break
        elif action == "use":
            if item.isInArmorInv:
                print("Item is already equipped")
            else:
                use_item(slot)
                break
        elif action == "back":
            break
        else:
            print("Invalid action. Type 'check', 'remove', 'use', or 'back'.")
        # Make the connections to use an item or equip it

def Item_selected_armor(item, armor_slot):
    while True:
        action = input("Choose an action: ").strip().lower()
        if action == "check":
            print(item)
        elif action == "remove" or action == "rm":
            # Find empty inventory slot
            for i in range(len(inventory)):
                if inventory[i] is None:
                    inventory[i] = item
                    armor_inventory[armor_slot] = None
                    item.isInArmorInv = False
                    print(f"Removed {item.name} from armor inventory")
                    break
            break
        elif action == "use":
            print("Item is already equipped")
        elif action == "back":
            break
        else:
            print("Invalid action. Type 'check', 'remove', 'use', or 'back'.")


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
                print(f"{slots[i]}: {item.name}")
        # for i, item_index in enumerate(armor_inventory):
        #     if item_index is None:
        #         print(f"{slots[i]}: Empty")
        #     # elif inventory[item] is None:
        #     #     print(f"{slots[i]}: Empty")
        #     else:
        #         item = inventory[item_index]
        #         if item is None:
        #             print(f"{slots[i]}: Empty")
        #         else:
        #             print(f"{slots[i]}: {item.name}")
        print(92 * "-")
        print("type 'help' for instructions for the armor inventory system")
        print('\n')

inventory = [None] * 10
armor_inventory = [None, None, None, None]

def check_armor_inventory():
    while True:
        action = input("You are in the armor inventory menu, Enter the slot number (1-4) ").strip().lower()
        if action.isdigit():
            action = int(action) - 1
            if  0 <= action < len(armor_inventory):
                item = armor_inventory[action]
                if item is not None:
                    if hasattr(item, 'name'):
                        print(f"item selected is: {item.name}")
                        item.isInArmorInv = True
                        Item_selected_armor(item, action)
                    else:
                        print("aughhthhth why life is pain")
                else: 
                    print("This slot is empty")
            else:
                print("invalid slot")
        elif action == "help":
            Help()
        elif action == "exit" or action == "quit" or action == "exit inventory" or action == "leave":
            return
        elif action == "inventory" or action == "show inventory" or action == "open inventory" or action == "inv":
            check_inventory()
        elif action == "armor" or action == "armor inventory" or action == "open":
            armor_inventory_screen()

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
        elif action == "inventory" or action == "show inventory" or action == "open inventory" or action == "inv":
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
    def __init__(self, name, description, stats, effects, equippable, Class, isInArmorInv):
        self.name = name
        self.description = description
        self.stats = stats
        self.effects = effects
        self.equippable = equippable
        self.Class = Class
        self.isInArmorInv = isInArmorInv

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
    item = inventory[slot]
    if isinstance(item, Armor):
        if armor_inventory[0] is None:
            armor_inventory[0] = item
            inventory[slot] = None
            print(f"Added {item.name} to armor slot")
        else:
            print("Armor slot is already occupied")
    elif isinstance(item, Weapons):
        if armor_inventory[1] is None:
            armor_inventory[1] = item
            inventory[slot] = None
            print(f"Added {item.name} to weapon slot")
        else:
            print("Weapon slot is already occupied")
    elif isinstance(item, Trinkets):
        if armor_inventory[2] is None:
            armor_inventory[2] = item
            inventory[slot] = None
            print(f"Added {item.name} to trinket slot 1")
        elif armor_inventory[3] is None:
            armor_inventory[3] = item
            inventory[slot] = None
            print(f"Added {item.name} to trinket slot 2")
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
    item = inventory[slot]
    if item.stats is not None:
        if item.equippable is True:
            add_to_armor_inventory(slot)
        else:
            print("not so skibidi")
    else:
        print("no stats")
        
def remove_armor_item(slot):
    item = inventory[slot]
    if item.isInArmorInv is True:
        item.isInArmorInv = False
        armor_inventory[armor_inventory.index(slot)] = None
        inventory[slot] = item
        print(f"Removed {item.name} from armor inventory")

class Trinkets(Item):
    pass


def add_trinket(trinket):
    add_item(trinket)

class Weapons(Item):
    def __init__(self, name, description, damage, special_effects, equippable, Class, isInArmorInv):
        super().__init__(name, description, damage, special_effects, equippable, Class, isInArmorInv)


def add_weapon(weapon):
    add_item(weapon)

class Armor(Item):
    def __init__(self, name, description, damage, special_effects, equippable, Class, isInArmorInv):
        super().__init__(name, description, damage, special_effects, equippable, Class, isInArmorInv)


def add_armor(armor):
    add_item(armor)

trumpet = Item(
    "Trumpet",
    "Makes a Funny toot sound!",
    None,
    "trumpet sound.mp3",
    False,
    Class=Item,
    isInArmorInv=False,
)
epic_sword_of_death = Weapons(
    'Epic sword of death',
    '"This thing is so epic it kills all things to death"',
    1,
    "idkkk it does killy thing",
    True,
    Class=Weapons,
    isInArmorInv = False,
)
super_armor = Armor(
    "Super armor",
    "It is supa armor",
    5,
    "superly defends against everything",
    True,
    Class=Armor,
    isInArmorInv = False,
)
supa_armor = Armor(
    "Supa armor",
    "It is super armor",
    5,
    "supaly defends against everything",
    True,
    Class=Armor,
    isInArmorInv=False,
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




