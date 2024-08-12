import sys
from database import Database
from transaction import Transaction
from reports import generate_report

def main_menu():
    print("\nPersonal Finance Tracker")
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. Generate Report")
    print("4. Exit")
    return input("Choose an option: ")

def add_transaction(db):
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    description = input("Enter description: ")
    transaction_type = input("Enter type (income/expense): ").lower()

    transaction = Transaction(amount, category, description, transaction_type)
    db.add_transaction(transaction)
    print("Transaction added successfully!")

def view_transactions(db):
    transactions = db.get_all_transactions()
    for transaction in transactions:
        print(transaction)

def main():
    db = Database()

    while True:
        choice = main_menu()
        if choice == '1':
            add_transaction(db)
        elif choice == '2':
            view_transactions(db)
        elif choice == '3':
            generate_report(db)
        elif choice == '4':
            print("Thank you for using Personal Finance Tracker!")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()