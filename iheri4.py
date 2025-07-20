class A:
    def show(self):
        print("I am Base class")

class B(A):
     def disp(self):
        print("I am intermidiat class")
class C(A):
     def disp1(self):
        print("I am intermidiat class")
class D(B,C):
     def disp2(self):
        print("I am Derived class")
ob=D()
ob.show()
ob.disp()
ob.disp1()
ob.disp2()





    
