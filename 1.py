def freq(List, ele):
    c = 0
    for i in List:
        if i == ele:
            c += 1
    return c
L = []
size = int(input("Enter size of list: "))
for i in range(size):
    num = input("Enter element: ")
    L.append(num)

to_find = input("Enter element of needed frequency: ")
print(freq(L, to_find))
