# ATM Interface using Python

# Dummy user data
users = {
    "1234": {
        "pin": "4321",
        "balance": 1000.0
    },
    "5678": {
        "pin": "8765",
        "balance": 500.0
    }
}

def authenticate(account_number, pin):
    user = users.get(account_number)
    if user and user['pin'] == pin:
        return True
    return False

def show_menu():
    print("\n--- ATM Menu ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

def atm_session(account_number):
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            print(f"Your current balance is: ${users[account_number]['balance']:.2f}")
        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                users[account_number]['balance'] += amount
                print(f"${amount:.2f} deposited successfully.")
            else:
                print("Invalid amount.")
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            if 0 < amount <= users[account_number]['balance']:
                users[account_number]['balance'] -= amount
                print(f"${amount:.2f} withdrawn successfully.")
            else:
                print("Insufficient balance or invalid amount.")
        elif choice == '4':
            print("Thank you for using our ATM!")
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    print("Welcome to Python ATM!")
    account_number = input("Enter your account number: ")
    pin = input("Enter your PIN: ")

    if authenticate(account_number, pin):
        print("Login successful!")
        atm_session(account_number)
    else:
        print("Authentication failed. Exiting.")

if __name__ == "__main__":
    main()
