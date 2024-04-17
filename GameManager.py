from Player import Player
from Dealer import Dealer
from Game import Game
# Game flow
class GameManager:
    def __init__(self, n_deck, player_name) -> None:
        self.game = Game(n_deck)
        self.dealer = Dealer()
        self.player = Player(player_name, 3000)


    def dealers_turn_active(self):
        self.game.showTableDealers(self.dealer, self.player)
        while self.dealer.getTotal() < 17:
            self.game.personHit(self.dealer)
            self.game.showTableDealers(self.dealer, self.player)

    def players_turn_active(self):
        choice = 0
        turn = 1
        if self.player.getTotal() == 21: 
            self.game.playerWins(self.player, 1.5)
            print("BLACKJACK ! ")
        while self.player.getTotal() < 21 and choice != 1:
            self.game.showTableHidden(self.dealer, self.player)
            if turn == 1 : choice = int(input("0: Hit, 1: stand, 2: double :"))
            else : choice = int(input("0: Hit, 1: stand :"))
            if choice == 0: self.game.personHit(self.player)
            elif choice == 2 and turn == 1:
                 self.game.personHit(self.player)
                 self.game.raiseBet(self.game.current_bet, self.player)
                 choice = 1
            turn += 1
        self.game.showTableHidden(self.dealer, self.player)
        if self.player.getTotal() > 21:
                    self.game.playerLoses()
                    input(f"{self.player.getName()} BUSTS ! ")


    def startGame(self):
        self.game.startGame()
        while self.game.getShoeLength() > 15:
            self.game.startHand(self.player, self.dealer, 10)
            self.players_turn_active()
            self.dealers_turn_active()
            #if self.player.getTotal() > self.dealer.getTotal() and self.game.current_bet != 0 or self.dealer.getTotal() > 21 and self.game.current_bet !=0:
            if self.game.playerWinsCheck(self.player, self.dealer) == 1:
                if self.game.playerPush(self.player, self.dealer): self.game.playerWins(self.player, 0)
                else: 
                    self.game.playerWins(self.player, 1)
                    input(f"{self.player.getName()} Wins")
            self.game.discardTable(self.player, self.dealer)