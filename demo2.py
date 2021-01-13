import mysql.connector

mydb=mysql.connector.connect(

    host="localhost",
    user="root",
    password="",
    database="Employee"
)

mycursor=mydb.cursor()

#sql="CREATE DATABASE Employee"

#sql="show databases"

#sql="drop database hello"
#sql=create table fresher (name varchar(255),address varchar(255))
#sql=alter table fresher (id int auto_increment primary key) 
#sql=Insert into fresher (name,address)  values (%s,%s)
#val=('John','Haldwani')

mycursor.execute(val)
mydb.commit()

