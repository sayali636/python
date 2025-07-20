n=int(input("enter number"))
cnt1=0
cnt2=0
cnt3=0
while(n>0):
    d=n%10
    if n%2==0:
        cnt1=cnt1+1
    elif n==0:
        cnt2=cnt2+1
    else:
        cnt3=cnt3+1
    n=n/10

print("even count",cnt1)
print("Odd count",cnt2)
print("Zero count",cnt3)
        
