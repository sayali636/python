#. Define a function that accept two strings as input and
#find union and intersection of them.
def un(s1,s2):
    s1=set(s1)
    s2=set(s2)
    union=s1.union(s2)
    intersection=s1.intersection(s2)
    print("Union of characters:",''.join(sorted(union)))
    print("Intersection of characters:",''.join(sorted(intersection)))
p=input("Enter first string: ")
q=input("Enter second string: ")
un(p, q)
