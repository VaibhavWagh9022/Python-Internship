# 💰 Personal Finance Tracker (Week 4 Final Project)

A **menu-driven Personal Finance Tracker** built using **Python file handling, modular programming, and error handling**.  
This project helps users **record, store, analyze, and manage expenses** with persistent data storage using **JSON and CSV files**.

---

## 📌 Project Overview

Managing personal expenses manually can be difficult and error-prone.  
This project provides a **simple command-line application** that allows users to:

- Add daily expenses
- Categorize spending
- Store data permanently using files
- Generate expense reports
- Export data for further analysis
- Create backups for data safety

The project demonstrates **real-world usage of Python file handling concepts** taught in Weeks 1–4.

---

## 🎯 Objectives

- Understand file operations in Python
- Implement data persistence using JSON and CSV
- Practice modular programming
- Handle file-related errors gracefully
- Build a real-world, end-to-end application
- Improve debugging and testing skills

---

## 🛠️ Technologies Used

- **Language:** Python 3.13.7
- **File Formats:** JSON, CSV  
- **Concepts:**  
  - File Handling  
  - Context Managers (`with` statement)  
  - Exception Handling  
  - Object-Oriented Programming  
  - Modular Code Structure  

---

## 📂 Project Structure
```
week4-finance-tracker/
│
├── run.py 
├── requirements.txt
├── README.md
│
├── finance_tracker/
│ ├── init.py
│ ├── main.py
│ ├── expense.py 
│ ├── expense_manager.py
│ ├── file_handler.py
│ ├── reports.py
│ └── utils.py
│
├── data/
│ ├── expenses.json 
│ ├── backup/ 
│ └── exports/ 
│
└── tests/
├── test_expense.py 
├── test_file_handler.py
└── test_reports.py

```
---

## ⚙️ Features Implemented

### 📥 Expense Management
- Add new expenses with:
  - Date
  - Amount
  - Category
  - Description
- Input validation for date and amount
- Persistent storage using JSON files

### 🔍 Search Functionality
- Search expenses by:
  - Category
  - Description keywords

### 📊 Reports & Statistics
- Category-wise expense breakdown
- Monthly total calculation
- Text-based visual charts for quick analysis

### 💾 File Handling
- Save and load expenses using JSON
- Export expenses to CSV format
- Automatic backup creation
- Safe file operations using context managers

### 🧰 Error Handling
- Invalid date format handling
- Negative/zero amount validation
- Missing file handling
- Graceful program termination

---

## ▶️ How to Run the Project

### Step 1: Clone or Download
```bash
git clone https://github.com/VaibhavWagh9022/Python-Internship.git

cd Week 4

pip install -r requirements.txt
```
### Step 2: Run the Application
```bash
python run.py
```
---

## 🧭 Sample Menu

    Add Expense

    View Expenses

    Search Expenses

    Generate Report

    Export to CSV

    Backup Data

    Exit


---

## 🧪 Testing

Basic unit tests are provided in the `tests/` folder.

To run tests:
```bash
# On new terminal
python -m pytest 
```
---

## 📦 Data Storage Details

- **JSON File:**  
  Used for permanent storage of expenses between runs.
  
- **CSV Export:**  
  Used for opening data in Excel or Google Sheets.

- **Backup System:**  
  Automatically copies data into `data/backup/` directory.

---

## 🧠 Concepts Demonstrated

- File reading & writing
- Context managers (`with open(...)`)
- JSON serialization/deserialization
- CSV handling
- Object-oriented design
- Modular programming
- Debugging & testing
- Real-world problem solving

---

## 🚀 Future Enhancements

- Budget tracking & alerts
- Recurring expenses
- Graphical visualizations
- GUI or web-based interface
- Database integration
- Expense prediction using analytics

---

## 📚 Learning Outcome

After completing this project, you will be able to:

- Build real-world applications using Python
- Handle files safely and efficiently
- Structure large programs using modules
- Apply error handling and debugging techniques
- Prepare industry-level mini projects

---

## 👨‍🎓 Author

**Vaibhav wagh**  
Computer Engineering Student  

---
