import random


class Bank:
    def __init__(self):
        self.amount = 0
        self.accno = random.randint(100000, 999999)
        self.name = input("Enter your name = ")
        self.bankname = input("Enter your bank name = ")
