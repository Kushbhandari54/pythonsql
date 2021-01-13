import mysql.connector

mydb=mysql.connector.connect(
    user="root",
    host="localhost",
    password="",
    database="hello"
)

mycursor=mydb.cursor()
#---------------------------creating the database--------------------------------------------
#mycursor.execute("create database hello")

#---------------------------show the present databases---------------------------------------
#mycursor.execute("show databases")
# for i in mycursor:
#     print(i)

#---------------------------creating table in database---------------------------------------
#mycursor.execute("create table student (name VARCHAR(255),address VARCHAR(255))")

#--------------------------show the present table--------------------------------------------
# mycursor.execute("show tables")
# for i in mycursor:
#     print(i)

#-----------------------------alter table in database----------------------------------------
#mycursor.execute("ALTER TABLE student ADD  COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
# mycursor.execute("show tables")
# for i in mycursor:
#     print(i)

#-----------------------------insert data into table-----------------------------------------
# sql="INSERT INTO student (name,address) VALUES (%s,%s)"
# val=("John","haldwani")
# mycursor.execute(sql,val)
# mydb.commit()

#----------------------------Inserting multiple rows-----------------------------------------
# sql="INSERT INTO student (name,address) VALUES (%s,%s)"
# val=[
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
#     ]
# mycursor.executemany(sql,val)
# mydb.commit()
# print(mycursor.rowcount,"was inserted!")

#----------------------------------------Python mysql select from------------------------------

#------------------Select all records from the "customers" table, and display the result-------
# mycursor.execute("SELECT * FROM student")
# myresult=mycursor.fetchall()
# for i in myresult:
#     print(i)

#-----------------------------------Selecting Columbs------------------------------------------
# mycursor.execute("SELECT address FROM student")
# myresult=mycursor.fetchall()
# for i in myresult:
#     print(i)


#-----------------------------------Using FETCHALONE method--------------------------------------
# mycursor.execute("SELECT * FROM student")
# myresult=mycursor.fetchone()
# for i in myresult:
#     print(i)


#----------------------------------------WHERE() Clause------------------------------------------

#--------------------------------SELECT WITH FILTER----------------------------------------------
# mycursor.execute("SELECT * FROM student WHERE address ='Park Lane 38'")
# mydata=mycursor.fetchall()
# for i in mydata:
#     print(i)

# sql="SELECT * FROM student WHERE address LIKE '%way%'"
# mycursor.execute(sql)
# mydata=mycursor.fetchall()
# for i in mydata:
#     print(i)


#-----------------------------------------PREVENT SQL INJECTION------------------------------------
# sql="SELECT * from student WHERE address = %s"
# val=('Park Lane 38',)
# mycursor.execute(sql,val)
# mydata=mycursor.fetchall()
# for i in mydata:
#     print(i)

#----------------------------Order By--------------------------------------------------------------
#Order by clause by default sort the data in ascending order
# TO sort the data in descending order USE DESC. 
# sql="SELECT * from student ORDER BY name DESC"
# mycursor.execute(sql)
# mydata=mycursor.fetchall()
# for i in mydata:
#     print(i)

#---------------------------------DELETE FROM BY--------------------------------------------------
# sql="DELETE FROM student where name=%s"
# val=('Yellow Garden 2',)
# mycursor.execute(sql,val)
# mydb.commit()
# print(mycursor.rowcount,"record deleted")

#----------------------------------DROP TABLE-----------------------------------------------------
# sql="DROP TABLE student"

# sql="DROP TABLE IF EXISTS student "
# mycursor.execute(sql)

# sql="CREATE TABLE student name (varchar(255),address varchar(255))"
# mycursor.execute(sql)

sql="INSERT INTO student (name,address) VALUES (%s,%s)"
val=