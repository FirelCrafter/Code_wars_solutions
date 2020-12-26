import math

def sol_equa(n):
    res = []
    for i in range(1, int(math.sqrt(n))+ 1):
        if n%1 != 0:
            continue
        r = n/i
        y = (r-i)/4
        x = i+2*y
        if x>=0 and y>=0 and (r == x+2*y) and (i == x-2*y) and x%1 == 0 and y%1 == 0:
            res.append([int(x),int(y)])

    return sorted(res, reverse=True)
