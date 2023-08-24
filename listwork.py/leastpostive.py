# lst=[1,3,4,6]
# for i in range(0,len(lst)):
#     elem1=(lst[i])
#     elem2=(lst[i+1])
#     if elem2-elem1!=1:
#         print(elem1+1,"is missing")
#         break


lst=[2,3,4,6]
for i in range(0,len(lst)):
    if lst[0]!=1:
        print(1,"is missing")
        break
    else:
        elem1=lst[i]
        elem2=lst[i+1]
        if elem1-elem2 !=1:
            print(elem1+1,"is missing")
            break

        #lst=[2,3,4,4,5,5,6,7]
        #find duplicate element from the lst
        
            
