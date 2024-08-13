from collections import defaultdict

def generate_report(db):
    transactions = db.get_all_transactions()
    
    total_income = sum(t.amount for t in transactions if t.type == 'income')
    total_expenses = sum(t.amount for t in transactions if t.type == 'expense')
    net_savings = total_income - total_expenses

    category_expenses = defaultdict(float)
    for t in transactions:
        if t.type == 'expense':
            category_expenses[t.category] += t.amount

    print("\nFinancial Report")
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Net Savings: ${net_savings:.2f}")
    
    print("\nExpenses by Category:")
    for category, amount in category_expenses.items():
        print(f"{category}: ${amount:.2f}")