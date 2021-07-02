# 1.Create a connection for DB and print the version using a python program

import mysql.connector
mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "Abhishek@2000"
)
print(mydb)

# 2.Create a multiple tables & insert data in table
import sys
cur = mydb.cursor()
cur.execute("SELECT VERSION()")
data = cur.fetchone()
print("DBMS Version :",str(data))


dbse = mydb.cursor()
dbse.execute("CREATE DATABASE 3_database")
dbse = mydb.cursor()
dbse.execute("SHOW DATABASES")
for entry in dbse:
  print(entry)

mydb = mysql.connector.connect(
  host="localhost",
 user="root",
  password="Abhishek@2000",
  database="4_database"
)
dbse = mydb.cursor()

dbse.execute("CREATE TABLE employee (Employee_name VARCHAR(255), Employee_dep VARCHAR(255), Employee_id VARCHAR(255))")
dbse.execute("SHOW TABLES")

for value in dbse:
  print(value)

# 3.Create a employee table and read all the employee name in the table using for loop

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "Abhishek@2000",
  databse = "4_database"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE Employee1(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), address VARCHAR(255)")

mydb = mysql.connector.connect(
  host="localhost",
 user="root",
  password="Abhishek@2000",
  database="4_database"
)
mycursor = mydb.cursor()

sql = "INSERT INTO Employee1 (id, name, address) VALUES (%s, %s,%s)"
val = ("123","divya","T Nagar 56")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

