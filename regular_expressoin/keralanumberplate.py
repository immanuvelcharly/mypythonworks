# KL08bu0399.\
from re import*
rule="[K][L][-][0-9]{2}[-][a-z]{2}[-][0-9]{4}"
var_name="TN-08-bu-0399"
matcher=fullmatch(rule,var_name)
if matcher==None:
    print("invalid")
else:
    print("valid")