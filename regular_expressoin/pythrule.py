# starts with an alphabest
# any number of alphabetstanddigit
from re import *
rule="[a-zA-Z_][a-zA-Z0-9_]*"
var_name="num_"
matcher=fullmatch(rule,var_name)
if matcher==None:
    print("invalid")
else:
    print("valid")