def solution(array, commands):
    answer = []
    count = len(commands)
    for i in range(count):
        command_1 = commands[i][0] - 1
        command_2 = commands[i][1]
        #print(f'array[{command_1}:{command_2}]>> {array[command_1:command_2]}')
        sort_array = sorted(array[command_1:command_2])
        #print(f'sort_array>> {sort_array}')
        #print(f'sort_array[commands[0][2] - 1]>> {sort_array[commands[i][2] - 1]}')
        #print('')
        answer.append(sort_array[commands[i][2] - 1])
    return answer
