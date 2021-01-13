import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="College"
)

mycursor=mydb.cursor()

# a="create database College"
#b="show databases"
#mycursor.execute("create table Student (SrNo int(144) not null,Name varchar(144) not null,Id varchar(144) primary key,Mobile int(144) not null,Dob varchar(144) not null)")
# sql="insert into Student (SrNo,Name,Id,Mobile,dob) values(%s,%s,%s,%s,%s)"
# val=[(1,"kush bhandari","18btcse0013",991730,14/11/2000),(2,"Ankit bisht","18btcse0029",931730,1/1/2000),(3,"Akash Gusain","18btcse0039",993730,4/11/2000)]
# mycursor.executemany(sql,val)
# mydb.commit()
# for i in mycursor:
#     print(i)

#----------------------MYSQL SELECT-----------------------------------------------
# mycursor.execute("SELECT * from Student")

# for i in mycursor:
#     print(i)

#--------------------for selecting particular columb-------------------------------
# # mycursor.execute("Select SrNo,Name from Student")
#myresult=mycursor.fetchall()
# for i in myresult:
#   print(i)
#----------------------for selection of one row------------------------------------
mycursor.execute("Select * from Student")
myresult=mycursor.fetchone()
for i in myresult:
    print(i)
