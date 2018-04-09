import operator
import random
import os

#****Class Definitions****
#Abstract Base Class for game entities
class entity():
    name = None
    initiative = None

#Implementation of subclass of entity for player objects
class player(entity):
    def __init__(self):
        self.get_name()
        self.get_initiative()
    def get_name(self):
        self.name = input ("Enter player name: ")
    def get_initiative(self):
        self.initiative = int(input("Enter %s's initiative: " % (self.name)))

#Implementation of subclass of entity for monster/creature
class monster(entity):
    def __init__(self, monster_count):
        self.set_name(monster_count)
        self.get_dex_mod()
        self.set_initiative()

    def get_dex_mod(self, monster_count):
        self.dex_mod = int(input("Enter monster group %d's dexterity modifier: "))

    def set_initiative(self):
        self.initiative = int(random.randint(1, 20) + dex_mod)

    def set_name(self, monster_count):
        self.name = ("Monster Group %d" % (monster_count))

    dex_mod = 0

#****Start Program****
new_game = None

os.system ('cls')

#Retrieves number of players from the user
number_of_players = int(input ("Enter the number of players: "))

#Initializes empty lists to contain players outside of the loop
players = []

#Populates player list with initialized objects to be stored
for i in range(0, number_of_players):
  players.append(player())
#Begin program loop
while (new_game != 'Q' or new_game != 'q'):
    monsters = []
    entities = []
    sorted_entities = []
    os.system ('cls')

    #Retrieves number of monsters from the user
    number_of_monsters = int(input("Enter the number of monsters: "))

    #Gets the initiative for all entities
    for i in range(0, number_of_monsters):
        monsters.append(monster(int(i + 1)))
    for i in players:
        i.get_initiative()

    #Compiles entities into one list and sorts them in descending (reversed) initiative order
    entities = players + monsters
    sorted_entities = sorted(entities, reverse = True, key=operator.attrgetter("initiative"))

    #Prints the sorted list of entities
    os.system('cls')
    for obj in sorted_entities:
        print ("%s's initiative is %d" % (obj.name, obj.initiative))
    new_game = input ("(Enter) - New Battle    (Q) - Quit\n")
