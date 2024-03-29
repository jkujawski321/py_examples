import psycopg2

class Database:
    def __init__(self, db):
        self.conn = psycopg2.connect("dbname= 'database1' user='postgres' password='postgres123' host='localhost' port='5432'")
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        self.conn.commit()

    def add_entry(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO book VALUES (NULL, ?, ? ,?, ?)",(title, author, year, isbn))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * from book")
        rows = self.cur.fetchall()
        return rows

    def search(self, title="", author="", year="", isbn=""):
        self.cur.execute("SELECT * FROM book WHERE title=? OR author =? OR year=? OR isbn=?",(title, author, year, isbn))
        rows = self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM book WHERE id=?",(id,))
        self.conn.commit()

    def update(self, id, title, author, year, isbn):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn?",(title, author, year, isbn))

    def __del__(self):
        self.conn.close()
