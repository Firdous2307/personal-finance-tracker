class Budget:
    def __init__(self, currency_symbol='$'):
        self.budgets = {}
        self.currency_symbol = currency_symbol

    def set_budget(self, category, amount):
        self.budgets[category] = amount
        print(f"Budget set: {category} - {self.currency_symbol}{amount:.2f}")

    def check_budget(self, category, spent):
        if category in self.budgets:
            budget = self.budgets[category]
            if spent > budget:
                print(f"Alert! {category} budget exceeded by {self.currency_symbol}{spent - budget:.2f}")
            elif spent > budget * 0.9:
                print(f"Warning: {category} spending is close to budget ({self.currency_symbol}{spent:.2f} of {self.currency_symbol}{budget:.2f})")

    def view_budgets(self):
        for category, amount in self.budgets.items():
            print(f"{category}: {self.currency_symbol}{amount:.2f}")
