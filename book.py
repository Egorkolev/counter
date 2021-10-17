data = [
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Barry', 3, 32.95],
    [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]

tuples = map(lambda x: (x[0], x[2], round(x[3]) + 10 if round(x[3]) < 100 else round(x[3])), data)
print(list(tuples))
