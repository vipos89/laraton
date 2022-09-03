import sqlite3
import os


class Sqlite:
    def __init__(self):
        self.connection = sqlite3.connect(os.getenv('DB_NAME', 'test.db'))
        self.sql =  self.connection.cursor()

    def execute(self, sql: str):
        self.sql.execute(sql)
        self.connection.commit()
