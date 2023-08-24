class bank:
    accno:int
    balance:int
    ac_type:str
    p_name:str

    def add_bankacc(self,accno,balance,ac_type,p_name):
        self.accno=accno
        self.balance=balance
        self.ac_type=ac_type
        self.p_name=p_name
    def deposit(self,amount):
        self.balance+=amount
        print(f"your sbi account{self.accno}has been credited rs{amount} and avilable balance{self.balance}")
    def withdrew(self,amount):
        if self.balance>=amount:
           self.balance-=amount
           print(f"your account"{self.accno}"has been debited re")

    