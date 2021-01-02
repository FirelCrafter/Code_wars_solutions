import re


def increment_string(strng):
    digits = re.compile(r'\d+$')
    matches = digits.search(strng)
    if matches:
        string = strng[:matches.span()[0]]
        number = strng[matches.span()[0]:]
        return string + str(int(number) + 1).zfill(len(number))
    else:
        return strng + '1'
