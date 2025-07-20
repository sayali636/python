class A:
    def show(self):
        print("I am Base class")

class B(A):
     def disp(self):
        print("I am Derived class")
class C(B):
     def disp1(self):
        print("I am Derived class")

ob=C()
ob.show()
ob.disp()
ob.disp1()





    
