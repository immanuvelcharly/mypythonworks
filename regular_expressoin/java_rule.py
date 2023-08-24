# java var rule
# starting with a alphabet
# specilal $_
# length of limit 



from re import*
rule="[a-zA-Z][a-zA-Z0-9_$]{0,10}"
var_name="num$"
matcher=fullmatch(rule,var_name)
if matcher==None:
    print("invalid")
else:
    print("valid")
