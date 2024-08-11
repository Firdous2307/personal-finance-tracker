import sqlite3
from transaction import Transaction

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('finance_tracker.db')
        self.create_table()

        