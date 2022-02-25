#!C:\Users\ASUS\AppData\Local\Programs\Python\Python39\python
import http.cookies as Cookie
import random
import sqlite3
import cgi

def printHeader(title):
	print ("Content-type: text/html")
	print ("")
	print ("<html><head><title>{}</title></head><body>".format(title))
def printFooter():
	print ("</body></html>")

printHeader("Create Advertisement")
form = cgi.FieldStorage()

if ("street" in form.keys() and "city_2" in form.keys() and "bedroom" in form.keys() and "fee" in form.keys()):
    try:
        conn = sqlite3.connect("rental.db")
        c = conn.cursor()
        c.execute("SELECT cid FROM city WHERE cname = ?",(form["city_2"].value,))
        row = c.fetchone()
        city_id = int(row[0])
        sql = "INSERT INTO house (street, noOfBedrooms, MonthlyFee, cityId) VALUES (?, ?, ?, ?);"
        val = (form["street"].value,form["bedroom"].value,form["fee"].value,city_id)
        c.execute(sql,val)
        conn.commit()
        print("<p>Successfully created!</p>")
        conn.close()
        print ("<script>")
        print ("window.location = 'afterLogin.html';")
        print ("</script>")
    except:
        print("<p>Please control your advertisement information</p>")
else:
    print("<p>Please enter your all information</p>")

printFooter()
