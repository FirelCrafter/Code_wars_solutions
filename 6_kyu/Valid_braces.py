def validBraces(s):
    while len(s)!=0:
        if s[0]=='(' and s[-1]==')' or s[0]=='[' and s[-1]==']' or s[0]=='{' and s[-1]=='}':
            s = s[1:-1]
        elif s[0]=='(' and s[1]==')' or s[0]=='[' and s[1]==']' or s[0]=='{' and s[1]=='}':
            s = s[2:]
        else:
            return False
    return True


print(validBraces('(){}[]'))
print(validBraces('([{}])'))
print(validBraces('[({})](]'))
print(validBraces('()'))
