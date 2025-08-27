#Write a Python program to remove the characters which have odd index values of a given string.
s="sayali"
result = ""
for i in range(len(s)):
    if i % 2 == 0:
        result += s[i]

string = "programming"
print("Original String:", s)
print("After Removing Odd Index Chars:",result)
