#!C:\Users\ASUS\AppData\Local\Programs\Python\Python39\python
import os
import urllib.parse
import sqlite3

print("Content-type: text/html")
print("")

query = os.environ["QUERY_STRING"]
pairs = urllib.parse.parse_qs(query)
if "q" in pairs.keys():
    houseId = pairs["q"][0]
    conn = sqlite3.connect("rental.db")
    c = conn.cursor()
    c.execute("DELETE FROM rent where houseId = ?", (houseId,))
    c.execute("DELETE FROM house where houseId = ?", (houseId,))
    conn.commit()
    print("row[4]")
    conn.close()
else:
    print ("row[3]")
