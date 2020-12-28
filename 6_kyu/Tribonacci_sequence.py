def tribonacci(signature, n):
    for i in range(n):
        i = sum(signature[-1:-4:-1])
        signature.append(i)
    return signature[:n]


print(tribonacci([1, 1, 1], 10))
