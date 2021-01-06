def tower_builder(n_floors):
    length = n_floors * 2 - 1
    return ['{:^{}}'.format('*' * a, length) for a in range(1, length + 1, 2)]


print(tower_builder(6))
