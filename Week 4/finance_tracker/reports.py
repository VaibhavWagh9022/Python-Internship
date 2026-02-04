from collections import defaultdict

def category_report(expenses):
    report = defaultdict(float)
    for e in expenses:
        report[e.category] += e.amount
    return report

def monthly_total(expenses):
    return sum(e.amount for e in expenses)

def text_chart(data):
    for key, value in data.items():
        print(f"{key:<15}: {'#' * int(value // 100)} ₹{value}")
