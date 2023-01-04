def swap(info):
    l = list(info)
    flag = 1
    
    for i in range(0, len(l)-1, 1):
        if l[i] % 7 == 0 and flag == 1:
            l[i], l[i+1] = l[i+1], l[i]
            flag= 0
        else:
            flag = 1
        
    if l[-1] % 7 == 0 and flag== 1:
        l[0], l[-1] = l[-1], l[0]

    return tuple(l)    

l = eval(input("Enter elements: "))
swap_list = swap(l)
print(swap_list)
