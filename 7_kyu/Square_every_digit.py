def square_digits(num):
    return int("".join(map(str, [int(x) ** 2 for x in str(num)])))
