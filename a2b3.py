sen="the cat and the dog and the cat"
w=sen.split()
freq = {}
for word in w:
    freq[word] = freq.get(word, 0) + 1
print("Word Frequency:", freq)
