file1=open("testfile3.txt" , "r")
s=" "
c=0
while s:
    s=file1.readline()
    l=[]
    l=s.split()
    for i in l:
        if i=="am":
            c+=1
print("no of (am): ", c)