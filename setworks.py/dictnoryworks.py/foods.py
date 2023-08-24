items=[
    {"name":"biriyani","price":130,"category":"nonveg"},
    {"name":"dosa","price":70,"category":"veg"},
    {"name":"vegfriedrice","price":130,"category":"veg"},
    {"name":"noodles","price":130,"category":"nonveg"},
    {"name":"burger","price":130,"category":"nonveg"},
    
]

# print all items
# all_items=list(map(lambda i:i.get("name"),items))
# print(all_items)

# all_names=[i.get("name") for i in items]
# print(all_names)

# map_price=list(map(lambda it:it.get("price"),items))

# lst_price=[i.get("price") for i in items]
# print(lst_price)

# veg
veg_items=list(filter(lambda i:i.get("category")=="veg",items))
print(veg_items)

list_veg=[i.get("name") for i in items if i.get("category")=="veg"]
print(list_veg)
