from finance_tracker.expense import Expense

def test_expense():
    e = Expense("2024-01-01", 100, "Food", "Lunch")
    assert e.amount == 100
