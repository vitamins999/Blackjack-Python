import Deck
from random import shuffle

class DrawPile:
    
    drawPile = []

    def __init__(self, numberOfDecks):
        for i in range(numberOfDecks):
            deck = Deck.Deck()
            self.drawPile += deck.GetAllCardsInDeck()

        shuffle(self.drawPile)

    def DrawCard(self):
        return self.drawPile.pop(0)

