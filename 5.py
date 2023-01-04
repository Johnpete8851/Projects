n = int(input("Enter the number of countries to be be entered: "))
print()
cnt_dict = dict()

for i in range(n):

   x = input("Enter the country name: ")
   z = input("Enter the currency: ")
   print()
   cnt_dict[x] = z
print()

print("This is your given dictionary: ")
print("Country", "\t\t", "Currency")
for i in cnt_dict:
    print(i, "\t\t\t", cnt_dict[i])
print()

rc = input("Enter the country whose currency you'd like view: ")
if rc in cnt_dict:
    print(rc, ":", cnt_dict[rc])
else:
    print("No such country in the given dictionary.")