def solution(s):
    S_SIZE = len(s)
    answer = ''
    if S_SIZE%2==1:
        answer = s[int(S_SIZE/2)]
    else:
        answer = s[int(S_SIZE/2)-1] + s[int(S_SIZE/2)]
    return answer