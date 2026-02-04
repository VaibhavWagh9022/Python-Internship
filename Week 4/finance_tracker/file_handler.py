import json, csv, os, shutil
from finance_tracker.expense import Expense

DATA_FILE = "data/expenses.json"
BACKUP_DIR = "data/backup/"

def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as f:
        data = json.load(f)
        return [Expense(**e) for e in data]

def save_expenses(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump([e.to_dict() for e in expenses], f, indent=4)

def backup_data():
    os.makedirs(BACKUP_DIR, exist_ok=True)
    shutil.copy(DATA_FILE, BACKUP_DIR + "expenses_backup.json")

def export_csv(expenses):
    os.makedirs("data/exports", exist_ok=True)
    with open("data/exports/expenses.csv", "w", newline="") as f:
        writer = csv.DictWriter(
            f, fieldnames=["date", "amount", "category", "description"]
        )
        writer.writeheader()
        for e in expenses:
            writer.writerow(e.to_dict())
