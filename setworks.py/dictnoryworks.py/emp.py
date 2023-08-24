employee={"id":100,"name":"vijay","department":"hr","salary":25000}
# def get_name(emp):
#     return emp.get("name")

# print(get_name(employee))

# get_name=lambda emp:emp.get("name")
# print(get_name(employee))

get_salary=lambda emp:emp.get("salary")
print(get_salary(employee))

#args positional argument takes any number of parameters type tuple 
# def addition(*args):
#     return sum(args)
# print(addition(10,20,40,545))

addition=lambda *args:sum(args)
print(addition(2039,49452,2995,259520,520025,52579))

max_nums=lambda *args:max(args)
print(max_nums(2,3,30,40,40,))