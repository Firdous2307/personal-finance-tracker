import sys
from database import Database
from transaction import Transaction
from reports import generate_report
from config import save_currency_symbol, load_currency_symbol
from budget import Budget
from alert import Alerts

def main_menu():
    print("\nPersonal Finance Tracker")
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. Generate Report")
    print("4. Manage Budget")
    print("5. Clear All Transactions")
    print("6. Exit")
    return input("Choose an option: ")

def add_transaction(db, currency_symbol):
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    description = input("Enter description: ")
    transaction_type = input("Enter type (income/expense): ").lower()

    # Create a Transaction object
    transaction = Transaction(amount, category, description, transaction_type)
    
    # Add the transaction to the database
    db.add_transaction(transaction)
    print(f"Transaction added successfully! {currency_symbol}{amount:.2f}")

def view_transactions(db, currency_symbol):
    transactions = db.get_all_transactions()
    for txn in transactions:
        print(f"{txn.date}: {txn.type.capitalize()} - {currency_symbol}{txn.amount:.2f} - {txn.category} - {txn.description}")

def manage_budget(budget, currency_symbol):
    while True:
        print("\nBudget Management")
        print("1. Set Budget")
        print("2. View Budgets")
        print("3. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            category = input("Enter category: ")
            amount = float(input("Enter budget amount: "))
            budget.set_budget(category, amount)
        elif choice == '2':
            budget.view_budgets()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")        

def main():
    # Ask user to set currency symbol
    currency_symbol = input("Enter your preferred currency symbol: ")
    save_currency_symbol(currency_symbol)

    # Load currency symbol
    CURRENCY_SYMBOL = load_currency_symbol()

    db = Database()
    budget = Budget(CURRENCY_SYMBOL)
    alerts = Alerts(budget) 

    # Set up sample budgets
    budget.set_budget('Food', 100.00)
    budget.set_budget('Entertainment', 50.00)

    # Add sample transactions
    db.add_transaction(Transaction(120.00, 'Food', 'Groceries', 'expense'))
    db.add_transaction(Transaction(30.00, 'Entertainment', 'Movie', 'expense'))

    while True:
        choice = main_menu()
        if choice == '1':
            add_transaction(db, CURRENCY_SYMBOL)
        elif choice == '2':
            view_transactions(db, CURRENCY_SYMBOL)
        elif choice == '3':
            generate_report(db, CURRENCY_SYMBOL)
        elif choice == '4':
            manage_budget(budget, CURRENCY_SYMBOL)
        elif choice == '5':
            # Clear all transactions
            db.clear_transactions()
        elif choice == '6':
            # Check alerts before exiting
            transactions = db.get_all_transactions()
            alerts.check_alerts(transactions)
            print("Thank you for using Personal Finance Tracker!")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
