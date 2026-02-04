from finance_tracker.expense import Expense

class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense: Expense):
        self.expenses.append(expense)

    def search(self, keyword):
        return [
            e for e in self.expenses
            if keyword.lower() in e.category.lower()
            or keyword.lower() in e.description.lower()
        ]

    def get_monthly(self, year, month):
        return [
            e for e in self.expenses
            if e.date.year == year and e.date.month == month
        ]
