import mysql.connector as sql
mydb=sql.connect(host='localhost',user='root',passwd='123',database='school')
if mydb.is_connected():
    print("Successfully Connected")
mc=mydb.cursor()
print("Enter details of students:")
roll=int(input("Enter roll: "))
name=input("Enter Name: ")
marks=int(input("Enter marks: "))
mc.execute("insert into student values(%s,'%s',%s)"%(roll,name,marks))
mydb.commit()
print("Record Written")
mc.close()
mydb.close()