def find_even_index(nums):
    sum = 0
    f = []

    for idx, val in enumerate(nums):
        if idx == 0:
            f.append(val)
        else:
            f.append(f[idx-1] + val)
        sum += val

    for idx, val in enumerate(nums):
        t = 0
        if idx != 0:
            t = f[idx - 1]
        if t == sum - f[idx]:
            return idx

    return -1
