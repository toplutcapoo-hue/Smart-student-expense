class User:
    def __init__(self, username):
        self.username = username
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def get_expenses(self):
        return self.expenses

    def total_spending(self):
        return sum(exp.amount for exp in self.expenses)
