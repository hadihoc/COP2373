#
class BankAcct:
    def __init__(self, acct_name, acct_num, balance, apr):
        self.aact_name = acct_name
        self.acct_num = acct_num
        self.balance = float(balance)
        self.apr = float(apr)

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount cannot be negative.")
        else:
            try:
                self.balance += float(amount)
            except ValueError:
                print("Invalid amount.")

    def adjust_apr(self, new_rate):
        if 0 > new_rate > 1:
            print("Interest rate cannot be negative nor more than 1.")
        else:
            try:
                self.apr = float(new_rate)
            except ValueError:
                print("Invalid interest rate.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount

    def get_balance(self):
        return self.balance

    def calculate_apr(self, days):
        if days < 0:
            print("Number of days cannot be negative.")
        else:
            interest = self.balance * self.apr * days / 365
        return interest

    def __str__(self):
        interest = self.calculate_apr(365)
        return (f"Account Holder: {self.aact_name}\n"
                f"Account Number: {self.acct_num}\n"
                f"Account Balance: {self.balance: .2f}\n"
                f"Annual Interest Rate: {self.apr * 100: .2f}\n"
                f"Estimated Interest (1 year): ${interest:.2f}"
                )

# Test Function
def test_bank_acct():
    # Creating account
    acct = BankAcct("Anna Nguyen","1234567891", 653.55, 0.01)
    print()
    print(f"Beginning balance: ${acct.get_balance():.2f}")
    # Depositing $100.56
    print("Depositing $100.56")
    acct.deposit(100.56)
    print(f"Balance after deposit: ${acct.get_balance():.2f}")

    # Withdrawing $50
    print("Withdrawing $50.00")
    acct.withdraw(50)
    print(f"Balance after withdrawal: ${acct.get_balance():.2f}")

    # Adjusting interest rate to 3%
    acct.adjust_apr(0.03)
    print(f"New interest rate: {acct.apr * 100:.2f}%\n")

    # Calculating interest for 90 days
    interest_90_days = acct.calculate_apr(90)
    print(f"Interest for 90 days: ${interest_90_days:.2f}")

    print("\nFinal account summary:")
    print("+++++++++++++++++++++++++")
    print(acct)


# Run test function
test_bank_acct()
