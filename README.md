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

A good resource about [The Four Pillars of Object-Oriented Programming](https://www.freecodecamp.org/news/four-pillars-of-object-oriented-programming/)

Although the language used was in JavaScript, the principle still remains the same.


## SQL Lite



Using an SQLite database for this project is advantageous because:

**Simplicity**: SQLite is lightweight and easy to set up, making it ideal for small to medium-sized projects without the need for complex database configurations.

**Embedded**: SQLite is a serverless database, meaning it runs in-process with your application. This eliminates the need for a separate database server and simplifies deployment.

**File-Based Storage**: It stores data in a single file, which is convenient for a personal finance tracker where data management needs are straightforward.

**Zero Configuration**: SQLite requires minimal configuration, allowing you to focus more on developing your application rather than managing database settings.


[SQL Lite Docs](https://www.sqlite.org/docs.html)


[SQLite3](https://docs.python.org/3/library/sqlite3.html#module-sqlite3)



The Database class in my code is responsible for managing the connection to an SQLite database and performing operations like creating tables, adding transactions, and retrieving data.

The import statement **from transaction import Transaction** is used to work with the Transaction class, likely representing individual financial transactions.



## Adding a New Table

The **create_table** method creates a table named **transactions** in the SQLite database if it doesn't already exist. It defines columns for transaction details such as amount, category, description, type, and a date with a default timestamp. After executing the SQL command, it commits the changes to ensure the table is created.

## Creating a Transaction Python File

Well, I thought I had this created already, cause when i was running the python command for the main.py and checking the database using SQLite CLI, it was empty i.e the **finance_tracker.db**. So let us go ahead in creating a **transaction.py** file.

This file defines the Transaction class, which represents a financial transaction with attributes for amount, category, description, type, and date. The __init__ method initializes these attributes, while the __str__ method provides a formatted string representation of the transaction.



## Using SQLite Command Line Interface

Open your terminal or command prompt and start the SQLite command line tool with:
```
bash
sqlite3 finance_tracker.db
```

Check Tables:

List all tables in the database with:
```
sql
.tables
```
View Table Schema:

Check the schema of the transactions table with:
```
sql
.schema transactions
```

Query Data:

If you want to view all records from a specific table:
```
sql
SELECT * FROM table_name;
```
Exit SQLite:

Exit the SQLite command line tool with:
```
sql
.exit
```


Pictures and texts will be implemented later for the Adding Transactions.

## Viewing Transactions

After adding more transactions to the database, I  need to view and analyze these transactions to ensure the data is being recorded accurately.

This can involve querying the database to retrieve and display transaction records, allowing me to verify that each transaction was stored correctly and to review details such as amount, category, and type.
