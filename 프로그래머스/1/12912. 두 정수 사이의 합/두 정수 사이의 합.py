def solution(a, b):
    n_max = b
    n_min = a
    n_sum = 0
    if a>b:
        n_max = a
        n_min = b
    for i in range(n_min,n_max+1):
        n_sum += i
    return n_sum