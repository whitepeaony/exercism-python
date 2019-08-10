class Results(object):
    # A class used to store and compare teams results
    # throughout the tournament. Attributes can be changed
    # with add_ methods. String representation generates
    # a table row for output. Implementation of < operator
    # allows sorting by points (and breaking ties by name).
    def __init__(self, name):
        self.name = name
        self.matches_won = 0
        self.matches_drawn = 0
        self.matches_lost = 0
    
    def matches_played(self):
        return self.matches_won + self.matches_drawn + self.matches_lost

    def add_win(self):
        self.matches_won += 1


    def add_draw(self):
        self.matches_drawn += 1

    def add_loss(self):
        self.matches_lost += 1

    def points(self):
        points = 0
        matches = [self.matches_won, self.matches_drawn, self.matches_lost]
        point = [3, 1, 0]
        for match, p in zip(matches, point):
            points += match * p 
        return points

    def __lt__(self, other) -> bool:
        # compare with other Results based on points,
        # breaking ties with alphabetical order of names
        return Results.points(self) < Results.points(other) 
        
    _repr_str = "{:30} | {:>2} | {:>2} | {:>2} | {:>2} | {:>2}"
    
    def __repr__(self):
        return self._repr_str.format(self.name, self.matches_played(),
            self.matches_won, self.matches_drawn,
            self.matches_lost, self.points())

    @staticmethod
    def header_string():
        return "Team                           " \
               "| MP |  W |  D |  L |  P" 

def tally(rows):
    teams = {} # str (name) -> Results

    for row in rows:

        score = row.split(';')[2]

        if score == 'win':
            team1 = Results(row.split(';')[0])
            team2 = Results(row.split(';')[1])
            team1.add_win()
            team2.add_loss()
            teams[row.split(';')[0]] = team1
            teams[row.split(';')[1]] = team2

        elif score == 'loss':
            team1 = Results(row.split(';')[0])
            team2 = Results(row.split(';')[1])
            team1.add_loss()
            team2.add_win()
            teams[row.split(';')[0]] = team1
            teams[row.split(';')[1]] = team2

        elif score == 'draw':
            team1 = Results(row.split(';')[0])
            team2 = Results(row.split(';')[1])
            team1.add_draw()
            team2.add_draw()
            teams[row.split(';')[0]] = team1
            teams[row.split(';')[1]] = team2


    result = [Results.header_string()]

    for t in sorted(teams.values(), reverse=True):
        result.append(str(t))
    return result

#results = ["Allegoric Alaskans;Blithering Badgers;win"]
#print(tally(results))