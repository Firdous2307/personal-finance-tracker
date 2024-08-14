import sys
import os

# Insert the 'app' directory into sys.path to allow imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from alert import Alerts
from budget import Budget
from transaction import Transaction

def test_alerts():
    currency_symbol = '₦'  # Example currency symbol
    budget = Budget(currency_symbol)
    alerts = Alerts(budget)

    # Set budget
    budget.set_budget('Food', 100.00)

    # Add transactions
    transactions = [
        Transaction(120.00, 'Food', 'Groceries', 'expense'),
        Transaction(80.00, 'Food', 'Restaurant', 'expense')
    ]

    # Test checking alerts
    alerts.check_alerts(transactions)

if __name__ == "__main__":
    print("Testing Alerts class...")
    test_alerts()
