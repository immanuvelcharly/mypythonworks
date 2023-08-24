#find out factorial of a number(fact=5=5*4*3*2*1)
# num=5
# fact=1
# while(num>=1):
#     fact*=num
#     num-=1
# print("factorial:",fact)

#print even number
# num=1
# limit=25
# while(num<=limit):
#     if(num%2==1):
#         print(num)
#     num+=1

#print odd number
# num=1
# limit=25
# while(num<=limit):
#     if(num%2==0):
#         print(num)
#     num+=1


num=1
sum=0
while(num<=8):
    if(num%2==1):
        sum+=num
    num+=1
print("sum of 8 odd number",sum)
