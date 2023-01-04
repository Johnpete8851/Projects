f=open('testfile.txt','r')
vowels='aeiou'
c=0
s=" "
while s:
    s=f.read()
    for i in s:
        if i.lower() in vowels:
            c=c+1
print("no of vowel are: ",c)
    
