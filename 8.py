f=open("testfile.txt" , "r")
vowels='aeiou'
a=f.read()
f.close()
f=open("testfile.txt" , "w")

for i in a:
    if i in  vowels:
      
        f.write(i.upper())
    elif i in vowels.upper():
        

        f.write(i.lower())
    else:
        

        f.write(i)
        
        
f.close()
