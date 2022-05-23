import Card

class Deck:
    
    allCards = []

    def __init__(self):
        heartsList = self.GenerateSuite("Hearts")
        diamondsList = self.GenerateSuite("Diamonds")
        spadesList = self.GenerateSuite("Spades")
        clubsList = self.GenerateSuite("Clubs")

        self.allCards = [*heartsList, *diamondsList, *spadesList, *clubsList]

    def GenerateSuite(self, suiteName):
        suite = []

        suite.append(Card.Card("Two", suiteName, 2))
        suite.append(Card.Card("Three", suiteName, 3))
        suite.append(Card.Card("Four", suiteName, 4))
        suite.append(Card.Card("Five", suiteName, 5))
        suite.append(Card.Card("Six", suiteName, 6))
        suite.append(Card.Card("Seven", suiteName, 7))
        suite.append(Card.Card("Eight", suiteName, 8))
        suite.append(Card.Card("Nine", suiteName, 9))
        suite.append(Card.Card("Ten", suiteName, 10))
        suite.append(Card.Card("Jack", suiteName, 10))
        suite.append(Card.Card("Queen", suiteName, 10))
        suite.append(Card.Card("King", suiteName, 10))
        suite.append(Card.Card("Ace", suiteName, 11))

        return suite

    def GetAllCardsInDeck(self):
        return self.allCards


