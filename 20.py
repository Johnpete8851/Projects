import mysql.connector as sql
mydb=sql.connect(host='localhost',user='root',passwd='123',database='school')
if mydb.is_connected():
    print("Successfully Connected")
mc=mydb.cursor()
x=int(input("Enter roll of student: "))
mc.execute("select * from student where roll=%s"%(x))
data=mc.fetchall()
if mc.rowcount==0:
    print("Record not found")
else:
    print("Roll Name Marks")
    for i in data:
        print(i,end="")
mc.close()
mydb.close()