num=7
for i in range(2,num):
    if(num%i==0):   
        is_prime=False

if(is_prime==True):
    print(num,"is prime")
    is_prime=False
else:
    print(num,"is not prime")

              