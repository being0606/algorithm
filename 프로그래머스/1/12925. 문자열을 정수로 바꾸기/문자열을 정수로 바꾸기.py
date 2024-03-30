def solution(s):
    if s[0] == '-':
        n = int(s[1:])*(-1)
    elif s[0] == '+':
        n = int(s[1:])
    else:
        n = int(s[:])
    return n