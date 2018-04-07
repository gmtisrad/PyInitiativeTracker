import operator
import random
import os

#Abstract Base Class for game entities
class entity():
    name = None
    initiative = None

#Implementation of entity for player objects
class player(entity):
    def __init__(self):
        self.name = input ("Enter name: ")
    def get_initiative(self):
        self.initiative = int (input("Enter %s's initiative: " % (self.name)))

#Implementation of entity for monster/creature objects
class monster(entity):
    def __init__(self, monster_count):
        self.initiative = int(random.randint(1, 20))
        self.name = ("Monster%d" % (monster_count))
    dex_mod = 0

new_game = None

os.system ('cls')

#Retrieves number of players from the user
number_of_players = int(input ("Enter the number of players: "))

#Initializes empty lists to contain players outside of the loop
players = []

#Populates player list with initialized objects to be stored
for i in range(0, number_of_players):
  players.append(player())

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

    #Compiles entities into one list and sorts them in descending initiative order
    entities = players + monsters
    sorted_entities = sorted(entities, reverse = True, key=operator.attrgetter("initiative"))

    #Prints the sorted list of entities
    os.system('cls')
    for obj in sorted_entities:
        print ("%s's initiative is %d" % (obj.name, obj.initiative))
    new_game = input ("(Enter) - New Battle    (Q) - Quit\n")
