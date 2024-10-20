from bank_account import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, transfer_limit=1000):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.transfer_limit = transfer_limit

    # Method to transfer money
    def transfer(self, amount, target_account):
        if amount > self.transfer_limit:
            print(f"Transfer limit exceeded: ${amount} > ${self.transfer_limit}.")
            return
        if self.current_balance - amount >= self.minimum_balance:
            self.withdraw(amount)
            target_account.deposit(amount)
            print(f"Transfer complete. ${amount} sent to {target_account.customer_name}.")
        else:
            print("Transfer denied. Minimum balance is insufficient.")
