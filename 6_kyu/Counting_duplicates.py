from collections import Counter


def duplicate_count(text):
    string = ''.join([i.lower() if i.isalpha else i for i in text])
    d_counter = 0
    for l, c in Counter(string).items():
        if c > 1:
            d_counter += 1
    return d_counter
