class BankAccount:
    # Class attribute
    bank_title = "National Bank"

    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        # Instance attributes
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self._account_number = account_number  # Protected member
        self.__routing_number = routing_number  # Private member

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.current_balance += amount
            print(f"${amount} has been deposited. New balance for {self.customer_name}: ${self.current_balance}")
        else:
            print("Deposit amount must be positive.")

    # Method to withdraw money
    def withdraw(self, amount):
        if self.current_balance - amount >= self.minimum_balance:
            self.current_balance -= amount
            print(f"${amount} has been withdrawn. New balance for {self.customer_name}: ${self.current_balance}")
        else:
            print("Withdrawal denied. Minimum balance is insufficient.")

    # Method to print customer information including the bank title
    def print_customer_information(self):
        print(f"Bank: {self.bank_title}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Current Balance: ${self.current_balance}")
        print(f"Minimum Balance: ${self.minimum_balance}")
        print(f"Account Number: {self._account_number}")  # Protected member
        # Private member is not directly accessible outside the class, but you can create a getter for it
        print(f"Routing Number: {self.get_routing_number()}")

    # Getter for private member __routing_number
    def get_routing_number(self):
        return self.__routing_number