# text="ABABC"
# #find first recursive character

# we={}
# for ch in text:
#     if ch in we:


words=["hello","hai","hello","hai"]
wc={}
for w in words:
    if w in wc:
        wc[w]+=1
    else:
        wc[w]=1

print(wc)