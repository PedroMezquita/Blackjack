#Card unity
class Card:
    value:int = None
    symbol:str = None
    name:str = None
    
    def __init__(self, value, symbol, name):
        self.value = value
        self.symbol = symbol
        self.name = name
    

    def getValue(self):
        return self.value
    
    def setValue(self, new_value:int):
        self.value = new_value

    def getSymbol(self):
        return self.symbol
    
    def getName(self):
        return self.name
    
    def showCard(self):
        print(self.name,self.symbol)

    def cardToString(self) -> str:
        return f"{self.name}{self.symbol}"