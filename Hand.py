from Card import Card
from Cards import Cards
class Hand(Cards):

    def __init__(self) -> None:
        super().__init__()
        self.total = 0
        self.has_a = False

    def __countTotal(self):
        total = 0
        for card in self.cards_list:
            total += card.value
        return total

    def __AValueCheck(self):
        if self.total > 21:
            for idx, card in enumerate(self.cards_list):
                if card.name == "A" and card.value == 11: #Checks if theres an Ace to change its value
                    card.value = 1
                    self.cards_list[idx] = card
                    return
            #bust code here

    def receiveCard(self, card:Card):
        self.cards_list.append(card)
        self.__AValueCheck()
        self.total = self.__countTotal()

    def giveCard(self) -> Card:
        return self.cards_list.pop()

    def getTotal(self):
        return self.total
    