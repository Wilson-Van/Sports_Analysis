# Passing Stats Class inherits from Stats
from .Stats import Stats

class Passing(Stats):
    def __init__(self, total_yards, attempts, completions, comp_pct, longest, td, picks, sacks, qbr):
        super.__init__(self, total_yards, attempts)
        self.completions = completions
        self.comp_pct = comp_pct
        self.longest = longest
        self.td = td
        self.picks = picks
        self.sacks = sacks
        self.qbr = qbr