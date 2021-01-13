import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="employee"
)

mycursor=mydb.cursor()


#sql="CREATE TABLE Customer (CustomerID int(255),CustomerName varchar(255),ContactName varchar(255),Address varchar(255),City varchar(255),PostalCode int(255),Country varchar(255))" 

#sql="INSERT INTO Cusqlstomer (CustomerID,CustomerName,ContactName,Address,City,PostalCode,Country) VALUES (%s,%s,%s,%s,%s,%s,%s)"
# val=('1','Alfreds Futterkiste','Maria Anders','Obere Str. 57','Berlin','12209','Germany')
# mycursor.execute(sql,val)

# sql="INSERT INTO Customer (CustomerID,CustomerName,ContactName,Address,City,PostalCode,Country) VALUES (%s,%s,%s,%s,%s,%s,%s)"
# val=[('2','Ana Trujillo Emparedados y helados','Ana Trujillo','Avda. de la Constitución 2222','México D.F.','05021','Mexico'),('3','Antonio Moreno Taquería','Antonio Moreno','Mataderos 2312','México D.F.','05023','Mexico')]
# mycursor.executemany(sql,val)
# mydb.commit()
# mycursor.execute("SELECT * FROM Customer")

# a=mycursor.fetchall()
# for i in a:
#     print(i)

# print(mycursor.rowcount,"row inserted")
# for i in mycursor:
#     print(i)

#------------------------------SELECT fetch()-----------------------------------------------
# sql="SELECT CustomerId,CustomerName FROM Customer"

# mycursor.execute(sql)
# a=mycursor.fetchall()

# print(a)


#------------------------------The SQL SELECT DISTINCT Statement-----------------------------
#sql="SELECT DISTINCT Country FROM Customer"

#--------------------------------Count the distinct country---------------------------------
sql='SELECT COUNT(DISTINCT Country) FROM Customer'
mycursor.execute(sql)
a=mycursor.fetchall()
print(a)