stud_name=[]
length=int(input("enter the size of list: "))
for i in range(length):
    name=input(f"enter {i}th name:")
    stud_name.append(name)
ch_name=input("enter a name :")

for s in range(length):
    if (stud_name[s]==ch_name):
        stud_name[s]="anamika"
        break
    elif(s==length-1):
        stud_name[0]="amal"
print(stud_name)




