limit=25
start=1

even_sum=0
odd_sum=0
for num in range(start,limit):
    if(num%2==0):
        even_sum+=num
    else:
        odd_sum+=num
print("odd sum =",odd_sum)
print("even sum =",even_sum)

