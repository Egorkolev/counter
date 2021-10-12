data = {
    'apple': ['malum', 'pomum', 'popula'],
    'fruit': ['baca', 'bacca', 'popum'],
    'punishment': ['malum', 'multa']
}

result = {}

for key, value in data.items():
    for v in value:
        if v not in result:
            result[v] = []

        result.get(v).append(key)

print(result)
