import itertools
import math

def is_prime_number(x):
    result = 0
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    result += 1
    # print(result)
    return True

def solution(nums):
    answer = -1
    count = 0
    for x in itertools.combinations(nums, 3):
        # print(f'List : {list(x)}')
        # print(f'SUM : {sum(x)}')
        if is_prime_number(sum(x)) == True:
            count += 1
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    # print(nums)
    # print(f'count : {count}')
    return count
