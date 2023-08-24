# from re import *
# text="luminar tecgno lab luminar tecno hub "
# matcher=finditer("luminar",text)
# count=0
# for m in matcher:
#     count+=1
# print(count)

import re 
text="aabdxyz$#098"
matchcter=re.finditer("[^a-zA-Z0-9]",text)
print(matchcter)
for m in matchcter:
    print(m.group())