#inports libraries
import random

#manages decks
class Deck:
    #creates deck objects
    def __init__(self, cards):
        self.cards = cards.copy()

    #shuffles deck
    def shuffle(self):
        random.shuffle(self.cards)
        return self.cards

    #draws a card ferom deck
    def draw(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop(0)

    #shows number of cards left in deck
    def remaining(self):
        return len(self.cards)

#manages players
class Player:
    #creates player objects
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
        self.score = 0

    #draws a card for the player from a deck
    def draw_card(self, deck):
        if len(deck.cards) > 0:
            self.hand.append(deck.draw())

    #plays one of the player's cards
    def play_card(self):
        if len(self.hand) == 0:
            return None
        else:
            print(f"{self.name} plays {self.hand[len(self.hand)-1]}")
            return self.hand.pop(len(self.hand)-1)

#manages games
class Game:
    #creates game objects
    def __init__(self, player1_name, player2_name):
        self.deck = Deck([i for i in range(1,11)])
        self.deck.shuffle()
        self.player1 = Player(player1_name, [])
        self.player2 = Player(player2_name, [])
        self.round = 1

    #plays a round of the game
    def play_round(self):
        print("-------------------")
        print(f"Round {self.round}")
        print("-------------------")
        self.player1.draw_card(self.deck)
        self.player2.draw_card(self.deck)

        player1_card = self.player1.play_card()
        player2_card = self.player2.play_card()

        if player1_card > player2_card:
            self.player1.score +=1
        elif player1_card < player2_card:
            self.player2.score +=1

        self.round +=1

    #gets the winner of the game
    def get_winner(self):
        if self.player1.score > self.player2.score:
            return self.player1
        elif self.player1.score < self.player2.score:
            return self.player2
        else:
            return None

    #plays through the game
    def play_game(self):
        for _ in range(5):
            self.play_round()

        print("-------------------")
        print(f"{self.player1.name}'s Score: {self.player1.score}")
        print(f"{self.player2.name}'s Score: {self.player2.score}")

        if self.get_winner() != None:
            print(f"Winner: {self.get_winner().name}")
        else:
            print("It is a draw")

player1_name = input("Player 1: ")
player2_name = input("Player 2: ")
Game(player1_name, player2_name).play_game()