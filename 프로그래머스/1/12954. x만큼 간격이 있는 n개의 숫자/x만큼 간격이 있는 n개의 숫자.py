def solution(x, n):
    N_init = x
    answer = []
    for i in range(1,n+1):
        answer.append(x*i)
    return answer