#!C:\Users\ASUS\AppData\Local\Programs\Python\Python39\python
import os
import urllib.parse
import sqlite3

print("Content-type: text/html")
print("")

conn = sqlite3.connect("rental.db")
c = conn.cursor()
c.execute("SELECT * FROM house LIMIT 0,10")
data = c.fetchall()
if data != None:
    table = "<table>\n"
    # Create the table's column headers
    header = ["House ID", "Street", "Number of Bedrooms", "Monthly Fee","City ID"]
    table += "  <tr>\n"
    for column in header:
        table += "    <th>{0}</th>\n".format(column)
    table += "  </tr>\n"
    # Create the table's row data
    for line in data:
        row = line
        table += "  <tr>\n"
        for column in row:
            table += "    <td>{0}</td>\n".format(column)
        table += "  </tr>\n"
    table += "</table>"
    print(table)
else:
    print("")
conn.close()
