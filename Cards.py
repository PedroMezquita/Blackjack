from Card import Card

#Cards in plural, card behaviour while in a list
class Cards:

    cards_value = {
        "A":11,
        "2":2,
        "3":3,
        "4":4,
        "5":5,
        "6":6,
        "7":7,
        "8":8,
        "9":9,
        "10":10,
        "J":10,
        "Q":10,
        "K":10
    }

    cards_symbol = ["♠", "♥", "♣", "♦"]

    def __init__(self):
        self.cards_list = []

    def getCardList(self):
        return self.cards_list
    def getCardsLength(self) -> int:
        return len(self.cards_list)

    def showCards(self):
        for card in self.cards_list:
            card.showCard()
    def showCard(self, position:int):
        try:
            self.cards_list[position].showCard()
        except:
            print("Card out of boundaries")
    def getCardStr(self, position:int) -> str:
        try:
            return self.cards_list[position].cardToString()
        except:
            print("Card out of boundaries")
            return ""
    
    def getCardsStr(self) -> str:
        card_str = ""
        for card in self.cards_list:
            card_str += f"{card.cardToString()} "
        return card_str