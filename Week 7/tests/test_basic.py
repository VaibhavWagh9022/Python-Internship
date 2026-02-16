import pandas as pd
from sales_analyzer.analyzer import SalesAnalyzer


def test_total_sales():
    data = {
        "total_amount": [100, 200, 300],
        "customer_id": [1, 2, 3],
        "product_id": [10, 20, 30],
        "category": ["A", "B", "C"],
        "product_name": ["P1", "P2", "P3"],
    }

    df = pd.DataFrame(data)
    analyzer = SalesAnalyzer(df)

    assert analyzer.basic_stats()["Total Sales"] == 600
