'''
Megan Hanna
This game is about navigating around a mountain, starting in an underground cave,
and collecting different materials to start a fire. You also must find and drink
some water on the way.
December 4, 2023
'''


from Item import Item
from Location import Location

class Game:
    """creating a class called Game"""

    def __init__(self):
        """setting the initial start of the game, and making a satchel for possessions"""
        self.mystuff = []
        self.create_world()
        self.currentroom = self.cave
        self.set_welcome_message()

    def create_world(self):
        """creating locations and items for the world, along with setting their locations and directions"""
        self.flint = Item('flint', 'flintstones', 5, False)
        self.feathers = Item('feathers', 'bird feathers', 1, False)
        self.wood = Item('wood', 'fire wood', 55, False)
        self.sticks = Item('sticks', 'a bunch of sticks', 15, False)
        self. apple = Item('apple', 'an apple', .5, True)


        self.cave = Location('in a cave', None)
        self.tunnel = Location('a tunnel from the cave', None)
        self.underground = Location('in an underground room', self.flint)
        self.ladder = Location('at the ladder at the end of the underground room', None)
        self.landing = Location('on a grassy wooded area', self.wood)
        self.peak = Location('at the top of the mountain', self.feathers)
        self.tree = Location('under an apple tree', self.apple)
        self.pond = Location('near a pond', self.sticks)

        self.cave.add_neighbor('east', self.tunnel)
        self.tunnel.add_neighbor('west', self.cave)
        self.tunnel.add_neighbor('east', self.underground)
        self.underground.add_neighbor('west', self.tunnel)
        self.underground.add_neighbor('east', self.ladder)
        self.ladder.add_neighbor('east', self.underground)
        self.ladder.add_neighbor('down', self.underground)
        self.ladder.add_neighbor('up', self.landing)
        self.landing.add_neighbor('south', self.ladder)
        self.landing.add_neighbor('west', self.pond)
        self.landing.add_neighbor('east', self.tree)
        self.landing.add_neighbor('north', self.peak)
        self.pond.add_neighbor('east', self.landing)
        self.peak.add_neighbor('south', self.landing)
        self.tree.add_neighbor('west', self.landing)

    def get_current_location(self):
        """printing out the current location"""
        return self.currentroom

    def go(self, dir):
        """the call to move around the map if the direction is available"""
        next = self.currentroom.get_neighbor(dir)

        #this loop checks to see if there is the direction associated with the location, and if there is, the player will move to that location
        if next == None:
            self.msg = "Direction not available"
        else:
            self.currentroom = next
            self.msg = self.currentroom.__str__()

    def get_message(self):
        """returning the game's updated commands"""
        return self.msg

    def set_welcome_message(self):
        """setting the message for the beginning of the game"""
        self.msg = f'Welcome to the Mountain! Navigate around the mountain while collecting fire starting materials to build a firego. Be sure to find an apple! '

    def parse_command(self):
        """the inputs from the player are split up and set as commands for the game"""
        words = input('Enter>>> ').split()
        first = words[0]

        # checking to see if there is a second command, and than returning the input to the commands of the game
        if len(words) > 1:
            second = words[1]
        else:
            second = None
        return first, second

    def start(self):
        first = ''

        #this loop will continue if the input is not 'quit'
        while (first != 'quit') and not over:

            first, second = self.parse_command()

            #if the input is go, the game will go in the direction inputted
            if first == 'go':
                self.go(second)

            #this loop looks around the room if the command is given
            elif first == 'look':
                self.look()

            #if help is typed, a hint for the game appears
            elif first == 'help':
                self.help()

            #list is called, the list method is called and produces the inventory of the satchel
            elif first == 'list':
                self.list()

            #this method picks up an item if the pickup method is called by typing 'pickup'
            elif first == 'pickup':
                self.pickup()

            elif first == 'eat':
                self.eat(second)

            #when 'drop' is given, the drop method removes an item from the satchel
            elif first == 'drop':
                self.drop(second)

            #the search method searches for a specific item in the satchel
            elif first == 'search pouch':
                self.search_pouch().get_item(second)

            #this method checks to see if the requirements of the game ending have been completed
            elif first == 'game over':
                self.game_over()

            #this method climbs the ladder when called
            elif first == 'climb':
                self.climb()

            #this command picks an apple from the tree, which is required to end the game
            elif first == 'pick':
                self.pick()

            over = self.game_over()


        print(self.get_message())

    def look(self):
        """getting location information"""
        self.msg = self.currentroom

    def help(self):
        """returning the hints for the game"""
        self.msg = 'You are lost in a mountain!\n   -Look for (3) fire-starting objects to pickup'\
                   '\n   -Pick an apple to eat\n   -Find a good location to set up camp by dropping\n'\
                   '   -Be in an area to build a fire(Hint: End up near the pond).'

    def list(self):
        """how to output a list of items in your possession"""
        self.msg ='You are holding:\n'

        #this loop is changing the games message to each item iterated through in the satchel
        for i in self.mystuff:
            self.msg += f'   {i}'

    def pickup(self):
        """if a location has an item, the pick up command will add it to your satchel"""

        #these loops check if a location has an item, checks to see if it is able to be picked up, and adds the item to the satchel if both of those things
        #come back as true to existing and being light enough. Also updates the message of the game to communicate to the player what is happening.
        if not self.currentroom.has_item():
            self.msg = 'Location has no items to pickup'
        elif self.currentroom.get_item().get_weight() > 50:   #calling method and instead of assigning were saying this is an item and allows us to call item method
            self.msg = 'The material is too heavy to pickup'
        elif self.currentroom.get_item() == 'apple':
            self.msg = 'You must -pick apple-'
        else:
            self.thing = self.currentroom.remove_item()
            self.msg = f'You have added {self.thing} to your satchel'
            self.mystuff.append(self.thing)

    def drop(self, name):
        """this command removes all items from satchel if you are at the pond to start a fire"""
        self.msg = f'You are not holding {name}'
        #removing all items from possession once you are at the pond'
        for i in self.mystuff:
            if i.get_name() == name:
                item = self.mystuff.remove(i)
                self.currentroom.set_item(item)
                self.msg = f'You have removed {i} from your satchel'

    def search_pouch(self, name):
        """searching for a specific item in the satchel"""

       #loop to iterate through the satchel to check if the item is in the bag, returning none if it isn't, and the item's name if it is
        found = None
        for i in self.mystuff:
            if i.get_name() == name:
                found = i
        return found

    def eat(self, name):
        """the command to eat the item"""
        self.name = name
        item = self.search_pouch(self.name)

        #checking to see if the item is edible by calling the is_edible method
        if item == None:
            self.msg = 'Not holding an item'
        elif item.is_edible():
            #self.msg = 'You found an apple\n'
            self.msg += '\nYou ate the apple. Good job!\nNow go to the pond once you have all three items to win the game'
            self.mystuff.remove(item)
            #self.msg += 'You no longer have an apple'
        else:
            self.msg = 'These are materials for a fire aka NOT FOOD'

    def game_over(self):
        """checking to see if the game is over."""
        self.gameover = False

        #checking to see if you dropped all the items, and are at the pond. Giving you help and telling you the game isn't over if those things aren't true
        if (len(self.mystuff) == 3) and (self.currentroom == self.pond):
            self.msg = 'Congradulations! You might survive The Mountain. May the odds be ever in your favor'
            self.gameover = True
        else:
            self.gameover = False
            self.help()
        return self.gameover

    def climb(self):
        """command to climb to ladder when you approach it"""

        #checking to see if you are at the ladder in order to climb it
        if self.currentroom == self.ladder:
            self.msg = 'You are climbing the ladder'


    def pick(self):
        """the command to pick the apple once you find it on the tree"""

        #if you are at the tree, you ave found the apple
        if self.currentroom == self.tree:
            #self.msg = 'You picked an apple'
            #print(self.msg)
            self.pickup()
            self.msg = 'You picked an apple'





    def auto_win(self):
        g = Game()
        print(g.get_message())
        g.pickup()
        print(g.get_message())
        g.go("south")
        print(g.get_message())
        g.drop("flint")
        print(g.get_message())
        g.go("north")
        print(g.get_message())
        g.go("south")
        print(g.get_message())
        g.pickup()
        print(g.get_message())
        if (g.game_over()):
            print(g.get_message())

if __name__ == '__main__':
    g = Game()
    g.start()

