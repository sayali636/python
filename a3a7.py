d = {1: 30, 2: 10, 3: 20}

# Ascending
print("Ascending:", dict(sorted(d.items(), key=lambda x: x[1])))

# Descending
print("Descending:", dict(sorted(d.items(), key=lambda x: x[1], reverse=True)))
