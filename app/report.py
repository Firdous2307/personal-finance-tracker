from collections import defaultdict

def generate_report(db, currency_symbol, return_data=False):
    transactions = db.get_all_transactions()
    
    total_income = sum(t.amount for t in transactions if t.type == 'income')
    total_expenses = sum(t.amount for t in transactions if t.type == 'expense')
    net_savings = total_income - total_expenses

    category_expenses = defaultdict(float)
    for t in transactions:
        if t.type == 'expense':
            category_expenses[t.category] += t.amount

    if return_data:
        return transactions, total_income, total_expenses, net_savings, category_expenses

    # Print report if not returning data
    print("\nFinancial Report")
    print(f"Total Income: {currency_symbol}{total_income:.2f}")
    print(f"Total Expenses: {currency_symbol}{total_expenses:.2f}")
    print(f"Net Savings: {currency_symbol}{net_savings:.2f}")
    
    print("\nExpenses by Category:")
    for category, amount in category_expenses.items():
        print(f"{category}: {currency_symbol}{amount:.2f}")
