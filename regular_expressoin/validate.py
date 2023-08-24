import re
text="abababab"
text1="aaaaaaabbbbbbbccc"
t=re.search("[a]{4}",text)
t1=re.search("[a]{4}",text1)
print(t)
print(t1)


