#!C:\Users\ASUS\AppData\Local\Programs\Python\Python39\python
import os
import urllib.parse
import sqlite3
import http.cookies as Cookie

print("Content-type: text/html")
print("")
print("<script src='main.js'></script>")

cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
conn = sqlite3.connect("rental.db")
c = conn.cursor()
c.execute("SELECT username FROM user WHERE sessionId = ?;",(cookie["session"].value,))
username = c.fetchone()
c.execute("SELECT * FROM rent LEFT JOIN house ON rent.houseId = house.houseId WHERE rent.username = ?", (username[0],))
data = c.fetchall()
if data != None:
    table = "<table>\n"
    # Create the table's column headers
    header = ["Street", "City", "Number of Bedrooms", "Monthly Fee", "Delete?"]
    table += "  <tr>\n"
    for column in header:
        table += "    <th>{0}</th>\n".format(column)
    table += "  </tr>\n"
    # Create the table's row data
    for line in data:
        row = line[3:]
        #print(row)
        table += "  <tr>\n"
        for column in row:
            table += "    <td>{0}</td>\n".format(column)
        table += "    <td><button type='submit' class='btn-login  gr-bg' id={0} onclick='deleteAd(this.id)' >Delete!</button></td>\n".format(line[2])
        table += "  </tr>\n"
    table += "</table>"
    print(table)
else:
    print("")
conn.close()
