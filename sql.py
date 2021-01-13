import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="student"
)

mycursor=mydb.cursor()

#sql="create table customer (CustomerID int(255),CustomerName varchar(255),ContactName varchar(255),Address varchar(255),City varchar(225),PostalCode int(255),Country varchar(255))"

sql="INSERT INTO customer(CustomerID int(255),CustomerName varchar(255),ContactName varchar(255),Address varchar(255),City varchar(225),PostalCode int(255),Country varchar(255) VALUES(%s,%s,%s,%s,%s,%s,%s))"
val=('1','Alfreds Futterkiste','Maria Anders','Obere Str. 57','Berlin','12209','Germany')
mycursor.execute(sql,val)
mydb.commit()

# mycursor.execute("SELECT *  from customer")
