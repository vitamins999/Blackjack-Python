from Card import Card

class Deck:
    
    all_cards = []

    def __init__(self):
        hearts_list = self.generate_suite("Hearts")
        diamonds_list = self.generate_suite("Diamonds")
        spades_list = self.generate_suite("Spades")
        clubs_list = self.generate_suite("Clubs")

        self.all_cards = [*hearts_list, *diamonds_list, *spades_list, *clubs_list]

    def generate_suite(self, suite_name):
        suite = []

        suite.append(Card("Two", suite_name, 2))
        suite.append(Card("Three", suite_name, 3))
        suite.append(Card("Four", suite_name, 4))
        suite.append(Card("Five", suite_name, 5))
        suite.append(Card("Six", suite_name, 6))
        suite.append(Card("Seven", suite_name, 7))
        suite.append(Card("Eight", suite_name, 8))
        suite.append(Card("Nine", suite_name, 9))
        suite.append(Card("Ten", suite_name, 10))
        suite.append(Card("Jack", suite_name, 10))
        suite.append(Card("Queen", suite_name, 10))
        suite.append(Card("King", suite_name, 10))
        suite.append(Card("Ace", suite_name, 11))

        return suite

    def get_all_cards_in_deck(self):
        return self.all_cards