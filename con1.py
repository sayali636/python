class demo:
    def accept(self):
        self.eno=int(input("enter emp no"))
        self.ename=(input("enter emp name"))
        self.sal=int(input("enter emp sal"))
    def disp(self):
        print("emp no=",self.eno)
        print("emp name=",self.ename)
        print("emp sal=",self.sal)
        return
ob=demo()
ob.accept()
ob.disp()
