from functools import reduce


def get_exp(n):
    if n <= 4:
        return n
    tail = n % 100 if n % 100 > 1 else n % 1000
    exp = 4 if tail % 4 == 0 else tail % 4
    result = exp if exp > 1 else tail
    return result


def last_digit(lst):
    if not lst:
        return 1
    if len(lst) == 1:
        return lst[0] % 10
    exp = lst[1] if len(lst) == 2 else reduce(lambda y, x: x ** get_exp(y), lst[1:][::-1])
    return ((lst[0] % 10) ** get_exp(exp)) % 10
