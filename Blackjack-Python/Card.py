class Card:
    
    name = ""
    suite = ""
    value = 0

    def __init__(self, name, suite, value):
        self.name = name
        self.suite = suite
        self.value = value

    def get_name(self):
        return f"{self.name} of {self.suite}"

    def get_value(self):
        return self.value