# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        self._account_balance = initial_balance  # Private attribute for balance

    def deposit(self, amount):
        """Deposit a specified amount into the account."""
        if amount > 0:
            self._account_balance += amount

    def withdraw(self, amount):
        """Withdraw a specified amount from the account if funds are sufficient."""
        if amount > 0 and amount <= self._account_balance:
            self._account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Display the current balance in a user-friendly format."""
        print(f"Current Balance: ${self._account_balance:.2f}")

# main-0.py

import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Example starting balance

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()

