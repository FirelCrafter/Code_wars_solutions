def accum(s):
    return '-'.join([str(letter*(index+1)).title() for index, letter in enumerate(s)]).strip('-')


print(accum('ZpglnRxqenU'))
