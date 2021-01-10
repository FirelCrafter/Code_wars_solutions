from collections import Counter


def is_isogram(string):
    return False if 2 in Counter(string.lower()).values() else True


print(is_isogram('Dermatoglyphics'))
print(is_isogram(''))
print(is_isogram('aba'))
