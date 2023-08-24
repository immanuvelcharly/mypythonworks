items=[
    [1,"potatto",45,"veg",10],
    [1,"tomatto",40,"veg",20],
    [1,"onion",35,"veg",0],
    [1,"brinjal",50,"veg",0],
    [1,"fish",145,"nonveg",10],
    [1,"chicken",145,"nonveg",10],
    [1,"egg",6,"nonveg",100]
 
    
]

# total number products
# print in stock product names
# print out of stock product names
# print veg category product names
# product available in range of 50-100
# veg products available in range of 40-80

print(len(items))

all_items=[it[1]for it in items ]
print(all_items)

stock_out=[it[1]for it in items if it[4]<1]
print(stock_out,"it's not avilable")

stock_in=[it[1]for it in items if it[4]>1]
print(stock_in,"it's avilable")

veg_category=[it[1]for it in items if it[3]==("veg")]
print(veg_category)

product_avilable=[it[1] for it in items if it[2] in range(50,100)]
print(product_avilable)

vegproduct_avilable=[it[1] for it in items if it[2] in range(40,80)]
print(vegproduct_avilable)