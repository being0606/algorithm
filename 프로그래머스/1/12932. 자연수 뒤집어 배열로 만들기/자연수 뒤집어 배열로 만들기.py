def solution(n):
    answer = []
    N = str(n)
    for i in range(1,len(N)+1):
        answer.append(int(N[-i]))
    return answer