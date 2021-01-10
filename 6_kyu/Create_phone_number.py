def create_phone_number(n):
    to_str = [str(i) for i in n]
    return '({}) {}-{}'.format(''.join(to_str[:3]), ''.join(to_str[3:6]), ''.join(to_str[6:]))


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
