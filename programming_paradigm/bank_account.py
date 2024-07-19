class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited {amount}. New balance: {self.account_balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.account_balance:
            self.account_balance -= amount
            print(f"Withdrew {amount}. New balance: {self.account_balance}")
            return True
        else:
            print("Insufficient funds or invalid withdrawal amount.")
            return False

    def display_balance(self):
        print(f"Current balance: {self.account_balance}")

# Example usage:
account = BankAccount(1000)  # Create an account with an initial balance of 1000
account.display_balance()
account.deposit(500)
account.withdraw(200)
account.withdraw(1500)  # Insufficient funds
account.display_balance()
class BankAccount:
    # ... existing code ...

def display_balance(amount):
  print(f"Current Balance: ${amount:.2f}")

# Example usage:
balance = 1234.5678
display_balance(balance)

