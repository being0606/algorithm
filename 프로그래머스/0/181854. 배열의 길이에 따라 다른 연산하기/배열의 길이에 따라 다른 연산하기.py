def solution(arr, n):
    LENGTH = len(arr)
    if LENGTH%2 != 0:
        for i in range(LENGTH):
            if i%2==0:
                arr[i] += n        
    else:
        for i in range(LENGTH):
            if i%2!=0:
                arr[i] += n
    answer = arr
    return answer