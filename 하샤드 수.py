def solution(x):
    list_num = list(map(int, str(x)))
    SUM = 0

    for i in range(len(list_num)):
        SUM += list_num[i]

    if x % SUM == 0:
        answer = True
    else:
        answer = False

    return answer
