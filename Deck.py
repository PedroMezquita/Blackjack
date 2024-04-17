from Card import Card
from Cards import Cards
class Deck(Cards):
    def __init__(self):
        #Cards from other instances seems to be kept in the list when created, this "resets" the list
        super().__init__()
        for symb in self.cards_symbol:
            for name in self.cards_value:
                self.cards_list.append(Card(self.cards_value[name], symb, name))
