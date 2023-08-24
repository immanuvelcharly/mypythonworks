from datetime import date
class Operations:
    num1:int
    num2:int
    def __init__(self,n1,n2):
        self.num1=n1
        self.num2=n2
    def add(self):
        return self.num1+self.num2
    def product(self):
        return self.num1*self.num2
    @staticmethod
    def get_date():
        return date.today()
op=Operations(100,200)
print(op.add())

print(Operations.get_date())