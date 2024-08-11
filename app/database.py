import sqlite3

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

    def __del__(self):
        self.conn.close()
