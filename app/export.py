import csv
from report import generate_report

def export_report_to_csv(db, currency_symbol, filename='financial_report.csv'):
    # Pass both db and currency_symbol to generate_report
    transactions, total_income, total_expenses, net_savings, category_expenses = generate_report(db, currency_symbol, return_data=True)

    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Date', 'Type', 'Amount', 'Category', 'Description']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for t in transactions:
            writer.writerow({'Date': t.date, 'Type': t.type, 'Amount': t.amount, 'Category': t.category, 'Description': t.description})

    print(f"Report exported to {filename}")
