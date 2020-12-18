def printer_error(s):
    return '{}/{}'.format(len([c for c in s if c not in 'abcdefghijklm']), len(s))

print(printer_error('aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz'))

