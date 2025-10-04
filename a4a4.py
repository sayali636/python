#Write a recursive function to calculate sum of digits
#of a given input number. 
def sum(n):
    if n==0:
        return 0
    else:
        d=n%10
        num=n//10
        return d+sum(num)

num=int(input("Enter a number:"))
print("Sum of digits:",sum(num))
