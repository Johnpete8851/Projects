import sys
L=[]
Top,ch=-1,0
choice='y'

def menu():
    print("Operations on a stack list")
    print("1. Push an element")
    print("2. Pop an element")
    print("3. Show stack status")
    print("4. Quit ")

def push(x):
    global Top
    Top=Top+1
    L.append(x)
    print("Stack Status:")
    for i in range(Top,-1,-1):
        print(L[i],end="")

def show():
    print("Stack Status:")
    if L==[]:
        print("Stack empty")
    else:
        for i in range(Top,-1,-1):
            print(L[i],end="")

def rem():
    global Top
    if L!=[]:
        L.pop()
        Top=Top-1
        show()
    else:
        print("Stack Empty")

while True:
    menu()
    ch=int(input("Ener your choice"))
    if ch==1:
        x=int(input("Enter element"))
        push(x)
    elif ch==2:
        rem()
    elif ch==3:
        show()
    elif ch==4:
        print("Program Over")
        sys.exit()
    else:
        print("Wrong choices")
    choice=input("\nDo you want to continue")
    if choice=='Y' or choice=='y':
        continue
    else:
        break