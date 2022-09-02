
class A:
    n1=100

class B(A):
    n2=500

class C(B):
    n3=1000
    def sum(self):
        print(self.n1+self.n2+self.n3)

obj=C()
obj.sum()
