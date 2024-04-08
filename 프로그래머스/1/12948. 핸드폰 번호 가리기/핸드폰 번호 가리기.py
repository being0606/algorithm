def solution(phone_number):
    SIZE_PN = len(phone_number)
    answer = []

    for i in range(SIZE_PN):
        if i <= SIZE_PN-5:
            answer.append("*")
        else:
            answer.append(phone_number[i])

    return ''.join(answer)