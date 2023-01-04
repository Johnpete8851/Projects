import pickle
file1=open("emp.dat", "rb")
l=[]

while True:
    try:
        l=pickle.load(file1)
        while l:
            salary=l[2]
            if salary>20000 and salary<40000:
                print(l)
                break
            l=pickle.load(file1)

    except EOFError:
        break
    
file1.close()




