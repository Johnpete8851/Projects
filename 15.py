import csv
n=0
UserID=0
Password=""
fields=['UserID','Password']
file=open("emp.csv","w",newline='')
n=int(input("How many records do you want to enter: ?"))
W=csv.writer(file)
W.writerow(fields)
for i in range(0,n,1):
    UserID=int(input("Enter ID of employee: "))
    Password=input("Enter Password of employee: ")
    fields=[UserID,Password]
    W.writerow(fields)
file.close()
file1=open("emp.csv","r")
R=csv.reader(file1)
search=input("Enter password to search: ")
for row in R:
    if row[1]==search:
        print(row)
file1.close()