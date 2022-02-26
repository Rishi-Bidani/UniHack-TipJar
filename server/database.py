import sqlite3


class Database:
    def __init__(self, dbname):
        self.dbname = dbname
        self.con = sqlite3.connect(self.dbname)

    def create_table_user(self):
        sql = """CREATE TABLE IF NOT EXISTS users 
                 (UUID text PRIMARY KEY, created_at date, username text, password text)"""
        cursor = self.con.cursor()
        cursor.execute(sql)
        self.con.commit()

