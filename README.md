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
```bash
sqlite3 finance_tracker.db
```

Check Tables:
```sql
.tables
```

View Table Schema:
```sql
.schema transactions
```

Query Data:
```sql
SELECT * FROM table_name;
```

Exit SQLite:
```sql
.exit
```


Pictures and texts will be implemented later for the Adding Transactions.

## Viewing Transactions

After adding more transactions to the database, I  need to view and analyze these transactions to ensure the data is being recorded accurately.

This can involve querying the database to retrieve and display transaction records, allowing me to verify that each transaction was stored correctly and to review details such as amount, category, and type.

Okay, so when i ran the python command to run the **main.py** and viewed the transactions, I got a list of the transactions made alongside datestamps

Oh, also forgot to add exit option in **main.py**

!Pictures Later




## Generating Reports

With the ability to add and view transactions, generating reports is important for understanding spending habits and managing finances. Reports help users see where their money is going, track income, and make better financial choices by turning data into useful insights.


Currently, looking for a way to streamline the process of aggregating expenses by category.


Well, I found a way. In the **generate_report** function, **defaultdict** from the collections module is utilized to streamline the process of aggregating expenses by category.


**defaultdict(float)** simplifies the handling of expenses by automatically initializing any new category with a default value of 0.0.

Using **defaultdict**, we can directly update the total amount for each category without additional conditional logic. When adding an expense, defaultdict ensures that the category exists and is initialized to 0.0 if not previously encountered.


Good Resource on [How to Use DefaultDict in Python](https://www.freecodecamp.org/news/how-to-use-defaultdict-python/)



Adding a configuration file would be nice so as to prevent hardcoding them into the application, Change configurations without altering the main codebase etc.
 

 Also, let's allow users to use their preferred currency symbol. I know Dollar is the global currency but lets add more functionalities. 



 ## All Done

 So currently, if you run the main.py and test it out, it works successfully, but i am thinking of turning the Personal Finance Tracker into a web app, so as to enhance its usability by providing an intuitive interface that's accessible from any device with a browser.



## Budgeting

The `Budget` class allows me to manage budget categories and amounts. It initializes with an empty dictionary for storing budgets and a currency symbol, defaulting to '$'. This setup enables me to customize the currency symbol for display purposes. Looking good so far.


### Budget Class Methods

- **`set_budget(category, amount)`**: Sets the budget for a specified category and prints the budget set with the currency symbol.

- **`check_budget(category, spent)`**: Checks if spending exceeds the budget for a category and prints an alert or warning if spending is close to or over the budget.

- **`view_budgets()`**: Displays all budget categories and their amounts with the currency symbol.


## Importing Budget into Main

The `manage_budget` function provides an interface for users to manage their budgets. It allows users to:
- **Set Budget**: Enter a category and amount to set a budget.
- **View Budgets**: Display all current budgets with the specified currency symbol.
- **Back to Main Menu**: Exit the budget management interface and return to the main menu

Unfortunately, when i ran the main.py, it showed an error(picture later), now i am thinking why this?. Everything is already in place 

Oh forgot to define the variable budget in the main function.

Now, the **main.py** should handle the user's choices for setting a budget or viewing budgets. 


## Alerting
Now, let us work on the alert system to combat overspending.

The `Alerts` class monitors spending and triggers budget alerts. 

The `Alerts` class does not need its own menu in `main.py` because it's integrated into the existing functionality. Alerts are checked when exiting the application, rather than being a separate feature the user interacts with directly.

Alerts shows when exiting the application, I am so happy and excited, I will upload pictures later.

So as to not make the process of transactions to be clogeled up, i have decided to add a Method to Clear Transactions in Database, Add a Menu Option to Clear Transactions.


Added successfully.

## Running the Tests

**Standalone Testing**: Run the test files (test_budget.py and test_alerts.py) independently to verify the functionality.

**Integrated Testing**: Run main.py and perform transactions to see how the budgets and alerts behave in a real use case.


I initially rushed into integrating the components without conducting standalone testing first, which isn't the best practice. I realize now that performing standalone tests before integration is crucial for ensuring each component functions correctly on its own.

**sys.path.insert:**

This line adds the app directory to the sys.path, allowing the script to find and import alert.py, budget.py, and transaction.py from the app directory.

## CSV Report Export

The **export_report_to_csv** function allows users to export their financial data from the Personal Finance Tracker into a CSV file. This feature enhances the usability and accessibility of the data by providing a portable, widely compatible format that can be used across different platforms and applications.


## Time to add Cloud Services

I want to integrate AWS services into the Personal Finance Tracker because I enjoy using cloud services and believe scalable features will be beneficial.


## Using AWS SDK

The AWS SDK provides:

- **API Documentation**: Detailed references and guides for all AWS services, helping you understand how to interact with them programmatically.
- **Code Samples**: Example code snippets in various programming languages to illustrate how to use AWS services effectively.
- **Documentation**: Comprehensive guides, tutorials, and best practices for setting up, configuring, and optimizing AWS services.

These resources make it easier to integrate AWS services into your applications, streamline development, and troubleshoot issues.


## AWS SNS

To integrate AWS services into the personal finance tracker for receiving alerts, we can use AWS Simple Notification Service (SNS). AWS SNS allows you to send notifications (e.g., email, SMS) when certain conditions are met, like exceeding a budget in your finance tracker.


Really good code snippets here, Kudos to the AWS SDK Community;

[Shows how to use the AWS SDK for Python (Boto3) with Amazon Simple Notification
Service (Amazon SNS) to create notification topics, add subscribers, and publish
messages](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/python/example_code/sns/sns_basics.py#L33)

The `SNSNotifier` class initializes an SNS resource using boto3 and provides a method to create an SNS topic with a default name of `BudgetAlerts`. It includes error handling with logging to track the creation process and catch any issues.

[What is Amazon SNS?](https://docs.aws.amazon.com/sns/latest/dg/welcome.html)

[Get started with Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/sns-getting-started.html)

[How it works](https://docs.aws.amazon.com/sns/latest/dg/sns-how-it-works.html)


The alert system is set up to send emails when the budget is exceeded or close to being exceeded.



## Note

A few points to consider:

**Alert Timing:** In the current setup, the alerts are only checked when the user chooses to exit the program (option 7 in the main menu). This means that even if a transaction causes the budget to be exceeded, the alert won't be sent until the user exits the program.

Remember that when you first subscribe an email to an SNS topic, AWS sends a confirmation email. The subscription must be confirmed before any alerts will be received.


Check alerts after each transaction is added:

In the `add_transaction` function, after adding the transaction to the database, 

```python
alerts.check_alerts(db.get_all_transactions())
```

Initialize the SNSNotifier in the main function:
```python
alerts.notifier.setup()
```
This ensures the SNS topic is created and the email is subscribed.


This setup will send an alert email (if conditions are met) right after a transaction is added, rather than waiting until the program exits.