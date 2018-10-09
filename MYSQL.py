import mysql.connector
import sys
import datetime
#args=sys.argv[1]
#x=str(args);
mydb = mysql.connector.connect(
  host="localhost",
  user="greshan",
  passwd="password",
  database="IP",
  buffered = True
)

date = datetime.datetime(2018, 5, 17)
date.strftime('%Y-%m-%d')
mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE IP")
mycursor.execute("SHOW DATABASES")
#mycursor.execute("CREATE TABLE Detail (id INT AUTO_INCREMENT PRIMARY KEY,Fname varchar(255),Lname varchar(255), DOB date)")
#mycursor.execute("ALTER TABLE addresses ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
#val = ("Greshan" "Aranha")
#mycursor.execute(sql, val)
sql = "INSERT INTO Detail (id, Fname, Lname, DOB) VALUES (%s, %s, %s, %s)"
val = ("181041011", "Greshan", "Aranha", date )
mycursor.execute(sql, val)
mydb.commit()
