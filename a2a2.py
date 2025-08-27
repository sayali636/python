#Write a python script to count the number of characters (character frequency) in a string. Sample 
#String : google.com'. Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
string = "google.com"
freq = {}
for char in string:
    freq[char] = freq.get(char, 0) + 1
print("Character Frequency:", freq)
