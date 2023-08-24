word="peirfqlheflierufcroerhbyewi"
#print number of words
vowels={"a","e","i","o","u"}
v_count=0
for ch in word:
    if ch in vowels:
        v_count+=1
print(v_count)