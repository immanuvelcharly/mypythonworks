#methods insid dict

#list(append,pop,insert,extend,clear)
#set(add,union,intersection,diffrence)
#tuple(count,index)
# dictnory(.values(),.keys(),.items(),.get(),.pop())

student={"roll":1234,"name":"hari","age":25,"course":"mca"}
print(student.values())
print(student.keys())

# #items()will return both keys and values

for k,v in student.items():
    print(k,v)

#get (key) fetchating value wrt key

print(student.get("names"))

print("file transfer")
print("database commit")

#pop(key)
student.pop("course")
print(student)