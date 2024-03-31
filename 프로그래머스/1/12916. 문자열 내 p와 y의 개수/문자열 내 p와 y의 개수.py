def solution(s):
    answer = True
    SIZE_S = len(s)
    s_lower = s.lower()
    
    stack = 0
    for i in range(SIZE_S):
        if s_lower[i]=='p':
            stack += 1
        elif s_lower[i]=='y':
            stack += -1
            
    if stack!=0:
        answer = False
    return answer