string = "thequickbrownfoxjumpsoverthelazydog"
freq = {}
for ch in string:
    freq[ch]=freq.get(ch,0)+1
for ch, count in freq.items():
    if count>1:
        print(ch, count)
