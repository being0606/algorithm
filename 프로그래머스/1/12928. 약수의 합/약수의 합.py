def solution(n):
    n_sum = 0
    for i in range(1, n+1):
        if (n%i == 0): # 약수를 발견
            n_sum += i
    return n_sum