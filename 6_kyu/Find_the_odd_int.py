from collections import Counter

def find_it(seq):
    return int(''.join(str(num) for num, count in Counter(seq).items() if count%2!=0))

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))
