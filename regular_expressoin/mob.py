import re 
mob=input("enter your mobile number with country code: ")
print(mob)
x=re.search("^91",mob)
if(x):
    print("numer is indain")
else:
    print("numer is not indain")


resi=input("enter a residance number")
resi=input("enter a residence number")
ekm=re.search("^0484",resi)
ijk=re.search("^0480",resi)
tcr=re.search("^0487",resi)
mpr=re.search("^0494",resi)
ksd=re.search("^04994",resi)
cct=re.search("^0495",resi)
if ekm:
    print("ekm")
elif ijk:
    print(ijk)
elif tcr:
    print(tcr)
elif mpr:
    print(mpr)
elif ksd:
    print(ksd)
else:
    print(cct)

