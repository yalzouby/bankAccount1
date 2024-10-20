from bank_account import BankAccount
from savings_account import SavingsAccount
from checking_account import CheckingAccount

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

###Bank Account 2 Addition
# Create instances of SavingsAccount and CheckingAccount
savings = SavingsAccount("Alice", 3000, 500, interest_rate=0.05)
checking = CheckingAccount("Bob", 1500, 200, transfer_limit=500)

# Test the SavingsAccount methods
savings.print_customer_information()
savings.apply_interest()  # Apply interest to savings account

# Test the CheckingAccount methods
checking.print_customer_information()
checking.transfer(400, savings)  # Transfer money from checking to savings
checking.transfer(600, savings)  # Should exceed the transfer limit