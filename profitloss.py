c=int(input("enter cost price"))
s=int(input("enter selling price"))
if s>c:
    p=s-c
    print("profit=",p)
else:
    l=c-s
    print("Loss=",l)
