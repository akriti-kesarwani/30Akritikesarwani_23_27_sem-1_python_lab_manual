# bank_module.py

class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True, self.balance  # Successful withdrawal
        else:
            return False, "Insufficient funds"  # Insufficient funds for withdrawal
