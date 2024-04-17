from Deck import Deck
from Person import Person
from Card import Card
import random
#Game actions
class Game:
    def __init__(self, n_decks) -> None:
        self.game_deck = self.deck_shoe = self.deck_deprecate = []
        for deck in range(n_decks):
            deck_raw = Deck()
            for card in deck_raw.getCardList():
                self.game_deck.append(card)
        self.current_bet = 0
    

    def __deckMerge(self, deck1, deck2):
        new_deck = []
        for a in deck1:
            new_deck.append(a)
        for b in deck2:
            new_deck.append(b)
        return new_deck

#Simulate dealer shuffle
    def __shuffle(self, deck):
        random.shuffle(deck)
        temp_deck = self.__deckMerge(deck[1::2], deck[0::2])
        cut = random.randint(1, len(temp_deck))
        shuffled_deck = self.__deckMerge(deck[:cut],deck[cut:])
        return shuffled_deck

    def __takeCard(self) -> Card:
        return self.deck_shoe.pop(0)

    def __giveCard(self, person:Person):
        person.getCard(self.__takeCard())

#   whoWins not used 
    def whoWins(self, person:Person, dealer:Person):
        if person.getTotal() > dealer.getTotal():
            return person
        elif person.getTotal() < dealer.getTotal():
            return dealer
# -----------------------------------

    def playerWins(self, person:Person, dealer:Person) -> bool:
        if person.getTotal() > 21:
            return False
        if dealer.getTotal() > 21:
            return True
        return person.getTotal() >= dealer.getTotal()

    def playerPush(self, player:Person, dealer:Person) -> bool:
        return player.getTotal() == dealer.getTotal()

    def personHit(self, person:Person):
        self.__giveCard(person)

    def raiseBet(self, bet_raise:int, player:Person):
        self.current_bet += player.placeBet(bet_raise)

    def startBet(self, min_bet:int, player:Person):
        print(f"Place your bet!             Balance:{player.chips}")
        bet = int(input(f"(Minimum : {min_bet}):       "))
        if bet < player.chips and bet >= min_bet:
            self.current_bet = player.placeBet(bet)
        else:
            print("Not Enough")
            exit()

    def startHand(self, player:Person, dealer:Person, min_bet:int):
        self.startBet(min_bet, player)
        self.__giveCard(player)
        self.__giveCard(dealer)
        self.__giveCard(player)
        self.__giveCard(dealer)

    def getShoeLength(self) -> int:
        return len(self.deck_shoe)

    def discardTable(self, player:Person, dealer:Person):
        deprecate_tmp = self.__deckMerge(self.deck_deprecate, player.getCards())
        self.deck_deprecate = self.__deckMerge(deprecate_tmp, dealer.getCards())

    #def tableInsurance(self, dealer:Person)

    def playerLoses(self):
        self.current_bet = 0

    def playerWinsCheck(self, player:Person, dealer:Person):
        if player.getTotal() > 21 : return False
        elif player.getTotal() <= 21 and dealer.getTotal() > 21 : return True
        elif player.getTotal() == dealer.getTotal() : return True
        elif player.getTotal() > dealer.getTotal() : return True
        elif player.getTotal() < dealer.getTotal() : return False

    def playerWins(self, player:Person, rate):
        bet_rate = 1 + rate
        player.getChips(int(self.current_bet*bet_rate))
        self.current_bet = 0

    def startGame(self):
        self.deck_shoe = self.__shuffle(self.game_deck)

    def showGameDeck(self):
        for card in self.game_deck:
            card.showCard()

    def showShoeDeck(self):
        for card in self.deck_shoe:
            card.showCard()

    def showTableHidden(self, dealer:Person, player:Person):
        print("")
        print(dealer.getName(),f":  {dealer.getHand().getCardStr(1)}  [?]")
        print(player.getName(), ":  ",player.getHand().getCardsStr(),"      (",player.getTotal(),")          $",self.current_bet)

    def showTableDealers(self, dealer:Person, player:Person):
        print("")
        print(dealer.getName(), ":  ", dealer.getHand().getCardsStr(),"     (",dealer.getTotal(),")")
        print(player.getName(), ":  ", player.getHand().getCardsStr(),"     (",player.getTotal(),")          $", self.current_bet)
        input()
