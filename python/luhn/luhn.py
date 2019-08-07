class Luhn(object):
    def __init__(self, card_num):
        self.card_num = card_num.replace(' ', '')

    def valid(self):
        if not self.card_num.isdigit():
            return False

        if len(self.card_num) <= 1:
            return False

        card = [int(ch) for ch in self.card_num]

        for i in range(len(card)-2, -1,  -2):

            if card[i] * 2 < 9:
                card[i] *= 2

            else:
                card[i] = 2 * card[i] - 9

        return sum(card) % 10 == 0
