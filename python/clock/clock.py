def _time(hour, minute):
    total = 60 * hour + minute
    hours = total // 60
    minut = total % 60
    return [hours, minut]

class Clock(object):
    def __init__(self, hour, minute):
        self.h = hour
        self.m = minute

    
    def __repr__(self):
        t = _time(self.h, self.m)
        if t[0] < 10:
            a = 0
        else:
            a =''
        if t[1] < 10:
            b = 0
        else:
            b =''

        return "{}{}:{}{}".format(a, t[0], b, t[1])

 


    def __eq__(self, other):
        pass

    def __add__(self, minutes):
        pass

    def __sub__(self, minutes):
        pass

print(Clock(2, 20))

