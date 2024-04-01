def solution(absolutes, signs):
    n_sum = 0
    for i in range(len(absolutes)):
        if signs[i]:
            n_sum+=absolutes[i]
        else:
            n_sum-=absolutes[i]
    return n_sum