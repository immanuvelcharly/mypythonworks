class Brands:
    data=[
        {"productno":1,"brand":"msi","processer":"rayzen7","price":70000},
        {"productno":2,"brand":"apple","processer":"appleM1","price":120000},
        {"productno":3,"brand":"asuz","processer":"inteli5","price":45000},
        {"productno":4,"brand":"dell","processer":"intelevo","price":60000},
        {"productno":5,"brand":"acer","processer":"inteli3","price":30000},
        {"productno":6,"brand":"hp","processer":"rayzen5","price":50000},
        {"productno":7,"brand":"lenovo","processer":"rayzen3","price":29999},


    ]
    def get(self):
        return self.data
    def retrive(self,productno):
        return[b for b in self.data if b.get("productno")==productno]
    def post(self,obj):
        self.data.append(obj)
    def destroy(self,productno):
        obj=[b for b in self.data if b.get("productno")==productno][0]
        
        

obj=Brands()
print(obj.get())
print(obj.retrive(7))
laptop={"productno":8,"brand":"thoshiba","processer":"rayzen7","price":70000},
obj.post(laptop)
print(obj.get())
print(obj.get(1))
    

