data={
    "django":"framework",
    "react":"library",
    "fastapi":"framework",
    "vue":"framework",
    "ajax":"library"
    }
wc={}

# for d  in data.values():
#     if d in wc:
#         wc[d]+=1
#     else:
#         wc[d]=1

# print(wc)

#op=

for k,v in data.items():
    if v in wc:
        wc[v].append(k)
    else:
        wc[v]=[k]
    

print(wc)

    