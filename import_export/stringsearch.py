word="observe"
inpt="see"
wc={}
is_kangaroo=True
for c in word:
    if c in wc:
        wc[c]+1
    else:
        wc[c]=1
print(wc)
for ch in inpt:
    if ch in wc and wc[ch]>0:
        wc[ch]
    else:
        is_kangaroo=False
        break
    print(is_kangaroo)
