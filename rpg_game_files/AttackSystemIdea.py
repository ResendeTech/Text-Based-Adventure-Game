import random
weapons = ["Sword", "Spell", "Fire"]
shields = ["Armour", "Magic", "Water"]

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = 0
        self.shield = 0

    def damage(self):
        points = random.randint(10, 35)
        self.health -= points

    def selectWeapon(self):
        choice = int(input("Choose your weapon 1-Sword, 2-Spell or 3-Fire:  "))
        self.weapon = choice - 1

    def selectShield(self):
        choice = int(input("Choose your shield 1-Armour, 2-Magic or 3-Water:  "))
        self.shield = choice - 1


# Child class of player with override methods for weapon
# and shield selection
class AiPlayer(Player):
    def __init__(self,name):
        super().__init__(name)

    def selectWeapon(self):
        choice = random.randint(1, 3)
        self.weapon = choice - 1

    def selectShield(self):
        choice = random.randint(1, 3)
        self.shield = choice - 1

class Game:
    def __init__(self):
        self.gameOver = False
        self.round = 0

    def newRound(self):
        self.round += 1
        print("\n***   Round: %d   ***\n" %(self.round))  

    # Check if either or both Players is below zero health
    def checkWin(self, player, opponent):
        if player.health < 1 and opponent.health > 0:
            self.gameOver = True
            print("You Lose")
        elif opponent.health < 1 and player.health > 0:
            self.gameOver = True
            print("You Win")
        elif player.health < 1 and ai.health < 1:
            self.gameOver = True
            print("*** Draw ***")


    def displayResult(self, player, opponent):
            print("%s used a %s, %s used a %s Shield\n" %(player.name, weapons[player.weapon], opponent.name, shields[opponent.shield]))
            print("%s caused damage to %s\n" %(player.name, opponent.name))

    def takeTurn(self, player, opponent):

        # Decision Array
        #
        #           Armour|  Magic |  Water
        #           ______|________|_______
        # Sword:    False |  True  |  True
        # Spell:    True  |  False |  True   
        # Fire :    True  |  True  |  False

        decisionArray = [[False, True, True], [True, False, True], [True, True, False]]
        if decisionArray[player.weapon][opponent.shield]:
            opponent.damage()
            currentGame.displayResult(player, opponent)
        else:
            print("\n%s used a %s, %s used a %s Shield" %(player.name, weapons[player.weapon], opponent.name, shields[opponent.shield]))
            print("%s blocked %s's attack - No Damage" %(opponent.name, player.name))


# Setup Game Objects
currentGame = Game()
human = Player("Mark")
ai = AiPlayer("Computer")

players = [human, ai]

# Main Game Loop
while not currentGame.gameOver:
    for player in players:
        player.selectWeapon()
        player.selectShield()
    currentGame.newRound()
    currentGame.takeTurn(human, ai)
    currentGame.takeTurn(ai, human)
    print("%s's health = %d" %(human.name, human.health))
    print("%s's health = %d" %(ai.name, ai.health))
    currentGame.checkWin(human, ai)