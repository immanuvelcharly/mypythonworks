sen="joel is a very good student in may batch"
words=sen.split(" ")
# print(sen.startswith("joel"))
bol=sen.startswith("joel")
print(bol)
if bol==True:
    print("the sentence is starting with 'joel'")
if words[0]=="joel":
    print("the sentence is starting with 'joel'")

# =======================================================
import re
sen="joel is a very good student in may batch"
x=re.search("^Joel",sen)
print(x)
y=re.search("^joel",sen)
print(y)
en=re.search("^Joel$",sen)
print(en)

st_en=re.search("^joel.*batch$",sen)
print(st_en)



