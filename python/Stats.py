# Stats Class

class Stats:
    # Constructor
    def __init__(self, total_yards, attempts):
        self.total_yards= total_yards
        self.attempts = attempts
        # there is an avg yards in the api, however this seems easier than finding the dictionary for the avg in the array response 
        self.avg_yards = total_yards/attempts
    
    def __str__(self):
        return f"Total Yards: {self.total_yards} Attempts: {self.attempts} Average Yards: {self.avg_yards}"
    
    def display(self):
        return self.__str__()
    
    # getters
    def get_total_yards(self):
        return self.total_yards
    
    def get_attempts(self):
        return self.attempts
    
    def get_avg_yards(self):
        return self.avg_yards