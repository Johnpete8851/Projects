import pickle
l=[]
c=0
while True:
    print("1. to add detail")
    print("2. to display a specific student record")
    print("3. to exit")
    choice=int(input("enter your your choice: "))
    
    if choice==1:
        file=open("stu2.txt", "wb+")
        print("enter data of student  to add:-")
        name=input("enter student name: ")
        roll=int(input("enter roll number: "))
        age=int(input("enter age"))
        adm_no=int(input("enter addmission number"))
        data=[name,roll,age,adm_no]
        pickle.dump(data,file)
        print("data added successfully")
        ch=input("do you want add more records")
        if ch=='y' or ch=='Y':
            continue
        else:
            file.close()
    elif choice==2:
        file=open("stu2.txt" , "rb")
        try:
            l=pickle.load(file)
            to_search=int(input("enter roll no of student to see detail"))
            while l:
                if to_search in l:
                    print("record= ",l)
                    break
                l=pickle.load(file)
        except EOFError:
            print("record not found")
        file.close()
        

