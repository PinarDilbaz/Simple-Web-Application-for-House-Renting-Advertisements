#!C:\Users\ASUS\AppData\Local\Programs\Python\Python39\python
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

if ("nobedroom" in form.keys() and "monthlyFee" in form.keys() and "monthlyFee_2" in form.keys() and "city" in form.keys()):
	try:
		conn = sqlite3.connect("rental.db")
		c = conn.cursor()
		c.execute("SELECT cid FROM city WHERE cname = ?",(form["city"].value,))
		row = c.fetchone()
		city_id = int(row[0])
		c.execute("SELECT * FROM house WHERE noOfBedrooms = ? AND MonthlyFee >= ? AND MonthlyFee <= ? AND cityId = ?;",(form["nobedroom"].value,form["monthlyFee"].value,form["monthlyFee_2"].value,city_id,))
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
			    #print(row)
			    table += "  <tr>\n"
			    for column in row:
			        table += "    <td>{0}</td>\n".format(column)
			    table += "  </tr>\n"
			table += "</table>"
			if (data == []):
				print("<p>No advertisement found!!</p>")
			else:
				print(table)
		else:
		    print("<p>No advertisement found</p>")
		conn.commit()
		conn.close()
	except:
		print("<p>Wrong</p>")
