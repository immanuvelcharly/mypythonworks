alluseres=["mohanlal","fahad","dq","vijay","nivin","asif"]
dq_frienslist=["mohanlal","fahad","asif"]
asif_friendlist=["mohanlal","fahad","vijay","nivin",]
st1=set(alluseres)
st2=set(dq_frienslist)

suggetion_dq=set(alluseres).difference(set(dq_frienslist))
suggetion_dq.remove("dq")
print(suggetion_dq)
mutual_friends=set(asif_friendlist).intersection(dq_frienslist)
print(mutual_friends)