file=open("copy.txt", "r")
s=" "
while s:
    s=file.readline()
    l=s.split()
    for i in l:
        print(i+"#",end="")
    print()   
file.close()

