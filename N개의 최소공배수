def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

# 최소 공배수
def lcm(a, b):
    return a * b // gcd(a, b)

def solution(arr):
    answer = 0

    for i in range(len(arr)-1):
        m = gcd(arr[i], arr[i+1])
        arr[i+1] = (arr[i]*arr[i+1]) // m

    answer = arr[-1]

    return answer
