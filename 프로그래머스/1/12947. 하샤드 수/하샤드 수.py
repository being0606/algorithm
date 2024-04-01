def solution(x):
    x_list = list(str(x))
    X_SIZE = len(x_list)
    
    x_sum = 0
    for i in range(X_SIZE): # 자리수 더하기
        x_sum += int(x_list[i])
    
    if x%x_sum == 0: # 하샤드 수 검증
        answer = True
    else:
        answer = False
    return answer