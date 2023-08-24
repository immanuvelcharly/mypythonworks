from re import *
rule="[k-m][369][a-zA-Z0-9]*"
var_name="k3llo"
matcher=fullmatch(rule,var_name)
if match!=None:
    print("valid")
else:
    print("invalid")
