def find_outlier(integers):
    odd = 0
    even = 0
    for i in integers:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    if odd == 1:
        res = [i for i in integers if i % 2 != 0]
    else:
        res = [i for i in integers if i % 2 == 0]
    return res[0]


print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
