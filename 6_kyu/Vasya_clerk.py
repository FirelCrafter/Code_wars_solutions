def tickets(people):
    money = {
        '25': 0,
        '50': 0,
        '100': 0
    }

    for bill in people:
        if str(bill) == '25':
            money['25'] += 1
        elif str(bill) == '50':
            if money['25'] < 1:
                return 'NO'
            else:
                money['25'] -= 1
                money['50'] += 1
        elif str(bill) == '100':
            if money['25'] >= 1 and money['50']>= 1:
                money['25'] -= 1
                money['50'] -= 1
                money['100'] += 1
            elif money['25'] >= 3:
                money['25'] -= 3
                money['100'] += 1
            else:
                return 'NO'

    return 'YES' if sum(money.values()) >= 0 else 'NO'
