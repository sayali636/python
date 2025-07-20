class Emp:
    def accept(self):
        self.eno=int(input("enter emp no"))
        self.ename=int(input("enter emp name"))
        self.sal=int(input("enter emp sal"))
    def disp(self):
        print("emp no=",self.eno)
        print("emp name=",self.ename)
        print("emp sal=",self.sal)
        return
    Emp.accept()
    Emp.disp()
