class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def check_balance(self):
        print(f"\nCurrent Balance: ₹{self.balance:.2f}")

    def deposit(self):
        try:
            amount = float(input("Enter amount to deposit: ₹"))

            if amount <= 0:
                print("Amount must be greater than zero.")
            else:
                self.balance += amount
                print("Deposit successful.")
                self.check_balance()

        except ValueError:
            print("Please enter a valid amount.")

    def withdraw(self):
        try:
            amount = float(input("Enter amount to withdraw: ₹"))

            if amount <= 0:
                print("Amount must be greater than zero.")
            elif amount > self.balance:
                print("Insufficient balance.")
            else:
                self.balance -= amount
                print("Withdrawal successful.")
                self.check_balance()

        except ValueError:
            print("Please enter a valid amount.")


def menu():
    try:
        initial_balance = float(input("Enter your initial account balance: ₹"))

        if initial_balance < 0:
            print("Balance cannot be negative.")
            return

        account = BankAccount(initial_balance)

        while True:
            print("\n===== Safe Banking System =====")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                account.check_balance()
            elif choice == "2":
                account.deposit()
            elif choice == "3":
                account.withdraw()
            elif choice == "4":
                print("Thank you for using Safe Banking System!")
                break
            else:
                print("Invalid choice. Please try again.")

    except ValueError:
        print("Invalid balance entered.")


menu()