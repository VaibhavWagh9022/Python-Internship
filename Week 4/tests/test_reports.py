from finance_tracker.expense import Expense
from finance_tracker.reports import category_report, monthly_total

def test_category_report():
    expenses = [
        Expense("2024-01-01", 100, "Food", "Lunch"),
        Expense("2024-01-02", 50, "Food", "Snack"),
        Expense("2024-01-03", 200, "Travel", "Train")
    ]

    report = category_report(expenses)

    assert report["Food"] == 150
    assert report["Travel"] == 200

def test_monthly_total():
    expenses = [
        Expense("2024-01-01", 100, "Food", "Lunch"),
        Expense("2024-01-02", 200, "Travel", "Taxi")
    ]

    assert monthly_total(expenses) == 300
