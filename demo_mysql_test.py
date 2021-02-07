import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="myusername",
  password="mypassword",
  port='8006'
)

print(mydb)
