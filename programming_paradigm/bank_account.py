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

    @staticmethod
    def perform_action(action, amount=None):
        # Create an account instance with initial balance of 0 (for display)
        account = BankAccount(0)
        if action == "deposit":
            account.deposit(amount)
        elif action == "withdraw":
            result = account.withdraw(amount)
            if not result:
                print("Insufficient funds.")
        elif action == "display":
            account.display_balance()
        else:
            print("Invalid action.")

