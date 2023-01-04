import mysql.connector as sql
mydb=sql.connect(host='localhost',user='root',passwd='123',database='school')
if mydb.is_connected():
    print("Successfully Connected")
mc=mydb.cursor()
mc.execute("Select * from student")
records=mc.fetchall()
for i in records:
    print(i)
mc.close()
mydb.close()