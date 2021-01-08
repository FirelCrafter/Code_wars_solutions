def find_missing_letter(chars):
    prev = None
    for i in chars:
        cur = ord(i)
        if prev is None or cur - 1 == prev:
            prev = cur
        else:
            return chr(cur - 1)


print(find_missing_letter(['a','b','c','d','f']))
