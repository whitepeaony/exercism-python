class Luhn(object):
    def __init__(self, card_num):
        self.card_num = card_num.replace(' ', '')
        self.card_num = [ch for ch in self.card_num]      

        

    def valid(self):
        #print(self.card_num)

        if len(self.card_num) <= 1:
            return False

        else:
            card = self.card_num
            card = [int(i) for i in card]

            for i in range(0, len(card), -2):
                a = card[i]
                if card[i] * 2 < 9:
                    card.remove(a)
                    card.insert(a * 2, i)
                    
                else:
                    card.remove(a)
                    card.insert(a * 2 - 9, i)
                    

            sum = 0
            for n in card:
                sum += int(n)
            return card
            #sum % 10 == 0
                


print(Luhn("055 444 285").valid())

