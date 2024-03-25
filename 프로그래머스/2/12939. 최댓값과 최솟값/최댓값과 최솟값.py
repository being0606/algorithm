def solution(s):
    N_arr = list(map(int,s.split()))
    SIZE_N_ARR = len(N_arr)
    MAX = N_arr[0]
    MIN = N_arr[0]
    
    for i in N_arr:
        if i>=MAX:
            MAX=i
        if i<=MIN:
            MIN=i
        
    answer = str(MIN) + " " + str(MAX)
    return answer