# program 1
#Create a list
my_list = [10, 20, 30, 40, 50]

print("Original List:", my_list)
print("Reversed List:", my_list[::-1])

# program 2
s = "PYTHONPROGRAMMING"

# Alternate characters from left to right
left = s[::2]

# Alternate characters from right to left
right = s[::-2]

print("Original String:", s)
print("Alternate characters (left to right):", left)
print("Alternate characters (right to left):", right)

# program 3
# Input string
s = input("Enter a string: ").lower()

vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for ch in s:
    if ch.isalpha():  # Only consider alphabets
        if ch in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)

# program 4

nums = []

for i in range(5):
    n = int(input(f"Enter integer {i+1}: "))
    nums.append(n)

# Check duplicates
if len(nums) != len(set(nums)):
    print("DUPLICATES")
else:
    print("ALL UNIQUE")








