lst=[10,20,30,40,50]
location=int(input("enter location to fetch value form list"))
try:
    print(lst[location])
except Exception as e:
    print(e.args)
finally:
    print("dbcommit")
    print("file read")