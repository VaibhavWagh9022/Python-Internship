import pandas as pd


class Reporter:
    """Generates Excel report"""

    def __init__(self, df):
        self.df = df

    def generate(self, output_path="data/reports/sales_report.xlsx"):
        try:
            with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
                # Summary
                summary = {
                    "Total Sales": self.df["total_amount"].sum(),
                    "Average Order": self.df["total_amount"].mean(),
                    "Total Orders": len(self.df),
                }
                pd.DataFrame([summary]).to_excel(
                    writer, sheet_name="Summary", index=False
                )

                # Monthly
                self.df["month"] = self.df["order_date"].dt.to_period("M")
                monthly = self.df.groupby("month")["total_amount"].sum()
                monthly.to_excel(writer, sheet_name="Monthly Sales")

                # Category
                category = (
                    self.df.groupby("category")["total_amount"].sum()
                )
                category.to_excel(writer, sheet_name="Category Sales")

            print("Report generated successfully.")
        except Exception as e:
            print(f"Error generating report: {e}")
