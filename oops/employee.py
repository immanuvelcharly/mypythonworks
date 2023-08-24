class Employee:

    id:int
    name:str
    desig:str
    salary:str

    def __init__(self,id,name,desig,salary):
        self.id=id
        self.name=name
        self.desig=desig
        self.salary=salary

    def get_emp(self):
        print(self.name,self.id,self.desig,self.salary)

emp1=Employee(12,"hari","hr",40000)
emp1.get_emp()