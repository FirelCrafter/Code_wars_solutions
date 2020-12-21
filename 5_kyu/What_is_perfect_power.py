def isPP(n):
    for i in range(2, int(n**0.5) + 1):
        result = n
        counter = 0
        while result % i == 0:
            result /= i
            counter += 1
            if result == 1:
                return [i, counter]
    return None
