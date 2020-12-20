import re

def kebabize(string):
    string = re.sub(r'[0-9]', '', string)
    if string == '':
        return ''
    elif list(string)[0].islower():
        return ''.join('-' + cap.lower() if cap.isupper() else cap for cap in string)
    else:
        string = re.findall('[A-Z][^A-Z]*', string)
        return '-'.join(string).lower()
