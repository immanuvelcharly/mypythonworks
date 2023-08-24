class Users:
    data=[
        {"id":1,"username":"jhon","email":"jhon@gmail.com","password":"password@123"},
        {"id":2,"username":"hari","email":"hari@gmail.com","password":"password@123"},
        {"id":3,"username":"ravi","email":"ravi@gmail.com","password":"password@123"},
        {"id":4,"username":"vijay","email":"vijay@gmail.com","password":"password@123"},
        {"id":5,"username":"vinu","email":"vinu@gmail.com","password":"password@123"},
        {"id":6,"username":"tom","email":"tom@gmail.com","password":"password@123"},
    ]
    def get(self):
        return self.data

    def getuser_details(self,id):
       return [u for u in self.data if u.get("id")==id]
    def retrive(self,id):
        for u in self.data:
            return u 
    def post(self,obj):
        self.data.append(obj)
    def destroy(self,id):
        obj=[u for u in self.data if u.get("id")==id][0]
        self.data.remove(obj)
    def put(self,id,value):
        object=[u for u in self.data if u.get("id")==id][0]
        pos=self.data.index(object)
        self.data[pos]=value[0]


# obj=Users()
# student_data={"id":7,"username":"ram","email":"ram@gmail","password":"pasw123"}
# obj.post(student_data)
# print(obj.get())

# obj.destroy(5)
# print(obj.get())e
obj=Users
print(obj.retrive(4))
payload= {"id":4,"username":"vinu","email":"vinu@gmail.com","password":"password@123"},
obj.put(4,payload)

# get()=all list
# retrieve()=a obj details
# post()create
# put()update
# destroy()delete