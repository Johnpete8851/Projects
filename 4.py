def roll_stu(l):
    for i in l:
        if i.isupper(): 
            print(l[i])

            
students = {}
size = int(input("Enter number of students: "))
for i in range(size):
    name = input("Enter name of student: ")
    roll = int(input("Enter roll no of student:"))
    students[name] = roll
roll_stu(students)
