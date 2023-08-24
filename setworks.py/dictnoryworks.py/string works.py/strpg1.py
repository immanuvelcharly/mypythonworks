text="one 100 and fifty 5"
# word=text.split(" ")
# for w in word:
#     if w.isdigit():
#         print(w)

nums=[w for w in text.split(" ") if w.isdigit()]
print(nums)
