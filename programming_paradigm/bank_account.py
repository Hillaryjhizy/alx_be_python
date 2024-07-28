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
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the account.
        :param amount: The amount of money to withdraw.
        :return: True if withdrawal is successful, False otherwise.
        """
        if amount > 0:
            if amount <= self._account_balance:
                self._account_balance -= amount
                print(f"Withdrew: ${amount}")
                return True
            else:
                print("Insufficient funds.")
                return False
        else:
            print("Withdrawal amount must be positive.")
            return False

    def display_balance(self):
        """
        Display the current account balance.
        """
        print(f"Current Balance: ${self._account_balance}")

# Example usage (for testing purposes)
if __name__ == "__main__":
    account = BankAccount()
    account.deposit(100)
    account.withdraw(50)
    account.display_balance()
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
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the account.
        :param amount: The amount of money to withdraw.
        :return: True if withdrawal is successful, False otherwise.
        """
        if amount > 0:
            if amount <= self._account_balance:
                self._account_balance -= amount
                print(f"Withdrew: ${amount}")
                return True
            else:
                print("Insufficient funds.")
                return False
        else:
            print("Withdrawal amount must be positive.")
            return False

    def display_balance(self):
        """
        Display the current account balance.
        """
        print(f"Current Balance: ${self._account_balance}")

# Example usage (for testing purposes)
if __name__ == "__main__":
    account = BankAccount()
    account.deposit(100)
    account.withdraw(50)
    account.display_balance()
