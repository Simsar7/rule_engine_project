import sqlite3

class RuleStorage:
    def __init__(self, db_path):
        # Allow the connection to be used across threads
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.create_table()

    def create_table(self):
        query = '''CREATE TABLE IF NOT EXISTS rules (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    rule TEXT NOT NULL
                );'''
        self.conn.execute(query)
        self.conn.commit()

    def store_rule(self, rule):
        query = "INSERT INTO rules (rule) VALUES (?)"
        self.conn.execute(query, (rule,))
        self.conn.commit()

    def get_rules(self):
        query = "SELECT * FROM rules"
        return self.conn.execute(query).fetchall()
