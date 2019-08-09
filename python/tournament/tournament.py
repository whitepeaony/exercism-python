class Results(object):
    # A class used to store and compare teams results
    # through the tournament. Attributes can be changed
    # with add_ methods. String representation generates
    # a table row for output. Implementation of < operator
    # allows sorting by points (and breaking ties by name).
    def __init__(self, name):
        self.name = name
        self.matches_played = 0
        self.matches_won = 0
        self.matches_drawn = 0
        self.matches_lost = 0
    
    def add_win(self):
        pass

    def add_draw(self):
        pass

    def add_loss(self):
        pass

    def points(self):
        pass
        return 0

    def __le__(self, other: Results) -> bool:
        # compare with other Results based on points,
        # breaking ties with alphabetical order of names
        return True 
        
    _repr_str = "{:30} | {:>2} | {:>2} | {:>2} | {:>2} | {:>2}"
    
    def __repr__(self):
        return _repr_str.format(self.name, self.points(),
            self.matches_won, self.matches_drawn,
            self.matches_lost, self.matches_played)

    @staticmethod
    def header_string():
        return "Team                           " \
               "| MP |  W |  D |  L |  P" 

def tally(rows):
    teams = {} # str (name) -> Results
    for r in rows:  # preprocessing needed
        pass
    result = [Results.header_string()]
    for t in sorted(teams.values(), reverse=True):
        result.append(str(t))
    return result
