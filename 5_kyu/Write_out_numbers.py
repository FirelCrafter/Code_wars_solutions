import inflect


def number2words(n):
    s = inflect.engine()
    return s.number_to_words(n)


print(number2words(1991))
