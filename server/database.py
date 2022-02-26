import sqlite3
from datetime import datetime


class Database:
    def __init__(self, dbname):
        self.dbname = dbname
        self.con = sqlite3.connect(self.dbname)

    def create_table_user(self):
        sql = """CREATE TABLE IF NOT EXISTS users 
                 (uuid text PRIMARY KEY, created_at date, username text, password text)"""
        cursor = self.con.cursor()
        cursor.execute(sql)
        self.con.commit()

    def insert_user(self, uuid, username, password):
        created_at = datetime.today().strftime('%Y-%m-%d')
        sql = "INSERT INTO users (uuid, created_at, username, password) VALUES (?,?,?,?)"
        cursor = self.con.cursor()
        cursor.execute(sql, (uuid, created_at, username, password))
        self.con.commit()

    def select_username_from_users(self, username):
        sql = f"""SELECT password from users WHERE username={username}"""
        cursor = self.con.cursor()
        cursor.execute(sql)
        return cursor.fetchone()[0]
