from collections import Counter

# Reading user input
inputVal = input('введите текс :')

Counter = Counter(inputVal.split())

print(Counter.most_common(1))

