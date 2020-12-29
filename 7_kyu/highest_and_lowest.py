def high_and_low(numbers):
    n = sorted([int(num) for num in numbers.split()])
    return '{} {}'.format(n[-1], n[0])


print(high_and_low('4 5 29 54 4 0 -214 542 -64 1 -3 6 -6'))
