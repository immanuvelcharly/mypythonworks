#nuum=1634
num=1634
org=num
cnt=len(str(num))
sum=0
while(num!=0):
    digit=num%10
    sum=sum+(digit**cnt)
    num=num//10
print(sum)
if(sum==org):
    print("amstrong number")
else:
    print("not amstrong number")