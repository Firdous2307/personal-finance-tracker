# Personal Finance Tracker

This is a simple personal finance tracker application built with Python. It allows users to track their income and expenses, manage budgets, receive alerts, view transactions, and generate detailed financial reports.


## Features

- **Add Income and Expense Transactions:** Easily add and categorize your income and expenses.

- **View Transactions:** View a detailed list of all your transactions, including dates, categories, and descriptions.

- **Budget Management:** Set budgets for different categories and monitor your spending against these budgets.

- **Alerts and Notifications:** Receive real-time alerts via AWS SNS when your spending exceeds or approaches your budget limits.

- **Financial Reports:** Generate comprehensive financial reports and export them to CSV for further analysis.

- **SQLite Database:** Securely store all financial data using SQLite.

## Installation

1. Fork the Repository:

Click the `Fork` button at the top right corner to create a copy of the repository in your GitHub account.

2. Clone Your Forked Repository:

Replace your-username with your GitHub username in the following command:

```bash
git clone https://github.com/your-username/personal-finance-tracker.git
```
3. Navigate to the Project Directory:

```bash
cd personal-finance-tracker
```

4. Install the required dependencies:
```python
pip install -r requirements.txt
```

## Usage

Run the main script to start the application:
```python
python main.py
```

Follow the on-screen prompts to add transactions, view transactions, and generate reports.

## Project Structure

- **main.py:** The main script that runs the application.

- **database.py:** Handles database operations.

- **transaction.py:** Defines the Transaction class.

- **report.py:** Contains functions for generating financial reports.

- **config.py:** Stores configuration settings.

- **requirements.txt:** Lists the project dependencies.

- **README.md:** This file, containing project information and instructions.


## Contributing

Feel free to fork this project and submit pull requests with any improvements or bug fixes.

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).


To run this project, you'll need Python installed on your system. The only external dependency is SQLite, which is included in Python's standard library.
