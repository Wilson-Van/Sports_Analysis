# this is a Team class

class Team:
    # constructor method
    def __init__(self, id, name, city):
        self.id = id
        self.name = name
        self.city = city

    # to string method
    def __str__(self):
        return f"Name: {self.name} ID: {self.id} City: {self.city}"
    
    def __repr__(self):
        return self.__str__()
    
    #getter methods
    def get_name(self):
        return self.name
    
    def get_id(self):
        return self.id
    
    def get_city(self):
        return self.city