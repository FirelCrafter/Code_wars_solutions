from itertools import groupby

def group_consecutives(lst):
    for d, g in groupby(enumerate(lst), lambda idx : idx[0] - idx[1]):
        r = [x for d, x in g]
        if len(r) > 2:
            yield f"{r[0]}-{r[-1]}"
        else:
            yield from map(str, r)

def solution(lst):
    return ','.join(group_consecutives(lst))


print(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]))
