
# main-0.py

import sys
from bank_account import BankAccount

def main():
    # Create a BankAccount instance (initial balance can be set here if needed)
    account = BankAccount()

    # Check if the command line argument is provided
    if len(sys.argv) != 2:
        print("Usage: python main-0.py [command:amount|display]")
        return

    command = sys.argv[1]

    if command.startswith('deposit:'):
        try:
            amount = float(command.split(':')[1])
            account.deposit(amount)
        except ValueError:
            print("Invalid amount for deposit.")
    
    elif command.startswith('withdraw:'):
        try:
            amount = float(command.split(':')[1])
            account.withdraw(amount)
        except ValueError:
            print("Invalid amount for withdrawal.")
    
    elif command == 'display':
        account.display_balance()
    
    else:
        print("Invalid command. Use 'deposit:amount', 'withdraw:amount', or 'display'.")

if __name__ == "__main__":
    main()
