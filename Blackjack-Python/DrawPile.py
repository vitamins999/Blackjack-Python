import Deck
from random import shuffle

class DrawPile:
    
    draw_pile = []

    def __init__(self, number_of_decks):
        for i in range(number_of_decks):
            deck = Deck.Deck()
            self.draw_pile += deck.get_all_cards_in_deck()

        shuffle(self.draw_pile)

    def draw_card(self):
        return self.draw_pile.pop(0)

