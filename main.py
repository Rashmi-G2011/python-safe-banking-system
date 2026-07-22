def check_balance(balance):
    print(f"\nCurrent Balance: ₹{balance:.2f}")

def deposit(balance):
    try:
        amount = float(input("Enter amount to deposit: ₹"))

        if amount <= 0:
            print("Amount must be greater than zero.")
        else:
            balance += amount
            print("Deposit successful.")
            check_balance(balance)

    except ValueError:
        print("Please enter a valid amount.")

    return balance

def withdraw(balance):
    try:
        amount = float(input("Enter amount to withdraw: ₹"))

        if amount <= 0:
            print("Amount must be greater than zero.")
        elif amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            print("Withdrawal successful.")
            check_balance(balance)

    except ValueError:
        print("Please enter a valid amount.")

    return balance


def menu():
    try:
        balance = float(input("Enter your initial account balance: ₹"))

        while True:
            print("\n===== Safe Banking System =====")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                check_balance(balance)
            elif choice == "2":
                balance = deposit(balance)
            elif choice == "3":
                balance = withdraw(balance)
            elif choice == "4":
                print("Thank you for using Safe Banking System!")
                break
            else:
                print("Invalid choice. Please try again.")

    except ValueError:
        print("Invalid balance entered.")

menu()