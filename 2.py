def to_find(string):
    for i in string.split(): 
        if i[0] == 'a' or i[0] == 'A': 
            print(i)

a = input("Enter string: ")
to_find(a)
