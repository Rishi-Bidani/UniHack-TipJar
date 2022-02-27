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

    def get_username(self, uuid):
        sql = f"SELECT username from users WHERE uuid=?"
        cursor = self.con.cursor()
        cursor.execute(sql, (uuid,))
        return cursor.fetchone()[0]

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

    # Table 3 - userData
    def create_table_userdata(self):
        sql = """CREATE TABLE IF NOT EXISTS userdata 
                 (uuid text PRIMARY KEY, username text UNIQUE, bio text, links text)"""
        cursor = self.con.cursor()
        cursor.execute(sql)
        self.con.commit()

    def insert_userdata(self, uuid, username, bio, links):
        sql = "INSERT INTO userdata(uuid, username, bio, links) VALUES(?,?,?,?)"
        cursor = self.con.cursor()
        cursor.execute(sql, (uuid, username, bio, links))
        self.con.commit()

    def update_bio(self, uuid, bio):
        sql = "UPDATE userdata SET bio=? WHERE uuid=?"
        cursor = self.con.cursor()
        cursor.execute(sql, (bio, uuid))
        self.con.commit()

    def update_links(self, uuid, links):
        sql = "UPDATE userdata SET links=? WHERE uuid=?"
        cursor = self.con.cursor()
        cursor.execute(sql, (links, uuid))
        self.con.commit()

    def update_userdata(self, uuid, links, bio):
        sql = "UPDATE userdata SET links=?, bio=? WHERE uuid=?"
        cursor = self.con.cursor()
        cursor.execute(sql, (links, bio, uuid))
        self.con.commit()

    def get_bio(self, uuid):
        sql = "SELECT bio FROM userdata WHERE uuid=?"
        cursor = self.con.cursor()
        cursor.execute(sql, (uuid,))
        return cursor.fetchone()[0]

    def get_links(self, uuid):
        sql = "SELECT links FROM userdata WHERE uuid=?"
        cursor = self.con.cursor()
        cursor.execute(sql, (uuid,))
        return cursor.fetchone()[0]
