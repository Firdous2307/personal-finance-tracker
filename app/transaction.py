class Transaction:
    def __init__(self, amount, category, description, type, date=None):
        self.amount = amount
        self.category = category
        self.description = description
        self.type = type
        self.date = date


    def __str__(self):
        return f"{self.date}: 