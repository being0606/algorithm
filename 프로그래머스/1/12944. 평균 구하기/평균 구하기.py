def solution(arr):
    SIZE_ARR = len(arr)
    sum_arr = 0
    for i in range(SIZE_ARR):
        sum_arr += arr[i]
    answer = sum_arr/SIZE_ARR
    return answer