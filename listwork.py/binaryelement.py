lst=[3,4,6,7,8,9,10]
element=8
is_found=False
low=0
upp=len(lst)-1
while(low<=upp):
    mid=(low+upp)//2
    if element==lst[mid]:
        is_found=True
        break
    elif element>lst[mid]:
        low=mid+1
    elif element <lst[mid]:
        upp=mid-1
print("element found" if is_found else "element is not found")
    