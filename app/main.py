import sys
from transaction import Transaction

def main_menu():
    print("\nPersonal Finance Tracker")
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. Exit")
    return input("Choose an option: ")

def add_transaction():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")



if __name__ == "__main__":
    main_menu()