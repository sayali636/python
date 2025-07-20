class demo:
    def get_string(self):
        self.s1=input("enter string")
    def print_string(self):
        print("string=",self.s1.upper())
        print("string=",self.s1[::-1])
        print("string=",self.s1.lower())

ob=demo()
ob.get_string()
ob.print_string()
        
