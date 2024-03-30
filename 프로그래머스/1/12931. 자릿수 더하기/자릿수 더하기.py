def solution(n):
    arr = str(n)
    SIZE_ARR = len(arr)
    arr_sum = 0
    
    for i in range(SIZE_ARR):
        arr_sum += int(arr[i])
        
    return arr_sum