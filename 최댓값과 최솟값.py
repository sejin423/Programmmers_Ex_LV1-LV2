def solution(s):
    
    number = list(map(int,s.split(' ')))
    answer = f'{min(number)} {max(number)}'
    
    return answer
