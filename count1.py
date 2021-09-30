counter = {}
for word in input('введите текст:').split():
    counter[word] = counter.get(word, 0) + 1
    print(counter[word], end=' ')