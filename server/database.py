import sqlite3
from datetime import datetime


class Database:
    def __init__(self, dbname):
        self.dbname = dbname
        self.con = sqlite3.connect(self.dbname, check_same_thread=False)

    def create_table_user(self):
        sql = """CREATE TABLE IF NOT EXISTS users 
                 (uuid text PRIMARY KEY, created_at date, username text UNIQUE, email text, password text)"""
        cursor = self.con.cursor()
        cursor.execute(sql)
        self.con.commit()

    def insert_user(self, uuid, username, email, password):
        created_at = datetime.today().strftime('%Y-%m-%d')
        sql = "INSERT INTO users (uuid, created_at, username, email, password) VALUES (?,?,?,?,?)"
        cursor = self.con.cursor()
        cursor.execute(sql, (uuid, created_at, username, email, password))
        self.con.commit()

    def get_password_for_user(self, username):
        sql = f"SELECT password from users WHERE username=?"
        cursor = self.con.cursor()
        cursor.execute(sql, (username,))
        return cursor.fetchone()[0]

    # Table 2 - Code
    def create_table_codes(self):
        sql = "CREATE TABLE IF NOT EXISTS codes (uuid text, code text)"
        cursor = self.con.cursor()
        cursor.execute(sql)
        self.con.commit()

    def insert_code(self, uuid, code):
        sql = "INSERT INTO codes (uuid, code) VALUES (?,?)"
        cursor = self.con.cursor()
        cursor.execute(sql, (uuid, code))
        self.con.commit()

    def get_uuid(self, code):
        sql = "SELECT uuid FROM codes WHERE code=?"
        cursor = self.con.cursor()
        cursor.execute(sql, (code,))
        return cursor.fetchone()[0]
