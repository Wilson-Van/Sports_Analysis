# Recieving Stats Class inherits from Stats
from .Stats import Stats

class Recieving(Stats):
    def __init__(self, total_yards, attempts, yac, longest, over_twenty, td, fumbles):
        super.__init__(self, total_yards, attempts)
        self.yac = yac
        self.longest = longest
        self.over_twenty = over_twenty
        self.td = td
        self.fumbles= fumbles