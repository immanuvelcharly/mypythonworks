text="Elephants are big "
vowel=("a","e","i","o","u")
# wor=[w for w in text.split() if w[0].casefold() in vowel]
# print(wor)
word=text.split()
for w in word:
    if w[0].casefold in vowel:
        print(w)
        