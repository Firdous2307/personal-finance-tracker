from budget import Budget
from sns.aws_sns import SNSNotifier
from collections import defaultdict

class Alerts:
    def __init__(self, budget):
        self.budget = budget
        self.notifier = SNSNotifier()

    def check_alerts(self, transactions):
        category_spend = defaultdict(float)
        for t in transactions:
            if t.type == 'expense':
                category_spend[t.category] += t.amount
        
        for category, spent in category_spend.items():
            self.budget.check_budget(category, spent)
            budget = self.budget.budgets.get(category)
            if budget and spent > budget:
                message = f"Alert! Your spending for {category} has exceeded the budget by ${spent - budget:.2f}."
                self.notifier.send_alert(subject="Budget Exceeded", message=message)
            elif budget and spent > budget * 0.9:
                message = f"Warning: Your spending for {category} is close to exceeding the budget (${spent:.2f} of ${budget:.2f})."
                self.notifier.send_alert(subject="Budget Warning", message=message)
