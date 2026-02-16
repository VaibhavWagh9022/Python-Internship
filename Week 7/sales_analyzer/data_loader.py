import pandas as pd


class DataLoader:
    """Loads sales data from different file formats"""

    def __init__(self, file_path):
        self.file_path = file_path

    def load(self):
        """Load CSV or Excel file"""
        try:
            if self.file_path.endswith(".csv"):
                df = pd.read_csv(self.file_path)
            elif self.file_path.endswith(".xlsx"):
                df = pd.read_excel(self.file_path)
            else:
                raise ValueError("Unsupported file format")

            print(f"Data loaded successfully: {df.shape}")
            return df

        except Exception as e:
            print(f"Error loading file: {e}")
            return None
