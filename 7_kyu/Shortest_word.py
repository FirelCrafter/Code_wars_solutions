def find_short(s):
    return sorted(len(i) for i in s.split())[0]
