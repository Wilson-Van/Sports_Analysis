# Rushing Stats Class inherits from Stats
from .Stats import Stats

class Rushing(Stats):
    def __init__(self, total_yards, attempts, longest, over_twenty, td, fumbles):
        super.__init__(self, total_yards, attempts)
        self.longest = longest
        self.over_twenty = over_twenty
        self.td = td
        self.fumbles= fumbles