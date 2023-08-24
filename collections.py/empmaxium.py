emplst=[]
# print(emplst)
length=int(input("enter size of list : "))
for i in range(length):
    num=int(input(f"enter {i}th postion ele:"))
    emplst.append(num)
maximum=max(emplst)+10
emplst.insert(2,maximum)
print(emplst)
