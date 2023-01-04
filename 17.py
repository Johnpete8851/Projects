import mysql.connector as sql
mydb=sql.connect(host='localhost',user='root',passwd='123',database='school')
if mydb.is_connected():
    print("Successfully Connected")
mc=mydb.cursor()
mc.execute("delete from student")
mydb.commit()
print("Successfully Deleted all records")
mc.close()
mydb.close()