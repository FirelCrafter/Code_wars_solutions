def maskify(cc):
    return ''.join(['#' for i in cc[:-4]]+[i for i in cc[-4:]]) if len(cc) > 4 else cc


print(maskify('4556364607935616'))
print(maskify('64607935616'))
print(maskify('1'))
