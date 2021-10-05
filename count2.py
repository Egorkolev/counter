inputVal = input('введите текст :').split()
counts = dict()

for word in inputVal:
    value = word.lower().strip()
    counts[value] = counts.get(value, 0) + 1

common = max(counts, key=counts.get)

print(common)