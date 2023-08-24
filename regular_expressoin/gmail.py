# verify  a gmail
import re
gmail=input("enter you r gmail: ")
g=re.search("$@gmail.com",gmail)
if g:
    print("Its valid")
else:
    print("its not valid")
    

