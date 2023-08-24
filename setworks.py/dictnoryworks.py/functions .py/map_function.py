lst=[1,2,3,4,5,6,7]
# square=list(map(lambda num:num**3,lst))
# cube=list(map(lambda num:num**3,lst))
# print(square)
# print(cube)

# filter

# odd
odd_numbers=list(filter(lambda n:n%2==1,lst))
print(odd_numbers)

# even
even_numbers=list(filter(lambda  n:n%2==0,lst))
print(even_numbers)

# print num>3
num_gt3=list(filter (lambda n:n>3,lst))
print(num_gt3)
