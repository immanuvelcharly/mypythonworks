lst=[1,5,15,8,9,30,10]
new_lst=[]
for i in lst:
    if i%2==1 and i%5==0 :
        new_lst.append(i)
print(new_lst)

