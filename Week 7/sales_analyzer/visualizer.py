import matplotlib.pyplot as plt
import os


class Visualizer:
    """Creates visualizations"""

    def __init__(self, df):
        self.df = df
        os.makedirs("data/reports", exist_ok=True)

    def monthly_trend(self):
        self.df["month"] = self.df["order_date"].dt.to_period("M")
        monthly = self.df.groupby("month")["total_amount"].sum()

        plt.figure(figsize=(10, 5))
        monthly.plot(kind="line", marker="o")
        plt.title("Monthly Sales Trend")
        plt.xlabel("Month")
        plt.ylabel("Total Sales")
        plt.tight_layout()
        plt.savefig("data/reports/monthly_trend.png")
        plt.close()

    def category_bar(self):
        category_sales = (
            self.df.groupby("category")["total_amount"]
            .sum()
            .sort_values(ascending=False)
        )

        plt.figure(figsize=(8, 5))
        category_sales.plot(kind="bar")
        plt.title("Sales by Category")
        plt.tight_layout()
        plt.savefig("data/reports/category_sales.png")
        plt.close()

    def sales_distribution(self):
        plt.figure(figsize=(8, 5))
        plt.hist(self.df["total_amount"], bins=30)
        plt.title("Order Value Distribution")
        plt.tight_layout()
        plt.savefig("data/reports/order_distribution.png")
        plt.close()
