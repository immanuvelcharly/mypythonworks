#create a empty list

emplst=[]
length=int(input("enter the size of the list"))
for i in range(length):
    num=int(input(f"enter {i}th postion elements:"))
    emplst.append(num)
print(emplst)

