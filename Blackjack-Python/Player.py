class Player:

    name = ""
    score = 0
    totalHandValue = 0
    totalBalance = 100.00

    def __init__(self, name):
        self.name = name

    def AddWinToScore(self):
        self.score += 1

    def GetScore(self):
        return self.score

    def AddValueToHand(self, value):
        self.totalHandValue += value

    def GetTotalHandValue(self):
        return self.totalHandValue

    def ResetTotalHandValue(self):
        self.totalHandValue = 0

    def AddToTotalBalance(self, value):
        self.totalBalance += value

    def SubtractFromTotalBalance(self, value):
        self.totalBalance -= value

    def GetTotalBalance(self):
        return self.totalBalance

    def GetName(self):
        return self.name

