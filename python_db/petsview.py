from get_connection import db_connect
class Petsview:
    def connect(self):
        db=db_connect(password="Password@123",database="animal")
        return db
    
    def get(self):
        db=self.connect()
        cursor=db.cursor()
        query="select * from pets"
        cursor.execute(query)
        qs=cursor.fetchall()
        return qs
    
    def retrieve(self,id):
        db=self.connect()
        cursor=db.cursor()
        query=f"select *from pets where id={id}"
        cursor.execute(query)
        record=cursor.fetchone()
        return record
    
    def post(self,*args,**kwargs):
        db=self.connect()
        cursor=db.cursor()
        query="insert into pets(age,gender,breed,location,price)" "values(%s,%s,%s,%s,%s)"
        data=tuple(v for v in kwargs.values())
        cursor.execute(query,data)
        db.commit()
        return kwargs
    
    def destroy(self,id):
        db=self.connect()
        cursor=db.cursor()
        query=f"delete from pets where id={id}"
        cursor.execute(query)
        db.commit()
        return "record deleted"
    
    def put(self,id,*args,**kwargs):
        db=self.connect()
        cursor=db.cursor()
        data=list(v for v in kwargs.values())
        data.append(id)
        query="update pets set age=%s gender=%s breed=%s location=%s price=%s where id=%s"
        cursor.execute(query,data)
        db.commit()
        return "updated"


pv=Petsview()
# print(pv.get())
# print(pv.retrieve(1))
# print(pv.post(age=26,gender="male",breed="breed3",location="kottayam",price=400))
# print(pv.destroy(1))
print(pv.put(id=2,age=26,gender="female",breed="breed6",location="thrissur",price=7000))
