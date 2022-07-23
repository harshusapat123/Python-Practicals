'''
a) Create a database in MySQL with a table of students. The table will contain the following 
fields: 
1. PRN number #this will be a primary key
2. First Name
3. Middle name
4. Last name
5. Address
6. mobile number
7. email id
8. DOB
b) Insert 4-5 records in the table.

'''

import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="harshala")
mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE students_data")


mydb = mysql.connector.connect(host="localhost",user="root",passwd="harshala",database="students_data")
mycursor = mydb.cursor()
mycursor2 = mydb.cursor()
#mycursor.execute("CREATE TABLE students_data (PRN VARCHAR (255) PRIMARY KEY, First_name VARCHAR(255), Middle_name VARCHAR(255), Last_name VARCHAR(255), Address VARCHAR(255), Mobile_Number VARCHAR(200) , Email_id VARCHAR(255), Date_of_Birth VARCHAR(255))")

print("Structure of Table students_data : ")
mycursor2.execute("DESCRIBE students_data.students_data")
table = mycursor2.fetchall()
print(table)


sql = "INSERT INTO students_data (PRN, First_name,Middle_name, Last_name,Address,Mobile_Number,Email_id,  Date_of_Birth ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

student1 = ("2130331245501","Harshala","Pandurang","Sapat","Kolad","8411095667","harshusapat123@gmail.com","2003-03-22")
student2 = ("2130331245502","Tanvi","Sanjay","Palkar","Poladpur","9112974690","tanvi12@gmail.com","2003-03-22")
student3 = ("2130331245503","Sheetal","Dunda","Wanghare","Mumbai","9067358295","sheetal89@gmail.com","2002-02-14")
student4 = ("2130331245504","Aarti","Yogesh","Pardeshi","Pali","8237677828","aarti34@gmail.com","2003-07-23")
student5 = ("2130331245505","Aakanksha","Sunil","Virkar","Satara","9420644874","akanksha123@gmail.com","2002-06-26")

mycursor.execute(sql,student1)
mycursor.execute(sql,student2)
mycursor.execute(sql,student3)
mycursor.execute(sql,student4)
mycursor.execute(sql,student5)
mydb.commit()

print ("Records Inserted!")
print()
print(" students_data Table contains following data :")
query ="SELECT * FROM students_data"
mycursor.execute(query)
for x in mycursor:
    print(x) 
