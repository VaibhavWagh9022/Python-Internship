from finance_tracker.expense import Expense
from finance_tracker.expense_manager import ExpenseManager
from finance_tracker.file_handler import (
    load_expenses, save_expenses, export_csv, backup_data
)
from finance_tracker.reports import category_report, monthly_total, text_chart

class FinanceTracker:
    def __init__(self):
        self.manager = ExpenseManager()
        self.manager.expenses = load_expenses()

    def run(self):
        while True:
            print("\n1.Add \n2.View \n3.Search \n4.Report \n5.Export \n6.Backup \n0.Exit")
            choice = input("Choice: ")

            if choice == "1":
                self.add()
                save_expenses(self.manager.expenses)
            elif choice == "2":
                self.view()
            elif choice == "3":
                self.search()
            elif choice == "4":
                self.report()
            elif choice == "5":
                export_csv(self.manager.expenses)
                print("Exported to CSV")
            elif choice == "6":
                backup_data()
                print("Backup created")
            elif choice == "0":     
                print("Thank You for using Finance Tracker!!")   
                break

    def add(self):
        try:
            
            e = Expense(
                input("Date (YYYY-MM-DD): "),
                input("Amount: "),
                input("Category: "),
                input("Description: ")
            )
            self.manager.add_expense(e)
            print("Expense added")
        except Exception as e:
            print("Error:", e)
            self.add()

    def view(self):
        for e in self.manager.expenses:
            print(e.to_dict())

    def search(self):
        key = input("Keyword: ")
        for e in self.manager.search(key):
            print(e.to_dict())

    def report(self):
        data = category_report(self.manager.expenses)
        text_chart(data)
        print("Total:", monthly_total(self.manager.expenses))

def main():
    FinanceTracker().run()
