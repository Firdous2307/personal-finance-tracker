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
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    description = input("Enter description: ")
    transaction_type = input("Enter type (income/expense): ").lower()


def main():
    db = Database()

    
if __name__ == "__main__":
    main_menu()