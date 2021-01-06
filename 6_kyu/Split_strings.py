from itertools import zip_longest


def solution(s):
    return [''.join(i) for i in zip_longest(s[::2], s[1::2], fillvalue='_')]


print(solution('asdfadsf'))
print(solution('s'))
