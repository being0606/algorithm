def solution(n):
    # selection sort 구현
    n_arr = str(n)
    answer = ''.join(sorted(n_arr, reverse=True))
    return int(answer)