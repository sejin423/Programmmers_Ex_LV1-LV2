def solution(n):
    answer = 0
    number = str(n)
    
    for i in range(len(number)):
        answer += int(number[i])

    return answer
