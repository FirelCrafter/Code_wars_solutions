def count_smileys(arr):
    smile_counter = 0
    for smile in arr:
        if len(list(smile)) == 2:
            if ':' == list(smile)[0] or ';' == list(smile)[0]:
                if ')' == list(smile)[1] or 'D' == list(smile)[1]:
                    smile_counter += 1
        if len(list(smile)) == 3:
            if ':' == list(smile)[0] or ';' == list(smile)[0]:
                if '-' == list(smile)[1] or '~'== list(smile)[1]:
                    if ')' == list(smile)[2] or 'D' == list(smile)[2]:
                        smile_counter += 1
    return smile_counter
