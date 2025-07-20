d = {"rno": 11, "name": "om", "per": 60}

n = input("Enter key to search: ")
s = input("Value to replace: ")

if n in d:
    d[n] = s  
    print("Key found", d)
else:
    print("Key not found")

print("Final dictionary:", d)
