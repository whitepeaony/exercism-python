def _time(hour, minute):
    total = 60 * hour + minute
    return (total // 60) % 24, total % 60


class Clock(object):
    def __init__(self, hour, minute):
        self.h = hour
        self.m = minute

    def __repr__(self):
        t = _time(self.h, self.m)
        return "{:02d}:{:02d}".format(t[0], t[1])

    def __eq__(self, other):
        s = _time(self.h, self.m)
        o = _time(other.h, other.m)
        return s[0] == o[0] and s[1] == o[1]

    def __add__(self, minutes):
        self.m += minutes
        t = _time(self.h, self.m)
        return "{:02d}:{:02d}".format(t[0], t[1])

    def __sub__(self, minutes):
        self.m -= minutes
        t = _time(self.h, self.m)
        return "{:02d}:{:02d}".format(t[0], t[1])


print(Clock(2, 20))
