"""
Megan Hanna
This game is about navigating around a mountain, starting in an underground cave,
and collecting different materials to start a fire. You also must find and drink
some water on the way.
December 4, 2023
"""

class Item:
    """creating a class called Item, and creating methods that will be called by the Game class"""

    def __init__(self, name, desc, weight = 0, edible = False):
        """setting initial variables, and tells the game the information for the items"""
        self.name = name
        self.desc = desc
        self.weight = weight
        self.edible = edible

    def __str__(self):
        """returns a description of the item"""
        return f'{self.desc}'

    def is_edible(self):
        """tells you whether an item is edible or not"""
        return self.edible
    

    def get_weight(self):
        """returns weight of an item"""
        return self.weight

    def get_name(self):
        """returns the name of an item"""
        return self.name

    def get_description(self):
        """returns a description of an item"""
        return self.desc

    def set_weight(self, wt):
        """sets an item's weight that is found"""
        self.weight = wt

    def set_name(self, name):
        """sets the name as an object found"""
        self.name = name

    def set_description(self, desc):
        """sets the description of the new item found"""
        self.desc = desc

    def set_edible(self, edible):
        """updates whether the item is edible or not"""
        self.edible = edible


