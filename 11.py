import pickle
file=open("stu1.txt", "wb")
while True:
    print("enter data to add:-")
    name=input("enter student name: ")
    roll=int(input("enter roll number: "))
    data=[name,roll]
    pickle.dump(data,file)
    print("data added successfully")
    choice=input("do you want add more records")
    if choice=='y' or choice=='Y':
        continue
    else:
        break
    
file.close()    