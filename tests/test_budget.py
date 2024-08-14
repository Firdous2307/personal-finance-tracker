import sys
import os

# Insert the 'app' directory into sys.path to allow imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from budget import Budget

def test_set_and_view_budget():
    currency_symbol = '₦'  # Example currency symbol
    budget = Budget(currency_symbol)

    # Test setting budgets
    budget.set_budget('Food', 100.00)
    budget.set_budget('Entertainment', 50.00)

    # Test viewing budgets
    budget.view_budgets()

def test_check_budget():
    currency_symbol = '₦'  # Example currency symbol
    budget = Budget(currency_symbol)

    # Set budgets
    budget.set_budget('Food', 100.00)

    # Test checking budgets
    budget.check_budget('Food', 120.00)  # Should trigger an alert
    budget.check_budget('Food', 90.00)   # Should trigger a warning
    budget.check_budget('Food', 50.00)   # Should not trigger any alert

if __name__ == "__main__":
    print("Testing Budget class...")
    test_set_and_view_budget()
    test_check_budget()
