import itertools

def solution(numbers):
    answer = []
    for i in itertools.combinations(numbers, 2):
        #print(f'i : {i}')
        #print(f'sum : {sum(i)}')
        
        answer.append(sum(i))
        #print(f'answer : {answer}')
        
        set_answer = list(set(answer))
        set_answer.sort()
        
        #print(f'set_answer : {list(set(answer))}\n')

    return set_answer
