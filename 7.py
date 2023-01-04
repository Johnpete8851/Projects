file1=open("testfile.txt", "r")
file2=open("copy.txt", "w")
s=file1.readline()
while s:
    if s[0]=="A"  or s[0]=="a":
        file2.write(s)
    s=file1.readline()
file1.close()
file2.close()



