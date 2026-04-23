class Expense:
    def __init__(self, name, amount, category):
        self.name = name
        self.amount = amount
        self.category = category

    def get_name(self):
        return self.name

    def get_amount(self):
        return self.amount

    def get_category(self):
        return self.category

    def display(self):
        return f"{self.name} - KES {self.amount} ({self.category})"
