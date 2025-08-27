s=input("Enter string")
if len(s)<2:
    result= ""   
elif len(s)==2:
    result=s*2  
else:
    result= s[:2] + s[-2:]
print(result)    


