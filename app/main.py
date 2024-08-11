import sys
from transaction import Transaction

def main_menu():
    print("\nPersonal Finance Tracker")
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. Exit")
    return input("Choose an option: ")

if __name__ == "__main__":
    main_menu()