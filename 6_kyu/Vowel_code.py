letters = {
    'a': '1',
    'e': '2',
    'i': '3',
    'o': '4',
    'u': '5'
}


def encode(st):
    return ''.join([letters[let] if let in letters.keys() else let for let in st])


def decode(st):
    return ''.join(
        [list(letters.keys())[list(letters.values()).index(let)] if let in letters.values() else let for let in st])
