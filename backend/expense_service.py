from .expense import Expense
from . database.db_manager import insert_expense, get_expenses

def add_expense(name, amount, category):
    if amount <= 0:
        print("❌ Invalid amount")
        return

    # Create object
    expense = Expense(name, amount, category)

    # Store in database
    insert_expense(expense.get_name(), expense.get_amount(), expense.get_category())

    print("✅ Expense added successfully!")


def view_expenses():
    expenses = get_expenses()

    if not expenses:
        print("No expenses found.")
        return

    print("\n--- Expense List ---")

    for exp in expenses:
        # Convert DB data into object
        expense_obj = Expense(exp[1], exp[2], exp[3])
        print(expense_obj.display())
