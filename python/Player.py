# this is a Player class

class Player:
    # constructor method
    def __init__(self, id, name, stats):
        self.id = id
        self.name = name
        self.stats = stats

    # to string method
    def __str__(self):
        return f"Name: {self.name} ID: {self.id}"
    
    def __repr__(self):
        return self.__str__()
    
    #getter methods
    def get_name(self):
        return self.name
    
    def get_id(self):
        return self.id
    
    def get_stats(self):
        return self.stats
    