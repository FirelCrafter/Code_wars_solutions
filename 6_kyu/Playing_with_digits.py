def dig_pow(n, p):
    res = sum(int(num)**(p+pos) for pos, num in enumerate(map(int, str(n))))
    return int(res/n) if res%n == 0 else -1


print(dig_pow(92, 1))
