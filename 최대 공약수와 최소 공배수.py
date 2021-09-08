# 최대 공약수
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

# 최소 공배수
def lcm(a, b):
    return a * b // gcd(a, b)

def solution(n, m):
    answer = []

    max_number = gcd(n, m)
    answer.append(max_number)
    min_number = lcm(n,m)
    answer.append(min_number)

    return answer
