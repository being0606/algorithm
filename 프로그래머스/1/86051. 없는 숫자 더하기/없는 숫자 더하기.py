def solution(numbers):
    N_sum=0
    for i in range(len(numbers)):
        N_sum += numbers[i]
    return 45-N_sum