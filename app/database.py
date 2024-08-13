import sqlite3
from transaction import Transaction

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('finance_tracker.db')
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount REAL,
                category TEXT,
                description TEXT,
                type TEXT,
                date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()    

    def add_transaction(self, transaction):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO transactions (amount, category, description, type)
            VALUES (?, ?, ?, ?)
        ''', (transaction.amount, transaction.category, transaction.description, transaction.type))
        self.conn.commit()    

    def get_all_transactions(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM transactions')
        rows = cursor.fetchall()
        return [Transaction(*row[1:5], row[5]) for row in rows]

    def clear_transactions(self):
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM transactions')
        self.conn.commit()
        print("All transactions have been deleted.")

    def __del__(self):
        self.conn.close()
