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

printHeader("Register")
form = cgi.FieldStorage()

if ("username" in form.keys() and "pass" in form.keys() and "fullname" in form.keys() and "email" in form.keys() and "phone" in form.keys()):
    try:
        conn = sqlite3.connect("rental.db")
        c = conn.cursor()
        sql = "INSERT INTO user VALUES (?,?,?,?,?,?)"
        val = (form["username"].value,form["pass"].value,form["fullname"].value,form["email"].value,form["phone"].value,-1)
        c.execute(sql,val)
        conn.commit()
        print("<p>Register is successful</p>")
        conn.close()
        print ("<script>")
        print ("window.location = 'Home.html';")
        print ("</script>")
    except:
        print("<p>Please change your username</p>")
else:
    print("<p>Please enter your information</p>")

printFooter()
