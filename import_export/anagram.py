# #anagram
# word="fast"
# input="fats"

# list1=[word,input]
# sortword1=(sorted(word))
# sortword2=(sorted(input))
# if sortword1==sortword2:
#     print(" anagram")
# else:
#     print("not anagram")

word=input("enter a string>")
out=input("enter anthor word>")
srt_word=sorted(word)
srt_out=sorted(out)
print("anagram"if srt_word==srt_out else "not anagram")