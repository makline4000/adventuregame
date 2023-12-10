'''
Megan Hanna
This game is about navigating around a mountain, starting in an underground cave,
and collecting different materials to start a fire. You also must find and drink
some water on the way.
December 4, 2023
'''

from Item import Item 

class Location:
    """creating a class called Location,
    creating a list of moves and directions to take"""

    neighbors = {}

    def __init__(self, desc, thing=None):
        """updating items and locations found"""
        self.desc = desc
        self.thing = thing

    def get_item(self):
        """returning an item's name"""
        return self.thing

    def get_description(self):
        """returning description of item found"""
        return self.desc

    def set_item(self, thing):
        """setting item as the thing found"""
        self.thing = thing

    def has_item(self):
        """seeing if an item is in your possession"""
        
        #checking if the item is found in your possession, returning true if it is
        if self.thing != None:
            has_item = True
        else:
            has_item = False
        return has_item

    def add_neighbor(self, dir, loc):
        """adding a location to the map"""
        self.loc = loc
        self.neighbors[dir] = self.loc
        
    def get_neighbor(self, dir):
        """the ability to see if a location exists and is available to move to"""
        
        #checking if the direction input has neighbors to that direction
        if dir in self.neighbors:
            return self.neighbors[dir]
        else:
            return None

    def remove_item(self):
        """removing items from possession"""
        removed_item = self.thing
        self.thing = None
        return removed_item

    def __str__(self):
        """guiding the movements of the game, and returning where you are
        and if you've found an item"""
        
        statement = f'You are {self.desc} \n'
        
        #this loop checks a location to see if it holds an item, 
        #and returns the name of the item found
        if self.thing != None:
            statement = statement + f'You see {self.thing}'
        return statement

