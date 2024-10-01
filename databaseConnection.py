#This sample file demonstrate SQL capabilities with python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="shikhar",
  database="classicmodels"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM offices")
offices = mycursor.fetchall()
for x in offices:
  print(x)
