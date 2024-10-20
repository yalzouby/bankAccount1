from bank_account import BankAccount
from savings_account import SavingsAccount
from checking_account import CheckingAccount

# Creating instances of BankAccount
#account1 = BankAccount("John Smith", 1000, 100)
#account2 = BankAccount("Jane Doe", 2000, 200)

# Test the methods with account1
#account1.print_customer_information()
#account1.deposit(500)
#account1.withdraw(1300)  # Should succeed
#account1.withdraw(300)   # Should be denied

# Test the methods with account2
#account2.print_customer_information()
#account2.deposit(200)
#account2.withdraw(1800)  # Should succeed
#account1.withdraw(300)   # Should be denied

### Bank Account 2 Addition
# Create instances of SavingsAccount and CheckingAccount
alice_savings = SavingsAccount("Alice", 3000, 500, "123456789", "987654321", interest_rate=0.05)
bob_savings = SavingsAccount("Bob", 1500, 200, "123456788", "987654322", interest_rate=0.02)

anna_checking = CheckingAccount("Anna", 3000, 500, "123456789", "987654321", transfer_limit=400)
jon_checking = CheckingAccount("Jon", 1500, 200, "123456788", "987654322", transfer_limit=500)

# Test the SavingsAccount methods
alice_savings.print_customer_information()
alice_savings.apply_interest()  # Apply interest to savings account
print()
bob_savings.print_customer_information()
bob_savings.apply_interest()
print()

# Test the CheckingAccount methods
jon_checking.print_customer_information()
jon_checking.transfer(400, bob_savings)  # Transfer money from checking to savings
jon_checking.transfer(600, bob_savings)  # Should exceed the transfer limit
print()
anna_checking.print_customer_information()
anna_checking.transfer(400, alice_savings)
anna_checking.transfer(600, alice_savings)
