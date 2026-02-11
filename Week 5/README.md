## 📚 Library Management System (Week 5 Final Project)

A menu-driven Library Management System built using Object-Oriented Programming (OOP), file handling, and modular architecture in Python.
This project allows librarians to manage books, members, borrowing operations, and overdue tracking with persistent data storage using JSON files.
___

## 📌 Project Overview

Managing a library manually can be complex and inefficient.
This project provides a command-line application that allows users to:

Add and manage books

Register and manage members

Borrow and return books

Track due dates and overdue books

Search books by title, author, or ISBN

Save and load data automatically

Create automatic backups for data safety

The project demonstrates real-world implementation of Object-Oriented Programming concepts learned in Week 5.
___

## 🎯 Objectives

Understand and apply OOP principles

Design real-world class relationships

Implement multi-class interaction

Practice JSON file persistence

Build a modular Python application

Implement unit testing

Improve debugging and system design skills
___
## 🛠️ Technologies Used

Language: Python 3.x

File Format: JSON

Concepts:

Object-Oriented Programming

Classes & Objects

Inheritance

Encapsulation

File Handling

Context Managers

Exception Handling

Modular Programming

Unit Testing
___

## 📂 Project Structure
~~~
week5-library-system/
│
├── requirements.txt
├── README.md
├── .gitignore
│
├── library_system/
│   ├── __init__.py
│   ├── main.py
│   ├── book.py
│   ├── member.py
│   └── library.py
│
├── data/
│   ├── books.json
│   ├── members.json
│   └── backup/
│
└── tests/
    ├── test_book.py
    ├── test_member.py
    └── test_library.py
~~~
___
# ⚙️ Features Implemented
📘 Book Management

Add new books with:

Title

Author

ISBN

Year

Track availability status

Track borrowed member

Due date assignment

### 👤 Member Management

Register new members

Borrow limit per member (default: 5 books)

Track borrowed books

Member validation

### 🔄 Borrow & Return System

Borrow books with automatic due date (14 days)

Prevent double borrowing

Return books with overdue detection

Automatic overdue calculation

### 🔍 Search Functionality

Search books by:

Title

Author

ISBN

Display formatted search results

## 📊 Library Statistics

Total books

Available books

Borrowed books

Overdue books

Total members

## ▶️ How to Run the Project

## Step 1: Navigate to Project Folder
~~~bash
cd week5-library-system
~~~
## Step 2: Run the Application
~~~bash
python -m library_system.main
~~~

## 🧭 Sample Menu
~~~
===== LIBRARY MANAGEMENT SYSTEM =====

1. Add Book
2. Register Member
3. Borrow Book
4. Return Book
5. Search Books
6. View All Books
7. Save & Exit
0. Exit Without Saving
~~~


## 👨‍🎓 Author

Vaibhav Wagh <br> 
Computer Engineering Student