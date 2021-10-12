data = [
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Barry', 3, 32.95],
    [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]


def to_tuple(arr):
    order_number = arr[0]
    quantity = arr[2]
    price = round(arr[3])

    return order_number, quantity, price + 10 if price < 100 else price


tuples = map(lambda x: to_tuple(x), data)
print(list(tuples))