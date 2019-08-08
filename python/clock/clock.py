def _time(hour, minute):
    total = 60 * hour + minute
    return (total // 60) % 24, total % 60


class Clock(object):
    def __init__(self, hour, minute):
        t = _time(hour, minute)
        self.h = t[0]
        self.m = t[1]

    def __repr__(self):
        return "{:02d}:{:02d}".format(self.h, self.m)

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.h == other.h and self.m == other.m

    def __add__(self, minutes):
        self.m += minutes
        t = _time(self.h, self.m)
        return "{:02d}:{:02d}".format(t[0], t[1])
    
    def __sub__(self, minutes):
        m = self.m - minutes
        self.m = _time(self.h, m)
        return "{:02d}:{:02d}".format(self.h, self.m)

    
