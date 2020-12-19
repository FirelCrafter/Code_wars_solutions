from collections import Counter


def find_uniq(arr):
    for num, count in Counter(arr).items():
        if count == 1:
            return num
