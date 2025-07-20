s=int(input("enter emp sal"))
print(s)
if s<250000:
    print("Tax=0%=",s)
elif s<400000:
    t=s/100*10
    print("tax=10%=",t)
elif s>500000:
    t=s/100*20
    print("Tax=20%=",t)
      
  
