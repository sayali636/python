class Rect:
    def findarea(self):
        l=float(input("enter length"))
        b=float(input("enter bredth"))
        a=l*b
        print("area=",a)

class tra(Rect):
    def findarea(self):
        super().findarea()
        h=float(input("enter hight"))
        b=float(input("enter bredth"))
        a=0.5*h*b
        print("area=",a)

ob=tra()
ob.findarea()

    
