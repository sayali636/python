n=int(input("enter number"))
f=0
for i in range(1,50):
    if n==i:
        f=1
        break
if f==1:
    print("OK")
else:
    print("Out of renge")
