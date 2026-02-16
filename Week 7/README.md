# 📊 Sales Data Analysis Dashboard

A comprehensive sales data analysis system built using **Python, Pandas, NumPy, and Matplotlib**.  
This project processes raw sales data, performs business analysis, generates insights, and creates visual reports.

---

## 🚀 Project Overview

This project simulates a real-world business scenario where sales data is analyzed to:

- Clean and preprocess raw data
- Calculate key performance metrics
- Analyze sales trends
- Generate business insights
- Create visual reports
- Export analysis results to Excel

---

## 📂 Project Structure
```
week7-sales-analysis/
│── sales_analyzer/
│ ├── init.py
│ ├── data_loader.py
│ ├── data_cleaner.py
│ ├── analyzer.py
│ ├── visualizer.py
│ └── reporter.py
│── notebooks/
│ ├── exploration.ipynb
│ └── analysis.ipynb
│── data/
│ ├── raw/
│ │ └── sales_data.csv
│ ├── processed/
│ └── reports/
│── tests/
│── requirements.txt
│── README.md
│── .gitignore
└── main.py
```

---


## 📈 Features

✔ Load sales data from CSV or Excel  
✔ Automatic data cleaning  
✔ Calculate key metrics:
- Total Sales
- Average Order Value
- Total Orders
- Unique Customers
- Top Products
✔ Monthly sales trend analysis  
✔ Sales by category analysis  
✔ Generate visualizations:
- Line chart
- Bar chart
- Histogram  
✔ Export Excel report  
✔ Modular and scalable architecture  

---

## 🛠️ Installation

```bash
cd week7
```

## Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

Make sure your sales dataset exists at:

data/raw/sales_data.csv


Then run:
```bash
python main.py
```

---

## 📊 Sample Output

### Console Output
```
=== BASIC STATISTICS ===
Total Sales: 4880
Average Order Value: 488.0
Total Orders: 10
Unique Customers: 8
Unique Products: 10
```

### Generated Reports
```
data/reports/
│── monthly_trend.png
│── category_sales.png
│── order_distribution.png
└── sales_report.xlsx
```

---

## 📌 Technologies Used

- Python 3.x
- Pandas
- NumPy
- Matplotlib
- OpenPyXL
- Jupyter Notebook

---

## 📊 Key Business Insights Generated

- Highest performing product categories
- Monthly growth trends
- Top-selling products
- Customer distribution
- Order value distribution

---

## 🔮 Future Improvements

- Add Streamlit interactive dashboard
- Add customer lifetime value (CLV) calculation
- Add cohort analysis
- Add forecasting using moving averages
- Connect to SQL database
- Deploy as web application

---





