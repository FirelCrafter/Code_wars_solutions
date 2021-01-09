def in_array(array1, array2):
    array2 = ' '.join(array2)
    return sorted(set(a for a in array1 if a in array2))


print(in_array(["live", "arp", "strong"], ["lively", "alive", "harp", "sharp", "armstrong"]))
