def solution(s):
    return ''.join(list(map(upper, list(s))))


def upper(letter):
    return ' ' + letter if letter.isupper() else letter
