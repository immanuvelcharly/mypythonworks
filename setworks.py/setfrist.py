# st={10,20,30.40,50,"hello",True,}
# print(st)

#
# for el in st:
    # print(el)
# class set
        # .add




#adding a objectbin to set
# st.add(100)
# print(st)

#converting list into set
# lst=[1,2,3,4,5,6]
# st=set(lst)
# print(st)

st1={10,11,12,13}
st2={10,12,25,30}
#union,intersection,difference
union_set=st1.union(st2)
print(union_set)
#intersection 
# same elements
intersection_set=st1.intersection(st2)
print(intersection_set)

difference_set=st1.difference(st2)
print(difference_set)

