'''
문제 설명
두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.
'''
def solution(a, b):
    data = []
    for i in range(a,b+1):
        if a<b:
            data.append(a)
            a += 1
        elif a==b:
            data.append(a)
    
    if b < a:
        for i in range(b, a+1):
            data.append(b)
            b += 1
    sum = 0
    for i in range(len(data)):
        sum += data[i]
    return sum
