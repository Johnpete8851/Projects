import csv
n=0
roll=0
name=""
class1=0
marks=0
data=['Roll','Name','Class','Marks']
file=open("stx12.csv","w")

n=int(input("How many records do you want to enter?  "))
W=csv.writer(file,delimiter=',')
W.writerow(data)
for i in range(0,n,1):
    roll=int(input("Enter Roll Number: "))
    name=input("Enter Name of student: ")
    class1=int(input("Enter Class of student: "))
    marks=int(input("Enter Marks of student: "))
    data=[roll,name,class1,marks]
    W.writerow(data)

file.close()