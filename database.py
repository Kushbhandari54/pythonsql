# import mysql.connector

# mydb=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="college"
# )

# mycursor=mydb.cursor()

# # mycursor.execute("show databases")
# #dbs = mycursor.execute("create table Employee(name varchar(20) not null, id int(20) not null primary key, salary float not null, Dept_id int not null)")
# #mycursor.execute("alter table Employee add branch_name varchar(20) not null")
# # sql="insert into Employee(name,id,salary,Dept_id,branch_name) values(%s,%s,%s,%s,%s)"
# # val=("kush bhandari","18btcse0013",10000,101,"software Training")
# # mycursor.execute(sql,val)
# # mydb.commit()

# sql="insert into Employee(name,id,salary,Dept_id,branch_name) values(%s,%s,%s,s%,%s)"
# val=[("ankit bisht","18btcse0039",20000,102,"btech"),("Akash singh gusain","18btcse0029",30000,103,"btech")]
# mycursor.executemany(sql,val)
# mydb.commit()
# print(mycursor.rowcount,"row inserted")
# # for i in mycursor:
# #     print(i)


import mysql.connector

#creating the connection
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    )

mycursor=mydb.cursor()

# mycursor.execute("create database Enemy")
a="show databases"
#a="drop  database enemy"
mycursor.execute(a)

for  i in mycursor:
    print(i)

























