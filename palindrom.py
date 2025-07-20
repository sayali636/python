n=int(input("enter number"))
n1=n
s=0
while(n>0):
    d=n%10
    s=(s*10)+d
    n=n//10

if n1==s:
    print("number is palindrom")
else:
    print("number is not palindrom")

    
