# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize a BankAccount instance with an optional initial balance.
        :param initial_balance: The starting balance of the account. Defaults to 0.
        """
        self._account_balance = initial_balance

    def deposit(self, amount):
        """
        Deposit a specified amount into the account.
        :param amount: The amount of money to deposit.
        """
        if amount > 0:
            self._account_balance += amount
            return f"Deposited: ${amount:.1f}"

    def withdraw(self, amount):
        if amount > 0 and amount <= self._account_balance:
            self._account_balance -= amount
            return f"Withdrew: ${amount:.1f}"
        else:
            return "Insufficient funds."

    def display_balance(self):
        return f"Current Balance: ${self._account_balance:.1f}"
    

# Example usage 
if __name__ == "__main__":
    account = BankAccount()
    account.deposit(100)
    account.withdraw(50)
    account.display_balance()


