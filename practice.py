import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Rahul@2203"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mydatabase")