import mysql.connector

conn=mysql.connector.connect(host='localhost', username='root',password='Rahul@2203')
my_cursor=conn.cursor()

conn.commit()
conn.close()

print("Rahul Singh Mera Naam")