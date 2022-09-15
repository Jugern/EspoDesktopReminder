import sqlite3

class Base():

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.correctBase = 0

    def checkDatabase(self):
        conn = sqlite3.connect('base.db')
        cur = conn.cursor()
        cur.execute("""SELECT * FROM Notifications""")

    def checkNotification(self):
        conn = sqlite3.connect('base.db')
        cur = conn.cursor()
        cur.execute("""SELECT * FROM Notifications""")

