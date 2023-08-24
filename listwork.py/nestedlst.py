#nestedlist
lst=[
    [1,2],
    [4,50],
    [50,45],

]
# for sublist in lst:
#     for num in sublist:
#         print(num)

allnumbers=[num for sublist in lst for num in sublist]
print(allnumbers)

num_gt_5=[num for is in lst for num in is if num >5]
print(num_gt_5)
    
#print all numbers > 5
# for sublist in lst:
#     for num in sublist:
#         if(num>5):
#             print(num)
