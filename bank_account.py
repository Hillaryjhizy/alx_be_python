class BankAccount:
    def __init__(self, initial_balance=0):
        self._account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            return f"Deposited: ${amount:.1f}"
        return "Invalid deposit amount."

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self._account_balance:
                self._account_balance -= amount
                return f"Withdrew: ${amount:.1f}"
            else:
                return "Insufficient funds."
        return "Invalid withdrawal amount."

    def display_balance(self):
        return f"Current Balance: ${self._account_balance:.1f}"
