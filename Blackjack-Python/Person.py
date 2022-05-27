class Person:
    
    name = ""
    score = 0
    total_hand_value = 0

    def __init__(self, name):
        self.name = name

    def add_win_to_score(self):
        self.score += 1

    def get_score(self):
        return self.score

    def add_value_to_hand(self, value):
        self.total_hand_value += value

    def get_total_hand_value(self):
        return self.total_hand_value

    def reset_total_hand_value(self):
        self.total_hand_value = 0

    def get_name(self):
        return self.name