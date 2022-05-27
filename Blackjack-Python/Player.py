from Person import Person

class Player (Person):

    total_balance = 100.00

    def add_to_total_balance(self, value):
        self.total_balance += value

    def subtract_from_total_balance(self, value):
        self.total_balance -= value

    def get_total_balance(self):
        return self.total_balance