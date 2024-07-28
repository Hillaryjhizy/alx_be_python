import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Initialize with a default balance for testing
    
    if len(sys.argv) != 2:
        print("Usage: python main-0.py [command:amount/display]")
        return

    command = sys.argv[1]
    
    if command.startswith('deposit:'):
        try:
            amount = float(command.split(':')[1])
            print(account.deposit(amount))
        except ValueError:
            print("Invalid amount for deposit.")

    elif command.startswith('withdraw:'):
        try:
            amount = float(command.split(':')[1])
            print(account.withdraw(amount))
        except ValueError:
            print("Invalid amount for withdrawal.")
        
    elif command == 'display':
        print(account.display_balance())
    
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()

