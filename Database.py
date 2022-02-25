import sqlite3
from sqlite3 import Error


class Database:

    def __init__(self):
        self.file = "rental.db"

    def connect(self):
        # Establish Connection with database
        conn = None

        try:
            conn = sqlite3.connect(self.file)
        except Error as e:
            print(e)

        return conn

    def queryExecute(self, query, param=[]):
        # Execute Query commands
        conn = self.connect()
        try:
            curs = conn.cursor()
            curs.execute(query, param)
        except Error as e:
            print(e)
        conn.commit()
        return curs.fetchone()

