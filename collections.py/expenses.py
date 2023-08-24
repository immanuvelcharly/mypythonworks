expenses=[20000,23000,15000,14000,35000]

#print all expenses
for exp in expenses:
    print(exp)

#print all exp>16000
for exp in expenses:
    if exp>16000:
        print(exp)
# print highest expense
max_exp=max(expenses)
print(max_exp)

#
min_exp=min(expenses)
print(min_exp)

#
total_exp=sum(expenses)
print(total_exp)
