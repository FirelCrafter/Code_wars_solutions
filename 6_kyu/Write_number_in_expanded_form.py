def expanded_form(num):
    result = []
    for a in range(len(str(num)) - 1, -1, -1):
        current = 10 ** a
        quote, num = divmod(num, current)
        if quote:
            result.append(str(quote * current))
    return ' + '.join(result)


print(expanded_form(70304))

