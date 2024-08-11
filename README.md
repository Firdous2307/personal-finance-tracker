# Personal Finance Tracker

This is a simple personal finance tracker application built with Python. It allows users to track their income and expenses, view transactions, and generate basic financial reports.


## Features

- Add income and expense transactions
- View all transactions
- Generate a basic financial report
- SQLite database for data storage


## Modules

- This package contains a generic transaction implementation for Python.

[Transaction](https://pypi.org/project/transaction/)

**Note** - The **main_menu()** is executed when you run your script. The if **__name__ == "__main__":** check ensures that main_menu() is only called when the script is run directly, not when it's imported as a module.



A database is crucial for this project to store and manage transaction data efficiently, ensuring quick access, data integrity, and scalability as the project grows.

# **Note**

The import statement **(from database import Database)** is used in the project to integrate a custom or third-party database module that handles transaction data storage and retrieval.

While there are many Python packages available for database management on the [Python Package Index](https://pypi.org/).

So, creating a custom database module ensures that your database management is perfectly aligned with your project's needs, offering flexibility and control over data handling and future enhancements.


It follows the 4 principles of OOP(Object Oriented Programming)