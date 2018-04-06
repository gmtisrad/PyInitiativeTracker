import operator

class player():
  def __init__(self):
    self.name = input ("Enter name: ")
    self.initiative = int (input("Enter %s's initiative: "%self.name))
  initiative = None
  name = None

class monster():
    def __init__(self, monster_count):
        self.initiative = int(input("Enter monster %d's initiative:", %monster_count))
        self.name = ("Monster%d", %monster_count)
    initiative = None
    name = None

number_of_players = int(input ("Enter the number of players: "))
number_of_monsters = int(input("Enter the number of monsters: "))
players = list ()
monsters = list()
entities = list()
sorted_entities = list()

for i in range(number_of_players):
  entities.append(player())
for i in range(number_of_monsters):
  entities.append(monster())

sorted_entities = sorted(entities, reverse = True, key=operator.attrgetter("initiative"))
for obj in entities:
    print ("{first}'s initiative is {second}".format(first = obj.name, second = obj.initiative))
for obj in sorted_entities:
    print ("{first}'s initiative is {second}".format(first = obj.name, second = obj.initiative))
