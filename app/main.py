import sys
from transaction import Transaction
from database import Database

def main_menu():
    print("\nPersonal Finance Tracker")
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. Exit")
    return input("Choose an option: ")

def add_transaction(db):
    # Example values for testing
    amount = 200.50
    category = "Car Expenses"
    description = "Monthly car testing"
    transaction_type = "expense"
    # Creating a Transaction object to represent the transaction
    transaction = Transaction(amount, category, description, transaction_type)

    db.add_transaction(transaction)
    print("Transaction added successfully!")



def main():
    db = Database()

    while True:
        choice = main_menu()
        if choice == '1':
            add_transaction(db)
        else:
            print("Invalid choice. Please try again.")        

if __name__ == "__main__":
    main()