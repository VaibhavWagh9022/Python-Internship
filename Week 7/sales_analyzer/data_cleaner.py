import numpy as np
import pandas as pd


class DataCleaner:
    """Cleans sales dataset"""

    def __init__(self, df):
        self.df = df

    def clean(self):
        if self.df is None:
            print("No data to clean.")
            return None

        # Remove duplicates
        initial_rows = len(self.df)
        self.df = self.df.drop_duplicates()
        print(f"Removed {initial_rows - len(self.df)} duplicates")

        # Handle missing values
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        for col in numeric_cols:
            self.df[col].fillna(self.df[col].median(), inplace=True)

        categorical_cols = self.df.select_dtypes(include=["object"]).columns
        for col in categorical_cols:
            if not self.df[col].mode().empty:
                self.df[col].fillna(self.df[col].mode()[0], inplace=True)

        # Convert date column
        if "order_date" in self.df.columns:
            self.df["order_date"] = pd.to_datetime(self.df["order_date"], errors="coerce")

        print("Data cleaning completed.")
        return self.df
