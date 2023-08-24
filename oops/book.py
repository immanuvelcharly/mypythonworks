class Books:
    name:str
    author:str
    price:int
    pages:int

    def __init__(self,**kwargs):
        self.name=kwargs.get("name")
        self.author=kwargs.get("author")
        self.price=kwargs.get("price")
        self.pages=kwargs.get("pages")

    def __str__(self):
        return self.name
        
obj=Books(name="randamoozham",author="mt",price=600,page=300)
print(obj)