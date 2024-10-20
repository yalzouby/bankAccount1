from bank_account import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, interest_rate=0.01):
        super().__init__(customer_name, current_balance, minimum_balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.current_balance * self.interest_rate
        self.deposit(interest)
        print(f"Interest applied: {interest}. New balance is {self.current_balance}")
