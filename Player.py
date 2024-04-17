from Person import Person

class Player(Person):
    
    def __init__(self, name:str, chips:int):
        super().__init__(name)
        self.chips = chips

    def placeBet(self, bet:int) -> int:
            self.chips -= bet
            return bet
    
    def showHand(self):
        self.hand.showCards()

    def getChips(self, chips:int):
        self.chips += chips