class P1:
    def m1(self):
        print("class p1 m1 method")

class P2:
    def m1(self):
        print("class p2 m2 methof")
class C1(P1,P2):
    pass
c=C1()
c.m1()