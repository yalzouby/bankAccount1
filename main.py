class BankAccount:
    # Class attribute
    bank_title = "National Bank"

    def __init__(self, customer_name, current_balance, minimum_balance):
        # Instance attributes
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.current_balance += amount
            print(f"{amount} has been deposited. New balance is {self.current_balance}")
        else:
            print("Deposit amount must be positive.")

    # Method to withdraw money
    def withdraw(self, amount):
        if self.current_balance - amount >= self.minimum_balance:
            self.current_balance -= amount
            print(f"{amount} has been withdrawn. New balance is {self.current_balance}")
        else:
            print("Withdrawal denied. Minimum balance is insufficient.")

    # Method to print customer information including the bank title
    def print_customer_information(self):
        print(f"Bank: {self.bank_title}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Current Balance: {self.current_balance}")
        print(f"Minimum Balance: {self.minimum_balance}")

# Creating instances of BankAccount
account1 = BankAccount("John Smith", 1000, 100)
account2 = BankAccount("Jane Doe", 2000, 200)

# Test the methods with account1
account1.print_customer_information()
account1.deposit(500)
account1.withdraw(1300)  # Should succeed
account1.withdraw(300)   # Should be denied

# Test the methods with account2
account2.print_customer_information()
account2.deposit(200)
account2.withdraw(1800)  # Should succeed
account1.withdraw(300)   # Should be denied
