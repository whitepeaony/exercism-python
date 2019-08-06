class Luhn(object):
    def __init__(self, card_num):
        self.card_num = card_num.replace(' ', '')
        

    def valid(self):
        if len(self.card_num) <= 1:
            return False
        else:
            card = self.card_num.split()
            for i in range(0, len(card), -2):
                if 2 * i < 9:
                    card[i] = 2*i
                else:
                    card[i] = 2*i - 9
            sum = 0
            for n in card:
                sum += int(n)
            return sum % 10 == 0
                


print(Luhn("0859").valid())


