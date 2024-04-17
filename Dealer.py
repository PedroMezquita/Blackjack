from Person import Person

class Dealer(Person):
    
    def __init__(self):
        super().__init__("Dealer")
        self.chips = 9999999999999
