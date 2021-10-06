def solution(a, b):
    answer = 1234567890
    result = 0
    for i in range(len(a)):
        result += a[i] * b[i]

    return result
