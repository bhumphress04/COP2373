# bank_account.py
# BankAcct class definition and test function

class BankAcct:
    def __init__(self, name, account_number, amount, interest_rate):
        """Initialize account with name, account number, amount, and interest rate (as a percent)."""
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.interest_rate = interest_rate  # stored as a percentage (e.g., 3.5 for 3.5%)

    def adjust_interest_rate(self, new_rate):
        """Adjust the interest rate to a new percentage."""
        self.interest_rate = new_rate
        print(f"Interest rate adjusted to {self.interest_rate}%")

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.amount += amount
            print(f"Deposited ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money from the account, if sufficient funds exist."""
        if amount > 0:
            if amount <= self.amount:
                self.amount -= amount
                print(f"Withdrew ${amount:.2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        """Return the current balance."""
        return self.amount

    def calculate_interest(self, days):
        """Calculate simple interest based on the number of days."""
        daily_rate = self.interest_rate / 100 / 365
        interest = self.amount * daily_rate * days
        return interest

    def __str__(self):
        """Display account details with balance and interest info."""
        return (f"Account Holder: {self.name}\n"
                f"Account Number: {self.account_number}\n"
                f"Balance: ${self.amount:.2f}\n"
                f"Interest Rate: {self.interest_rate}%")

# ---------------------------
# Test function
# ---------------------------
def test_bank_acct():
    # Create a Bank Account object
    acct = BankAcct("Alex Johnson", "123456789", 1000.00, 3.5)
    print(acct)

    # Test deposit
    acct.deposit(500)
    print(f"New balance after deposit: ${acct.get_balance():.2f}\n")

    # Test withdrawal
    acct.withdraw(200)
    print(f"New balance after withdrawal: ${acct.get_balance():.2f}\n")

    # Test interest calculation
    days = 30
    interest = acct.calculate_interest(days)
    print(f"Interest for {days} days: ${interest:.2f}\n")

    # Test interest rate adjustment
    acct.adjust_interest_rate(4.0)
    print(acct)

# Run the test function if the file is executed directly
if __name__ == "__main__":
    test_bank_acct()