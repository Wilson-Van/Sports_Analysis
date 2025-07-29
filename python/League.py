# this is a League class

class League:
    # constructor method
    def __init__(self, id, name, seasons):
        self.id = id
        self.name = name
        self.seasons = seasons

    # to string method
    def __str__(self):
        return f"Name: {self.name} ID: {self.id} Seasons: {self.seasons}\n"
    
    def __repr__(self):
        return self.__str__()
    
    #getter methods
    def get_name(self):
        return self.name
    
    def get_id(self):
        return self.id
    
    def get_seasons(self):
        return self.seasons