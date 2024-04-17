from Hand import Hand
class Person:

    def __init__(self, name):
        self.name = name
        self.hand = Hand()

    def getCard(self, card):
        self.hand.receiveCard(card)
    def getCards(self):
        cards = []
        for card in range(0, self.hand.getCardsLength()):
            cards.append(self.hand.giveCard())
        return cards
    def getTotal(self) -> int:
        return self.hand.getTotal()
    def getHand(self) -> Hand:
        return self.hand
    def getName(self):
        return self.name
    def getChips(self, chips:int):
        self.chips += chips