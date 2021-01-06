def order(sentence):
    return ' '.join(sorted(sentence.split(), key=lambda a: next(b for b in a if b.isdigit())))


print(order('is2 Thi1s T4est 3a'))
