import math

def solution(n):

    # 정수 n 이 제곱근이 존재한다면,
    if n % math.sqrt(n) == 0:
        # 정수 n+1의 제곱근을 리턴
        answer = math.pow(math.sqrt(n)+1, 2)
        return answer
        
    else:
        return -1
