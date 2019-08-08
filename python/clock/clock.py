def _time(hour, minute):
    total = 60 * hour + minute
    return [(total // 60) % 24, total % 60]

class Clock(object):
    def __init__(self, hour, minute):
        self.h = hour
        self.m = minute

    
    def __repr__(self):
        t = _time(self.h, self.m)
        return "{:02d}:{:02d}".format(t[0], t[1])


    def __eq__(self, other):
        pass

    def __add__(self, minutes):
        pass

    def __sub__(self, minutes):
        pass

print(Clock(2, 20))

