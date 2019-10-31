class Account():
    #public static
    myass = 0
    shit = lambda self, amount: self.withdraw(amount)

    def __init__(self, account_holder = 'clown'):
        # private
        self.balance = 0
        self.account_holder = account_holder
        # self.myass = 1/0

    def withdraw(self, amount):
        assert amount >= 0, "NM$L!"
        if amount > self.balance:
            return "Insufficient balance!"
        self.balance -+ amount
        return self.balance

    def desposit(self, amount):
        assert amount >= 0, "NM$L!"
        self.balance += amount
        return self.balance

class Joker():
    def __init__(self, abused):
        self.abused = abused
        self.mother = None
        self.father = None

    def shoot(self):
        pass

    def stab(self):
        pass

    def laugh(self):
        pass

    def revolution(self):
        pass