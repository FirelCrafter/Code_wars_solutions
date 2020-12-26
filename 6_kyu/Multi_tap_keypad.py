def presses(phrase, tap=str.maketrans(
    '1ABC2DEF3GHI4JKL5MNO6PQRS7TUV8WXYZ9 0*#',
    '112341234123412341234123451234123451211')):
    return sum([int(s) for s in phrase.upper().translate(tap)])
