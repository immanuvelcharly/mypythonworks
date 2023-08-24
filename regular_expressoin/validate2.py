import re
te="abDcd1234"
check=re.search("[a-z],{4}",te)
print(check)