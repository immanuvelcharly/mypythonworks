mobiles=[
    [100,"redminote12",23000,"5g"],
    [101,"oneplusnord",32000,"5g"],
    [102,"iphnoe14",123000,"5g"],
    [103,"s23ultra",133000,"5g"],
    [104,"pexel12",43000,"5g"],
    [105,"nothing",13000,"4g"],
    [106,"galaxya52",23000,"5g"]
        
]
print(len(mobiles),"mobiles available")

for mob in mobiles:
    print(mob[1])

mobile_names=[mob[1] for mob in mobiles]

print(mobile_names)
