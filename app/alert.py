from collections import defaultdict

class Alerts:
    def __init__(self, budget):
        self.budget = budget

    def check_alerts(self, transactions):
        category_spend = defaultdict(float)
        for t in transactions:
            if t.type == 'expense':
                category_spend[t.category] += t.amount
        
        for category, spent in category_spend.items():
            self.budget.check_budget(category, spent)
