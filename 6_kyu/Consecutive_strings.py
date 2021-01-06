def longest_consec(strarr, k):
    if not strarr or k > len(strarr) or k <= 0:
        return ''
    lengths = [len(a) for a in strarr]
    dex, left, maximum, total = 0, 0, 0, 0
    for i, b in enumerate(lengths, 1):
        total += b
        if i >= k:
            if total > maximum:
                maximum = total
                dex = i
            total -= lengths[left]
            left += 1
    return ''.join(strarr[dex - k:dex])


print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))
