def solution(left, right):
    answer = 0

    for j in range(left, right + 1):
        result = []
        # print(f'j : {j}')
        count = 0
        for i in range(1, j + 1):
            if j % i == 0:
                result.append(i)
        if len(result) % 2 == 0:
            answer += j
        elif len(result) % 2 == 1:
            answer -= j
        # print(result)
        # print(len(result))
    # print(answer)
    return answer
