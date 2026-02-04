import os
from finance_tracker.expense import Expense
from finance_tracker.file_handler import save_expenses, load_expenses, export_csv

def test_save_and_load_expenses():
    expenses = [
        Expense("2024-01-01", 100, "Food", "Lunch"),
        Expense("2024-01-02", 200, "Travel", "Bus pass")
    ]

    save_expenses(expenses)
    loaded = load_expenses()

    assert len(loaded) == 2
    assert loaded[0].category == "Food"
    assert loaded[1].amount == 200

def test_export_csv():
    expenses = [
        Expense("2024-01-03", 50, "Snacks", "Chips")
    ]

    export_csv(expenses)
    assert os.path.exists("data/exports/expenses.csv")
