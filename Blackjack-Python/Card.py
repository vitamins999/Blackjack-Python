class Card:
    
    name = ""
    suite = ""
    value = 0

    def __init__(self, name, suite, value):
        self.name = name
        self.suite = suite
        self.value = value

    def GetName(self):
        return f"{self.name} of {self.suite}"

    def GetValue(self):
        return self.value




