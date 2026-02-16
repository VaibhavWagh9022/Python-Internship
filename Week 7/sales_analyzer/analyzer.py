import pandas as pd


class SalesAnalyzer:
    """Performs sales data analysis"""

    def __init__(self, df):
        self.df = df

    def basic_stats(self):
        stats = {
            "Total Sales": self.df["total_amount"].sum(),
            "Average Order Value": self.df["total_amount"].mean(),
            "Total Orders": len(self.df),
            "Unique Customers": self.df["customer_id"].nunique(),
            "Unique Products": self.df["product_id"].nunique(),
        }
        return stats

    def sales_by_category(self):
        return (
            self.df.groupby("category")["total_amount"]
            .sum()
            .sort_values(ascending=False)
        )

    def monthly_sales(self):
        if "order_date" not in self.df.columns:
            return None

        self.df["month"] = self.df["order_date"].dt.to_period("M")
        monthly = self.df.groupby("month")["total_amount"].sum()
        return monthly

    def top_products(self, n=5):
        return (
            self.df.groupby("product_name")["total_amount"]
            .sum()
            .sort_values(ascending=False)
            .head(n)
        )
