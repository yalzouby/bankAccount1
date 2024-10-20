from main import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, transfer_limit=1000):
        super().__init__(customer_name, current_balance, minimum_balance)
        self.transfer_limit = transfer_limit

    def transfer(self, amount, target_account):
        if amount > self.transfer_limit:
            print(f"Transfer limit exceeded: {amount} > {self.transfer_limit}.")
            return
        if self.current_balance - amount >= self.minimum_balance:
            self.withdraw(amount)
            target_account.deposit(amount)
            print(f"Transferred {amount} to {target_account.customer_name}. New balance: {self.current_balance}")
        else:
            print("Transfer denied. Minimum balance is insufficient.")
